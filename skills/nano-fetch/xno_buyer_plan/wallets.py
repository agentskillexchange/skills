"""wallet_calls: turn a plan into the exact tool call each outside Nano wallet needs to carry it out.

Pure functions: NO network, NO key, NO
signing. The wallet tool the host already runs signs and sends; this module only names the call.

    wallet_calls(plan, quote=None, seller_url="") -> {"kilkelly-mcp": call, "nano-pay": call}

A call:    {"ok": True, "tool": <name>, "arguments": {...}, "amount_raw": <digits the wallet will send>,
            "returns": <where the result / send hash comes back>, "then": <what the host does next>,
            "source": <file:line read>}
A refusal: {"ok": False, "error": <code>, "detail": <words>, "source": ...}
    codes: plan_refused, unsupported_version, network_name, over_wallet_cap, no_send_tool,
           http_only, no_url, offer_order,
           no_representative (a rep-binding plan: neither wallet tool sets a block's representative;
           the refusal carries "set_rep": False)
    unsigned_block codes: no_account_state, bad_account, bad_previous, unopened, bad_balance,
           insufficient_balance, bad_pay_to, self_send, bad_amount, bad_order_id (orderId missing, not
           a string, or not a fullmatch of the gateway's ORDER_ID rule [A-Za-z0-9_-]{22,128},
           client_fit.ORDER_ID = x402-gateway src/nano.js:167), rep_mismatch (plan["representative"] missing or not
           order_representative(orderId, payTo, amount_raw), which the block always recomputes)
    restore_block codes: no_send_block, no_prior_representative, bad_prior_representative,
           bad_bound_representative (see "Restore block" below)

    wallet_calls(plan, quote=None, seller_url="", account=None)

A rep-binding plan adds one top-level key, "unsigned_block", when the caller passes `account` (the payer's
state the host read itself with account_info: {"account": nano_/xrb_ address, "previous": 64 hex frontier,
"balance": decimal raw string}; this module never fetches it). It is an UNSIGNED Nano state send block,
{"type": "state", "account", "previous", "representative": order_representative(orderId, payTo,
amount_raw) recomputed (it must equal plan["representative"], else rep_mismatch), "balance": balance -
amount_raw, "link": payTo's public key (64 upper hex), "link_as_account", "amount_raw", "signature": None,
"work": None, "note"}, for any signer that takes the representative as an input (nanocurrency-js
createBlock does); work is computed for `previous`, then the plan's steps are followed. A bad or missing
state gives {"ok": False, "error": <code>, "detail": ...} in that key instead. Without `account` the key is
left out, so the result has exactly the two wallet entries it had before (account={} names the three
fields as no_account_state). Other dialects never carry the key.

Restore block: in Nano a send that carries a new representative also MOVES the payer's
delegation to it, and the bound representative is a hash-derived account no node runs. So with `account` a
rep-binding plan also gets "restore_block" (the "unsigned_block" key is kept exactly as before, a second key
rather than a list, for backward compatibility): an UNSIGNED state CHANGE block that follows the send,
{"needed": True, "type": "state", "account", "previous": the send block's hash (state_block_hash),
"representative": account["representative"] (the payer's PRIOR rep, re-encoded nano_), "balance": the
send's new balance (unchanged), "link": 64 zeros, "send_hash", "signature": None, "work": None, "note"}.
The prior rep comes only from the caller: add "representative" to the `account` dict (account_info's
representative field). Cases (the send block stays in "unsigned_block" in each, except no_send_block):
    {"needed": False, "detail"}  the prior rep IS the bound rep: the send moves no delegation, no change block
    refusal codes: no_prior_representative (missing or ""; carries "fields": ["representative"]),
                   bad_prior_representative (not a string / bad checksum), bad_bound_representative,
                   no_send_block (the send block itself was refused, or could not be hashed)
Sign and publish it only after the send is confirmed and the seller has settled the order.
state_block_hash: blake2b-256 over preamble (32 bytes, ...06), account key, previous, representative key,
balance (16 bytes big-endian), link. Checked against an independent implementation; no published Nano hash vector with its fields was found offline.

Read from source on 2026-11-21 (raw clone, read only, never run):
  kilkelly/nano-currency-mcp-server @ 403b0cd nano-currency.js (server nano_currency 1.1.0)
    raw_send {destination_account, amount (raw digits)}            :245-290, returns RPC `process` JSON
    x402_payment_signature_exact_scheme_create {x402_payment_required_header}  :436-500, v2 only (:56),
      accepts entry must be scheme exact AND network == X402_NANO_NETWORK ('nano:mainnet') (:476-486),
      cap RAW_MAX_SEND_AMOUNT default 1e28 raw (:18, :489), returns JSON string of the encoded header.
      (read from package.json, package-lock.json:92-95 and npm's
      nano-currency-mcp-server 1.1.0 dependencies): kilkelly installs @x402nano/exact ^0.1.1 = 0.1.1,
      whose client reads only payTo and amount, so a quote without `extra` is signed. The
      extra.workOptional TypeError is in @x402nano/exact 1.1.0, which kilkelly never installs.
      @x402/core 2.3.1 x402Client() signs the FIRST exact nano:mainnet entry (client/index.js:84,
      :265-288); when that is not the planned one, the argument carries the planned entry only.
  Feeless402/feeless402 @ fab7f69 nano_pay/mcp_server.py
    x402_pay {url, method, json_body, max_xno (decimal XNO string)}  :100-125: fetches the URL itself,
      pays the first Nano offer, refuses above max_xno; HTTP only. Returns JSON {status_code, receipt, body};
      receipt.block is the send hash (x402.py:564-570). Its MCP tools have no plain send (wallet_status,
      x402_quote, x402_compare, x402_pay, faucet_claim, topup_quote).
      pick_nano_offer (x402.py:250-274) takes any network starting with 'nano', so 'nano-mainnet'
      (nanswap-nodes) is paid; it pays the first exact Nano offer, so when that is not the planned
      one the call is refused `offer_order` (it has no argument to choose).
"""
import base64
import hashlib
import json
import re

