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
import unittest
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import fetch as nf  # noqa: E402
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


if __name__ == "__main__":
    unittest.main()
