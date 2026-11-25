"""Read one Nano (XNO) HTTP 402 quote in the dialects sellers use today.

x402 v2 (a base64 JSON PAYMENT-REQUIRED header), x402 v1 (the JSON body, maxAmountRequired), the bound
order xno-binding/v1/rep (extra.binding and extra.orderId on an exact accept), and the send-hash quote
(pay first, present the hash). Also: the nano_ address checksum (blake2b-40 of the key) and the account of
a public key. Pure functions, standard library only: no network, no key, no signing. plan.py builds on
parse_402; the client table helpers (load_clients) need a clients.json that this folder does not ship.
"""
import base64
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
HEADER_NAMES = ("PAYMENT-REQUIRED", "X-PAYMENT-REQUIRED")
ALPHABET = "13456789abcdefghijkmnopqrstuwxyz"
REP_BINDING = "xno-binding/v1/rep"  # x402-gateway src/nano.js:166 BINDING
ORDER_ID = re.compile(r"[A-Za-z0-9_-]{22,128}")  # src/nano.js:167, fullmatch


def load_clients(path=None, include_pending=False):
    """Clients that install today. A client with a `pending` key (a fix on a branch, not merged or
    released) is left out unless include_pending is True, so a count never credits unmerged code."""
    with open(path or os.path.join(HERE, "clients.json")) as f:
        data = json.load(f)
    return {k: v for k, v in data.items()
            if not k.startswith("_") and (include_pending or "pending" not in v)}


def nano_checksum_ok(address):
    """True when a nano_/xrb_ address's 8-char checksum is blake2b-40 of its key (reversed)."""
    if not isinstance(address, str):
        return False
    for prefix in ("nano_", "xrb_"):
        if address.startswith(prefix):
            rest = address[len(prefix):]
            break
    else:
        return False
    if len(rest) != 60 or any(c not in ALPHABET for c in rest):
        return False
    bits = "".join(format(ALPHABET.index(c), "05b") for c in rest)
    key_bits, check_bits = bits[4:260], bits[260:]
    if bits[:4] != "0000":
        return False
    key = int(key_bits, 2).to_bytes(32, "big")
    check = int(check_bits, 2).to_bytes(5, "big")
    return hashlib.blake2b(key, digest_size=5).digest()[::-1] == check


def account_from_key(key):
    """32 bytes -> the nano_ account that encodes them: the key as 52 base32 chars (4 zero bits first),
    then blake2b-40 of the key, byte-reversed, as 8 chars. The inverse of nano_checksum_ok's decode;
    x402-gateway 0.18.2 src/nano.js:112, :117-121 (encode32), :130 (checksumOf), :133-141 (accountFromKey)."""
    if not isinstance(key, (bytes, bytearray)) or len(key) != 32:
        raise ValueError("an account is 32 bytes")
    k = int.from_bytes(bytes(key), "big")
    c = int.from_bytes(hashlib.blake2b(bytes(key), digest_size=5).digest()[::-1], "big")
    enc = lambda v, n: "".join(ALPHABET[(v >> (5 * i)) & 31] for i in range(n - 1, -1, -1))  # noqa: E731
    return "nano_" + enc(k, 52) + enc(c, 8)


def _header(headers, name):
    for k, v in (headers or {}).items():
        if k.lower() == name.lower():
            return v
    return None


def _json(text):
    if isinstance(text, (dict, list)):
        return text
    if isinstance(text, bytes):
        text = text.decode("utf-8", "replace")
    try:
        return json.loads(text)
    except (TypeError, ValueError, RecursionError):  # RecursionError: deeply nested body
        return None


def _norm_accept(a):
    amount, mar = a.get("amount"), a.get("maxAmountRequired")
    if amount is not None and mar is not None and str(amount) != str(mar):
        amount_raw = None
        ambiguous = True
    else:
        amount_raw = str(amount if amount is not None else mar) if (amount is not None or mar is not None) else None
        ambiguous = False
    pay_to = a.get("payTo")
    out = {
        "scheme": a.get("scheme"),
        "network": a.get("network"),
        "asset": a.get("asset"),
        "amount_raw": amount_raw,
        "amount_ambiguous": ambiguous,
        "payTo": pay_to,
        "payTo_checksum_valid": nano_checksum_ok(pay_to),
        "has_extra": isinstance(a.get("extra"), dict),
        "keys": sorted(k for k in a if isinstance(k, str)),
    }
    if rep_binding_of(a):
        out["binding"] = REP_BINDING  # only then, so every other accept normalises exactly as before
    elif isinstance(a.get("extra"), dict) and "binding" in a["extra"]:
        # a binding this table cannot build (unknown name, or no well-formed orderId): read only by a row
        # with `bindings` (buyer_plan refuses it by name); every other row sees the accept as before
        out["binding_malformed"] = True
    return out