try:  # installed as the xno_buyer_plan package
    from .client_fit import ALPHABET, ORDER_ID, account_from_key, nano_checksum_ok
except ImportError:  # run from the repository: client_fit.py sits one directory up (or next to this file)
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from client_fit import ALPHABET, ORDER_ID, account_from_key, nano_checksum_ok  # noqa: E402

KILKELLY = "kilkelly-mcp"
NANO_PAY = "nano-pay"
KILKELLY_CAP_RAW = 10 ** 28  # RAW_MAX_SEND_AMOUNT default; the host may raise it by env
K_SRC = "kilkelly/nano-currency-mcp-server@403b0cd nano-currency.js"
N_SRC = "Feeless402/feeless402@fab7f69 nano_pay/mcp_server.py"


def _no(code, detail, src):
    return {"ok": False, "error": code, "detail": detail, "source": src}


def raw_to_xno(raw):
    """Exact decimal XNO string for a raw amount (1 XNO = 10**30 raw). No float, no Decimal context:
    Decimal(int(raw)).scaleb(-30) rounded to 28 digits, so the point is placed
    in the digits themselves."""
    digits = str(int(raw))
    if digits.startswith("-"):
        raise ValueError("negative raw amount")
    digits = digits.rjust(31, "0")
    whole, frac = digits[:-30].lstrip("0") or "0", digits[-30:].rstrip("0")
    return whole + "." + frac if frac else whole


def _as_doc(x):
    if isinstance(x, str):
        try:
            return json.loads(x)
        except ValueError:
            return None
    return x


def _payment_required(quote):
    """The PaymentRequired document a quote carries, and whether it arrived as a base64 header."""
    q = _as_doc(quote)
    if not isinstance(q, dict):
        return None, None
    if "headers" in q or "body" in q:
        hdrs = q.get("headers") if isinstance(q.get("headers"), dict) else {}
        for k, v in hdrs.items():
            if isinstance(k, str) and k.lower() == "payment-required" and isinstance(v, str):
                try:
                    return json.loads(base64.b64decode(v).decode("utf-8")), v
                except (ValueError, UnicodeDecodeError):
                    return None, None
        body = _as_doc(q.get("body"))
        return (body, None) if isinstance(body, dict) else (None, None)
    msg = q.get("mcp", q)
    res = msg.get("result", msg) if isinstance(msg, dict) else None
    if not isinstance(res, dict):
        return None, None
    sc = res.get("structuredContent")
    if isinstance(sc, dict) and "accepts" in sc:
        return sc, None
    for c in res.get("content") or []:
        if isinstance(c, dict) and c.get("type") == "text":
            d = _as_doc(c.get("text"))
            if isinstance(d, dict) and "accepts" in d:
                return d, None
    return None, None


