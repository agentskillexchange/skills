---
name: GitHub Discussions Community Digest
description: Queries GitHub GraphQL API for new and unanswered Discussions, ranks them by reaction count and recency, and drafts a weekly digest via SendGrid. Automatically labels stale discussions as needs-triage
category: Integrations & Connectors
framework: MCP
verification: security_reviewed
rating: 4.8
reviews: 31
source: https://agentskillexchange.com/skill/github-discussions-community-digest/
---

# GitHub Discussions Community Digest

Queries GitHub GraphQL API for new and unanswered Discussions, ranks them by reaction count and recency, and drafts a weekly digest via SendGrid. Automatically labels stale discussions as needs-triage via the GitHub REST API. Digest content is also mirrored as a pinned post to a linked Discord channel.

## Overview

Queries GitHub GraphQL API for new and unanswered Discussions, ranks them by reaction count and recency, and drafts a weekly digest via SendGrid. Automatically labels stale discussions as needs-triage via the GitHub REST API. Digest content is also mirrored as a pinned post to a linked Discord channel.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill github-discussions-community-digest
```

### OpenClaw

```bash
openclaw install github-discussions-community-digest
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | Integrations & Connectors |
| Framework | MCP |
| Verification | Security Reviewed |
| Rating | ⭐⭐⭐⭐ 4.8/5.0 (31 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/github-discussions-community-digest/)*
