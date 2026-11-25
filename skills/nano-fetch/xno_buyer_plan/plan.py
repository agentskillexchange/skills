"""Buyer client core: turn one unpaid Nano 402 into a payment plan, or a named refusal.

Pure functions: NO network, NO key, NO signing, NO send. The plan says
what a wallet tool (nano-wallet-xno, or any other) must send and what to present afterwards; this
module never does either.

    plan_402(headers, body, cap_raw, seller_url="", journal=None) -> dict

A plan:
    {"ok": True, "dialect": "exact"|"rep-binding"|"send-hash"|"invoice", "x402Version": 1|2|None,
     "network": "nano:mainnet", "network_seen": <as the seller wrote it>, "network_mapped": bool,
     "amount_raw": "<digits>", "payTo": "nano_...", "work_threshold": "<hex>"|None,
     "proof": {"header": <name>|None, "field": <what goes in it>},
     "steps": [<plain words, in order>], "journal_key": "<seller|payTo|amount|nonce>"}

A refusal:
    {"ok": False, "error": <code>, "detail": <words>}
    codes: unknown_shape, wrong_network, bad_checksum, amount_ambiguous, no_amount, over_cap, replayed,
           binding_unknown (extra.binding is not xno-binding/v1/rep), binding_order_id (extra.orderId is
           not 22-128 of A-Za-z0-9_-)

Bound orders: an exact accept whose extra
carries binding "xno-binding/v1/rep" and an orderId plans as dialect "rep-binding", HTTP or MCP. The plan
adds "binding", "orderId" and "representative" (the nano_ account of SHA-256("xno-binding/v1/rep|" +
orderId + "|" + payTo + "|" + amountRaw), order_representative(), read from profullstack/x402-gateway
0.18.2 src/nano.js:182-190 and :133-141); the send is published with that representative and confirmed,
then payload.orderId + payload.blockHash are presented. journal_key ends in the orderId, so one order is
never planned twice. Network "nano" (x402-gateway's name, src/x402.js:126) is read as Nano mainnet for a
bound accept only. Checks: network, payTo checksum, amount, cap, then the binding, then replay. Either of
the two orderIds one gateway 402 carries (body and header) binds: the seller checks statelessly (see
client_fit.py, rep-binding).

MCP transport:
    plan_mcp(message, cap_raw, seller_url="", journal=None, profile=None) -> the same plan plus
    "transport": "mcp", "profile": "spec"|"xmcp", "mcp_where", "settlement_meta", and
    proof {"meta_key": "x402/payment", "encoding": "object"|"base64", "field": ...}.
    mcp_settlement(message) reads result._meta["x402/payment-response"].
    A fixtures file may mix HTTP entries (headers/body) and MCP entries ("mcp": <tools/call response>).

Check order is fixed (the first failure is the one named): shape, network, payTo checksum, amount,
cap, replay. A quote with several accepts is planned on the first that passes; when none passes the
first accept's refusal is returned.

`journal` is any container of journal keys already paid (a set, or a dict). plan_402 only reads it;
`journal_record(journal, plan)` adds a key. One quote is never planned twice.

Usage: python3 -m xno_buyer_plan.plan FIXTURES.json [CAP_RAW]
"""
import base64
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
try:  # installed as the xno_buyer_plan package
    from .client_fit import (ORDER_ID, REP_BINDING, _header, _norm_accept, account_from_key, dialect_of,
                             nano_checksum_ok, parse_402)
    from .wallets import wallet_calls
except ImportError:  # loose files, not a package
    sys.path.insert(0, os.path.dirname(HERE))
    from client_fit import (ORDER_ID, REP_BINDING, _header, _norm_accept, account_from_key,  # noqa: E402
                            dialect_of, nano_checksum_ok, parse_402)
    sys.path.insert(0, HERE)
    from wallets import wallet_calls  # noqa: E402

