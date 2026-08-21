---
name: "USDCtoFiat Cash-Out"
slug: "usdctofiat-cashout"
description: "Add non-custodial Base USDC-to-fiat cash-out with @usdctofiat/offramp cashout({ mode: \"fast\" | \"best\" }). Use when an agent must sell USDC from a real viem WalletClient into Venmo, Cash App, Revolut, PayPal, Zelle, Monzo, or Chime without an exchange account."
category: "Integrations & Connectors"
framework: "Multi-Framework"
verification: listed
source: "https://github.com/ADWilkinson/usdctofiat-skills/tree/main/skills/cashout"
tool_ecosystem:
  tool: "@usdctofiat/offramp"
  github_repo: "ADWilkinson/usdctofiat-skills"
  npm_package: "@usdctofiat/offramp"
  license: "MIT"
  maintained: true
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

### Direct repo / npx skills

```bash
npm exec --package=skills@1.5.23 -- skills add ADWilkinson/usdctofiat-skills --skill cashout
npm install @usdctofiat/offramp@8.0.1
```

### Agent Skill Exchange

```bash
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/skills/usdctofiat-cashout ~/.agent-skills/usdctofiat-cashout
```

### Optional Third-Party Installer

```bash
npm exec --package=skills@1.5.23 -- skills add agentskillexchange/skills --skill usdctofiat-cashout
```

## Source

- Skill repo: https://github.com/ADWilkinson/usdctofiat-skills/tree/main/skills/cashout
- SDK: https://www.npmjs.com/package/@usdctofiat/offramp
- Product: https://usdctofiat.xyz/developers
