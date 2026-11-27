"""A Scrapy downloader middleware that pays a bound Nano (XNO) x402 order and retries the page.

In the nano-fetch skill folder it is also the settle core of fetch.py (Scrapy optional). Off unless NANO_PAY_ENABLED is set:
with it unset the middleware is never loaded (NotConfigured) and a 402 reaches the spider as before.

What it does with a 402 (and nothing else; every other status passes through untouched):
  1. xno_buyer_plan.plan_402 reads the quote (PAYMENT-REQUIRED header or JSON body) and returns a plan or a
     named refusal. Only a bound order (dialect "rep-binding", xno-binding/v1/rep as profullstack/x402-gateway
     0.18.2 offers it) is paid: its send names a representative derived from the orderId, payTo and amount,
     so the payment is bound to this one request. A plain exact accept is refused here (unbound).
  2. Spend checks: the per-page cap (NANO_PAY_CAP_RAW) inside plan_402, then the crawl budget
     (NANO_PAY_BUDGET_RAW) summed over the journal, restarts included.
  3. The journal (NANO_PAY_JOURNAL, a JSON-lines file, flushed and fsynced) gets an "intent" line BEFORE the
     signer is called and a "paid" line with the block hash after. Every key in it - intent or paid - is a
     replay to plan_402, so one order is never handed to the signer twice, across a crash or a restart.
     Reserving is one transaction under an exclusive lock on NANO_PAY_JOURNAL + ".lock" (fcntl.flock, or
     msvcrt.locking on Windows; with neither the payment is refused, never made unlocked): reload the file,
     check replay and budget, write and fsync the intent, release. Only then is the signer called, so two
     processes sharing one journal can never both reserve one order or the last unit of budget. A journal
     line that does not parse (a torn write, an edit) makes the whole journal refuse to sign
     (journal_corrupt) until a person reconciles it: unknown payment history is never skipped.
  4. The signer hook (NANO_PAY_SIGNER: a callable or "module.attr") receives the order - payTo, amount_raw,
     representative, orderId, network - and returns the 64-hex hash of a send it published AND saw
     confirmed. The key lives only inside the operator's signer; this module never sees a key or a seed and
     makes no network call of its own.
  5. The request is re-issued once (dont_filter) with PAYMENT-SIGNATURE (x402 v2) or X-PAYMENT (v1): base64
     JSON {x402Version, accepted, payload: {orderId, blockHash}}, with meta dont_redirect so the proof is
     never carried to another URL. A paid retry that meets 402 again is returned to the spider as is:
     never a second payment for one request.

Amounts are raw (1 XNO = 10**30 raw), parsed from the quote as integers, never floats.
"""
import base64
import contextlib
import importlib
import json
import os
import re
import sys

try:
    import fcntl
except ImportError:  # Windows
    fcntl = None
try:
    import msvcrt
except ImportError:  # POSIX
    msvcrt = None

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.dirname(HERE)
from xno_buyer_plan.plan import DEFAULT_CAP_RAW, plan_402  # the package next to this file

try:
    from scrapy.exceptions import NotConfigured
except ImportError:  # scrapy absent: the same name, so tests and from_crawler behave alike
    class NotConfigured(Exception):
        pass

RAW_PER_XNO = 10 ** 30
META_KEY = "nano_pay"
_HEX64 = re.compile(r"[0-9A-Fa-f]{64}")


class SignerError(Exception):
    """The signer returned something that is not a 64-hex block hash."""


class JournalCorrupt(Exception):
    """A journal line does not parse as a journal record (a torn write or an edit). Nothing is signed
    until a person reconciles the file: a skipped line could be a payment that was already made."""


class JournalUnavailable(Exception):
    """The journal cannot be locked (no fcntl or msvcrt, or the lock file cannot be opened)."""


_STATES = ("intent", "paid")
_DIGITS = re.compile(r"[0-9]+")


def _text(x):
    if isinstance(x, (bytes, bytearray)):
        return x.decode("latin-1")
    return str(x)


def headers_dict(headers):
    """Scrapy Headers (bytes keys, list-of-bytes values) or a plain mapping -> {str: str} (first value)."""
    out = {}
    if headers is None:
        return out
    items = headers.items() if hasattr(headers, "items") else headers
    for k, v in items:
        if isinstance(v, (list, tuple)):
            v = v[0] if v else b""
        out[_text(k)] = _text(v)
    return out


def load_signer(spec):
    if spec is None or spec == "":
        return None
    if callable(spec):
        return spec
    mod, _, attr = str(spec).rpartition(".")
    if not mod:
        raise NotConfigured("NANO_PAY_SIGNER %r is not 'module.attr'" % spec)
    return getattr(importlib.import_module(mod), attr)


