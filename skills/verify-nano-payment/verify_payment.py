#!/usr/bin/env python3
"""Verify a Nano (XNO) payment read-only. Exit 0 only when the block is
confirmed AND it was sent to the expected receive address."""
import json, sys, urllib.request

RPC = "https://rpc.nano.to/"

def rpc(action, **params):
    req = urllib.request.Request(
        RPC, data=json.dumps({"action": action, **params}).encode(),
        headers={"Content-Type": "application/json",
                 "User-Agent": "nano-payment-verify/1.0"}, method="POST")
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.load(r)

def main():
    block = sys.argv[1]
    expect_addr = sys.argv[2]          # your Nano receive address
    expect_min_raw = int(sys.argv[3])  # minimum raw units owed (1 XNO = 10**30)
    info = rpc("block_info", json_block="true", hash=block)
    addr = info.get("block_account")
    amount = int(info.get("amount", "0"))
    if info.get("confirmed") != "true":
        print("NOT_CONFIRMED"); sys.exit(1)
    if addr != expect_addr:
        print(f"WRONG_ADDRESS {addr}"); sys.exit(1)
    if amount < expect_min_raw:
        print(f"AMOUNT_SHORT {amount}"); sys.exit(1)
    print(f"OK {amount} raw to {addr}")

if __name__ == "__main__":
    main()
