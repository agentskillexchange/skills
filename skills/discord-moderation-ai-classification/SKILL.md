---
name: "Discord Moderation Bot with AI Classification"
description: "Listens to Discord gateway events, passing flagged messages to the OpenAI Moderation API and a custom classifier to detect spam and coordinated inauthentic behavior. Issues timeouts via the Discord REST API and logs incidents to a Supabase Postgres table for moderator review. Rule sets are stored in Supabase and hot-reloaded without restart."
category: "Security & Verification"
framework: "Cursor"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/discord-moderation-ai-classification/"
tool_ecosystem:
  tool: "discord"
  github_stars: 10761
  npm_weekly_downloads: 508798
  github_repo: "openai/openai-node"
  license: "Apache-2.0"
  maintained: true
---

# Discord Moderation Bot with AI Classification

Listens to Discord gateway events, passing flagged messages to the OpenAI Moderation API and a custom classifier to detect spam and coordinated inauthentic behavior. Issues timeouts via the Discord REST API and logs incidents to a Supabase Postgres table for moderator review. Rule sets are stored in Supabase and hot-reloaded without restart.

## Installation

### Any Agent (npx)
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

| | |
|---|---|
| **Category** | Security & Verification |
| **Framework** | Cursor |
| **Verification** | 📋 Listed |
| **Tool** | [discord](https://github.com/openai/openai-node) — ⭐ 10.8k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/discord-moderation-ai-classification/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
