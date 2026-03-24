---
name: "GitHub Discussions Community Digest"
description: "Queries GitHub GraphQL API for new and unanswered Discussions, ranks them by reaction count and recency, and drafts a weekly digest via SendGrid. Automatically labels stale discussions as needs-triage via the GitHub REST API. Digest content is also mirrored as a pinned post to a linked Discord channel."
category: "Integrations & Connectors"
framework: "MCP-compatible"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/github-discussions-community-digest/"
tool_ecosystem:
  tool: "sendgrid"
  github_stars: 3054
  npm_weekly_downloads: 3287627
  github_repo: "sendgrid/sendgrid-nodejs"
  license: "MIT"
  maintained: true
---

# GitHub Discussions Community Digest

Queries GitHub GraphQL API for new and unanswered Discussions, ranks them by reaction count and recency, and drafts a weekly digest via SendGrid. Automatically labels stale discussions as needs-triage via the GitHub REST API. Digest content is also mirrored as a pinned post to a linked Discord channel.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill github-discussions-community-digest
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill github-discussions-community-digest -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill github-discussions-community-digest -a cursor
```

### OpenClaw
```bash
clawhub install github-discussions-community-digest
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill github-discussions-community-digest -a codex
```

## Details

| | |
|---|---|
| **Category** | Integrations & Connectors |
| **Framework** | MCP-compatible |
| **Verification** | 📋 Listed |
| **Tool** | [sendgrid](https://github.com/sendgrid/sendgrid-nodejs) — ⭐ 3.1k · MIT |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/github-discussions-community-digest/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
