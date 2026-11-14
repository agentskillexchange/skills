"""Tests for nano_binding.py and the optional flags of verify_payment.py.

Standard library only, no network:
    python3 -m unittest discover -s skills/verify-nano-payment -p 'test_*.py'
"""
import contextlib
import io
import os
import tempfile
import unittest
from unittest import mock

import nano_binding as nb
import verify_payment

# xno-binding v1 test vectors (docs/BINDING-STANDARD.md in dhyabi2/xno-call-binding).
BURN = "nano_1111111111111111111111111111111111111111111111111111hifc8npp"
PRICE = 5 * nb.RAW_PER_XNO // 100  # 0.05 XNO, derived, never restated
VECTOR_HEX = "86e75a339b908cc926a478c1a0e5eb5dd6fc612c1d3251eb661faa78135c36cf"
VECTOR_REP = "nano_33q9dassq66es6mcay83n5kypqgpzjikr9bkc9ope9xch1borfphgehj4ozj"

PAY_TO = nb.public_key_to_account(bytes([7]) * 32)
BLOCK_A = "A" * 64
BLOCK_B = "b" * 64


def send_block(order_id="order-1", amount=PRICE, pay_to=PAY_TO, confirmed="true", rep=None, subtype="send"):
    return {
        "subtype": subtype,
        "confirmed": confirmed,
        "amount": str(amount),
        "block_account": nb.public_key_to_account(bytes([9]) * 32),
        "contents": {
            "link_as_account": pay_to,
            "representative": rep or nb.commitment_rep_account(order_id, PAY_TO, PRICE),
        },
    }


class AccountTests(unittest.TestCase):
    def test_burn_account_round_trips(self):
        self.assertEqual(nb.public_key_to_account(bytes(32)), BURN)
        self.assertEqual(nb.account_public_key(BURN), bytes(32))

    def test_checksum_is_enforced(self):
        bad = BURN[:-1] + ("q" if BURN[-1] != "q" else "r")
        self.assertFalse(nb.is_valid_account(bad))
        self.assertFalse(nb.is_valid_account("nano_1234"))
        self.assertFalse(nb.is_valid_account(None))
        self.assertTrue(nb.is_valid_account(PAY_TO))
        self.assertTrue(nb.is_valid_account("xrb_" + BURN[5:]))

    def test_key_part_must_fit_256_bits(self):
        # 52 base-32 characters hold 260 bits; only a leading '1' or '3' fits a 256-bit key.
        self.assertFalse(nb.is_valid_account("nano_" + "z" * 52 + BURN[-8:]))


class CommitmentTests(unittest.TestCase):
    def test_published_vector(self):
        self.assertEqual(PRICE, 50000000000000000000000000000)
        self.assertEqual(nb.order_commitment("order-0001", BURN, PRICE).hex(), VECTOR_HEX)
        self.assertEqual(nb.commitment_rep_account("order-0001", BURN, PRICE), VECTOR_REP)

    def test_float_and_non_positive_prices_are_refused(self):
        for price in (0.05, 0, -1, True, "5"):
            with self.assertRaises(TypeError):
                nb.order_commitment("order-0001", BURN, price)

    def test_commitment_covers_order_destination_and_price(self):
        base = nb.order_commitment("o", PAY_TO, PRICE)
        self.assertNotEqual(base, nb.order_commitment("p", PAY_TO, PRICE))
        self.assertNotEqual(base, nb.order_commitment("o", BURN, PRICE))
        self.assertNotEqual(base, nb.order_commitment("o", PAY_TO, PRICE + 1))