class Journal:
    """Append-only JSON-lines journal shared by every process that pays from it.

    Keys of every line (intent or paid) are replays, and every line's amount_raw counts against the
    budget: an intent with no paid line is an order whose send may have gone out, so it stays reserved.
    Readers are strict: a line that is not a complete record (including a last line without its newline)
    raises JournalCorrupt. Use transaction() for anything that decides to pay."""

    def __init__(self, path):
        self.path = path
        self.lock_path = path + ".lock"
        self.entries = {}  # journal_key -> {"state", "amount_raw", "blockHash"?}

    def reload(self):
        """Read the whole file again. Raises JournalCorrupt on any malformed line."""
        entries = {}
        if os.path.exists(self.path):
            with open(self.path, "rb") as f:
                data = f.read()
            if data and not data.endswith(b"\n"):
                raise JournalCorrupt("%s: the last line has no newline (a torn write); reconcile the file "
                                     "before paying again" % self.path)
            for n, raw in enumerate(data.split(b"\n")[:-1] if data else [], 1):
                if not raw.strip():
                    continue
                try:
                    row = json.loads(raw.decode("utf-8"))
                except (ValueError, UnicodeDecodeError):
                    row = None
                if (not isinstance(row, dict) or not isinstance(row.get("key"), str)
                        or row.get("state") not in _STATES
                        or not _DIGITS.fullmatch(str(row.get("amount_raw", "")))):
                    raise JournalCorrupt("%s line %d is not a journal record; reconcile the file before "
                                         "paying again" % (self.path, n))
                prev = entries.get(row["key"], {})
                prev.update(row)
                entries[row["key"]] = prev
        self.entries = entries
        return self

    @contextlib.contextmanager
    def locked(self):
        """An exclusive lock on the sidecar lock file, across processes. Never runs unlocked."""
        if fcntl is None and msvcrt is None:
            raise JournalUnavailable("no file locking on this platform (neither fcntl nor msvcrt); "
                                     "refusing to pay without an exclusive journal lock")
        try:
            fd = os.open(self.lock_path, os.O_RDWR | os.O_CREAT, 0o600)
        except OSError as e:
            raise JournalUnavailable("cannot open the journal lock %s: %s" % (self.lock_path, e))
        try:
            if fcntl is not None:
                fcntl.flock(fd, fcntl.LOCK_EX)
            else:
                while True:
                    os.lseek(fd, 0, os.SEEK_SET)
                    try:
                        msvcrt.locking(fd, msvcrt.LK_LOCK, 1)
                        break
                    except OSError:  # LK_LOCK gives up after ~10 s; keep waiting
                        continue
            try:
                yield self
            finally:
                if fcntl is not None:
                    fcntl.flock(fd, fcntl.LOCK_UN)
                else:
                    os.lseek(fd, 0, os.SEEK_SET)
                    msvcrt.locking(fd, msvcrt.LK_UNLCK, 1)
        finally:
            os.close(fd)

    @contextlib.contextmanager
    def transaction(self):
        """Lock, then reload from disk: what is checked inside is what every other process wrote."""
        with self.locked():
            self.reload()
            yield self

    def __contains__(self, key):
        return key in self.entries

    def spent_raw(self):
        return sum(int(row["amount_raw"]) for row in self.entries.values())

    def write(self, row):
        """Append one record, flushed and fsynced. Call inside transaction(). The record always starts
        on a fresh line: if the file does not end in a newline one is written first, so a torn tail can
        never swallow this record (and the torn line still makes the next reload refuse)."""
        line = json.dumps(row, sort_keys=True).encode("utf-8") + b"\n"
        with open(self.path, "a+b") as f:
            f.seek(0, os.SEEK_END)
            if f.tell() > 0:
                f.seek(-1, os.SEEK_END)
                if f.read(1) != b"\n":
                    line = b"\n" + line
                f.seek(0, os.SEEK_END)
            f.write(line)
            f.flush()
            os.fsync(f.fileno())
        prev = self.entries.get(row["key"], {})
        prev.update(row)
        self.entries[row["key"]] = prev


def _quote_doc(headers, body):
    """The decoded PaymentRequired document the plan was made from: header first, then JSON body."""
    for k, v in headers.items():
        if k.lower() == "payment-required":
            try:
                return json.loads(base64.b64decode(v).decode("utf-8"))
            except (ValueError, UnicodeDecodeError, TypeError):
                return None
    try:
        return json.loads(body.decode("utf-8") if isinstance(body, (bytes, bytearray)) else body)
    except (ValueError, UnicodeDecodeError, TypeError, AttributeError):
        return None


