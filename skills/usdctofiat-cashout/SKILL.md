---
name: "USDCtoFiat Cash-Out"
slug: "usdctofiat-cashout"
description: "Add non-custodial Base USDC-to-fiat cash-out with @usdctofiat/offramp cashout({ mode: \"fast\" | \"best\" }). Use when an agent must sell USDC from a real viem WalletClient into Venmo, Cash App, Revolut, PayPal, Zelle, Monzo, or Chime without an exchange account."
verification: "listed"
source: "https://github.com/ADWilkinson/usdctofiat-skills/tree/main/skills/cashout"
category: "Integrations & Connectors"
framework: "Multi-Framework"
---

# USDCtoFiat Cash-Out

Teaches coding agents to cash out native Base USDC through USDCtoFiat by Galleon. The golden path is one function: `cashout({ mode: "fast" | "best" })` from `@usdctofiat/offramp` on a real viem `WalletClient` (`chain_id: 8453`). Fast uses the live oracle route at 0% spread (TOFIAT). Best delegates pricing to the Delegate vault at 10 bps on USDC. Both modes are valid; the user must choose.

SDK support is technical compatibility, not permission from a payment provider. Wise currently prohibits receiving P2P crypto-sale payments. PayPal may require preapproval for cryptocurrency-related payments. Read the provider's current first-party policy before offering a route.

```ts
import { cashout } from "@usdctofiat/offramp";
import type { WalletClient } from "viem";

export async function sellUsdc(signer: WalletClient) {
  return cashout({
    mode: "fast",
    signer,
    amount: "100",
    currency: "EUR",
    platform: "revolut",
    payee: "alice",
  });
}
```

Persist `depositId` immediately. Fast `depositId` is the composite resume key for `createOfframp().watch()`. Best `depositId` is the numeric EscrowV2 id for `deposits()` / `close()`. Production Base only. No sandbox.

## Installation

No source-backed install or usage instructions could be extracted automatically. Review the upstream project before running this skill in a sensitive workflow.

- Source: https://github.com/ADWilkinson/usdctofiat-skills/tree/main/skills/cashout

## Source

- Skill repo: https://github.com/ADWilkinson/usdctofiat-skills/tree/main/skills/cashout
- SDK: https://www.npmjs.com/package/@usdctofiat/offramp
- Product: https://usdctofiat.xyz/developers