def rep_binding_of(a):
    """True when a raw accept carries xno-binding/v1/rep in extra: binding AND a well-formed orderId
    (x402-gateway src/x402.js:140 sets both together; src/nano.js:167 ORDER_ID)."""
    extra = a.get("extra") if isinstance(a, dict) else None
    if not isinstance(extra, dict) or extra.get("binding") != REP_BINDING:
        return False
    oid = extra.get("orderId")
    return isinstance(oid, str) and ORDER_ID.fullmatch(oid) is not None


def parse_402(headers, body):
    """Where the terms are, their version, and the normalised accepts list. Never raises."""
    out = {"where": None, "x402Version": None, "accepts": [], "parsed": False, "body_json": None,
           "has_resource": False}
    for name in HEADER_NAMES:
        raw = _header(headers, name)
        if raw is None:
            continue
        out["where"] = "header:" + name
        try:
            # a saved capture can hold a number or a list as a header value: undecodable, not a crash
            #
            doc = json.loads(base64.b64decode(raw.strip(), validate=True).decode("utf-8")) \
                if isinstance(raw, str) else None
        except (ValueError, UnicodeDecodeError, TypeError, RecursionError):
            doc = None
        if isinstance(doc, dict) and isinstance(doc.get("accepts"), list):
            out["x402Version"] = doc.get("x402Version")
            out["accepts"] = [_norm_accept(a) for a in doc["accepts"] if isinstance(a, dict)]
            out["parsed"] = True
            out["has_resource"] = "resource" in doc
        out["body_json"] = _json(body)
        return out
    doc = _json(body)
    out["body_json"] = doc
    if body is not None and body != "":
        out["where"] = "body"
    if isinstance(doc, dict) and isinstance(doc.get("accepts"), list):
        out["x402Version"] = doc.get("x402Version")
        out["accepts"] = [_norm_accept(a) for a in doc["accepts"] if isinstance(a, dict)]
        out["parsed"] = True
        out["has_resource"] = "resource" in doc
    return out


MCP_WHERE = ("mcp:structuredContent", "mcp:content[0].text")


def _is_terms(doc):
    return isinstance(doc, dict) and "x402Version" in doc and isinstance(doc.get("accepts"), list)


def parse_mcp(body):
    """An MCP payment-required tool result -> the parse_402 shape with where "mcp:...", plus "doc" (the
    terms object). None when the body is no such result. Never raises.

    Follows @x402/mcp 2.32.0 extractPaymentRequiredFromResult (dist/esm/index.mjs:714-742): only an
    isError result; structuredContent first, then JSON in content[0].text. A JSON-RPC envelope
    ({"jsonrpc", "id", "result"}) or a bare tool result are both read."""
    doc = _json(body)
    if not isinstance(doc, dict):
        return None
    res = doc.get("result") if isinstance(doc.get("result"), dict) else doc
    if res.get("isError") is not True:
        return None
    terms, where = None, None
    if _is_terms(res.get("structuredContent")):
        terms, where = res["structuredContent"], MCP_WHERE[0]
    else:
        content = res.get("content")
        first = content[0] if isinstance(content, list) and content else None
        if isinstance(first, dict) and first.get("type") == "text" and isinstance(first.get("text"), str):
            inner = _json(first["text"])
            if _is_terms(inner):
                terms, where = inner, MCP_WHERE[1]
    if terms is None:
        return None
    return {"where": where, "x402Version": terms.get("x402Version"),
            "accepts": [_norm_accept(a) for a in terms["accepts"] if isinstance(a, dict)],
            "parsed": True, "body_json": terms, "has_resource": "resource" in terms, "doc": terms}


def bridge_header(doc):
    """What a host bridge hands a header-only wallet: base64 of the terms' JSON (kilkelly-mcp's
    x402_payment_required_header argument)."""
    return base64.b64encode(json.dumps(doc, separators=(",", ":")).encode("utf-8")).decode("ascii")


def client_view(client, p, mcp, buyer=None):
    """(terms as this client is handed them, None) or (None, verdict) when it is refused before any field
    is read. `p` is parse_402's view, `mcp` parse_mcp's (or None)."""
    if mcp is None or p["parsed"]:
        return p, None
    if any(w in MCP_WHERE for w in client["where"]):
        return mcp, None
    handoff = (buyer or {}).get("mcp_handoff")
    if client.get("mcp_bridge") and handoff == "raw":
        return None, "no:bridge"  # an object where a base64 string argument is required
    if client.get("mcp_bridge") and handoff == client["mcp_bridge"]:
        bridged = parse_402({HEADER_NAMES[0]: bridge_header(mcp["doc"])}, None)
        bridged["doc"] = mcp["doc"]
        return bridged, None
    return p, None


