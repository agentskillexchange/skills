"""Bind a Nano (XNO) payment to one order and credit each block once.

Standard library only. No wallet, no key, no seed: everything here reads a
block that a public node already returned and decides whether it pays one
specific order.

Two optional pieces, used by ``verify_payment.py`` only when asked for:

* Order binding (xno-binding v1, option C). A Nano block has no memo, so the
  payer puts a commitment to the order in the send block's representative
  field: ``sha256("xno-binding/v1/rep|" + order_id + "|" + pay_to + "|" +
  price_raw)`` encoded as a ``nano_`` account. The payer signs it, so the
  block pays that order, that address and that exact price, and no other.
* A claims file. One JSON line per credited block, appended and fsynced
  before the caller delivers. It is read back on start, so a restart does
  not forget which blocks were already used.

Amounts are integer raw (1 XNO = 10**30 raw); floats are refused.
"""

import hashlib
import json
import os
import re
import secrets

try:  # POSIX advisory lock
    import fcntl
except ImportError:  # pragma: no cover
    fcntl = None
try:  # Windows byte-range lock, used when fcntl is missing
    import msvcrt
except ImportError:
    msvcrt = None

RAW_PER_XNO = 10 ** 30

_ALPHABET = "13456789abcdefghijkmnopqrstuwxyz"
_ACCOUNT_RE = re.compile(r"\A(?:nano|xrb)_[13][13456789abcdefghijkmnopqrstuwxyz]{59}\Z")
_HASH_RE = re.compile(r"\A[0-9A-Fa-f]{64}\Z")
_RAW_RE = re.compile(r"\A[0-9]{1,40}\Z")

# Verdicts, named as in the xno-binding v1 seller ledger rules.
MATCHED = "matched"
ALREADY_CLAIMED = "already_claimed"
DUPLICATE = "duplicate_refund_due"
WRONG_AMOUNT = "refusable_wrong_amount"
NOT_BOUND = "not_bound_to_order"
WRONG_ACCOUNT = "wrong_pay_to"
NOT_CONFIRMED = "not_confirmed"
NOT_A_SEND = "not_a_send"


def _b32_encode(value, length):
    out = []
    for _ in range(length):
        out.append(_ALPHABET[value & 31])
        value >>= 5
    return "".join(reversed(out))


def _b32_decode(text):
    value = 0
    for ch in text:
        value = value * 32 + _ALPHABET.index(ch)
    return value


def account_public_key(account):
    """Return the 32-byte public key of a checksum-valid account, else raise ValueError."""
    if not isinstance(account, str) or not _ACCOUNT_RE.match(account):
        raise ValueError("not a Nano account: %r" % (account,))
    body = account.split("_", 1)[1]
    key_value = _b32_decode(body[:52])
    if key_value >> 256:
        raise ValueError("not a Nano account: %r" % (account,))
    key = key_value.to_bytes(32, "big")
    check = hashlib.blake2b(key, digest_size=5).digest()[::-1]
    if _b32_decode(body[52:]).to_bytes(5, "big") != check:
        raise ValueError("Nano account checksum mismatch: %r" % (account,))
    return key


def is_valid_account(account):
    try:
        account_public_key(account)
    except ValueError:
        return False
    return True


def public_key_to_account(key):
    if not isinstance(key, (bytes, bytearray)) or len(key) != 32:
        raise ValueError("a public key is 32 bytes")
    check = hashlib.blake2b(bytes(key), digest_size=5).digest()[::-1]
    return "nano_" + _b32_encode(int.from_bytes(key, "big"), 52) + _b32_encode(int.from_bytes(check, "big"), 8)


def _require_raw(price_raw):
    if isinstance(price_raw, bool) or not isinstance(price_raw, int) or price_raw <= 0:
        raise TypeError("price_raw must be a positive int of raw (1 XNO = 10**30 raw)")


def order_commitment(order_id, pay_to, price_raw):
    """xno-binding v1 option C commitment (32 bytes)."""
    _require_raw(price_raw)
    if not isinstance(order_id, str) or not order_id:
        raise ValueError("order_id must be a non-empty string")
    msg = b"xno-binding/v1/rep|" + order_id.encode() + b"|" + pay_to.encode() + b"|" + str(price_raw).encode()
    return hashlib.sha256(msg).digest()


