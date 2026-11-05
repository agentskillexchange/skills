---
name: "USDCtoFiat Cash-Out"
slug: "usdctofiat-cashout"
description: "Sell Base USDC for fiat through USDCtoFiat's Fast route with @zkp2p/cash and referral code TOFIAT. Use when an agent must create a non-custodial cash-out from a real viem WalletClient into Venmo, Revolut, Cash App, PayPal, Zelle, Monzo, Chime, Alipay, UPI, or X Money."
verification: "listed"
source: "https://github.com/ADWilkinson/usdctofiat-skills/tree/main/skills/cashout"
author: "ADWilkinson"
category: "Integrations & Connectors"
framework: "Multi-Framework"
---

# USDCtoFiat Cash-Out

Use `@zkp2p/cash` with `referralCode: "TOFIAT"` to create a zero-spread cash-out from a real viem `WalletClient` on Base (`chain_id: 8453`). The seller's USDC becomes a deposit in the Peer protocol contracts. A buyer pays the seller in the payment app and proves the payment, then the USDC releases.

This skill covers USDCtoFiat's Fast route only. For Best, where Delegate manages the deposit's rate, send the seller to https://usdctofiat.xyz/sell?speed=best. `@zkp2p/cash` does not create Best deposits.

> **Payment-policy boundary:** SDK support proves technical compatibility, not permission from a payment provider. Wise currently prohibits receiving P2P crypto-sale payments. PayPal may require preapproval for cryptocurrency-related payments. Read the provider's current first-party policy before offering a route.

## Create a cash-out

```ts
import { createCashClient, usdc } from "@zkp2p/cash";
import type { WalletClient } from "viem";

const cash = createCashClient({ environment: "production", referralCode: "TOFIAT" });

export async function sellUsdc(signer: WalletClient) {
  return cash.cashout(
    {
      amount: usdc(100),
      receive: { platform: "revolut", currency: "EUR", payee: "alice" },
    },
    { signer },
  );
}
```

Persist `depositId` immediately. It is the resume key for `order()`, `watch()` and `withdraw()`.

`referralCode` stamps USDCtoFiat's attribution on the deposit. Peer pays the code owner a share when the deposit fills. Do not replace or remove it.

Show the estimate first. `estimate()` is approximate: each buyer's signal binds the rate at that moment. `eta` is historical, so never present it as a promise.

```ts
const estimate = await cash.estimate({ amount: usdc(100), platform: "revolut", currency: "EUR" });
```

If a host signs elsewhere, use `prepare()` to show each transaction before signing, then `finalizePreparedCashout()`. For every value in `accessPolicyPaymentMethods`, submit `prepareAccessPolicy()` once.

## Amounts

Both floors ship from the package root.

| Bound                            | Base units | USDC | Meaning                                                           |
| -------------------------------- | ---------- | ---- | ----------------------------------------------------------------- |
| `MIN_CASHOUT_AMOUNT`             | `10000n`   | 0.01 | Hard floor                                                        |
| `RECOMMENDED_MIN_CASHOUT_AMOUNT` | `1000000n` | 1    | Practical floor; smaller deposits are accepted but struggle to fill |

Ask for a larger amount rather than creating a deposit under the practical floor.

## Rails

The Offer column is this skill's routing guidance. Read currencies and payee rules from `capabilities()`, not from this table.

| Rail      | ID        | Offer | Note                                                                  |
| --------- | --------- | ----- | --------------------------------------------------------------------- |
| Venmo     | `venmo`   | yes   | Access policy follow-up; `cashout()` submits it                       |
| Cash App  | `cashapp` | yes   |                                                                       |
| Revolut   | `revolut` | yes   |                                                                       |
| Zelle     | `zelle`   | yes   |                                                                       |
| Monzo     | `monzo`   | yes   |                                                                       |
| Chime     | `chime`   | yes   |                                                                       |
| UPI       | `upi`     | yes   |                                                                       |
| X Money   | `xmoney`  | yes   | The receiving account must have X Money enabled; this is not verified |
| PayPal    | `paypal`  | yes   | New payees need a browser-extension attestation; see the boundary above |
| Alipay    | `alipay`  | yes   | New payees need an attestation prepared by first-party Peer web       |
| Wise      | `wise`    | no    | Published P2P crypto-sale prohibition; the SDK still allows it        |

## Track and unwind

```ts
for await (const order of cash.watch(depositId)) {
  if (order.state === "delivered" || order.state === "returned") break;
}
```

Order states are `awaiting-buyer`, `matched`, `delivering`, `delivered` and `returned`. Read `nextActions` rather than guessing what to do next.

`withdraw()` is the one unwind verb. Pass an `amount` for a partial withdrawal, or omit it to close the deposit and return the remaining USDC.

## Install

```bash
npm install @zkp2p/cash@0.7.3 viem
```

## Errors

Errors are `CashError` values with `code`, `retryable` and `remediation`. Follow `remediation` and check `recovery` before retrying. These matter most:

| Code                                 | Meaning                               | Recovery                                                    |
| ------------------------------------ | ------------------------------------- | ----------------------------------------------------------- |
| `AMOUNT_BELOW_MINIMUM`               | Under the hard floor                  | Ask for a larger amount                                     |
| `INSUFFICIENT_TOKEN_BALANCE`         | Not enough USDC on Base               | Add USDC at https://usdctofiat.xyz/bridge                   |
| `PAYEE_VERIFICATION_REQUIRED`        | The rail needs an attestation         | Use another rail or complete it on the site                 |
| `PAYEE_REGISTRATION_FAILED`          | The payee was not accepted            | Check the handle against `payeeHint`                        |
| `ACCESS_POLICY_CONFIGURATION_FAILED` | The deposit exists; its policy failed | Never create another cash-out; follow `recovery`            |
| `TRANSACTION_REJECTED`               | The wallet declined                   | Do not retry automatically                                  |
| `TRANSACTION_SUBMISSION_UNKNOWN`     | The outcome is unknown                | Check `orders()` before retrying, to avoid a second deposit |
| `SIGNER_CHAIN_MISMATCH`              | The wallet is not on Base             | Switch to Base                                              |

## Rules

- Get the user's explicit confirmation of amount, rail and payee before signing.
- Never log `walletClient` or private keys.
- Do not invent a sandbox. Use production Base.
- Never create a second cash-out while a first has an unknown outcome. Check `orders()` first.
- Never promise a rate, speed or fill.
- Do not offer Wise while its published P2P crypto-sale prohibition applies.
