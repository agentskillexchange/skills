#!/usr/bin/env python3
"""Verify a Nano (XNO) payment read-only. Exit 0 only when the block is
confirmed AND it pays the expected receive address: for a send block that is
contents.link_as_account, for a receive/open block it is block_account.

Optional, off unless given (see nano_binding.py, standard library only):
  --order-id ID       the block must be a send of EXACTLY the third argument
                      in raw to the address, carrying this order's
                      xno-binding v1 commitment as its representative
  --claims-file PATH  credit each block once, recorded on disk before exit 0,
                      so a restart does not let an old block pay again
  --rpc URL           node to read from (default $NANO_RPC_URL or rpc.nano.to)
"""
import argparse, json, os, sys, urllib.parse, urllib.request

try:  # only the optional flags need it; a lone copy of this file still works
    import nano_binding
except ImportError:
    nano_binding = None

RPC = "https://rpc.nano.to/"
MAX_RESPONSE_BYTES = 1 << 20

def rpc(action, rpc_url=RPC, **params):
    req = urllib.request.Request(
        rpc_url, data=json.dumps({"action": action, **params}).encode(),
        headers={"Content-Type": "application/json",
                 "User-Agent": "nano-payment-verify/1.0"}, method="POST")
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read(MAX_RESPONSE_BYTES))

def checked_rpc_url(url):
    """https anywhere; plain http only to this machine."""
    parts = urllib.parse.urlsplit(url)
    if parts.scheme == "https" and parts.hostname:
        return url
    if parts.scheme == "http" and parts.hostname in ("localhost", "127.0.0.1", "::1"):
        return url
    raise ValueError("node URL must be https, or http on localhost: %r" % (url,))

def parse_args(argv):
    p = argparse.ArgumentParser(description="Verify a Nano (XNO) payment read-only.")
    p.add_argument("block", help="block hash (the payer's send or your receive/open)")
    p.add_argument("expect_addr", help="your Nano receive address")
    p.add_argument("expect_min_raw", type=int,
                   help="raw owed (1 XNO = 10**30 raw); a minimum, or the exact price with --order-id")
    p.add_argument("--order-id", default=None)
    p.add_argument("--claims-file", default=None)
    p.add_argument("--rpc", default=None)
    return p.parse_args(argv)

def main(argv=None):
    args = parse_args(sys.argv[1:] if argv is None else argv)
    block = args.block
    expect_addr = args.expect_addr          # your Nano receive address
    expect_min_raw = args.expect_min_raw    # minimum raw units owed (1 XNO = 10**30)
    try:
        rpc_url = checked_rpc_url(args.rpc or os.environ.get("NANO_RPC_URL") or RPC)
        if args.order_id is not None or args.claims_file is not None:
            if nano_binding is None:
                raise ValueError("--order-id and --claims-file need nano_binding.py beside this file")
            nano_binding.account_public_key(expect_addr)
            block = nano_binding.normalize_block_hash(block)
        if args.order_id is not None and expect_min_raw <= 0:
            raise ValueError("the exact price in raw must be positive")
    except ValueError as e:
        print(f"BAD_INPUT {e}"); sys.exit(2)
    info = rpc("block_info", rpc_url=rpc_url, json_block="true", hash=block)
    if args.order_id is not None:
        verdict = nano_binding.check_bound_send(info, expect_addr, expect_min_raw, args.order_id)
        if verdict != nano_binding.MATCHED:
            print(verdict.upper()); sys.exit(1)
        addr, amount = expect_addr, expect_min_raw
    else:
        subtype = info.get("subtype")
        contents = info.get("contents") or {}
        if subtype == "send":
            # A send block belongs to the sender; the recipient is link_as_account.
            addr = contents.get("link_as_account")
        elif subtype in ("receive", "open"):
            addr = info.get("block_account") or contents.get("account")
        else:
            print(f"NOT_A_PAYMENT {subtype}"); sys.exit(1)
        amount = int(info.get("amount", "0"))
        if info.get("confirmed") != "true":
            print("NOT_CONFIRMED"); sys.exit(1)
        if addr != expect_addr:
            print(f"WRONG_ADDRESS {addr}"); sys.exit(1)
        if amount < expect_min_raw:
            print(f"AMOUNT_SHORT {amount}"); sys.exit(1)
    if args.claims_file is not None:
        if nano_binding.ClaimsFile(args.claims_file).claim(block, args.order_id) != nano_binding.MATCHED:
            print("ALREADY_CLAIMED"); sys.exit(1)
    print(f"OK {amount} raw to {addr}")

if __name__ == "__main__":
    main()
