---
name: "Run agent mailboxes and pull verification codes or reply context programmatically with Mails"
slug: "run-agent-mailboxes-and-pull-verification-codes-or-reply-context-programmatically-with-mails"
description: "Give an agent a mailbox it can send from, read from, search, sync locally, and mine for login codes or attachments without hand-driving a normal email client."
github_stars: 294
verification: "security_reviewed"
source: "https://github.com/chekusu/mails"
author: "chekusu"
publisher_type: "individual"
category: "Calendar, Email & Productivity"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "chekusu/mails"
  github_stars: 294
  npm_package: "mails"
  npm_weekly_downloads: 1289
---

# Run agent mailboxes and pull verification codes or reply context programmatically with Mails

Give an agent a mailbox it can send from, read from, search, sync locally, and mine for login codes or attachments without hand-driving a normal email client.

## Prerequisites

Node.js or Bun, Mails CLI or SDK, a claimed or self-hosted mailbox, optional Resend key for sending, optional Cloudflare Worker deployment for self-hosted mode

## Installation

Use the upstream install or setup path that matches your environment:
- npm install -g mails
- npx mails

Requirements and caveats from upstream:
- All /api/* endpoints require Authorization: Bearer <mailbox-token>. The token must belong to the mailbox in ?to=, the email being fetched, or the from address being sent. /health is always public. If no mailbox token...
- bun test:live # Live E2E with real Resend + Cloudflare (requires .env)

Basic usage or getting-started notes:
- | mails send --to user@example.com | email to agent@mails.dev
- bash
- # or

- Source: https://github.com/chekusu/mails
- Extracted from upstream docs: https://raw.githubusercontent.com/chekusu/mails/HEAD/README.md

## Documentation

- https://mails.dev

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-agent-mailboxes-and-pull-verification-codes-or-reply-context-programmatically-with-mails/)