NETWORKS = {"nano:mainnet": False, "nano-mainnet": True}  # value: True when mapped
# A bound accept is a Nano send by construction (its representative is a nano_ account), and
# x402-gateway 0.18.2 names its XNO entry network "nano" (src/x402.js:126); kept for bound accepts only.
BOUND_NETWORKS = dict(NETWORKS, nano=True)
DEFAULT_CAP_RAW = str(10 ** 29)  # 0.1 XNO per call; the caller sets its own
_RAW = re.compile(r"[1-9][0-9]*")  # x402-gateway src/nano.js:168 RAW, the amount string that is hashed


def _refuse(code, detail):
    return {"ok": False, "error": code, "detail": detail}


def _network(seen, table=NETWORKS):
    # a list or dict network is unhashable: `in` would raise TypeError
    if isinstance(seen, str) and seen in table:
        return "nano:mainnet", table[seen]
    return None, False


def _header_name(text):
    """'X-Nano-Payment: <send hash>' -> 'X-Nano-Payment'."""
    if not isinstance(text, str):
        return None
    m = re.match(r"\s*([A-Za-z0-9-]+)\s*:", text)
    return m.group(1) if m else None


_ASCII_DIGITS = re.compile(r"[0-9]+")


def _amount_cap(amount, cap_raw):
    # str.isdigit() accepts '²' and other Unicode digits that int() rejects; a seller's quote
    # must give a named refusal, never a crash.
    if amount is None or not _ASCII_DIGITS.fullmatch(str(amount)):
        return _refuse("no_amount", "the quote carries no raw amount in digits")
    if int(amount) == 0:
        # a Nano state block that leaves the balance unchanged is not a send: nothing pays
        return _refuse("no_amount", "the quote asks for 0 raw, which no send can pay")
    if int(amount) > int(cap_raw):
        return _refuse("over_cap", "amount %s raw is above the cap %s raw" % (amount, cap_raw))
    return None


def _key(seller_url, pay_to, amount, nonce=""):
    return "|".join([seller_url or "", pay_to or "", str(amount or ""), nonce or ""])


def _replayed(journal, key):
    return journal is not None and key in journal


def _plan_exact(accept, version, cap_raw, seller_url, journal, raw_extra):
    net, mapped = _network(accept.get("network"))
    if net is None:
        return _refuse("wrong_network", "network %r is not Nano mainnet" % accept.get("network"))
    if not accept.get("payTo_checksum_valid"):
        return _refuse("bad_checksum", "payTo %r fails the Nano checksum" % accept.get("payTo"))
    if accept.get("amount_ambiguous"):
        return _refuse("amount_ambiguous", "amount and maxAmountRequired differ")
    bad = _amount_cap(accept.get("amount_raw"), cap_raw)
    if bad:
        return bad
    key = _key(seller_url, accept["payTo"], accept["amount_raw"])
    if _replayed(journal, key):
        return _refuse("replayed", "this quote is already in the journal: " + key)
    extra = raw_extra if isinstance(raw_extra, dict) else {}
    work = extra.get("workThreshold") if extra.get("work") == "required" else None
    header = "X-PAYMENT" if version == 1 else "PAYMENT-SIGNATURE"
    steps = ["build a send block of amount_raw to payTo from the caller's wallet"]
    if work:
        steps.append("attach proof of work at or above work_threshold")
    steps += ["sign it (wallet tool, not this module) and do NOT publish it",
              "retry the request with %s: base64 x402 v%s payload holding the signed block"
              % (header, version or 2)]
    return {"ok": True, "dialect": "exact", "x402Version": version, "network": net,
            "network_seen": accept.get("network"), "network_mapped": mapped,
            "amount_raw": accept["amount_raw"], "payTo": accept["payTo"], "work_threshold": work,
            "proof": {"header": header, "field": "payload.block (signed send block)"},
            "steps": steps, "journal_key": key}