def _nano_only(headers, body):
    """The same quote with only its Nano accepts, or None. Used only to name a refusal, never to pay."""
    doc = _quote_doc(headers, body)
    if not isinstance(doc, dict) or not isinstance(doc.get("accepts"), list):
        return None
    keep = [a for a in doc["accepts"] if isinstance(a, dict) and str(a.get("network", "")).startswith("nano")]
    if not keep or len(keep) == len(doc["accepts"]):
        return None
    doc = dict(doc, accepts=keep)
    if any(k.lower() == "payment-required" for k in headers):
        enc = base64.b64encode(json.dumps(doc).encode("utf-8")).decode("ascii")
        return {"PAYMENT-REQUIRED": enc}, b""
    return {}, json.dumps(doc).encode("utf-8")


def accepted_entry(doc, plan):
    """The raw accepts entry the plan was made from: same payTo, amount and extra.orderId."""
    if not isinstance(doc, dict) or not isinstance(doc.get("accepts"), list):
        return None
    for a in doc["accepts"]:
        if not isinstance(a, dict):
            continue
        extra = a.get("extra") if isinstance(a.get("extra"), dict) else {}
        amount = a.get("amount", a.get("maxAmountRequired"))
        if (a.get("payTo") == plan["payTo"] and str(amount) == plan["amount_raw"]
                and extra.get("orderId") == plan["orderId"]):
            return a
    return None


def payment_header(plan, accepted, block_hash):
    version = plan.get("x402Version") or 2
    doc = {"x402Version": version, "accepted": accepted,
           "payload": {"orderId": plan["orderId"], "blockHash": block_hash}}
    if version == 1:
        doc = {"x402Version": 1, "scheme": accepted.get("scheme"), "network": accepted.get("network"),
               "payload": doc["payload"]}
    name = "X-PAYMENT" if version == 1 else "PAYMENT-SIGNATURE"
    return name, base64.b64encode(json.dumps(doc, separators=(",", ":")).encode("utf-8")).decode("ascii")


def settle_402(headers, body, url, signer, journal, cap_raw, budget_raw, allow_unbound=False):
    """One 402 -> a paid proof header, or a named refusal. Shared by this middleware and nano_fetch.

    headers: {str: str}; journal: a Journal. Returns {"ok": True, "header": (name, value), "plan": plan,
    "blockHash": hash} or {"ok": False, "error": code, "detail": words}. Under the journal's exclusive
    lock, after reloading it from disk: plan (shape, network, checksum, amount, per-call cap, binding,
    replay), bound-or-allowed, budget, intent journalled (fsynced). Then, unlocked, the signer; then the
    hash check and the paid line (locked again). A send-hash quote (no binding) is paid only with
    allow_unbound; its signer gets representative None (keep the wallet's own). A malformed journal
    refuses with journal_corrupt, a journal that cannot be locked with journal_unavailable."""
    try:
        with journal.transaction():
            r = _reserve(headers, body, url, journal, cap_raw, budget_raw, allow_unbound)
    except JournalCorrupt as e:
        return {"ok": False, "error": "journal_corrupt", "detail": str(e)}
    except JournalUnavailable as e:
        return {"ok": False, "error": "journal_unavailable", "detail": str(e)}
    if not r["ok"]:
        return r
    plan, accepted, key = r["plan"], r["accepted"], r["key"]
    order = {"network": plan["network"], "payTo": plan["payTo"], "amount_raw": plan["amount_raw"],
             "representative": plan.get("representative"), "orderId": plan.get("orderId")}
    try:
        block_hash = signer(dict(order))
    except Exception as e:  # noqa: BLE001 - the intent stays reserved: the outcome is unknown
        return {"ok": False, "error": "signer_error", "detail": "signer raised %s: %s; the order stays "
                "reserved in the journal and is never signed again" % (type(e).__name__, e)}
    if not isinstance(block_hash, str) or not _HEX64.fullmatch(block_hash):
        # the intent stays journalled: an unknown outcome is never retried by this process or the next
        return {"ok": False, "error": "signer_no_hash", "detail": "signer returned %r" % (block_hash,)}
    block_hash = block_hash.upper()
    paid_row = {"key": key, "state": "paid", "amount_raw": plan["amount_raw"],
                "orderId": plan.get("orderId"), "blockHash": block_hash}
    try:
        with journal.locked():
            journal.write(paid_row)
    except (JournalUnavailable, OSError):
        # the intent already reserves this order; the hash is still returned to be presented and reported
        pass
    if plan["dialect"] == "send-hash":
        header = (plan["proof"]["header"], block_hash)
    else:
        header = payment_header(plan, accepted, block_hash)
    return {"ok": True, "header": header, "plan": plan, "blockHash": block_hash}


