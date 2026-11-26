"""Tests for the nano-fetch skill, against a loopback seller only. No network, no key, nothing to install.

    python3 -m unittest discover -s skills/nano-fetch -p 'test_*.py'
"""
import base64
import http.server
import io
import json
import os
import socket
import sys
import tempfile
import threading
import time
import types
import unittest
import unittest.mock
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import fetch as nf  # noqa: E402
import middleware as mw  # noqa: E402
from xno_buyer_plan.plan import order_representative  # noqa: E402

RAW_PER_XNO = 10 ** 30
PRICE = str(5 * RAW_PER_XNO // 4)  # 1.25 XNO in raw, derived
CAP = str(2 * RAW_PER_XNO)
HASH = "ab" * 32
PAY_TO = "nano_1111111111111111111111111111111111111111111111111111hifc8npp"  # the all-zero key, checksum valid
ORDER = "Hn4pY8sDk2Wj6eLx0RvT5g"


def bound_accept(amount=PRICE, pay_to=PAY_TO, order=ORDER, v1=False):
    a = {"scheme": "exact", "network": "nano:mainnet", "asset": "XNO", "payTo": pay_to, "maxTimeoutSeconds": 300,
         "extra": {"decimals": 30, "binding": "xno-binding/v1/rep", "orderId": order}}
    a["maxAmountRequired" if v1 else "amount"] = amount
    if v1:
        a["resource"] = "http://127.0.0.1/paid"
    return a


def v2_quote(**kw):
    """x402 v2: the quote is a base64 JSON PAYMENT-REQUIRED header; the proof goes in PAYMENT-SIGNATURE."""
    q = {"x402Version": 2, "resource": {"url": "http://127.0.0.1/paid"}, "accepts": [bound_accept(**kw)]}
    return {"PAYMENT-REQUIRED": base64.b64encode(json.dumps(q).encode()).decode()}, {"error": "payment required"}


def v1_quote(**kw):
    """x402 v1: the quote is the JSON body; the proof goes in X-PAYMENT."""
    return {}, {"x402Version": 1, "error": "X-PAYMENT header is required", "accepts": [bound_accept(v1=True, **kw)]}


class Seller:
    """Answers 402 until a request carries `paid_header`; records every request's headers."""

    def __init__(self, quote, paid_header):
        self.headers, self.body = quote
        self.paid_header = paid_header.lower()
        self.seen = []


def serve(seller):
    class H(http.server.BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def do_GET(self):
            hdrs = {k.lower(): v for k, v in self.headers.items()}
            seller.seen.append(hdrs)
            if self.path == "/free":
                return self._send(200, {}, b"free page")
            if seller.paid_header in hdrs:
                return self._send(200, {}, b"paid page")
            return self._send(402, seller.headers, json.dumps(seller.body).encode())

        def _send(self, code, headers, body):
            self.send_response(code)
            for k, v in headers.items():
                self.send_header(k, v)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

    srv = http.server.HTTPServer(("127.0.0.1", 0), H)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


class Signer:
    """Stands in for the operator's wallet: records each order and returns a fixed hash."""

    def __init__(self, answer=HASH):
        self.calls, self.answer = [], answer

    def __call__(self, order):
        self.calls.append(order)
        return self.answer


class Base(unittest.TestCase):
    def setUp(self):
        self._cc = socket.create_connection

        def loopback_only(addr, *a, **k):
            if addr[0] not in ("127.0.0.1", "localhost"):
                raise AssertionError("non-loopback connection attempted: %r" % (addr,))
            return self._cc(addr, *a, **k)
        socket.create_connection = loopback_only
        self.tmp = tempfile.TemporaryDirectory()
        self.journal = os.path.join(self.tmp.name, "pay.jsonl")
        self.servers = []

    def tearDown(self):
        socket.create_connection = self._cc
        for s in self.servers:
            s.shutdown()
            s.server_close()
        self.tmp.cleanup()

    def url(self, seller, path="/paid"):
        srv = serve(seller)
        self.servers.append(srv)
        return "http://127.0.0.1:%d%s" % (srv.server_address[1], path)

    def fetch(self, url, **kw):
        kw.setdefault("cap_raw", CAP)
        kw.setdefault("opener", urllib.request.build_opener(urllib.request.ProxyHandler({})))
        return nf.fetch(url, **kw)

    def journal_states(self):
        if not os.path.exists(self.journal):
            return []
        with open(self.journal, encoding="utf-8") as f:
            return [json.loads(x)["state"] for x in f if x.strip()]


class OffByDefault(Base):
    def test_free_page_passes_through(self):
        r = self.fetch(self.url(Seller(v2_quote(), "PAYMENT-SIGNATURE"), "/free"))
        self.assertEqual((r.status, r.body, r.paid), (200, b"free page", None))

    def test_402_without_signer_and_journal_is_not_paid(self):
        r = self.fetch(self.url(Seller(v2_quote(), "PAYMENT-SIGNATURE")))
        self.assertEqual(r.status, 402)
        self.assertEqual(r.refusal[0], "not_configured")
        self.assertFalse(os.path.exists(self.journal))


class PaysABoundOrder(Base):
    def test_v2_pays_once_with_the_order_representative_and_retries(self):
        seller, signer = Seller(v2_quote(), "PAYMENT-SIGNATURE"), Signer()
        r = self.fetch(self.url(seller), signer=signer, journal_path=self.journal)
        self.assertEqual((r.status, r.body), (200, b"paid page"))
        self.assertEqual(len(signer.calls), 1)
        order = signer.calls[0]
        self.assertEqual((order["payTo"], order["amount_raw"], order["orderId"]), (PAY_TO, PRICE, ORDER))
        self.assertEqual(order["representative"], order_representative(ORDER, PAY_TO, PRICE))
        proof = json.loads(base64.b64decode(seller.seen[-1]["payment-signature"]))
        self.assertEqual(proof["payload"], {"orderId": ORDER, "blockHash": HASH.upper()})
        self.assertEqual(self.journal_states(), ["intent", "paid"])

    def test_v1_body_quote_retries_with_x_payment(self):
        seller, signer = Seller(v1_quote(), "X-PAYMENT"), Signer()
        r = self.fetch(self.url(seller), signer=signer, journal_path=self.journal)
        self.assertEqual((r.status, r.body), (200, b"paid page"))
        self.assertEqual(len(signer.calls), 1)
        self.assertIn("x-payment", seller.seen[-1])


class Guards(Base):
    def test_the_same_order_is_refused_after_a_restart(self):
        url = self.url(Seller(v2_quote(), "PAYMENT-SIGNATURE"))
        self.fetch(url, signer=Signer(), journal_path=self.journal)
        again = Signer()
        r = self.fetch(url, signer=again, journal_path=self.journal)  # a new Journal reads the file again
        self.assertEqual((r.status, r.refusal[0]), (402, "replayed"))
        self.assertEqual(again.calls, [])

    def test_a_price_over_the_cap_is_refused_before_the_signer(self):
        signer = Signer()
        r = self.fetch(self.url(Seller(v2_quote(), "PAYMENT-SIGNATURE")), signer=signer,
                       journal_path=self.journal, cap_raw=str(RAW_PER_XNO))
        self.assertEqual((r.status, r.refusal[0]), (402, "over_cap"))
        self.assertEqual(signer.calls, [])

    def test_the_budget_counts_what_the_journal_already_paid(self):
        self.fetch(self.url(Seller(v2_quote(), "PAYMENT-SIGNATURE")), signer=Signer(), journal_path=self.journal,
                   budget_raw=str(2 * RAW_PER_XNO))
        signer = Signer()
        r = self.fetch(self.url(Seller(v2_quote(order="Zq9pY8sDk2Wj6eLx0RvT5h"), "PAYMENT-SIGNATURE")),
                       signer=signer, journal_path=self.journal, budget_raw=str(2 * RAW_PER_XNO))
        self.assertEqual((r.status, r.refusal[0]), (402, "over_budget"))
        self.assertEqual(signer.calls, [])

    def test_a_pay_to_with_a_bad_checksum_is_refused(self):
        signer = Signer()
        bad = PAY_TO[:-1] + ("q" if PAY_TO[-1] != "q" else "r")
        r = self.fetch(self.url(Seller(v2_quote(pay_to=bad), "PAYMENT-SIGNATURE")), signer=signer,
                       journal_path=self.journal)
        self.assertEqual((r.status, r.refusal[0]), (402, "bad_checksum"))
        self.assertEqual(signer.calls, [])

    def test_a_signer_without_a_hash_leaves_the_intent_and_never_retries(self):
        seller = Seller(v2_quote(), "PAYMENT-SIGNATURE")
        r = self.fetch(self.url(seller), signer=Signer(answer=None), journal_path=self.journal)
        self.assertEqual((r.status, r.refusal[0]), (402, "signer_no_hash"))
        self.assertEqual(self.journal_states(), ["intent"])
        self.assertEqual(len(seller.seen), 1)


class Command(Base):
    def test_signer_needs_a_journal(self):
        err = io.StringIO()
        self.assertEqual(nf.main(["https://seller.example/x", "--signer", "m.sign"], out=io.BytesIO(), err=err), 2)

    def test_raw_amounts_must_be_digits(self):
        err = io.StringIO()
        rc = nf.main(["https://seller.example/x", "--cap-raw", "0.1"], out=io.BytesIO(), err=err)
        self.assertEqual(rc, 2)



# ---- regression tests for the review of #181 -------------------------------------------------------------

ORDER_B = "Zq9pY8sDk2Wj6eLx0RvT5h"
XRB_PAY_TO = "xrb_" + PAY_TO[len("nano_"):]  # the same public key, the legacy prefix


def serve_fn(route):
    """A loopback server whose answers come from route(path, headers) -> (code, headers, body), or the
    string "drop" (close the connection without an answer), or ("sleep", seconds, answer)."""
    class H(http.server.BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def do_GET(self):
            ans = route(self.path, {k.lower(): v for k, v in self.headers.items()})
            if ans == "drop":
                self.close_connection = True
                return
            if ans[0] == "sleep":
                time.sleep(ans[1])
                ans = ans[2]
            code, headers, body = ans
            try:
                self.send_response(code)
                for k, v in headers.items():
                    self.send_header(k, v)
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
            except OSError:
                pass

    srv = http.server.HTTPServer(("127.0.0.1", 0), H)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


class SlowSigner:
    """Thread-safe dummy signer that takes a moment, so two settlements overlap."""

    def __init__(self):
        self.calls, self.lock = [], threading.Lock()

    def __call__(self, order):
        with self.lock:
            self.calls.append(order)
        time.sleep(0.2)
        return HASH


class Review(Base):
    def setUp(self):
        super().setUp()
        self.modules = []
        # the command builds urllib's default opener: keep any proxy from the environment out of loopback runs
        env = unittest.mock.patch.dict(os.environ, {"no_proxy": "*", "NO_PROXY": "*"})
        env.start()
        self.addCleanup(env.stop)

    def tearDown(self):
        for m in self.modules:
            sys.modules.pop(m, None)
        super().tearDown()

    def serve_fn(self, route):
        srv = serve_fn(route)
        self.servers.append(srv)
        return "http://127.0.0.1:%d" % srv.server_address[1]

    def signer_module(self, signer):
        name = "nf_review_signer_%d" % len(self.modules)
        mod = types.ModuleType(name)
        mod.sign = signer
        sys.modules[name] = mod
        self.modules.append(name)
        return name + ".sign"

    def settle_in_threads(self, quotes, budget):
        """One thread per quote, each with its OWN Journal on the same file, released together."""
        journals = [mw.Journal(self.journal) for _ in quotes]
        signer, results, gate = SlowSigner(), [None] * len(quotes), threading.Barrier(len(quotes))

        def run(i):
            h, b = quotes[i]
            gate.wait()
            results[i] = mw.settle_402(h, json.dumps(b).encode(), "http://127.0.0.1/paid", signer,
                                       journals[i], CAP, budget)
        threads = [threading.Thread(target=run, args=(i,)) for i in range(len(quotes))]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        return signer, results

    # 1. replay and budget are one transaction across journal users
    def test_two_journals_settling_one_order_at_once_sign_it_once(self):
        signer, results = self.settle_in_threads([v2_quote(), v2_quote()], budget=PRICE)
        self.assertEqual(len(signer.calls), 1)
        self.assertEqual(sorted(r["ok"] for r in results), [False, True])
        self.assertIn([r["error"] for r in results if not r["ok"]][0], ("replayed", "over_budget"))
        h, b = v2_quote()  # restart: a new Journal on the same file sees the reservation
        again = Signer()
        r = mw.settle_402(h, json.dumps(b).encode(), "http://127.0.0.1/paid", again, mw.Journal(self.journal),
                          CAP, str(10 * int(PRICE)))
        self.assertEqual((r["ok"], r["error"], again.calls), (False, "replayed", []))

    def test_two_journals_competing_for_the_last_budget_unit_sign_once(self):
        signer, results = self.settle_in_threads([v2_quote(), v2_quote(order=ORDER_B)], budget=PRICE)
        self.assertEqual(len(signer.calls), 1)
        self.assertEqual([r["error"] for r in results if not r["ok"]], ["over_budget"])
        h, b = v2_quote(order="Cc9pY8sDk2Wj6eLx0RvT5c")  # restart: the spent budget is still spent
        again = Signer()
        r = mw.settle_402(h, json.dumps(b).encode(), "http://127.0.0.1/paid", again, mw.Journal(self.journal),
                          CAP, PRICE)
        self.assertEqual((r["ok"], r["error"], again.calls), (False, "over_budget", []))

    def test_without_a_file_lock_nothing_is_signed(self):
        url, signer = self.url(Seller(v2_quote(), "PAYMENT-SIGNATURE")), Signer()
        with unittest.mock.patch.object(mw, "fcntl", None, create=True), \
                unittest.mock.patch.object(mw, "msvcrt", None, create=True):
            r = self.fetch(url, signer=signer, journal_path=self.journal)
            rc = nf.main([url, "--signer", self.signer_module(signer), "--journal", self.journal,
                          "--cap-raw", CAP], out=io.BytesIO(), err=io.StringIO())
        self.assertEqual((r.refusal[0], rc, signer.calls), ("journal_unavailable", 7, []))

    # 2. a torn journal refuses to sign; a crash inside the signer leaves the order reserved
    def test_a_torn_journal_tail_refuses_to_sign_until_reconciled(self):
        with open(self.journal, "w", encoding="utf-8") as f:
            f.write('{"torn":')
        url = self.url(Seller(v2_quote(), "PAYMENT-SIGNATURE"))

        def crash(order):
            crash.calls.append(order)
            raise RuntimeError("interrupted before a hash came back")
        crash.calls = []
        try:
            r = self.fetch(url, signer=crash, journal_path=self.journal)
        except RuntimeError:
            r = None
        self.assertEqual(crash.calls, [])
        self.assertEqual(r.refusal[0], "journal_corrupt")
        again = Signer()  # restart: still refused, still nothing signed
        r = self.fetch(url, signer=again, journal_path=self.journal)
        self.assertEqual((r.refusal[0], again.calls), ("journal_corrupt", []))
        rc = nf.main([url, "--signer", self.signer_module(again), "--journal", self.journal],
                     out=io.BytesIO(), err=io.StringIO())
        self.assertEqual((rc, again.calls), (6, []))

    def test_a_signer_that_raises_leaves_the_order_reserved_across_a_restart(self):
        url = self.url(Seller(v2_quote(), "PAYMENT-SIGNATURE"))

        def crash(order):
            crash.calls.append(order)
            raise RuntimeError("interrupted after publishing")
        crash.calls = []
        r = self.fetch(url, signer=crash, journal_path=self.journal)
        self.assertEqual((len(crash.calls), r.refusal[0]), (1, "signer_error"))
        again = Signer()
        r = self.fetch(url, signer=again, journal_path=self.journal)
        self.assertEqual((r.refusal[0], again.calls), ("replayed", []))

    # 3. replay identity is the bound order, not the URL or the payTo spelling
    def test_url_aliases_of_one_order_are_paid_once(self):
        seller = Seller(v2_quote(), "PAYMENT-SIGNATURE")
        base = self.url(seller, "")
        self.fetch(base + "/paid?view=a", signer=Signer(), journal_path=self.journal)
        again = Signer()
        r = self.fetch(base + "/paid?view=b", signer=again, journal_path=self.journal)
        self.assertEqual((r.refusal[0], again.calls), ("replayed", []))

    def test_nano_and_xrb_spellings_of_one_recipient_are_paid_once(self):
        seller = Seller(v2_quote(), "PAYMENT-SIGNATURE")
        url = self.url(seller)
        self.fetch(url, signer=Signer(), journal_path=self.journal)
        seller.headers, seller.body = v2_quote(pay_to=XRB_PAY_TO)
        again = Signer()
        r = self.fetch(url, signer=again, journal_path=self.journal)
        self.assertEqual((r.refusal[0], again.calls), ("replayed", []))

    def test_distinct_orders_at_one_url_are_both_paid(self):
        seller = Seller(v2_quote(), "PAYMENT-SIGNATURE")
        url, signer = self.url(seller), Signer()
        self.fetch(url, signer=signer, journal_path=self.journal)
        seller.headers, seller.body = v2_quote(order=ORDER_B)
        r = self.fetch(url, signer=signer, journal_path=self.journal)
        self.assertEqual((r.status, len(signer.calls)), (200, 2))

    # 4. redirects: a redirected quote is not signed; the paid retry follows no redirect
    def test_a_quote_reached_through_a_redirect_is_refused_before_signing(self):
        qh, qb = v2_quote()
        b_seen = []

        def seller_b(path, hdrs):
            b_seen.append(hdrs)
            if "payment-signature" in hdrs:
                return 200, {}, b"paid page"
            return 402, qh, json.dumps(qb).encode()
        b = self.serve_fn(seller_b)
        a = self.serve_fn(lambda path, hdrs: (302, {"Location": b + "/paid"}, b""))
        signer = Signer()
        r = self.fetch(a + "/start", signer=signer, journal_path=self.journal)
        self.assertEqual((r.status, r.refusal[0], signer.calls), (402, "redirected_quote", []))
        self.assertIn(b + "/paid", r.refusal[1])
        self.assertFalse(any("payment-signature" in h for h in b_seen))

    def test_the_paid_retry_does_not_follow_a_redirect(self):
        qh, qb = v2_quote()
        other_seen = []
        other = self.serve_fn(lambda path, hdrs: other_seen.append(hdrs) or (200, {}, b"elsewhere"))

        def seller(path, hdrs):
            if "payment-signature" in hdrs:
                return 302, {"Location": other + "/next"}, b""
            return 402, qh, json.dumps(qb).encode()
        signer = Signer()
        r = self.fetch(self.serve_fn(seller) + "/paid", signer=signer, journal_path=self.journal)
        self.assertEqual((r.status, len(signer.calls)), (302, 1))
        self.assertEqual(r.paid["blockHash"], HASH.upper())
        self.assertEqual(other_seen, [])

    # 5. a paid retry that cannot be delivered still reports the payment
    def paid_then(self, answer):
        qh, qb = v2_quote()

        def seller(path, hdrs):
            if "payment-signature" in hdrs:
                return answer
            return 402, qh, json.dumps(qb).encode()
        return self.serve_fn(seller) + "/paid"

    def test_a_dropped_connection_on_the_paid_retry_still_reports_paid(self):
        url, signer, err = self.paid_then("drop"), Signer(), io.StringIO()
        rc = nf.main([url, "--signer", self.signer_module(signer), "--journal", self.journal,
                      "--cap-raw", CAP], out=io.BytesIO(), err=err)
        self.assertEqual((rc, len(signer.calls)), (5, 1))
        text = err.getvalue()
        self.assertIn("paid but delivery failed", text)
        self.assertIn(HASH.upper(), text)
        self.assertIn(ORDER, text)
        self.assertEqual(self.journal_states(), ["intent", "paid"])

    def test_a_timeout_on_the_paid_retry_keeps_the_paid_status_and_hash(self):
        url, signer = self.paid_then(("sleep", 1.5, (200, {}, b"late"))), Signer()
        r = self.fetch(url, signer=signer, journal_path=self.journal, timeout=0.3)
        self.assertIsNone(r.status)
        self.assertEqual((r.paid["blockHash"], r.paid["orderId"]), (HASH.upper(), ORDER))
        self.assertIn("timed out", r.delivery_error)

    def test_a_connection_error_before_any_payment_says_nothing_was_paid(self):
        s = socket.socket()
        s.bind(("127.0.0.1", 0))
        port = s.getsockname()[1]
        s.close()
        signer, err = Signer(), io.StringIO()
        rc = nf.main(["http://127.0.0.1:%d/paid" % port, "--signer", self.signer_module(signer),
                      "--journal", self.journal], out=io.BytesIO(), err=err)
        self.assertEqual((rc, signer.calls), (1, []))
        self.assertIn("nothing was paid", err.getvalue())


if __name__ == "__main__":
    unittest.main()
