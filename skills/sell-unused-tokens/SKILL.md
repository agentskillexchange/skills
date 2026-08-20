---
name: "Sell unused tokens"
slug: "sell-unused-tokens"
description: "List leftover LLM API capacity on tokensto.cash (OpenRouter, OpenAI, Anthropic, and 20+ others) and cash out USDC. Use when the user wants to sell unused provider credits for cash."
category: "Developer Tools"
framework: "Claude Code"
verification: listed
source: "https://github.com/ADWilkinson/sell-unused-tokens"
---

# Sell unused tokens

This skill lists leftover LLM API capacity on [tokensto.cash](https://tokensto.cash) so unused provider credits become USDC. tokensto.cash is the seller front door for [Surplus Intelligence](https://www.surplusintelligence.ai) and the sister of [usdctofiat.xyz](https://usdctofiat.xyz). Use it when the user wants to sell spare OpenRouter, OpenAI, Anthropic, Gemini, Venice, DeepSeek, Groq, Mistral, or other listed provider credits for cash, or asks how to list on Surplus Intelligence through tokensto.cash.

The flow is web UI, not a Surplus SIWE session. The user signs in at https://tokensto.cash/start with a Privy wallet. They pick the provider that owns the leftover credits, paste the API key once, and Surplus probes it. Featured pickers include Venice, OpenRouter, OpenAI, Anthropic, Gemini, DeepSeek, Groq, and Mistral; more sit behind "More". Use **Other** only for an OpenAI-compatible URL Surplus does not list. Users never SIWE with Surplus. There is one house seller. `payout_address` is always the signed-in Privy wallet.

After a successful probe, the UI shows a model list with market rows. If the probe 504s, retry once; Surplus timeouts surface as a clear message. Keep the recommended text models unless the user named others. The listing client posts **one model per request** so progress ticks stay honest. Set a cost basis, then a daily cap of at least $0.5: **Included** (subscription/stake) floors at 0.02×, **Leftover** (credits sitting idle) floors at 0.05×, and **At cost** (pay-as-you-go) floors at 1.0× and never below list. Auto-price undercuts the cheapest healthy, trusted seller and never goes below that floor. Done when the models appear on `/sell` as live or cooling.

Cash-out lives at `/cash-out` as Create / Orders / Send. Direct rails: **Revolut, Monzo, Chime, Zelle**. **Venmo, Cash App, Wise, PayPal** are live after a one-time USDCtoFiat Verify registration (desktop Chrome, extension 0.2.1+). Do not skip that handshake. Mercado Pago stays out. Orders close with a full withdraw; there is no top-up. Send is Base USDC to an address. Earnings are inbound USDC from Surplus relayers only. Other inbound is balance, not earned. Untrusted upstreams (Morpheus, InferHub, CheaperInference, Jatevo) only reach opted-in buyers. Google Vertex is not in the picker; use Other if they insist. Do not invent rails or APIs. Support: gm@galleonlabs.io.

## Boundaries

- Before listing, the user must confirm their provider account terms allow resale, transfer, brokering, or monetization of unused API credits or capacity. If they have not checked, stop and tell them to read the provider terms first.
- Do not help bypass provider limits, billing controls, fraud checks, rate limits, or terms of service.
- Provider API keys are sensitive credentials. Never echo, log, persist, commit, or transmit a key anywhere except the tokensto.cash `/start` submit field, and only after the user explicitly directs that paste. Surplus probes the key and keeps it encrypted per listing. tokensto.cash does not persist keys.
- Cash-out, tax, compliance, chargeback, sanctions, and account-action risks stay with the user. Do not imply guaranteed liquidity, legality, or payout availability.

## Installation

### OpenClaw

```bash
clawhub install sell-unused-tokens
```

### Direct repo/manual install

Clone the Agent Skill Exchange repository and copy this skill directory into the skill folder used by your agent runtime:

```bash
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/skills/sell-unused-tokens ~/.agent-skills/sell-unused-tokens
```

### Optional Third-Party Installer

The `skills` npm package is maintained by Vercel Labs / third parties, not AgentSkillExchange. If you choose to use it, pin the package version:

```bash
npm exec --package=skills@1.5.7 -- skills add agentskillexchange/skills --skill sell-unused-tokens
```