def _glob(pattern, value):
    if not isinstance(pattern, str) or not isinstance(value, str):
        return False
    return re.fullmatch(".*".join(re.escape(s) for s in pattern.split("*")), value) is not None


def _usd_to_atomic(money, decimals):
    """@x402/core 2.32.0 parseMoney + convertToTokenAmount (chunk-XW2CWVLZ.mjs:22-60): "$1", "1", "1.5",
    "2 USD" -> the decimal string padded/truncated to `decimals`; anything else throws (None here)."""
    if isinstance(money, bool) or not isinstance(money, (str, int)):
        return None
    m = re.fullmatch(r"\$?\s*(\d+(?:\.\d+)?)(?:\s+(USD))?", str(money).strip(), re.I)
    if not m:
        return None
    whole, _, frac = m.group(1).partition(".")
    return int((whole + frac.ljust(decimals, "0")[:decimals]).lstrip("0") or "0")


def default_asset_for(accept, default_asset):
    """A scheme client's findDefaultAsset (clients.json `default_asset`):
    asset EXACTLY "XNO" (case-sensitive)
    on a network that starts with "nano:" -> {asset XNO, decimals 30, symbol XNO}; else undefined."""
    if not default_asset:
        return None
    asset, net = accept.get("asset"), accept.get("network")
    if asset == default_asset["asset"] and isinstance(net, str) and net.startswith(default_asset["network_prefix"]):
        return default_asset
    return None


def spend_controls_ok(accept, buyer=None, default_asset=None):
    """@x402/core 2.32.0 applySpendControls: client/index.mjs:25-57 (asset entry, atomic cap, the default
    "$1" cap read in the default asset's decimals), :503-527 (allowlist: a default asset passes),
    :528-575 (cap). With no default asset (ExactNanoScheme 1.1.0) {} refuses every Nano accept."""
    sc = (buyer or {}).get("spendControls", {})
    if sc is False:
        return True
    if not isinstance(sc, dict):
        sc = {}
    da = default_asset_for(accept, default_asset)
    allow_any = sc.get("allowedAssets") is True
    entries = sc.get("allowedAssets") if isinstance(sc.get("allowedAssets"), list) else []
    asset = accept.get("asset")

    def matches(e):
        if not (isinstance(e, dict) and _glob(e.get("network"), accept.get("network"))
                and isinstance(e.get("asset"), str) and isinstance(asset, str)):
            return False
        return e["asset"].lower() == asset.lower() or (da is not None and da["symbol"].lower() == e["asset"].lower())

    entry = None if allow_any else next((e for e in entries if matches(e)), None)
    if not allow_any and da is None and entry is None:
        return False
    amt = accept.get("amount_raw")
    atomic_amt = amt is not None and re.fullmatch(r"[0-9]+", str(amt)) is not None
    cap = entry.get("maxAmountPerPayment") if entry else None
    if cap is not None:
        if not re.fullmatch(r"[0-9]+", str(cap)) or not atomic_amt:
            return False  # core throws on a non-atomic cap (:44-49) and refuses a non-atomic amount (:540-544)
        return int(amt) <= int(cap)
    usd = sc.get("maxAmountPerPayment", "$1")
    if da is None or usd is False:
        return True
    cap = _usd_to_atomic(usd, da["decimals"])
    if cap is None:
        return False  # parseMoney throws
    if not atomic_amt:  # core :545-550: a decimal amount is compared with the USD cap, both at 18 decimals
        a18, c18 = _usd_to_atomic(amt, 18), _usd_to_atomic(usd, 18)
        return a18 is not None and a18 <= c18
    return int(amt) <= cap


def _text(doc):
    return json.dumps(doc).lower() if doc is not None else ""


def dialect_of(parsed):
    if any(a.get("scheme") == "exact" and a.get("binding") == REP_BINDING for a in parsed["accepts"]):
        return "rep-binding"
    if any(a.get("scheme") == "exact" for a in parsed["accepts"]):
        return "exact"
    t = _text(parsed.get("body_json"))
    if not t:
        return "UNKNOWN"
    if "invoice" in t:
        return "invoice"
    if "x-nano-payment" in t or "nano-send-hash" in t or "send hash" in t or "send_hash" in t:
        return "send-hash"
    if parsed["accepts"]:
        return "other"
    return "UNKNOWN"


