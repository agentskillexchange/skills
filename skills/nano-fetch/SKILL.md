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
mkdir -p ~/.agent-skills
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
2. **A journal** - `--journal FILE`: kept between runs. `--signer` without `--journal` is
   refused. Several agents or processes may share one journal: every payment decision is
   made under an exclusive lock on `FILE.lock` next to it.
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
- One order is one payment: replay is keyed on the network, the binding scheme, the
  `orderId`, the recipient's public key (an `xrb_` and a `nano_` spelling of one account are
  the same recipient) and the amount in raw. The URL is not part of it, so the same order
  quoted at `/paid?view=a` and `/paid?view=b` is paid once; distinct orders stay distinct.
- Redirects: a 402 that arrives after a redirect is refused before anything is signed
  (`redirected_quote`; the reason names the URL that quoted, to be fetched directly). The
  paid retry goes to the quoting URL only, with redirects off: a 3xx answer to it is returned
  as is, and the proof header is never sent to any other URL.
- A paid retry that meets 402 again is returned as is: one request never pays twice.

## Read the answer

| exit | meaning | what you do |
|------|---------|-------------|
| 0 | a 2xx or 3xx answer, paid or free | use the body (stdout or `-o FILE`) |
| 1 | failed before any payment: another HTTP status, or no connection | report it; nothing was paid |
| 2 | usage: a bad flag, URL or signer | fix the command; nothing was paid |
| 3 | a 402 that was not paid; stderr names why | report the reason; do not raise the cap on your own |
| 4 | paid, and the retry still met 402 | stop; the payment is in the journal; report the hash on stderr |
| 5 | paid, but the delivery failed (connection error, timeout or another status on the paid retry) | stop; report the order and hash stderr names; never pay that order again |
| 6 | the journal is corrupt (a torn or malformed line); nothing was signed | stop; ask a person to reconcile the journal |
| 7 | the journal cannot be locked or opened; nothing was signed | stop; report it |

Whenever a payment was made, stderr has a line `paid <amount> raw, order <orderId>, hash
<blockHash>`, also when the retry fails afterwards.

Reasons on stderr after `402 not paid:` include `not_configured` (no signer or journal),
`over_cap`, `over_budget`, `bad_checksum`, `unbound` (no order binding; a send-hash quote
is paid only with `--allow-unbound`), `signer_no_hash` (the signer returned no hash; the intent stays in the
journal and that order is never paid again), `signer_error` (the signer raised; the same),
`redirected_quote` (the 402 came after a redirect), `replayed` (the order is already in the
journal), `journal_corrupt` (exit 6) and `journal_unavailable` (exit 7).

## The journal

One JSON object a line, flushed and fsynced: an `intent` line (`key`, `amount_raw`,
`orderId`, `url`) before the signer is called, and a `paid` line (`key`, `amount_raw`,
`orderId`, `blockHash`) after. Every key in it is a replay, so an order handed to the signer
once is never handed to it again, across a crash or a restart.

Reserving a payment is one transaction under an exclusive lock on `FILE.lock`
(`fcntl.flock`, or `msvcrt.locking` on Windows; where neither exists nothing is paid, exit
7): reload the journal from disk, check replay and budget, write and fsync the `intent`,
release the lock, and only then call the signer. Two processes sharing a journal therefore
never both pay one order or both take the last of the budget. An `intent` without a `paid`
line (the signer crashed or returned nothing) stays reserved: it counts against the budget
and its order is never signed again.

The journal is read strictly. Any line that is not a complete record, including a last line
cut off by a crash, makes every later payment refuse with `journal_corrupt` (exit 6) until a
person reconciles the file against the wallet; a line is never skipped. To know what was
spent, add `amount_raw` over the `paid` lines; `intent` lines without one are payments of
unknown outcome. Do not edit or delete the file yourself.

## Tests

```bash
python3 -m unittest discover -s skills/nano-fetch -p 'test_*.py'
```

Against loopback sellers and a dummy signer only: off by default, a v2 and a v1 bound order
paid once with the order's representative, replay refused after a restart, cap, budget,
checksum, a signer that returns no hash or raises; two journals on one file settling one
order, or two orders for the last of the budget, at once; no lock, no payment; a torn
journal tail; URL and `xrb_` aliases of one order; a redirected quote and a redirect on the
paid retry; a dropped connection and a timeout on the paid retry. No network, no key.

## Safety

- No key, seed or wallet file is read or written by this skill; the signer is the operator's.
- Nothing is paid unless both `--signer` and `--journal` are given.
- The cap and the budget are checked before the signer is called, in integer raw.
- In Nano a send block also sets the payer's representative, so a bound send moves the
  payer's voting weight to the order's derived account. The signer should publish a change
  block back to the operator's own representative once the send is confirmed.
- Use `verify-nano-payment` on the seller's side to confirm the block before shipping work.
