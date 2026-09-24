---
name: "Verify a Nano (XNO) Payment"
slug: "verify-nano-payment"
description: "Verify that a Nano (XNO) payment has settled: confirm a send/receive block, read its amount and pay-to account from the block (not the request), and check confirmation — read-only against the public Nano RPC (rpc.nano.to), no wallet, no key. Use it whenever an agent has been told it was paid in Nano and needs to confirm the money actually landed before shipping work."
category: "Integrations & Connectors"
framework: "Custom Agents"
verification: listed
source: "https://rpc.nano.to/"
---

# Verify a Nano (XNO) Payment

Nano (XNO) is a feeless, instant, green digital currency settled peer-to-peer on a
single ledger with no issuer. When an agent is paid for work in Nano, the sender
tells it a block hash or an amount — but a claim is not a settlement. This skill
shows an agent how to confirm, from the ledger itself, that a payment actually
landed: the block exists, it is confirmed, its `account` is the agent's own
receive address, and its `amount` matches what was owed. It is strictly
read-only and needs no wallet, no seed and no API key — the public Nano RPC
(`rpc.nano.to`) answers every query used here.

## Why this is a real need

The whole point of agent payments is that an agent should not ship work or
release credentials on a promise. If you can read the ledger, you never have to
trust the payer's word. A pay-per-call or bounty agent should, before delivering,
answer three questions:

1. Does a block with the claimed hash exist and is it confirmed?
2. Was it sent to MY address (the block's `account`/`representative`)?
3. Is the raw `amount` at least what was owed?

Each is one read-only RPC call. Nothing here signs, spends or touches funds.

## Installation

### Direct repo/manual install

Clone the Agent Skill Exchange repository and copy this skill directory into
the skill folder used by your agent runtime:

```bash
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/skills/verify-nano-payment ~/.agent-skills/verify-nano-payment
```

### No install needed for the core technique

The skill's core technique needs no install at all: it is one read-only JSON
POST to the public Nano RPC over plain `curl` (shown below). The optional
`verify_payment.py` helper uses only the Python standard library, so it needs
no `pip install`. An HTTP client in any language (Node `fetch`, Python
`urllib`, `requests`, or a plain shell `curl`) can replicate it without
adding a dependency.

## Reading the ledger (curl, no key)

The Nano RPC is a simple JSON POST to a public node. Set a short timeout and,
for safety, only ever READ — never pass a `private_key` or `wallet` in an action.

### 1. Confirm a block exists and is confirmed — `block_info`

```bash
curl -sS -m 15 -X POST -H "Content-Type: application/json" \
  -d '{"action":"block_info","json_block":"true","hash":"8161FEE8C0A1676D7965A4771DBFA9937D88ECB4FFBE5DF36E431672D107D604"}' \
  https://rpc.nano.to/
```

The response names the block's account (`"block_account"`), the raw `amount`,
the `balance`, and — the key field — `"confirmed":"true"`. Only a confirmed
block is final; Nano finality is sub-second but a node reports confirmation
explicitly, so read it before acting.

### 2. Read the pay-to account from the block — not the request body

The block's `contents.account` (or `block_account` at the top level) is the
address the payment landed in. Compare it to the address you expect to be paid
into. Never trust a `payTo` field sent alongside a request; the ledger block is
the source of truth.

```bash
curl -sS -m 15 -X POST -H "Content-Type: application/json" \
  -d '{"action":"block_info","json_block":"true","hash":"<BLOCK_HASH>"}' \
  https://rpc.nano.to/ \
  | jq '{block_account, amount, confirmed}'
```

### 3. Check the account state — `account_info`

To confirm the receiving account is live and see its current balance (a balance
increase is the practical proof a receive landed):

```bash
curl -sS -m 15 -X POST -H "Content-Type: application/json" \
  -d '{"action":"account_info","account":"nano_1yo6c1t64ahfjdw1dxizmbbnpdmbrckwhw9phbg5pdkeubrizga4qhnjmnx7"}' \
  https://rpc.nano.to/
```

## A small helper script

Save `verify_payment.py` (dependency-free, stdlib only) next to this skill and
call it before you ship work after being told "you have been paid in Nano":

```python
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
```

Usage:

```bash
python3 verify_payment.py 8161FEE8C0A1676D7965A4771DBFA9937D88ECB4FFBE5DF36E431672D107D604 \
  nano_1yo6c1t64ahfjdw1dxizmbbnpdmbrckwhw9phbg5pdkeubrizga4qhnjmnx7 0
```

Only a `0`/OK exit means the agent may deliver: the block is on the ledger,
confirmed, in the expected account, for at least the expected raw amount.

## Safety

- This skill only READS the public ledger. Never add `private_key`, `wallet`,
  `seed`, or `destination` to any request — that would be trying to spend, which
  a verify skill must never do without explicit wallet tooling.
- Treat the ledger as the source of truth; a payment claim from chat is not
  settled until the block says so.

## Source

- [Nano public RPC — rpc.nano.to](https://rpc.nano.to/)
- Nano developer resources: https://hub.nano.org