class BoundSendTests(unittest.TestCase):
    def check(self, info, order_id="order-1"):
        return nb.check_bound_send(info, PAY_TO, PRICE, order_id)

    def test_bound_send_matches(self):
        self.assertEqual(self.check(send_block()), nb.MATCHED)

    def test_block_for_another_order_is_not_bound(self):
        self.assertEqual(self.check(send_block(order_id="order-2")), nb.NOT_BOUND)
        self.assertEqual(self.check(send_block(rep=nb.public_key_to_account(bytes([1]) * 32))), nb.NOT_BOUND)

    def test_amount_must_be_exact(self):
        self.assertEqual(self.check(send_block(amount=PRICE - 1)), nb.WRONG_AMOUNT)
        self.assertEqual(self.check(send_block(amount=PRICE + 1)), nb.WRONG_AMOUNT)
        self.assertEqual(self.check(send_block(amount="5e28")), nb.WRONG_AMOUNT)

    def test_destination_confirmation_and_subtype(self):
        self.assertEqual(self.check(send_block(pay_to=BURN)), nb.WRONG_ACCOUNT)
        self.assertEqual(self.check(send_block(confirmed="false")), nb.NOT_CONFIRMED)
        self.assertEqual(self.check(send_block(subtype="receive")), nb.NOT_A_SEND)

    def test_bad_pay_to_is_refused(self):
        with self.assertRaises(ValueError):
            nb.check_bound_send(send_block(), "nano_bad", PRICE, "order-1")


