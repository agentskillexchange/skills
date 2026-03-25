---
name: "Webhook Debugger"
description: "Use this skill when you need to inspect, replay, or debug webhook payloads from services like Stripe, GitHub, or Twilio. It captures webhook events, validates signatures, shows payload structure, and helps trace why a webhook handler failed to process correctly."
category: "Developer Tools"
framework: "Claude Agents"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/webhook-debugger/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "stripe"  # from ase_tool_match
  github_stars: 4377  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 8442269  # from ase_npm_downloads
  github_repo: "stripe/stripe-node"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Webhook Debugger

Use this skill when you need to inspect, replay, or debug webhook payloads from services like Stripe, GitHub, or Twilio. It captures webhook events, validates signatures, shows payload structure, and helps trace why a webhook handler failed to process correctly.

## Overview

Use this skill when you need to inspect, replay, or debug webhook payloads from services like Stripe, GitHub, or Twilio. It captures webhook events, validates signatures, shows payload structure, and helps trace why a webhook handler failed to process correctly.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill webhook-debugger
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill webhook-debugger -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill webhook-debugger -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill webhook-debugger -a codex
```

### OpenClaw

```bash
clawhub install webhook-debugger
```

## Source

- Marketplace: https://agentskillexchange.com/skills/webhook-debugger/
