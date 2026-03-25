---
name: "Slack Channel Summarizer"
description: "Generates channel summaries using Slack Bolt SDK with conversations.history and conversations.replies endpoints. Leverages OpenAI GPT-4 API for abstractive summarization and delivers digests via Slack Block Kit interactive messages."
category: "Calendar, Email & Productivity"
framework: "MCP-compatible"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/slack-channel-summarizer-bolt-sdk/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "slack"  # from ase_tool_match
  github_stars: 2899  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 2433529  # from ase_npm_downloads
  github_repo: "slackapi/bolt-js"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Slack Channel Summarizer

Generates channel summaries using Slack Bolt SDK with conversations.history and conversations.replies endpoints. Leverages OpenAI GPT-4 API for abstractive summarization and delivers digests via Slack Block Kit interactive messages.

## Overview

Generates channel summaries using Slack Bolt SDK with conversations.history and conversations.replies endpoints. Leverages OpenAI GPT-4 API for abstractive summarization and delivers digests via Slack Block Kit interactive messages.

This skill provides a comprehensive automation layer for developers and teams who need reliable, repeatable workflows. It handles authentication, rate limiting, and error recovery automatically, so you can focus on the logic that matters. The agent monitors for changes in real time and applies incremental updates to minimize API calls and reduce latency. Configuration is handled through a simple YAML manifest that defines inputs, outputs, and trigger conditions. Built-in logging captures every action for audit trails and debugging. Supports both interactive and headless modes, making it suitable for CI/CD pipelines as well as local development. The skill includes pre-built templates for common use cases and can be extended with custom plugins. Error handling follows exponential backoff with jitter for transient failures and provides clear diagnostic messages for permanent errors. Compatible with major operating systems and containerized environments. Tested against production workloads with comprehensive integration test suites.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill slack-channel-summarizer-bolt-sdk
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill slack-channel-summarizer-bolt-sdk -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill slack-channel-summarizer-bolt-sdk -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill slack-channel-summarizer-bolt-sdk -a codex
```

### OpenClaw

```bash
clawhub install slack-channel-summarizer-bolt-sdk
```

## Source

- Marketplace: https://agentskillexchange.com/skills/slack-channel-summarizer-bolt-sdk/
