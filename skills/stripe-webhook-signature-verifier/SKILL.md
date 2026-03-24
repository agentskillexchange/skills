---
name: "Stripe Webhook Signature Verifier"
description: "Verifies Stripe webhook payload signatures using the Stripe.js SDK and the stripe.webhooks.constructEvent method. Validates the Stripe-Signature header against the raw request body and a configured endpoint secret. Handles tolerance windows for replay attack prevention and logs verification failures to Datadog via the Datadog Logs API."
category: "Security & Verification"
framework: "ChatGPT Agents"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/stripe-webhook-signature-verifier/"
tool_ecosystem:
  tool: "stripe"
  github_stars: 4377
  npm_weekly_downloads: 8442269
  github_repo: "stripe/stripe-node"
  license: "MIT"
  maintained: true
---

# Stripe Webhook Signature Verifier

Verifies Stripe webhook payload signatures using the Stripe.js SDK and the stripe.webhooks.constructEvent method. Validates the Stripe-Signature header against the raw request body and a configured endpoint secret. Handles tolerance windows for replay attack prevention and logs verification failures to Datadog via the Datadog Logs API.

## Installation

### Any Agent (npx)
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

| | |
|---|---|
| **Category** | Security & Verification |
| **Framework** | ChatGPT Agents |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [stripe](https://github.com/stripe/stripe-node) — ⭐ 4.4k · MIT |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-webhook-signature-verifier/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