def _planned_accept(doc, plan):
    for a in doc.get("accepts") or []:
        if not isinstance(a, dict) or a.get("scheme") != "exact" or a.get("payTo") != plan.get("payTo"):
            continue
        amt = a.get("amount") or a.get("maxAmountRequired")
        if str(amt) == plan.get("amount_raw"):
            return a
    return None


def _kilkelly_send(plan, then):
    if int(plan["amount_raw"]) > KILKELLY_CAP_RAW:
        return _no("over_wallet_cap", "%s raw is above raw_send's default RAW_MAX_SEND_AMOUNT 1e28"
                   % plan["amount_raw"], K_SRC + ":267")
    return {"ok": True, "tool": "raw_send",
            "arguments": {"destination_account": plan["payTo"], "amount": plan["amount_raw"]},
            "amount_raw": plan["amount_raw"],
            "returns": "content[0].text: JSON of the node's `process` answer; its `hash` is the send hash "
                       "(published, not yet confirmed)",
            "then": then, "source": K_SRC + ":245-290"}


def _kilkelly(plan, quote):
    d, transport = plan["dialect"], plan.get("transport")
    if d == "send-hash":
        return _kilkelly_send(plan, "wait for confirmation, journal the hash, retry with %s: <hash>"
                              % plan["proof"]["header"])
    if d == "invoice":
        return _kilkelly_send(plan, "only after re-planning on the invoice's price_raw; then POST the "
                              "result path with invoice_id, payment_hash=<hash>, invoice_token")
    if transport == "mcp" and plan.get("profile") == "xmcp":
        return _kilkelly_send(plan, "wait for confirmation, journal the hash, then retry the tools/call "
                              "with _meta['x402/payment'] = base64 PaymentPayload whose payload.blockHash "
                              "is <hash> (the host builds it; kilkelly has no tool for this payload)")
    doc, header = _payment_required(quote) if quote is not None else (None, None)
    if doc is None:
        return _no("plan_refused", "exact needs the quote itself (its PaymentRequired) to build the "
                   "tool's header argument", K_SRC + ":436-441")
    if doc.get("x402Version") != 2:
        return _no("unsupported_version", "x402Version %r; the tool accepts [2] only"
                   % doc.get("x402Version"), K_SRC + ":56,471")
    acc = _planned_accept(doc, plan)
    if acc is None or acc.get("network") != "nano:mainnet":
        return _no("network_name", "the planned accepts entry must name network 'nano:mainnet' exactly "
                   "(seen %r)" % (acc or {}).get("network"), K_SRC + ":476-486")
    # No `extra` is NOT a refusal: kilkelly 1.1.0 depends on @x402nano/exact ^0.1.1
    # (package.json, package-lock.json:92-95, and npm's nano-currency-mcp-server 1.1.0), which resolves
    # to 0.1.1 and never to 1.x; 0.1.1's client/index.js:58-79 reads only payTo and amount. The
    # extra.workOptional TypeError is @x402nano/exact 1.1.0's, a version kilkelly does not install.
    if int(plan["amount_raw"]) > KILKELLY_CAP_RAW:
        return _no("over_wallet_cap", "%s raw is above RAW_MAX_SEND_AMOUNT 1e28" % plan["amount_raw"],
                   K_SRC + ":489")
    # @x402/core 2.3.1 x402Client() (kilkelly passes no selector) signs accepts[0] of the entries whose
    # scheme/network it registered (client/index.js:84, :265-288). If that is not the planned entry,
    # the wallet would sign another amount or payTo, so the argument then carries the planned entry only.
    first = next((a for a in doc.get("accepts") or [] if isinstance(a, dict)
                  and a.get("scheme") == "exact" and a.get("network") == "nano:mainnet"), None)
    narrowed = first is not acc
    if narrowed:
        doc, header = dict(doc, accepts=[acc]), None
    arg = header or base64.b64encode(json.dumps(doc, separators=(",", ":")).encode("utf-8")).decode("ascii")
    if transport == "mcp":
        then = ("base64-decode the returned header to the PaymentPayload object and retry the same "
                "tools/call with params._meta['x402/payment'] = that object; read result._meta"
                "['x402/payment-response']")
    else:
        then = "retry the request with %s: <returned header>" % plan["proof"]["header"]
    return {"ok": True, "tool": "x402_payment_signature_exact_scheme_create",
            "arguments": {"x402_payment_required_header": arg},
            "header_built_from": "seller header" if header else (
                "quote document narrowed to the planned accepts entry (base64 JSON)" if narrowed
                else "quote document (base64 JSON)"),
            "amount_raw": plan["amount_raw"],
            "returns": "content[0].text: JSON string of the base64 PAYMENT-SIGNATURE header. No hash: "
                       "the block is signed, not published; the seller settles it",
            "then": then, "source": K_SRC + ":436-500"}


