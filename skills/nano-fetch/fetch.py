"""nano_fetch - fetch a URL; when it answers HTTP 402 with a Nano (XNO) quote, pay it once and retry.

A command-line payer for any agent that has a shell tool.
Standard library only. It never holds a key or a seed: the payment is made by a signer hook YOU supply
(`--signer module.attr`), the same contract as middleware.py:

    signer({"network", "payTo", "amount_raw", "representative", "orderId"}) -> 64-hex block hash

The signer publishes a send of amount_raw raw (1 XNO = 10**30 raw) to payTo, with `representative` as the
block's representative field when it is not None (the xno-binding/v1/rep order binding), waits until the
send is confirmed, and returns its hash.

Off unless configured: with no --signer and --journal a 402 is printed and the command exits 3; nothing is
paid. With both, the 402 goes through middleware.settle_402 (xno_buyer_plan's quote reader, the per-call cap,
the run budget summed over the journal, an fsynced intent line before the signer is called, replay refused
from the journal across restarts). Paid quotes:
  - x402 v2 bound order (PAYMENT-REQUIRED header, extra.binding xno-binding/v1/rep): retried with
    PAYMENT-SIGNATURE;
  - x402 v1 bound order (JSON body, maxAmountRequired): retried with X-PAYMENT;
  - a send-hash quote (pay first, present the hash in X-Nano-Payment or the header the quote names): only
    with --allow-unbound, since nothing in it binds the send to this one request.
A paid retry that meets 402 again is returned as is (exit 4); one request never pays twice.

Redirects: a 402 reached through a redirect is refused before anything is signed (redirected_quote; the
refusal names the effective URL, to be fetched directly). The paid retry goes to the quoting URL only, with
redirects off: a 3xx answer to it is returned as is and the proof is never sent to another URL.

    python3 fetch.py URL [--signer mywallet.sign] [--journal pay.jsonl]
        [--cap-raw N] [--budget-raw N] [--allow-unbound] [-X METHOD] [-H 'Name: value']... [-d DATA]
        [-o FILE] [--timeout S]

Exit: 0 a 2xx/3xx answer (paid or not), 1 failed before any payment (another HTTP status or a connection
error; nothing was paid), 2 usage, 3 a 402 not paid (refusal named on stderr), 4 paid and the retry met 402
again, 5 paid but the delivery failed (a connection error, timeout or non-2xx/3xx answer on the paid retry;
stderr names the order and hash to re-present), 6 the journal is corrupt (a torn or malformed line; nothing
signed until a person reconciles it), 7 the journal cannot be locked or opened (nothing signed).
"""
import argparse
import copy
import http.client
import json
import os
import sys
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
from middleware import DEFAULT_CAP_RAW, Journal, load_signer, settle_402  # noqa: E402  (next to this file)


EXIT_OK, EXIT_FAILED_UNPAID, EXIT_USAGE, EXIT_NOT_PAID, EXIT_PAID_402, EXIT_PAID_UNDELIVERED = 0, 1, 2, 3, 4, 5
EXIT_JOURNAL_CORRUPT, EXIT_JOURNAL_UNAVAILABLE = 6, 7

# errors a request can raise once it is sent (URLError and socket timeouts are OSError)
DELIVERY_ERRORS = (OSError, http.client.HTTPException, ValueError)


class Result:
    def __init__(self, status, headers, body, paid=None, refusal=None, delivery_error=None):
        self.status, self.headers, self.body = status, headers, body
        self.paid = paid          # {"orderId", "blockHash", "amount_raw", "header"} when a payment was made
        self.refusal = refusal    # (code, detail) when a 402 was not paid
        self.delivery_error = delivery_error  # words, when paid and the retry raised (status is then None)


def _request(url, method, headers, data, timeout, opener, proof=None):
    """-> (status, headers, body, effective URL after any redirects the opener followed)."""
    req = urllib.request.Request(url, data=data, method=method, headers=dict(headers))
    if proof is not None:
        # Belt and braces: the paid retry's opener follows no redirect, and an unredirected header is never
        # copied onto one (urllib copies ordinary headers to any host a 3xx names).
        req.add_unredirected_header(*proof)
    try:
        resp = opener.open(req, timeout=timeout)
    except urllib.error.HTTPError as e:  # 402 and every other non-2xx arrive here
        body = e.read()
        return e.code, {k: v for k, v in e.headers.items()}, body, e.geturl() or req.full_url
    with resp:
        return resp.status, {k: v for k, v in resp.headers.items()}, resp.read(), resp.geturl() or req.full_url


def _without_redirects(opener):
    """A copy of opener that follows no redirect: a 3xx comes back as the answer itself."""
    o = urllib.request.OpenerDirector()
    for h in opener.handlers:
        if not isinstance(h, urllib.request.HTTPRedirectHandler):
            o.add_handler(copy.copy(h))
    return o