class ClaimsFileTests(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.path = os.path.join(self.dir.name, "claims.jsonl")

    def tearDown(self):
        self.dir.cleanup()

    def test_one_block_one_order(self):
        claims = nb.ClaimsFile(self.path)
        self.assertEqual(claims.claim(BLOCK_A, "order-1"), nb.MATCHED)
        self.assertEqual(claims.claim(BLOCK_A.lower(), "order-1"), nb.MATCHED)  # idempotent re-read
        self.assertEqual(claims.claim(BLOCK_A, "order-2"), nb.DUPLICATE)        # block already used
        self.assertEqual(claims.claim(BLOCK_B, "order-1"), nb.DUPLICATE)        # order already paid
        self.assertEqual(claims.claim(BLOCK_B, "order-2"), nb.MATCHED)

    def test_without_order_a_block_is_used_once(self):
        claims = nb.ClaimsFile(self.path)
        self.assertEqual(claims.claim(BLOCK_A), nb.MATCHED)
        self.assertEqual(claims.claim(BLOCK_A), nb.DUPLICATE)

    def test_claims_survive_a_restart(self):
        nb.ClaimsFile(self.path).claim(BLOCK_A, "order-1")
        reopened = nb.ClaimsFile(self.path)
        self.assertTrue(reopened.claimed(BLOCK_A))
        self.assertEqual(reopened.claim(BLOCK_A, "order-2"), nb.DUPLICATE)

    def test_torn_last_line_is_dropped_not_credited(self):
        nb.ClaimsFile(self.path).claim(BLOCK_A, "order-1")
        with open(self.path, "a", encoding="utf-8") as fh:
            fh.write('{"block": "' + BLOCK_B.upper() + '", "ord')
        claims = nb.ClaimsFile(self.path)
        self.assertFalse(claims.claimed(BLOCK_B))
        self.assertEqual(claims.claim(BLOCK_B, "order-2"), nb.MATCHED)
        self.assertEqual(nb.ClaimsFile(self.path).claim(BLOCK_B, "order-3"), nb.DUPLICATE)
        with open(self.path, encoding="utf-8") as fh:
            self.assertEqual(len(fh.read().splitlines()), 2)

    def test_damaged_complete_line_stops_instead_of_forgetting(self):
        with open(self.path, "w", encoding="utf-8") as fh:
            fh.write("not json\n")
        with self.assertRaises(ValueError):
            nb.ClaimsFile(self.path).claim(BLOCK_A, "order-1")

    def test_bad_block_hash_is_refused(self):
        with self.assertRaises(ValueError):
            nb.ClaimsFile(self.path).claim("12", "order-1")


class VerifyPaymentCliTests(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.claims = os.path.join(self.dir.name, "claims.jsonl")

    def tearDown(self):
        self.dir.cleanup()

    def run_cli(self, args, block_info):
        out = io.StringIO()
        code = 0
        with mock.patch.object(verify_payment, "rpc", return_value=block_info) as rpc, \
                contextlib.redirect_stdout(out):
            try:
                verify_payment.main(args)
            except SystemExit as e:
                code = e.code
        return code, out.getvalue().strip(), rpc

    def test_unchanged_without_options(self):
        legacy = send_block(rep=nb.public_key_to_account(bytes([1]) * 32), amount=PRICE + 5)
        code, out, rpc = self.run_cli([BLOCK_A, PAY_TO, str(PRICE)], legacy)
        self.assertEqual((code, out), (0, "OK %d raw to %s" % (PRICE + 5, PAY_TO)))
        self.assertEqual(rpc.call_args.kwargs["rpc_url"], verify_payment.RPC)

    def test_bound_payment_is_credited_once_across_restarts(self):
        args = [BLOCK_A, PAY_TO, str(PRICE), "--order-id", "order-1", "--claims-file", self.claims]
        self.assertEqual(self.run_cli(args, send_block())[:2], (0, "OK %d raw to %s" % (PRICE, PAY_TO)))
        args2 = [BLOCK_A, PAY_TO, str(PRICE), "--order-id", "order-2", "--claims-file", self.claims]
        self.assertEqual(self.run_cli(args2, send_block(order_id="order-2"))[:2], (1, "ALREADY_CLAIMED"))

    def test_block_paying_another_order_is_refused(self):
        args = [BLOCK_A, PAY_TO, str(PRICE), "--order-id", "order-1"]
        self.assertEqual(self.run_cli(args, send_block(order_id="order-9"))[:2], (1, "NOT_BOUND_TO_ORDER"))
        self.assertEqual(self.run_cli(args, send_block(amount=PRICE * 2))[:2], (1, "REFUSABLE_WRONG_AMOUNT"))

    def test_claims_file_alone_refuses_a_replayed_block(self):
        legacy = send_block(rep=nb.public_key_to_account(bytes([1]) * 32))
        args = [BLOCK_A, PAY_TO, str(PRICE), "--claims-file", self.claims]
        self.assertEqual(self.run_cli(args, legacy)[0], 0)
        self.assertEqual(self.run_cli(args, legacy)[:2], (1, "ALREADY_CLAIMED"))

    def test_node_url_and_inputs_are_checked_before_any_read(self):
        for args in (
            [BLOCK_A, PAY_TO, str(PRICE), "--rpc", "http://node.example:7076"],
            [BLOCK_A, "nano_bad", str(PRICE), "--order-id", "order-1"],
            ["12", PAY_TO, str(PRICE), "--claims-file", self.claims],
            [BLOCK_A, PAY_TO, "0", "--order-id", "order-1"],
        ):
            code, out, rpc = self.run_cli(args, send_block())
            self.assertEqual(code, 2, args)
            self.assertTrue(out.startswith("BAD_INPUT"), out)
            rpc.assert_not_called()

    def test_options_without_the_module_are_refused(self):
        with mock.patch.object(verify_payment, "nano_binding", None):
            code, out, rpc = self.run_cli([BLOCK_A, PAY_TO, str(PRICE), "--order-id", "order-1"], send_block())
        self.assertEqual(code, 2)
        self.assertIn("nano_binding.py", out)
        rpc.assert_not_called()

    def test_local_node_and_env_url(self):
        args = [BLOCK_A, PAY_TO, str(PRICE), "--rpc", "http://127.0.0.1:7076"]
        self.assertEqual(self.run_cli(args, send_block())[2].call_args.kwargs["rpc_url"], "http://127.0.0.1:7076")
        with mock.patch.dict(os.environ, {"NANO_RPC_URL": "https://node.example/rpc"}):
            rpc = self.run_cli([BLOCK_A, PAY_TO, str(PRICE)], send_block())[2]
        self.assertEqual(rpc.call_args.kwargs["rpc_url"], "https://node.example/rpc")


if __name__ == "__main__":
    unittest.main()
