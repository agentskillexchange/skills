---
name: "Stripe Webhook Signature Verifier"
description: "Verifies Stripe webhook payload signatures using the Stripe.js SDK and the stripe.webhooks.constructEvent method. Validates the Stripe-Signature header against the raw request body and a configured endpoint secret. Handles tolerance windows for replay attack prevention and logs verification failures to Datadog via the Datadog Logs API."
category: "Security & Verification"
framework: "ChatGPT Agents"
verification: verified_metadata
rating: 4.0
reviews: 36
creator: Tom Anderson
creator_handle: tanderson
creator_verified: false
source: https://agentskillexchange.com/skill/stripe-webhook-signature-verifier/
---

# Stripe Webhook Signature Verifier

Verifies Stripe webhook payload signatures using the Stripe.js SDK and the stripe.webhooks.constructEvent method. Validates the Stripe-Signature header against the raw request body and a configured endpoint secret. Handles tolerance windows for replay attack prevention and logs verification failures to Datadog via the Datadog Logs API.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill stripe-webhook-signature-verifier
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill stripe-webhook-signature-verifier -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill stripe-webhook-signature-verifier -a cursor
```

### OpenClaw

```bash
clawhub install stripe-webhook-signature-verifier
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill stripe-webhook-signature-verifier -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Security & Verification |
| Framework | ChatGPT Agents |
| Verification | Verified Metadata |
| Rating | 4.0/5 (36 reviews) |

## Creator

**Tom Anderson**
- Profile: [@tanderson](https://agentskillexchange.com/browse-skills/?creator=tanderson)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/stripe-webhook-signature-verifier/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