def order_representative(order_id, pay_to, amount_raw):
    """The nano_ account a bound send must name as its representative (xno-binding/v1/rep).

    x402-gateway 0.18.2, read only: SHA-256 of the UTF-8 text "xno-binding/v1/rep|<orderId>|<payTo>|<amount>"
    (src/nano.js:182-185 orderCommitment), the 32 bytes encoded as an account (:133-141 accountFromKey,
    :188-190 orderRepresentative). The seller hashes canonicalAccount(payTo) (:297), so an xrb_ payTo is
    hashed as its nano_ form; the amount is the raw digit string (:298)."""
    pay_to = "nano_" + pay_to[4:] if pay_to.startswith("xrb_") else pay_to
    text = "|".join([REP_BINDING, order_id, pay_to, str(amount_raw)])
    return account_from_key(hashlib.sha256(text.encode("utf-8")).digest())


def _plan_bound(accept, version, cap_raw, seller_url, journal, extra):
    """An exact accept whose extra names a binding. Checks in order: network, payTo checksum, amount,
    cap (as _plan_exact), then the binding itself (binding_unknown, binding_order_id), then replay on a
    key that includes the orderId. Never signs or sends: the plan names the representative to set."""
    net, mapped = _network(accept.get("network"), BOUND_NETWORKS)
    if net is None:
        return _refuse("wrong_network", "network %r is not Nano mainnet" % accept.get("network"))
    if not accept.get("payTo_checksum_valid"):
        return _refuse("bad_checksum", "payTo %r fails the Nano checksum" % accept.get("payTo"))
    if accept.get("amount_ambiguous"):
        return _refuse("amount_ambiguous", "amount and maxAmountRequired differ")
    bad = _amount_cap(accept.get("amount_raw"), cap_raw)
    if bad:
        return bad
    amount = accept["amount_raw"]
    if not _RAW.fullmatch(amount):
        # the seller hashes String(amount) and refuses anything but /^[1-9]\d*$/ (nano.js:168, :299)
        return _refuse("no_amount", "a bound amount must be raw digits without a leading zero: %r" % amount)
    binding, order_id = extra.get("binding"), extra.get("orderId")
    if binding != REP_BINDING:
        return _refuse("binding_unknown", "extra.binding %r is not %s, the one binding this client "
                       "builds" % (binding, REP_BINDING))
    if not isinstance(order_id, str) or ORDER_ID.fullmatch(order_id) is None:
        return _refuse("binding_order_id", "extra.orderId %r is not 22-128 of A-Za-z0-9_- "
                       "(x402-gateway src/nano.js:167)" % (order_id,))
    key = _key(seller_url, accept["payTo"], amount, order_id)
    if _replayed(journal, key):
        return _refuse("replayed", "this order is already in the journal: " + key)
    rep = order_representative(order_id, accept["payTo"], amount)
    header = "X-PAYMENT" if version == 1 else "PAYMENT-SIGNATURE"
    steps = ["publish a send of amount_raw to payTo from the caller's wallet with representative = %s "
             "(the block's representative field; any other representative and the seller refuses the block)"
             % rep,
             "wait until the send block is confirmed on a public node",
             "journal the hash with orderId %s before retrying, so a crash re-presents it instead of paying "
             "again" % order_id,
             "retry the request with %s: base64 x402 v%s payload whose payload.orderId = %s and "
             "payload.blockHash = <the send's hash>, accepted = this accepts entry"
             % (header, version or 2, order_id)]
    return {"ok": True, "dialect": "rep-binding", "x402Version": version, "network": net,
            "network_seen": accept.get("network"), "network_mapped": mapped,
            "amount_raw": amount, "payTo": accept["payTo"], "work_threshold": None,
            "binding": REP_BINDING, "orderId": order_id, "representative": rep,
            "proof": {"header": header, "field": "payload.orderId + payload.blockHash (published, confirmed "
                                                 "send whose representative is the plan's representative)"},
            "steps": steps, "journal_key": key}


def _flat_terms(doc):
    """send-hash and invoice quotes: terms at the top level or under `payment`."""
    inner = doc.get("payment") if isinstance(doc.get("payment"), dict) else {}
    merged = dict(doc)
    merged.update(inner)
    return merged