def commitment_rep_account(order_id, pay_to, price_raw):
    """The representative a payer sets on the send block for this order."""
    return public_key_to_account(order_commitment(order_id, pay_to, price_raw))


_XNO_RE = re.compile(r"\A([0-9]{1,10})(?:\.([0-9]{1,30}))?\Z")
_ORDER_ID_RE = re.compile(r"\A[A-Za-z0-9_-]{22,128}\Z")

NETWORK = "nano:mainnet"
BINDING_V1 = "xno-binding/v1/rep"


def xno_to_raw(amount):
    """Turn a decimal XNO string such as ``"0.05"`` into integer raw, exactly.

    Only a string is accepted (a float cannot hold 30 decimals); more than 30
    decimals, a sign, an exponent or a zero amount is refused.
    """
    match = _XNO_RE.match(amount) if isinstance(amount, str) else None
    if not match:
        raise ValueError("amount must be a decimal XNO string with at most 30 decimals, e.g. '0.05'")
    whole, frac = match.group(1), match.group(2) or ""
    raw = int(whole) * RAW_PER_XNO + int(frac.ljust(30, "0"))
    if raw <= 0:
        raise ValueError("amount must be more than zero")
    return raw


def new_order_id():
    """A fresh opaque order id: 128 random bits as 32 hex characters."""
    return secrets.token_hex(16)


def payment_requirement(pay_to, price_raw, order_id=None, max_timeout_seconds=300):
    """The x402 v2 ``accepts`` entry for one order, paid in Nano with scheme exact.

    It asks for exactly ``price_raw`` raw to ``pay_to`` and names the order the
    payer must commit to (``extra.binding`` and ``extra.orderId``, the shape the
    xmcp x402 plugin offers). ``extra.representative`` is that order's
    commitment account, so a payer can set it on its send block without
    recomputing it; ``check_bound_send`` (or ``verify_payment.py --order-id``)
    then accepts only a block that carries it. Keep the order id with the
    order: it is what the buyer presents again after a lost response.
    """
    _require_raw(price_raw)
    account_public_key(pay_to)
    if order_id is None:
        order_id = new_order_id()
    if not isinstance(order_id, str) or not _ORDER_ID_RE.match(order_id):
        raise ValueError("order_id must be 22 to 128 characters of A-Z, a-z, 0-9, '_' or '-'")
    if isinstance(max_timeout_seconds, bool) or not isinstance(max_timeout_seconds, int) or max_timeout_seconds <= 0:
        raise ValueError("max_timeout_seconds must be a positive int")
    return {
        "scheme": "exact",
        "network": NETWORK,
        "amount": str(price_raw),
        "asset": "XNO",
        "payTo": pay_to,
        "maxTimeoutSeconds": max_timeout_seconds,
        "extra": {
            "name": "XNO",
            "decimals": 30,
            "binding": BINDING_V1,
            "orderId": order_id,
            "representative": commitment_rep_account(order_id, pay_to, price_raw),
        },
    }


def _same_account(a, b):
    try:
        return account_public_key(a) == account_public_key(b)
    except ValueError:
        return False


def check_bound_send(info, pay_to, price_raw, order_id):
    """Decide whether a ``block_info`` (json_block=true) result pays this order.

    Only a confirmed send block can carry the commitment: it must send exactly
    ``price_raw`` to ``pay_to`` with the order's commitment as representative.
    Returns one of the verdict constants; MATCHED means bound and paid.
    """
    _require_raw(price_raw)
    account_public_key(pay_to)
    contents = info.get("contents") or {}
    if info.get("subtype") != "send":
        return NOT_A_SEND
    if info.get("confirmed") != "true":
        return NOT_CONFIRMED
    if not _same_account(contents.get("link_as_account"), pay_to):
        return WRONG_ACCOUNT
    amount = info.get("amount")
    if not isinstance(amount, str) or not _RAW_RE.match(amount) or int(amount) != price_raw:
        return WRONG_AMOUNT
    if not _same_account(contents.get("representative"), commitment_rep_account(order_id, pay_to, price_raw)):
        return NOT_BOUND
    return MATCHED