def _nano_pick(doc):
    """nano_pay/x402.py:250-274 pick_nano_offer, over collect_offers:189-194: the first offer whose
    network starts with 'nano' (so 'nano-mainnet' too) or whose asset is xno/nano, preferring one whose
    scheme/protocolScheme says exact."""
    offers = [o for k in ("accepts", "accepted") for o in (doc.get(k) or []) if isinstance(o, dict)]
    pay = doc.get("payment") if isinstance(doc.get("payment"), dict) else {}
    offers += [o for o in (pay.get("accepted") or []) if isinstance(o, dict)]
    nano = [o for o in offers if str(o.get("network", "")).lower().startswith("nano")
            or str(o.get("asset", "")).lower() in ("xno", "nano")]
    for o in nano:
        if "exact" in (str(o.get("protocolScheme", "")).lower() + str(o.get("scheme", "")).lower()):
            return o
    return nano[0] if nano else None


def _nano_pay(plan, seller_url, quote=None):
    if plan.get("transport") == "mcp":
        return _no("http_only", "x402_pay fetches an http(s) URL itself; it cannot answer an MCP "
                   "tools/call quote", N_SRC + ":100-125")
    if plan["dialect"] != "exact":
        return _no("no_send_tool", "dialect %s needs a plain send or a send hash; nano-pay's MCP tools "
                   "have no send" % plan["dialect"], N_SRC)
    if not seller_url:
        return _no("no_url", "x402_pay needs the seller URL to fetch and pay", N_SRC + ":105")
    doc = _payment_required(quote)[0] if quote is not None else None
    if isinstance(doc, dict):
        picked = _nano_pick(doc)
        acc = _planned_accept(doc, plan)
        if picked is not None and acc is not None and picked is not acc:
            return _no("offer_order", "x402_pay pays the offer pick_nano_offer picks (payTo %r, %r raw), "
                       "not the planned one; it cannot be told which" % (
                           picked.get("payTo"), picked.get("amount") or picked.get("maxAmountRequired")),
                       "nano_pay/x402.py:250-274")
    return {"ok": True, "tool": "x402_pay",
            "arguments": {"url": seller_url, "method": "GET", "max_xno": raw_to_xno(plan["amount_raw"])},
            "amount_raw": plan["amount_raw"],
            "returns": "JSON {status_code, receipt, body}; receipt.block is the send hash, receipt.settled "
                       "the ledger's answer",
            "then": "nothing: the tool re-fetches and pays the quote it sees; it refuses any quote above "
                    "max_xno, so a changed price is refused, never paid",
            "source": N_SRC + ":100-125; nano_pay/x402.py:457,564-570"}


_HEX64 = re.compile(r"[0-9A-Fa-f]{64}")
_BALANCE = re.compile(r"0|[1-9][0-9]*")
_MAX_BALANCE = 2 ** 128 - 1  # a state block's balance field is 16 bytes
STATE_FIELDS = ("account", "previous", "balance")


def key_from_account(address):
    """nano_/xrb_ address -> its 32-byte public key, or None when the blake2b-40 checksum (client_fit
    nano_checksum_ok) fails. The inverse of client_fit.account_from_key."""
    if not nano_checksum_ok(address):
        return None
    rest = address.split("_", 1)[1]
    bits = "".join(format(ALPHABET.index(c), "05b") for c in rest)
    return int(bits[4:260], 2).to_bytes(32, "big")


def _block_no(code, detail):
    return {"ok": False, "error": code, "detail": detail}


def _order_representative(order_id, pay_to, amount_raw):
    """plan.order_representative, imported at call time: plan.py imports this module at load, so a
    top-level import here would be circular."""
    try:  # installed as the xno_buyer_plan package
        from .plan import order_representative
    except ImportError:  # run from the repository: plan.py sits next to this file
        import os
        import sys
        here = os.path.dirname(os.path.abspath(__file__))
        if here not in sys.path:
            sys.path.insert(0, here)
        from plan import order_representative  # noqa: E402
    return order_representative(order_id, pay_to, amount_raw)


