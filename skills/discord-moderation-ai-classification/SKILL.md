---
name: "Discord Moderation Bot with AI Classification"
description: "Listens to Discord gateway events, passing flagged messages to the OpenAI Moderation API and a custom classifier to detect spam and coordinated inauthentic behavior. Issues timeouts via the Discord REST API and logs incidents to a Supabase Postgres table for moderator review. Rule sets are stored in Supabase and hot-reloaded without restart."
category: "Security & Verification"
framework: "Cursor"
verification: verified_metadata
rating: 4.4
reviews: 27
creator: "Rachel Green"
creator_handle: "@rachelgreen"
creator_verified: false
source: "https://agentskillexchange.com/skills/discord-moderation-ai-classification/"
---
# Discord Moderation Bot with AI Classification

Listens to Discord gateway events, passing flagged messages to the OpenAI Moderation API and a custom classifier to detect spam and coordinated inauthentic behavior. Issues timeouts via the Discord REST API and logs incidents to a Supabase Postgres table for moderator review. Rule sets are stored in Supabase and hot-reloaded without restart.

## Installation

### Any agent (npx skills)

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

### OpenClaw

```bash
clawhub install discord-moderation-ai-classification
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill discord-moderation-ai-classification -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Security & Verification |
| Framework | Cursor |
| Verification | Verified Metadata |
| Rating | 4.4/5 (27 reviews) |

## Creator

**Rachel Green**
- Profile: [@rachelgreen](https://agentskillexchange.com/browse-skills/?creator=rachelgreen)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/discord-moderation-ai-classification/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
