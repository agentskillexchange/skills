#!/usr/bin/env python3
"""Verify a Nano (XNO) payment read-only. Exit 0 only when the block is
confirmed AND it pays the expected receive address: for a send block that is
contents.link_as_account, for a receive/open block it is block_account."""
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
    print(f"OK {amount} raw to {addr}")

if __name__ == "__main__":
    main()
