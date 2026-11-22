#!/usr/bin/env python3
"""Print the x402 v2 PaymentRequired object for one order paid in Nano (XNO).

    python3 quote_payment.py <YOUR_NANO_ADDRESS> <PRICE_XNO> --resource-url URL
        [--description TEXT] [--mime-type TYPE] [--order-id ID]
        [--max-timeout SECONDS] [--header]

Prints the full object (``x402Version`` 2, ``resource`` and one ``accepts``
entry): scheme ``exact`` on ``nano:mainnet``, the price in integer raw
(derived from the decimal XNO string, 1 XNO = 10**30 raw, at most 2**128 - 1
raw), and the order the payer commits to in its send block's representative
(xno-binding v1). Without ``--order-id`` a fresh 128-bit id is made. With
``--header`` it prints the ``PAYMENT-REQUIRED`` header line instead (the same
object, JSON then base64). Keep the printed order id and raw price with the
order, then check the payment with:

    python3 verify_payment.py <SEND_BLOCK_HASH> <YOUR_NANO_ADDRESS> <PRICE_RAW> \\
      --order-id <ORDER_ID> --claims-file ./nano-claims.jsonl

Reads nothing from the network; no wallet, no key. Exit 0 with the output, or
exit 2 with BAD_INPUT and the reason.
"""
import argparse
import json
import sys

import nano_binding


def main(argv=None):
    p = argparse.ArgumentParser(description="Print an x402 v2 PaymentRequired object for one nano:mainnet exact order.")
    p.add_argument("pay_to", help="your Nano receive address")
    p.add_argument("price_xno", help="price as a decimal XNO string, e.g. 0.05")
    p.add_argument("--resource-url", required=True, help="URL of the protected resource")
    p.add_argument("--description", default=None)
    p.add_argument("--mime-type", default=None)
    p.add_argument("--order-id", default=None)
    p.add_argument("--max-timeout", type=int, default=300)
    p.add_argument("--header", action="store_true", help="print the PAYMENT-REQUIRED header line instead of JSON")
    args = p.parse_args(argv)
    try:
        price_raw = nano_binding.xno_to_raw(args.price_xno)
        entry = nano_binding.payment_requirement(args.pay_to, price_raw, args.order_id, args.max_timeout)
        body = nano_binding.payment_required(args.resource_url, [entry], args.description, args.mime_type)
    except (TypeError, ValueError) as exc:
        print("BAD_INPUT %s" % (exc,))
        return 2
    if args.header:
        print("PAYMENT-REQUIRED: %s" % nano_binding.payment_required_header(body))
    else:
        print(json.dumps(body, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