def unsigned_block(plan, account):
    """The unsigned state send block for a rep-binding plan from the payer's state the host read itself.
    Never raises; every refusal is {"ok": False, "error", "detail"}."""
    if not isinstance(account, dict) or any(account.get(f) in (None, "") for f in STATE_FIELDS):
        return dict(_block_no("no_account_state", "pass account={account, previous, balance}: the payer's "
                              "address, its frontier hash and its balance in raw, read by the host with "
                              "account_info (this module fetches nothing)"), fields=list(STATE_FIELDS))
    payer, previous, balance = account["account"], account["previous"], account["balance"]
    payer_key = key_from_account(payer) if isinstance(payer, str) else None
    if payer_key is None:
        return _block_no("bad_account", "account %r is not a nano_/xrb_ address with a valid checksum"
                         % (payer,))
    if not isinstance(previous, str) or not _HEX64.fullmatch(previous):
        return _block_no("bad_previous", "previous %r is not a 64-hex block hash" % (previous,))
    if int(previous, 16) == 0:
        return _block_no("unopened", "previous is all zeros: an unopened account has no balance and "
                         "cannot send")
    if not isinstance(balance, str) or not _BALANCE.fullmatch(balance) or int(balance) > _MAX_BALANCE:
        return _block_no("bad_balance", "balance %r is not a raw decimal string (digits, no leading zero "
                         "unless \"0\", at most 2^128-1)" % (balance,))
    amount = plan.get("amount_raw")
    if not isinstance(amount, str) or not _BALANCE.fullmatch(amount) or int(amount) == 0:
        return _block_no("bad_amount", "plan amount_raw %r is not positive raw digits" % (amount,))
    if int(balance) < int(amount):
        return _block_no("insufficient_balance", "balance %s raw is below the plan's %s raw"
                         % (balance, amount))
    pay_to = plan.get("payTo")
    pay_key = key_from_account(pay_to) if isinstance(pay_to, str) else None
    if pay_key is None:
        return _block_no("bad_pay_to", "payTo %r fails the Nano checksum" % (pay_to,))
    if pay_key == payer_key:
        return _block_no("self_send", "the payer is payTo; a send to itself pays no seller")
    order_id = plan.get("orderId")
    # the seller (x402-gateway src/nano.js:167) refuses any orderId that is not a fullmatch of ORDER_ID, so
    # a block for one would pay an order the seller never settles; checking here also keeps a lone surrogate
    # (which cannot be UTF-8 encoded) away from order_representative, so this never raises
    if not isinstance(order_id, str) or not ORDER_ID.fullmatch(order_id):
        return _block_no("bad_order_id", "plan orderId %r is missing, not a string, or does not match the "
                         "gateway's ORDER_ID rule [A-Za-z0-9_-]{22,128} (x402-gateway src/nano.js:167); the "
                         "bound representative is derived from it" % (order_id,))
    # recomputed exactly as plan._plan_bound builds it (same orderId, payTo and amount_raw string), never
    # copied: a plan edited after planning must not move the payer's delegation to an unbound account
    rep = _order_representative(order_id, pay_to, amount)
    if plan.get("representative") != rep:
        return _block_no("rep_mismatch", "plan representative %r is %s; order_representative(orderId, payTo, "
                         "amount_raw) gives %s" % (plan.get("representative"), "missing"
                                                   if plan.get("representative") in (None, "") else
                                                   "not the bound one", rep))
    return {"type": "state", "account": account_from_key(payer_key), "previous": previous.upper(),
            "representative": rep, "balance": str(int(balance) - int(amount)),
            "link": pay_key.hex().upper(), "link_as_account": pay_to, "amount_raw": amount,
            "signature": None, "work": None,
            "note": "unsigned: sign with a signer that takes representative as an input (e.g. nanocurrency-js "
                    "createBlock), compute work for previous, then follow the plan's steps (do not publish "
                    "if the plan's steps say not to)"}


STATE_PREAMBLE = (6).to_bytes(32, "big")  # a state block's hash preamble: 31 zero bytes, then 0x06


def state_block_hash(block):
    """64 upper hex: blake2b-256 over preamble (32 bytes, 0x..06), account public key, previous (32),
    representative public key, balance (16 bytes big-endian), link (32). Raises ValueError on a field it
    cannot encode (bad checksum, bad hex, balance out of range)."""
    acct, rep = key_from_account(block.get("account")), key_from_account(block.get("representative"))
    if acct is None or rep is None:
        raise ValueError("account or representative fails the Nano checksum")
    prev, link = bytes.fromhex(block["previous"]), bytes.fromhex(block["link"])
    if len(prev) != 32 or len(link) != 32:
        raise ValueError("previous and link are 32 bytes")
    bal = int(block["balance"])
    if not 0 <= bal <= _MAX_BALANCE:
        raise ValueError("balance out of range")
    h = hashlib.blake2b(digest_size=32)
    for part in (STATE_PREAMBLE, acct, prev, rep, bal.to_bytes(16, "big"), link):
        h.update(part)
    return h.hexdigest().upper()


