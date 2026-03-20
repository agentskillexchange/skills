---
name: Discord Moderation Bot with AI Classification
description: Listens to Discord gateway events, passing flagged messages to the OpenAI Moderation API and a custom classifier to detect spam and coordinated inauthentic behavior. Issues timeouts via the Discord REST API and logs incidents to a Supabase Postgres table for moderator review. Rule sets are stored in Supabase and hot-reloaded without restart.
category: Security &amp; Verification
framework: Any Agent
verification: verified_metadata
rating: 4.4
reviews: 27
source: https://agentskillexchange.com/skill/discord-moderation-ai-classification/
---

# Discord Moderation Bot with AI Classification

Listens to Discord gateway events, passing flagged messages to the OpenAI Moderation API and a custom classifier to detect spam and coordinated inauthentic behavior. Issues timeouts via the Discord REST API and logs incidents to a Supabase Postgres table for moderator review. Rule sets are stored in Supabase and hot-reloaded without restart.

## Overview

Listens to Discord gateway events, passing flagged messages to the OpenAI Moderation API and a custom classifier to detect spam and coordinated inauthentic behavior. Issues timeouts via the Discord REST API and logs incidents to a Supabase Postgres table for moderator review. Rule sets are stored in Supabase and hot-reloaded without restart.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill discord-moderation-ai-classification
```

### OpenClaw

```bash
clawhub install discord-moderation-ai-classification
```

### Claude Code

```bash
claude mcp add discord-moderation-ai-classification
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/discord-moderation-ai-classification/) for detailed installation instructions.

## Verification

- **Status**: verified_metadata
- **Category**: Security &amp; Verification
- **Framework**: Any Agent
- **Rating**: 4.4/5 (27 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/discord-moderation-ai-classification/)