def _plan_flat(dialect, doc, cap_raw, seller_url, journal):
    t = _flat_terms(doc)
    net, mapped = _network(t.get("network"))
    if net is None:
        return _refuse("wrong_network", "network %r is not Nano mainnet" % t.get("network"))
    pay_to = t.get("pay_to") or t.get("payTo")
    if not nano_checksum_ok(pay_to):
        return _refuse("bad_checksum", "pay_to %r fails the Nano checksum" % pay_to)
    if dialect == "send-hash":
        amount = t.get("amount_raw") or t.get("price_raw")
    else:
        amount = t.get("price_raw") or t.get("base_price_raw")
    bad = _amount_cap(amount, cap_raw)
    if bad:
        return bad
    nonce = str(t.get("invoice_id") or t.get("nonce") or "")
    key = _key(seller_url, pay_to, amount, nonce)
    if _replayed(journal, key):
        return _refuse("replayed", "this quote is already in the journal: " + key)
    plan = {"ok": True, "dialect": dialect, "x402Version": None, "network": net,
            "network_seen": t.get("network"), "network_mapped": mapped,
            "amount_raw": str(amount), "payTo": pay_to, "work_threshold": None,
            "journal_key": key}
    if dialect == "send-hash":
        header = _header_name(t.get("retry_header") or t.get("pay_header")) or "X-Nano-Payment"
        plan["proof"] = {"header": header, "field": "send block hash, after the send is confirmed"}
        plan["steps"] = ["publish a send of amount_raw to payTo from the caller's wallet",
                         "wait until the send block is confirmed on a public node",
                         "journal the hash before retrying, so a crash re-presents it instead of paying again",
                         "retry the request with %s: <hash>" % header]
    else:
        nxt = t.get("next") if isinstance(t.get("next"), str) else ""
        paths = re.findall(r"POST\s+(/[^\s,;]+)", nxt)
        plan["invoice_create"] = paths[0] if paths else None
        plan["invoice_result"] = paths[1] if len(paths) > 1 else None
        plan["proof"] = {"header": None, "field": "invoice_id, payment_hash, invoice_token (POST body)"}
        plan["steps"] = ["POST %s to create an invoice" % (plan["invoice_create"] or "<create path>"),
                         "re-plan on the invoice's price_raw (amount_raw here is the base price, a floor)",
                         "publish a send of exactly price_raw to pay_to; wait for confirmation",
                         "POST %s with invoice_id, payment_hash and invoice_token"
                         % (plan["invoice_result"] or "<result path>")]
    return plan


def _plan_accept(accept, version, cap_raw, seller_url, journal, raw_extra):
    """An exact accept: bound (extra carries `binding`, well-formed or not) or plain."""
    if isinstance(raw_extra, dict) and "binding" in raw_extra:
        return _plan_bound(accept, version, cap_raw, seller_url, journal, raw_extra)
    return _plan_exact(accept, version, cap_raw, seller_url, journal, raw_extra)


def plan_402(headers, body, cap_raw=DEFAULT_CAP_RAW, seller_url="", journal=None):
    p = parse_402(headers, body)
    d = dialect_of(p)
    if d in ("exact", "rep-binding"):
        raw = []
        doc = p.get("body_json") if p["where"] == "body" else None
        if p["where"] and p["where"].startswith("header:"):
            try:
                doc = json.loads(base64.b64decode(_header(headers, p["where"][7:])).decode("utf-8"))
            except (ValueError, UnicodeDecodeError, TypeError, RecursionError):
                doc = None
        if isinstance(doc, dict) and isinstance(doc.get("accepts"), list):
            raw = [a for a in doc["accepts"] if isinstance(a, dict)]
        first = None
        for i, a in enumerate(p["accepts"]):
            if a.get("scheme") != "exact":
                continue
            extra = raw[i].get("extra") if i < len(raw) else None
            r = _plan_accept(a, p["x402Version"], cap_raw, seller_url, journal, extra)
            if r["ok"]:
                return r
            first = first or r
        return first
    flat = None
    if d in ("send-hash", "invoice") and isinstance(p.get("body_json"), dict):
        flat = _plan_flat(d, p["body_json"], cap_raw, seller_url, journal)
        if flat["ok"]:
            return flat
    if p["accepts"]:
        # an accepts list with no `exact` entry, e.g.
        # {"scheme": "nano-send-hash", ...}, is refused by its scheme; nothing is signed for it
        # (nano-pay's fallback signs an exact payload for nano_offers[0], x402.py:268-275).
        schemes = sorted({str(a.get("scheme")) for a in p["accepts"]})
        return _refuse("scheme", "scheme %s in accepts: only exact is planned from accepts"
                       % ", ".join(schemes))
    if flat is not None:
        return flat
    return _refuse("unknown_shape", "dialect %s: no terms this client can read" % d)