def network_ok(accept, client):
    """The client's own network rule. A row with `network_rule` "nano-prefix" keeps any accept whose
    network starts with "nano" or whose asset is xno or nano, case-insensitive. Any other row needs the exact `network` string."""
    if client.get("network_rule") == "nano-prefix":
        net, asset = accept.get("network"), accept.get("asset")
        net = str(net).lower() if net is not None else ""
        asset = str(asset).lower() if asset is not None else ""
        return net.startswith("nano") or asset in ("xno", "nano")
    if client.get("networks") is not None:
        # a row with a list (buyer_plan: plan.py NETWORKS); `bound_networks` are kept only for an accept
        # whose extra names a binding, read or malformed, when the row builds bindings (plan.py
        # BOUND_NETWORKS: x402-gateway names XNO `nano`; a malformed one then fails `binding`, as in plan.py)
        allowed = list(client["networks"])
        if client.get("bindings") and (accept.get("binding") is not None or accept.get("binding_malformed")):
            allowed += client.get("bound_networks") or []
        return isinstance(accept.get("network"), str) and accept["network"] in allowed
    return accept.get("network") == client["network"]


def flat_fit(doc, dialect, client):
    """A send-hash or invoice quote (no accepts list) for a row whose `flat_dialects` names the dialect:
    the terms plan.py _plan_flat reads (top level, or under `payment`), checked in its order: network,
    payTo checksum, amount (ASCII digits, not 0), cap. Only buyer_plan has `flat_dialects`."""
    if not isinstance(doc, dict):
        return "UNKNOWN"
    t = dict(doc)
    if isinstance(doc.get("payment"), dict):
        t.update(doc["payment"])
    if not network_ok({"network": t.get("network")}, client):
        return "no:network"
    if not nano_checksum_ok(t.get("pay_to") or t.get("payTo")):
        return "no:payTo"
    amt = (t.get("amount_raw") or t.get("price_raw")) if dialect == "send-hash" \
        else (t.get("price_raw") or t.get("base_price_raw"))
    cap = client.get("cap_raw")
    if amt is None or not re.fullmatch(r"[0-9]+", str(amt)) or int(amt) == 0 \
            or (cap is not None and int(amt) > int(cap)):
        return "no:cap"
    return "yes"


def client_fit(accept, client, where, buyer=None):
    if accept.get("scheme") != client["scheme"]:
        return "no:scheme"
    if not network_ok(accept, client):
        return "no:network"
    if accept.get("binding") is not None and accept["binding"] not in (client.get("bindings") or []):
        return "no:binding"  # it cannot sign the representative the seller holds the block to
    if accept.get("binding_malformed") and client.get("bindings"):
        return "no:binding"  # a row that builds bindings refuses one it cannot read (plan.py binding_*)
    if where not in client["where"]:
        return "no:where"
    if client.get("asset") is not None and \
            str(accept.get("asset") or "").lower() != str(client["asset"]).lower():
        return "no:asset"
    if client.get("amount_key") is not None and client["amount_key"] not in (accept.get("keys") or []):
        return "no:amount_key"
    if not accept.get("payTo_checksum_valid"):
        return "no:payTo"
    if accept.get("amount_ambiguous"):
        return "no:amount_ambiguous"
    amt = accept.get("amount_raw")
    # ASCII digits only: str.isdigit() accepts '²', which int() then rejects with ValueError, and
    # a 0 raw quote is no send at all
    cap = client.get("cap_raw")
    if amt is None or not re.fullmatch(r"[0-9]+", str(amt)) or int(amt) == 0 \
            or (cap is not None and int(amt) > int(cap)):
        return "no:cap"
    if client.get("spend_controls") and not spend_controls_ok(accept, buyer, client.get("default_asset")):
        return "no:spend_controls"
    if client.get("needs_extra") and not accept.get("has_extra"):
        return "no:extra"
    return "yes"


def _nano_exact(accept):
    """A Nano exact accept: scheme "exact" (as dialect_of requires for rep-binding) on a network that starts
    with "nano", case-insensitive (network_ok's nano-prefix network test; covers plan.py NETWORKS and
    BOUND_NETWORKS: nano:mainnet, nano-mainnet, nano). The asset alone does not make it Nano here."""
    net = accept.get("network")
    return accept.get("scheme") == "exact" and isinstance(net, str) and net.lower().startswith("nano")


