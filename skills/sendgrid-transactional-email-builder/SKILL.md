---
name: "SendGrid Transactional Email Builder"
description: "Constructs and sends transactional emails using the SendGrid v3 Mail Send API. Builds dynamic templates with Handlebars substitutions, manages suppression groups, and tracks delivery via Event Webhook parsing."
category: "Integrations & Connectors"
framework: "MCP-compatible"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/sendgrid-transactional-email-builder/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "sendgrid"  # from ase_tool_match
  github_stars: 3054  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 3287627  # from ase_npm_downloads
  github_repo: "sendgrid/sendgrid-nodejs"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# SendGrid Transactional Email Builder

Constructs and sends transactional emails using the SendGrid v3 Mail Send API. Builds dynamic templates with Handlebars substitutions, manages suppression groups, and tracks delivery via Event Webhook parsing.

## Overview

The SendGrid Transactional Email Builder creates and manages transactional email workflows using SendGrid’s v3 Mail Send API. It constructs emails with dynamic template data using Handlebars syntax for personalization, handles recipient management, and provides delivery tracking.

The skill uses `@sendgrid/mail` to send single and batch emails via `sgMail.send()` and `sgMail.sendMultiple()`. It supports dynamic templates created in SendGrid with `template_id` and `dynamic_template_data` for variable substitution. Advanced personalization includes conditional sections and iteration blocks in templates.

Delivery management features include suppression group integration with `asm.group_id`, category tagging for analytics segmentation, and send-at scheduling with Unix timestamps. The agent parses Event Webhook payloads for delivery, open, click, bounce, and spam report events. It handles bounce management by updating suppression lists and implements exponential backoff for rate limit (429) responses. Supports sender identity verification and domain authentication status checks via the Sender Authentication API.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sendgrid-transactional-email-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sendgrid-transactional-email-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sendgrid-transactional-email-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sendgrid-transactional-email-builder -a codex
```

### OpenClaw

```bash
clawhub install sendgrid-transactional-email-builder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/sendgrid-transactional-email-builder/