# --- x402 MCP transport --------------
# Spec: coinbase/x402 specs/transports-v2/mcp.md. The quote is a tools/call result with
# isError true and a PaymentRequired object in structuredContent (or JSON in content[0].text);
# the payment goes back in params._meta["x402/payment"] (a PaymentPayload OBJECT); settlement
# comes in result._meta["x402/payment-response"].
# xmcp (basementstudio/xmcp packages/plugins/x402, read 2026-11-21 at HEAD) differs in two ways
# a buyer must follow: the _meta value is decoded with decodePaymentSignatureHeader (a BASE64
# string, verify.ts:154), and its Nano check reads payload.blockHash of a send the payer already
# published (verify.ts verifyNano), not a signed unpublished block. Its v1 offer names the
# network "nano" (the config name, verify.ts createPaymentRequirements). Its offer is recognised
# by extra == {"name": "XNO", "decimals": 30} (constants.ts NETWORKS.nano).

MCP_PAYMENT_META = "x402/payment"
MCP_RESPONSE_META = "x402/payment-response"
XMCP_NANO_EXTRA = {"name": "XNO", "decimals": 30}


def _as_json(x):
    if isinstance(x, (bytes, bytearray)):
        x = x.decode("utf-8", "replace")
    if isinstance(x, str):
        try:
            return json.loads(x)
        except (ValueError, RecursionError):
            # RecursionError: a deeply nested array from a seller
            return None
    return x


def _is_payment_required(doc):
    return isinstance(doc, dict) and "x402Version" in doc and isinstance(doc.get("accepts"), list)


def mcp_payment_required(message):
    """A JSON-RPC response, its `result`, or JSON text of either -> (PaymentRequired, where).

    where is "structuredContent" or "content[0].text"; on failure (None, <reason>). Never raises."""
    msg = _as_json(message)
    if not isinstance(msg, dict):
        return None, "the message is not a JSON object"
    result = msg["result"] if isinstance(msg.get("result"), dict) else msg
    if result.get("isError") is not True:
        return None, "the tool result is not isError true, so it asks for no payment"
    sc = result.get("structuredContent")
    if _is_payment_required(sc):
        return sc, "structuredContent"
    content = result.get("content")
    if isinstance(content, list) and content and isinstance(content[0], dict) \
            and content[0].get("type") == "text":
        doc = _as_json(content[0].get("text"))
        if _is_payment_required(doc):
            return doc, "content[0].text"
    return None, "no PaymentRequired (x402Version + accepts) in structuredContent or content[0].text"


def mcp_settlement(message):
    """result._meta["x402/payment-response"] of a paid tools/call response, or None."""
    msg = _as_json(message)
    if not isinstance(msg, dict):
        return None
    result = msg["result"] if isinstance(msg.get("result"), dict) else msg
    meta = result.get("_meta")
    if isinstance(meta, dict) and isinstance(meta.get(MCP_RESPONSE_META), dict):
        return meta[MCP_RESPONSE_META]
    return None


def plan_mcp(message, cap_raw=DEFAULT_CAP_RAW, seller_url="", journal=None, profile=None):
    """Plan one MCP Payment Required tool result. profile: "spec" (default) or "xmcp".

    The profile is never guessed: the xmcp profile publishes
    the send BEFORE the seller verifies, so a wrong guess costs the amount, while a wrong "spec" costs
    nothing. An offer that looks like xmcp's (its NETWORKS.nano extra) only sets "profile_hint"."""
    pr, where = mcp_payment_required(message)
    if pr is None:
        return _refuse("unknown_shape", where)
    accepts = [a for a in pr["accepts"] if isinstance(a, dict)]
    hint = "xmcp" if any(isinstance(a.get("extra"), dict) and
                         all(a["extra"].get(k) == v for k, v in XMCP_NANO_EXTRA.items())
                         for a in accepts) else None
    r = _plan_mcp_profile(pr, where, accepts, cap_raw, seller_url, journal,
                          "spec" if profile is None else profile)
    if hint:
        r = dict(r, profile_hint=hint)
    return r