def _reserve(headers, body, url, journal, cap_raw, budget_raw, allow_unbound):
    """The checks and the durable intent, inside journal.transaction()."""
    plan = plan_402(headers, body, cap_raw=cap_raw, seller_url=url, journal=journal)
    if not plan.get("ok") and plan.get("error") == "wrong_network":
        # plan_402 names the FIRST accept's refusal (a USDC entry on a mixed quote); name the Nano one
        nano = _nano_only(headers, body)
        if nano is not None:
            plan = plan_402(nano[0], nano[1], cap_raw=cap_raw, seller_url=url, journal=journal)
    if not plan.get("ok"):
        return {"ok": False, "error": plan.get("error"), "detail": plan.get("detail")}
    dialect = plan.get("dialect")
    if not (dialect == "rep-binding" or (dialect == "send-hash" and allow_unbound)):
        return {"ok": False, "error": "unbound", "detail": "dialect %s: only a bound order (xno-binding/v1/rep) "
                "is paid%s" % (dialect, " (a send-hash quote needs allow_unbound)" if dialect == "send-hash"
                               else "")}
    amount = int(plan["amount_raw"])
    spent = journal.spent_raw()
    if spent + amount > int(budget_raw):
        return {"ok": False, "error": "over_budget", "detail": "%d raw spent or reserved + %d > budget %d raw"
                % (spent, amount, int(budget_raw))}
    accepted = None
    if dialect == "rep-binding":
        accepted = accepted_entry(_quote_doc(headers, body), plan)
        if accepted is None:
            return {"ok": False, "error": "no_accepted", "detail": "the planned accept was not found again"}
    key = plan["journal_key"]
    journal.write({"key": key, "state": "intent", "amount_raw": plan["amount_raw"],
                   "orderId": plan.get("orderId"), "url": url})
    return {"ok": True, "plan": plan, "accepted": accepted, "key": key}


class NanoPaymentMiddleware:
    """Settings: NANO_PAY_ENABLED (bool, default False), NANO_PAY_SIGNER (callable or 'module.attr'),
    NANO_PAY_JOURNAL (file path, required), NANO_PAY_CAP_RAW (per page, default buyer_plan's 10**29 raw),
    NANO_PAY_BUDGET_RAW (whole crawl, default 10 x the cap)."""

    def __init__(self, signer, journal_path, cap_raw=DEFAULT_CAP_RAW, budget_raw=None, logger=None):
        if signer is None or not callable(signer):
            raise NotConfigured("NANO_PAY_SIGNER is not set: nothing can pay")
        if not journal_path:
            raise NotConfigured("NANO_PAY_JOURNAL is not set: replay refusal must survive a restart")
        self.signer = signer
        self.journal = Journal(journal_path)
        self.cap_raw = str(int(cap_raw))
        self.budget_raw = int(budget_raw) if budget_raw is not None else 10 * int(self.cap_raw)
        self.logger = logger
        self.refusals = []  # (url, code, detail), for the spider's stats and for tests

    @classmethod
    def from_crawler(cls, crawler):
        s = crawler.settings
        if not s.getbool("NANO_PAY_ENABLED", False):
            raise NotConfigured("NANO_PAY_ENABLED is off")
        cap = s.get("NANO_PAY_CAP_RAW") or DEFAULT_CAP_RAW
        budget = s.get("NANO_PAY_BUDGET_RAW")
        return cls(load_signer(s.get("NANO_PAY_SIGNER")), s.get("NANO_PAY_JOURNAL"), cap, budget)

    def _refuse(self, request, response, code, detail):
        self.refusals.append((request.url, code, detail))
        if self.logger is not None:
            self.logger.info("nano-pay refused %s: %s (%s)", request.url, code, detail)
        return response

    def process_response(self, request, response, spider=None):
        if getattr(response, "status", None) != 402:
            return response
        if (getattr(request, "meta", None) or {}).get(META_KEY):
            return self._refuse(request, response, "paid_retry_402", "the paid retry met 402 again; "
                                "not paying twice for one request")
        r = settle_402(headers_dict(response.headers), getattr(response, "body", b""), request.url,
                       self.signer, self.journal, self.cap_raw, self.budget_raw)
        if not r["ok"]:
            return self._refuse(request, response, r["error"], r["detail"])
        name, value = r["header"]
        plan, block_hash = r["plan"], r["blockHash"]
        key = plan["journal_key"]
        new_headers = headers_dict(request.headers)
        new_headers[name] = value
        meta = dict(getattr(request, "meta", None) or {})
        meta[META_KEY] = {"orderId": plan["orderId"], "blockHash": block_hash, "journal_key": key}
        meta["dont_redirect"] = True  # the proof goes to the quoting URL only, never to a redirect target
        return request.replace(headers=new_headers, meta=meta, dont_filter=True)