def normalize_block_hash(block_hash):
    if not isinstance(block_hash, str) or not _HASH_RE.match(block_hash):
        raise ValueError("a block hash is 64 hex characters")
    return block_hash.upper()


class ClaimsLockError(RuntimeError):
    """The claims file cannot be locked, so no claim is made."""


def _lock(fh):
    if fcntl is not None:
        fcntl.flock(fh.fileno(), fcntl.LOCK_EX)
        return
    # msvcrt.locking locks bytes from the current position; LK_LOCK retries
    # for about 10 seconds and then raises, so the wait is bounded.
    fh.seek(0)
    try:
        msvcrt.locking(fh.fileno(), msvcrt.LK_LOCK, 1)
    except OSError as e:
        raise ClaimsLockError("could not lock claims file: %s" % (e,))


def _unlock(fh):
    if fcntl is not None:
        fcntl.flock(fh.fileno(), fcntl.LOCK_UN)
        return
    fh.seek(0)
    msvcrt.locking(fh.fileno(), msvcrt.LK_UNLCK, 1)


class ClaimsFile:
    """Append-only record of credited blocks that survives a restart.

    Each line is ``{"block": <HASH>, "order": <order id or null>}``. A block
    is credited at most once; an order is credited by at most one block.
    ``claim`` returns MATCHED only for the first claim of a block. The same
    block presented again for the same order returns ALREADY_CLAIMED: it was
    credited before, so nothing may be delivered for it again. Any other
    reuse returns DUPLICATE. The read, check and append run under an
    exclusive lock (fcntl.flock, or msvcrt.locking on Windows); with neither,
    ``claim`` raises ClaimsLockError rather than run unlocked.
    """

    def __init__(self, path):
        self.path = path

    def _read(self, fh):
        """Parse every complete line. A tail with no newline is a write cut
        short by a crash before it was acknowledged; it is not a claim.

        The file is read as bytes, so the offset returned for the end of the
        last complete line is the real on-disk offset even when lines end in
        CRLF; truncating there never cuts into an acknowledged claim."""
        fh.seek(0)
        content = fh.read()
        complete = content[: content.rfind(b"\n") + 1]
        by_block, by_order = {}, {}
        for i, raw in enumerate(complete.split(b"\n")):
            try:
                line = raw.decode("utf-8").rstrip("\r")
                if not line.strip():
                    continue
                row = json.loads(line)
                block = normalize_block_hash(row["block"])
                order = row.get("order")
                if order is not None and not isinstance(order, str):
                    raise TypeError(order)
            except (ValueError, KeyError, TypeError, AttributeError):
                raise ValueError("claims file %s is damaged at line %d" % (self.path, i + 1))
            by_block[block] = order
            if order is not None:
                by_order[order] = block
        return by_block, by_order, len(complete), len(content) != len(complete)

    def claim(self, block_hash, order_id=None):
        block = normalize_block_hash(block_hash)
        if order_id is not None and (not isinstance(order_id, str) or not order_id):
            raise ValueError("order_id must be a non-empty string")
        if fcntl is None and msvcrt is None:
            raise ClaimsLockError("no file lock on this system (need fcntl or msvcrt); refusing to claim unlocked")
        fd = os.open(self.path, os.O_RDWR | os.O_CREAT | os.O_APPEND, 0o600)
        with os.fdopen(fd, "r+b") as fh:
            _lock(fh)
            try:
                return self._claim_locked(fh, block, order_id)
            finally:
                _unlock(fh)

    def _claim_locked(self, fh, block, order_id):
        by_block, by_order, complete_bytes, torn_tail = self._read(fh)
        if block in by_block:
            if order_id is not None and by_block[block] == order_id:
                return ALREADY_CLAIMED
            return DUPLICATE
        if order_id is not None and order_id in by_order:
            return DUPLICATE
        if torn_tail:
            fh.truncate(complete_bytes)
        fh.write((json.dumps({"block": block, "order": order_id}, sort_keys=True) + "\n").encode("utf-8"))
        fh.flush()
        os.fsync(fh.fileno())
        return MATCHED

    def claimed(self, block_hash):
        block = normalize_block_hash(block_hash)
        if not os.path.exists(self.path):
            return False
        with open(self.path, "rb") as fh:
            return block in self._read(fh)[0]