def _plan_mcp_profile(pr, where, accepts, cap_raw, seller_url, journal, profile):
    if profile not in ("spec", "xmcp"):
        return _refuse("unknown_shape", "profile %r is neither spec nor xmcp" % profile)
    version = pr.get("x402Version")
    first = None
    for a in accepts:
        if a.get("scheme") != "exact":
            continue
        seen = a.get("network")
        a2 = dict(a)
        if profile == "xmcp" and version == 1 and seen == "nano":
            a2["network"] = "nano:mainnet"
        extra = a.get("extra") if isinstance(a.get("extra"), dict) else {}
        r = _plan_accept(_norm_accept(a2), version, cap_raw, seller_url, journal, extra)
        if r["ok"]:
            return _mcp_rewrite(r, profile, where, seen, version)
        first = first or r
    return first or _refuse("unknown_shape", "no exact accepts entry in the PaymentRequired")


def _mcp_rewrite(plan, profile, where, seen, version):
    plan = dict(plan)
    plan.update({"transport": "mcp", "profile": profile, "mcp_where": where,
                 "network_seen": seen, "network_mapped": seen != "nano:mainnet",
                 "settlement_meta": MCP_RESPONSE_META})
    ver = version or 2
    if plan["dialect"] == "rep-binding":
        # a bound send is published before it is presented under either profile: the seller reads the
        # confirmed block and its representative (x402-gateway src/nano.js:303-310)
        enc = "object" if profile == "spec" else "base64"
        plan["proof"] = {"header": None, "meta_key": MCP_PAYMENT_META, "encoding": enc,
                         "field": "PaymentPayload: x402Version, accepted, payload.orderId + payload.blockHash "
                                  "(published send whose representative is the plan's representative)"}
        steps = [s for s in plan["steps"] if not s.startswith("retry the request")]
        steps.append("retry the same tools/call with params._meta[%r] = %s the x402 v%s PaymentPayload "
                     "whose payload.orderId = %s and payload.blockHash = the send's hash"
                     % (MCP_PAYMENT_META, "the" if enc == "object" else "base64 of", ver, plan["orderId"]))
    elif profile == "spec":
        plan["proof"] = {"header": None, "meta_key": MCP_PAYMENT_META, "encoding": "object",
                         "field": "PaymentPayload object: x402Version, accepted, payload.block (signed send block)"}
        steps = [s for s in plan["steps"] if not s.startswith("retry the request")]
        steps.append("retry the same tools/call with params._meta[%r] = the x402 v%s PaymentPayload "
                     "object (not base64) holding the signed block" % (MCP_PAYMENT_META, ver))
    else:
        plan["proof"] = {"header": None, "meta_key": MCP_PAYMENT_META, "encoding": "base64",
                         "field": "base64 JSON PaymentPayload: x402Version, accepted, payload.blockHash (published send)"}
        steps = ["publish a send of amount_raw to payTo from the caller's wallet",
                 "wait until the send block is confirmed on a public node",
                 "journal the hash before retrying, so a crash re-presents it instead of paying again",
                 "retry the same tools/call with params._meta[%r] = base64 of the x402 v%s "
                 "PaymentPayload JSON whose payload.blockHash is the send's hash" % (MCP_PAYMENT_META, ver)]
    steps.append("read the settlement from result._meta[%r]" % MCP_RESPONSE_META)
    plan["steps"] = steps
    return plan


