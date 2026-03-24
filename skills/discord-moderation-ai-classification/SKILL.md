---
name: "Discord Moderation Bot with AI Classification"
description: "Listens to Discord gateway events, passing flagged messages to the OpenAI Moderation API and a custom classifier to detect spam and coordinated inauthentic behavior. Issues timeouts via the Discord REST API and logs incidents to a Supabase Postgres table for moderator review. Rule sets are stored in Supabase and hot-reloaded without restart."
category: "Security & Verification"
framework: "Cursor"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/discord-moderation-ai-classification/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "discord"  # from ase_tool_match
  github_stars: 26650  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 508798  # from ase_npm_downloads
  github_repo: "discordjs/discord.js"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Discord Moderation Bot with AI Classification

Listens to Discord gateway events, passing flagged messages to the OpenAI Moderation API and a custom classifier to detect spam and coordinated inauthentic behavior. Issues timeouts via the Discord REST API and logs incidents to a Supabase Postgres table for moderator review. Rule sets are stored in Supabase and hot-reloaded without restart.

## Overview

Listens to Discord gateway events, passing flagged messages to the OpenAI Moderation API and a custom classifier to detect spam and coordinated inauthentic behavior. Issues timeouts via the Discord REST API and logs incidents to a Supabase Postgres table for moderator review. Rule sets are stored in Supabase and hot-reloaded without restart.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill discord-moderation-ai-classification
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill discord-moderation-ai-classification -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill discord-moderation-ai-classification -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill discord-moderation-ai-classification -a codex
```

### OpenClaw

```bash
clawhub install discord-moderation-ai-classification
```

## Source

- Marketplace: https://agentskillexchange.com/skills/discord-moderation-ai-classification/