def set_rep_blockers(accepts, client):
    """[{"blocker": "no:set_rep", "src": ...}] when `accepts` (normalised) holds a rep-binding accept and the
    row says it cannot set a chosen representative (`"set_rep": false`); else []. See `also` above."""
    if client.get("set_rep") is not False:
        return []
    if not any(a.get("binding") == REP_BINDING and _nano_exact(a) for a in accepts or ()):
        return []
    return [{"blocker": "no:set_rep", "src": client.get("set_rep_src") or "clients.json set_rep false"}]


def verdicts(headers, body, clients=None, buyer=None):
    """`buyer` (default {}): see the module docstring. Without it every row is checked as before.
    `also` is added only when some client has a later blocker (no:set_rep), see the module docstring."""
    clients = clients if clients is not None else load_clients()
    p0 = parse_402(headers, body)
    d = dialect_of(p0)
    mcp = parse_mcp(body) if not p0["parsed"] else None
    payable = {}
    also = {}
    for name, c in clients.items():
        p, refused = client_view(c, p0, mcp, buyer)
        seen = (p or mcp or p0)["accepts"]  # what this client is handed (the MCP terms when refused raw)
        blockers = set_rep_blockers(seen, c)
        if blockers:
            also[name] = blockers
        if refused is not None:
            payable[name] = refused
            continue
        if not p["parsed"] or not p["accepts"]:
            if d in (c.get("flat_dialects") or ()) and p["where"] in c["where"]:
                payable[name] = flat_fit(p.get("body_json"), d, c)
                continue
            payable[name] ={"send-hash": "no:scheme", "invoice": "no:invoice"}.get(d, "UNKNOWN")
            continue
        if c.get("versions") is not None and p["where"] not in c["where"]:
            payable[name] = "no:where"  # it never reads that place, so nothing else there matters
            continue
        if c.get("versions") is not None and p["x402Version"] not in c["versions"]:
            payable[name] = "no:version"
            continue
        if c.get("needs_resource") and not p["has_resource"]:
            payable[name] = "no:resource"
            continue
        fits = [client_fit(a, c, p["where"], buyer) for a in p["accepts"]]
        # no fit: the reason of the first accept on the client's own chain, else of the first with a
        # nano_ payee, else of the first accept (identical for a one-accept quote; the 11th fixture
        # lists USDC before its XNO entry)
        own = [f for f in fits if f not in ("no:scheme", "no:network")]
        nano = [f for f, a in zip(fits, p["accepts"]) if a.get("payTo_checksum_valid")]
        payable[name] = "yes" if "yes" in fits else (own or nano or fits)[0]
    out = {"dialect": d, "where": p0["where"], "x402Version": p0["x402Version"],
           "accepts": p0["accepts"], "payable_by": payable}
    if also:
        out["also"] = also
    if mcp is not None:
        # the MCP-binding view; the keys above stay the HTTP view, as before
        out["mcp"] = {"where": mcp["where"], "x402Version": mcp["x402Version"],
                      "dialect": dialect_of(mcp), "accepts": mcp["accepts"]}
    return out


def signers(clients=None):
    """{row: {signer: entry}} for every row with a `signers` key - informational, never a verdict or a count."""
    clients = load_clients(include_pending=True) if clients is None else clients
    return {k: dict(v["signers"]) for k, v in clients.items() if isinstance(v.get("signers"), dict)}


def count_payable(rows):
    """{client: number of rows whose verdict is yes} - the spec's counts.payable_by."""
    out = {}
    for r in rows:
        for c, v in (r.get("payable_by") or {}).items():
            out[c] = out.get(c, 0) + (1 if v == "yes" else 0)
    return out


def payto_fixed(probe_a, probe_b):
    """False when two probes of one seller name different payTo sets; None with one probe."""
    if probe_a is None or probe_b is None:
        return None
    a = sorted(x.get("payTo") or "" for x in probe_a.get("accepts", []))
    b = sorted(x.get("payTo") or "" for x in probe_b.get("accepts", []))
    return a == b


def main(argv):
    if len(argv) != 2:
        print(__doc__.strip().splitlines()[-1])
        return 2
    with open(argv[1]) as f:
        fixtures = json.load(f)
    clients = load_clients()
    rows = []
    for fx in fixtures:
        v = verdicts(fx.get("headers") or {}, fx.get("body"), clients)
        v["id"] = fx.get("id")
        rows.append(v)
        print("%-28s %-9s %-24s %s" % (v["id"], v["dialect"], v["where"],
                                        " ".join("%s=%s" % kv for kv in sorted(v["payable_by"].items()))))
        for c, bl in sorted((v.get("also") or {}).items()):
            for b in bl:
                print("    also %s %s  [%s]" % (c, b["blocker"], b["src"]))
    print("payable_by", json.dumps(count_payable(rows), sort_keys=True), "of", len(rows))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