def journal_record(journal, plan):
    """Add a successful plan's key to a set or dict journal. Returns the key."""
    if not plan.get("ok"):
        raise ValueError("only a plan with ok True is journalled")
    k = plan["journal_key"]
    if isinstance(journal, dict):
        journal[k] = plan["amount_raw"]
    else:
        journal.add(k)
    return k


def main(argv):
    if len(argv) not in (2, 3):
        print(__doc__.strip().splitlines()[-1])
        return 2
    cap = argv[2] if len(argv) == 3 else DEFAULT_CAP_RAW
    with open(argv[1]) as f:
        fixtures = json.load(f)
    n = 0
    for fx in fixtures:
        if "mcp" in fx:
            r = plan_mcp(fx["mcp"], cap, fx.get("id", ""), None, fx.get("profile"))
        else:
            r = plan_402(fx.get("headers") or {}, fx.get("body"), cap, fx.get("id", ""))
        n += 1 if r["ok"] else 0
        if r["ok"] and r.get("transport") == "mcp":
            how = "_meta[%s] %s (%s)" % (r["proof"]["meta_key"], r["proof"]["encoding"], r["profile"])
        else:
            how = r["proof"]["header"] if r["ok"] else None
        print("%-28s %s" % (fx.get("id"), ("plan %s %s raw -> %s" % (r["dialect"], r["amount_raw"], how))
              if r["ok"] else "refused " + r["error"]))
    print("planned", n, "of", len(fixtures))
    return 0


def plan_quote(quote, cap_raw=DEFAULT_CAP_RAW, seller_url="", journal=None, profile=None):
    """One quote of any shape this module knows -> plan or refusal. Never raises.

    {"headers": {...}, "body": ...} is an HTTP 402; {"mcp": <tools/call response>} or a bare
    JSON-RPC response / tool result is MCP. A JSON string of any of these is read first."""
    q = _as_json(quote)
    if isinstance(q, dict) and ("headers" in q or "body" in q) and "mcp" not in q:
        body = q.get("body")
        r = plan_402(q.get("headers") if isinstance(q.get("headers"), dict) else {}, body,
                     cap_raw, seller_url, journal)
    elif isinstance(q, dict) and "mcp" in q:
        r = plan_mcp(q["mcp"], cap_raw, seller_url, journal, profile or q.get("profile"))
    else:
        r = plan_mcp(q, cap_raw, seller_url, journal, profile)
    if r.get("ok"):  # the call each outside wallet needs
        r = dict(r, wallet_calls=wallet_calls(r, q, seller_url))
    return r


def cli(argv=None):
    """Console script `xno-buyer-plan QUOTE.json [--cap RAW] [--profile spec|xmcp] [--seller URL]`.

    Prints the plan (or the named refusal) as JSON; exit 0 planned, 1 refused, 2 usage.
    A file holding a JSON list is read as a fixtures file, as plan.py always did."""
    import argparse
    ap = argparse.ArgumentParser(prog="xno-buyer-plan", description="Plan one unpaid Nano x402 quote. "
                                 "No network, no key, no signing: it prints what a wallet must send.")
    ap.add_argument("quote", help="JSON file: an HTTP 402 {headers, body}, an MCP tools/call response, "
                    "or a list of fixtures; - reads stdin")
    ap.add_argument("--cap", default=DEFAULT_CAP_RAW, help="largest amount in raw (default 0.1 XNO)")
    ap.add_argument("--profile", choices=("spec", "xmcp"), default=None)
    ap.add_argument("--seller", default="", help="seller URL, for the journal key")
    a = ap.parse_args(sys.argv[1:] if argv is None else argv)
    try:
        if a.quote == "-":
            text = sys.stdin.read()
        else:
            with open(a.quote) as f:
                text = f.read()
    except OSError as e:
        print(json.dumps(_refuse("unknown_shape", "cannot read %s: %s" % (a.quote, e))))
        return 2
    q = _as_json(text)
    if isinstance(q, list):
        return main(["plan.py", a.quote, a.cap]) if a.quote != "-" else 2
    r = plan_quote(q, a.cap, a.seller, None, a.profile)
    print(json.dumps(r, indent=2, sort_keys=True))
    return 0 if r.get("ok") else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
