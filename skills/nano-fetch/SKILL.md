---
name: "Pay a Nano (XNO) 402 and Fetch"
slug: "nano-fetch"
description: "Fetch a URL and, when it answers HTTP 402 with an x402 nano:mainnet exact quote, pay it once through the operator's own signer and retry with the proof. A per-call cap and a total budget in raw are checked before anything is signed, the send is bound to this one order (xno-binding/v1/rep), and an fsynced journal refuses to pay the same order twice, also after a restart. Standard library Python; the skill holds no key and no seed. The buyer's side of verify-nano-payment."
verification: "listed"
category: "Integrations & Connectors"
framework: "Custom Agents"
---

# Pay a Nano (XNO) 402 and Fetch

Use this when an agent BUYS something priced in Nano (XNO): a page, an API answer or a tool
call that answers `402 Payment Required` until it is paid. `verify-nano-payment` is the
seller's side (confirm the money landed, credit each block once); this skill is the payer's
side of the same order.

`fetch.py` fetches the URL. On a 402 it reads the quote, checks it, hands one order to a signer
the operator wrote, records the payment, and retries once with the proof. It never sees a key.

## Installation

### Direct repo/manual install

Clone the Agent Skill Exchange repository and copy this skill directory into the skill folder
used by your agent runtime:

```bash
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/skills/nano-fetch ~/.agent-skills/nano-fetch
```

### Nothing else to install

`fetch.py`, `middleware.py` (the settle step) and the `xno_buyer_plan/` package (the quote
reader) use only the Python standard library. Copy the whole folder; there is no
`pip install`. Run `python3 fetch.py` from the folder, or give its path.

## Before the first paid call: the operator's three settings

Do not guess these. If one is missing, run without them (a 402 is then shown, never paid) and
ask the person you work for.

1. **A signer** - `--signer module.attr`, a Python function the operator wrote, which holds
   the key. It receives `{"network", "payTo", "amount_raw", "representative", "orderId"}`,
   publishes a send of `amount_raw` raw to `payTo` with `representative` as the block's
   representative (when it is not None), waits until the send is confirmed, and returns the
   64-hex block hash. The module is found on `PYTHONPATH` (for example `PYTHONPATH=~/wallet`,
   where the operator keeps `mywallet.py`). You never see the key and never write a key, a
   seed or a wallet file yourself.
2. **A journal** - `--journal FILE`: one file per agent, kept between runs. `--signer`
   without `--journal` is refused.
3. **The limits, in raw** (1 XNO = 10**30 raw): `--cap-raw N` per call, `--budget-raw N`
   over the whole journal (default 10 x the cap). A price over either is refused before the
   signer is called.

## Run it

Look first, pay nothing:

```sh
python3 fetch.py https://seller.example/report -o report.json
```

Pay at most one tenth of an XNO (10**29 raw) for this call, and at most 10**30 raw in all:

```sh
PYTHONPATH=~/wallet python3 fetch.py https://seller.example/report --signer mywallet.sign --journal ~/.nano-pay.jsonl --cap-raw 100000000000000000000000000000 --budget-raw 1000000000000000000000000000000 -o report.json
```

A POST with a header and a body (`-X`/`--request`, `-H`/`--header` as often as needed,
`-d`/`--data`, `-o`/`--output`, `--timeout` seconds; POST is used whenever `-d` is given):

```sh
PYTHONPATH=~/wallet python3 fetch.py https://seller.example/api -X POST -H 'Content-Type: application/json' -d '{"q": "nano"}' --signer mywallet.sign --journal ~/.nano-pay.jsonl --timeout 60
```

`--allow-unbound` also pays a quote that only asks for a send hash, with nothing binding the
send to this one request. Leave it off unless the operator asked for it.

## What it pays, and how the payment is bound

- **x402 v2** (`PAYMENT-REQUIRED` header, base64 JSON) and **x402 v1** (JSON body,
  `maxAmountRequired`): an `exact` accept on `nano:mainnet` whose `extra` carries
  `binding: "xno-binding/v1/rep"` and an `orderId`. The send's representative is the
  account of SHA-256("xno-binding/v1/rep|" + orderId + "|" + payTo + "|" + amount), so the
  block itself names the order; the seller can check it statelessly. The retry carries
  `PAYMENT-SIGNATURE` (v2) or `X-PAYMENT` (v1): base64 JSON with `payload.orderId` and
  `payload.blockHash`.
- Checks, in order, before the signer is called: the network, the `payTo` checksum, the
  amount (integer raw, never a float), the cap, the binding, the journal (replay), then the
  budget. An `exact` accept without the binding is not paid.
- The proof header is sent to the URL that quoted the price only; it is not carried to a
  redirect target.
- A paid retry that meets 402 again is returned as is: one request never pays twice.

## Read the answer

| exit | meaning | what you do |
|------|---------|-------------|
| 0 | a 2xx or 3xx answer, paid or free | use the body (stdout or `-o FILE`) |
| 1 | another HTTP status, or no connection | report it; nothing was paid unless stderr says `paid` |
| 2 | usage: a bad flag, URL or signer | fix the command; nothing was paid |
| 3 | a 402 that was not paid; stderr names why | report the reason; do not raise the cap on your own |
| 4 | paid, and the retry still met 402 | stop; the payment is in the journal; report the hash on stderr |

Reasons on stderr after `402 not paid:` include `not_configured` (no signer or journal),
`over_cap`, `over_budget`, `bad_checksum`, `unbound` (no order binding; a send-hash quote
is paid only with `--allow-unbound`), `signer_no_hash` (the signer returned no hash; the intent stays in the
journal and that order is never paid again) and `replayed` (the order is already in the
journal).

## The journal

One JSON object a line, flushed and fsynced: an `intent` line (`key`, `amount_raw`,
`orderId`, `url`) before the signer is called, and a `paid` line (`key`, `amount_raw`,
`orderId`, `blockHash`) after. Every key in it is a replay, so an order handed to the signer
once is never handed to it again, across a crash or a restart. To know what was spent, add
`amount_raw` over the `paid` lines. Never edit or delete the file.

## Tests

```bash
python3 -m unittest discover -s skills/nano-fetch -p 'test_*.py'
```

Against a loopback seller only: off by default, a v2 and a v1 bound order paid once with the
order's representative, replay refused after a restart, cap, budget, checksum and a signer
that returns no hash. No network, no key.

## Safety

- No key, seed or wallet file is read or written by this skill; the signer is the operator's.
- Nothing is paid unless both `--signer` and `--journal` are given.
- The cap and the budget are checked before the signer is called, in integer raw.
- In Nano a send block also sets the payer's representative, so a bound send moves the
  payer's voting weight to the order's derived account. The signer should publish a change
  block back to the operator's own representative once the send is confirmed.
- Use `verify-nano-payment` on the seller's side to confirm the block before shipping work.