def fetch(url, signer=None, journal_path=None, cap_raw=DEFAULT_CAP_RAW, budget_raw=None, method="GET",
          headers=None, data=None, timeout=30, allow_unbound=False, opener=None):
    """Fetch url; pay one Nano 402 when signer and journal_path are both given. Returns a Result."""
    opener = opener or urllib.request.build_opener()
    headers = dict(headers or {})
    status, rh, body, effective = _request(url, method, headers, data, timeout, opener)
    if status != 402:
        return Result(status, rh, body)
    if signer is None or not journal_path:
        return Result(status, rh, body, refusal=("not_configured", "a 402 needs --signer and --journal to be "
                                                 "paid; nothing was paid"))
    if effective != urllib.request.Request(url).full_url:
        # The quote came from another URL than the one asked for. Paying it would mean retrying a URL that
        # did not quote, or sending the proof somewhere the caller did not name: refuse before signing.
        return Result(status, rh, body, refusal=("redirected_quote", "the 402 came after a redirect to %s; "
                                                 "nothing was paid; fetch that URL directly to pay it"
                                                 % effective))
    cap_raw = str(int(cap_raw))
    budget_raw = int(budget_raw) if budget_raw is not None else 10 * int(cap_raw)
    r = settle_402(rh, body, url, signer, Journal(journal_path), cap_raw, budget_raw,
                   allow_unbound=allow_unbound)
    if not r["ok"]:
        return Result(status, rh, body, refusal=(r["error"], r["detail"]))
    name, value = r["header"]
    plan = r["plan"]
    paid = {"orderId": plan.get("orderId"), "blockHash": r["blockHash"], "amount_raw": plan["amount_raw"],
            "header": name}
    try:
        status, rh, body, _ = _request(url, method, headers, data, timeout, _without_redirects(opener),
                                       proof=(name, value))
    except DELIVERY_ERRORS as e:
        # paid and journalled: the payment must still be reported, with what is needed to re-present it
        return Result(None, {}, b"", paid=paid, delivery_error="%s: %s" % (type(e).__name__, e))
    refusal = None
    if status == 402:
        refusal = ("paid_retry_402", "the paid retry met 402 again; not paying twice for one request")
    return Result(status, rh, body, paid=paid, refusal=refusal)


def _parse_header(text):
    name, sep, value = text.partition(":")
    if not sep or not name.strip():
        raise argparse.ArgumentTypeError("header %r is not 'Name: value'" % text)
    return name.strip(), value.strip()


def _digits(text):
    if not text.isascii() or not text.isdigit():
        raise argparse.ArgumentTypeError("%r is not a raw amount in digits (1 XNO = 10**30 raw)" % text)
    return text


def main(argv=None, out=None, err=None):
    out = out or sys.stdout.buffer
    err = err or sys.stderr
    ap = argparse.ArgumentParser(prog="nano_fetch", description=__doc__.split("\n\n")[0])
    ap.add_argument("url")
    ap.add_argument("--signer", help="module.attr of your signer; the key lives only there")
    ap.add_argument("--journal", help="JSON-lines journal file; replays are refused from it across runs")
    ap.add_argument("--cap-raw", type=_digits, default=DEFAULT_CAP_RAW, help="per-call cap in raw")
    ap.add_argument("--budget-raw", type=_digits, help="total over the journal in raw (default 10 x cap)")
    ap.add_argument("--allow-unbound", action="store_true", help="also pay a send-hash quote (no binding)")
    ap.add_argument("-X", "--request", dest="method", default=None)
    ap.add_argument("-H", "--header", action="append", type=_parse_header, default=[])
    ap.add_argument("-d", "--data")
    ap.add_argument("-o", "--output")
    ap.add_argument("--timeout", type=float, default=30)
    try:
        a = ap.parse_args(argv)
    except SystemExit as e:
        return 2 if e.code else 0
    if not a.url.startswith(("http://", "https://")):
        print("nano_fetch: only http:// and https:// URLs", file=err)
        return 2
    if bool(a.signer) != bool(a.journal):
        print("nano_fetch: --signer and --journal go together (a payment without a journal could repeat)",
              file=err)
        return 2
    try:
        signer = load_signer(a.signer) if a.signer else None
    except Exception as e:  # noqa: BLE001 - an unloadable signer is a usage error, never a payment
        print("nano_fetch: cannot load signer %r: %s" % (a.signer, e), file=err)
        return 2
    data = a.data.encode("utf-8") if a.data is not None else None
    method = a.method or ("POST" if data is not None else "GET")
    try:
        r = fetch(a.url, signer=signer, journal_path=a.journal, cap_raw=a.cap_raw, budget_raw=a.budget_raw,
                  method=method, headers=dict(a.header), data=data, timeout=a.timeout,
                  allow_unbound=a.allow_unbound)
    except DELIVERY_ERRORS as e:  # only before any payment: fetch catches every error after the signer
        print("nano_fetch: nothing was paid: %s" % e, file=err)
        return EXIT_FAILED_UNPAID
    if r.paid:
        print("nano_fetch: paid %s raw, order %s, hash %s, presented in %s"
              % (r.paid["amount_raw"], r.paid["orderId"], r.paid["blockHash"], r.paid["header"]), file=err)
    if r.paid and r.delivery_error:
        print("nano_fetch: paid but delivery failed: %s; order %s, hash %s is in the journal; re-present "
              "that hash for that order, never pay it again" % (r.delivery_error, r.paid["orderId"],
                                                                r.paid["blockHash"]), file=err)
        return EXIT_PAID_UNDELIVERED
    if r.refusal:
        print("nano_fetch: 402 not paid: %s (%s)" % r.refusal, file=err)
    if a.output:
        with open(a.output, "wb") as f:
            f.write(r.body)
    else:
        out.write(r.body)
        out.flush()
    if r.status == 402:
        if r.paid:
            return EXIT_PAID_402
        if r.refusal and r.refusal[0] == "journal_corrupt":
            return EXIT_JOURNAL_CORRUPT
        if r.refusal and r.refusal[0] == "journal_unavailable":
            return EXIT_JOURNAL_UNAVAILABLE
        return EXIT_NOT_PAID
    if 200 <= r.status < 400:
        return EXIT_OK
    if r.paid:
        print("nano_fetch: paid but delivery failed: the paid retry answered %d; order %s, hash %s is in the "
              "journal; re-present it, never pay it again" % (r.status, r.paid["orderId"], r.paid["blockHash"]),
              file=err)
        return EXIT_PAID_UNDELIVERED
    return EXIT_FAILED_UNPAID


if __name__ == "__main__":
    sys.exit(main())