def restore_block(plan, account, send):
    """The unsigned state CHANGE block that follows `send` (unsigned_block's result) and gives the payer
    back its prior representative, account["representative"]. Never raises. See the module docstring."""
    if not isinstance(send, dict) or send.get("ok") is False:
        return _block_no("no_send_block", "no send block to follow (%s)" % (
            send.get("error") if isinstance(send, dict) else send,))
    prior = account.get("representative")
    if prior in (None, ""):
        return dict(_block_no("no_prior_representative", "pass account['representative']: the payer's "
                              "representative BEFORE the send, read by the host with account_info; without it "
                              "the payer's delegation stays on the bound account after the send"),
                    fields=["representative"])
    prior_key = key_from_account(prior) if isinstance(prior, str) else None
    if prior_key is None:
        return _block_no("bad_prior_representative", "account['representative'] %r is not a nano_/xrb_ "
                         "address with a valid checksum" % (prior,))
    bound_key = key_from_account(send.get("representative"))
    if bound_key is None:
        return _block_no("bad_bound_representative", "the send's representative %r fails the Nano checksum"
                         % (send.get("representative"),))
    if prior_key == bound_key:
        return {"needed": False, "detail": "the prior representative is the bound one: the send moves no "
                "delegation, so no change block is needed"}
    send_hash = state_block_hash(send)
    return {"needed": True, "type": "state", "account": send["account"], "previous": send_hash,
            "representative": account_from_key(prior_key), "balance": send["balance"], "link": "0" * 64,
            "send_hash": send_hash, "signature": None, "work": None,
            "note": "unsigned change block: sign it after the send, compute work for previous (the send's "
                    "hash), and publish it only after the send is confirmed and the seller has settled; it "
                    "moves the payer's delegation back to its prior representative"}


def wallet_calls(plan, quote=None, seller_url="", account=None):
    """Never raises. A refused plan gives a refusal for every wallet. `account` (rep-binding plans only):
    the payer's state for the extra "unsigned_block" and "restore_block" keys, see the module docstring."""
    if not isinstance(plan, dict) or not plan.get("ok"):
        why = (plan or {}).get("error") if isinstance(plan, dict) else None
        return {w: _no("plan_refused", "the plan was refused: %s" % why, "plan.py")
                for w in (KILKELLY, NANO_PAY)}
    if plan.get("dialect") == "rep-binding":
        # a bound order needs the send's representative set to plan["representative"]; neither wallet's
        # tool takes a representative (raw_send {destination_account, amount} :245-290; the exact-scheme
        # signer and x402_pay build the block themselves), and an unbound send is refused by the seller
        # after the money has moved (x402-gateway src/nano.js:307-310)
        why = "the send must set representative %s; this wallet's tool cannot" % plan.get("representative")
        out = {KILKELLY: dict(_no("no_representative", why, K_SRC + ":245-290,436-500"), set_rep=False),
               NANO_PAY: dict(_no("no_representative", why, N_SRC + ":100-125"), set_rep=False)}
        if account is not None:
            try:
                out["unsigned_block"] = unsigned_block(plan, account)
            except (ValueError, TypeError, AttributeError, KeyError) as e:
                out["unsigned_block"] = _block_no("no_account_state", "account state could not be read: %s"
                                                  % e)
            try:
                out["restore_block"] = restore_block(plan, account, out["unsigned_block"])
            except (ValueError, TypeError, AttributeError, KeyError) as e:
                out["restore_block"] = _block_no("no_send_block", "the send block could not be hashed: %s" % e)
        return out
    try:
        k = _kilkelly(plan, quote)
    except (ValueError, TypeError, AttributeError) as e:
        k = _no("plan_refused", "quote could not be read: %s" % e, K_SRC)
    try:
        n = _nano_pay(plan, seller_url, quote)
    except (ValueError, TypeError, AttributeError) as e:
        n = _no("plan_refused", "amount could not be read: %s" % e, N_SRC)
    return {KILKELLY: k, NANO_PAY: n}
