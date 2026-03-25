---
name: "GitHub Discussions Community Digest"
description: "Queries GitHub GraphQL API for new and unanswered Discussions, ranks them by reaction count and recency, and drafts a weekly digest via SendGrid. Automatically labels stale discussions as needs-triage via the GitHub REST API. Digest content is also mirrored as a pinned post to a linked Discord channel."
category: "Integrations & Connectors"
framework: "MCP-compatible"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/github-discussions-community-digest/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "sendgrid"  # from ase_tool_match
  github_stars: 3054  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 3287627  # from ase_npm_downloads
  github_repo: "sendgrid/sendgrid-nodejs"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# GitHub Discussions Community Digest

Queries GitHub GraphQL API for new and unanswered Discussions, ranks them by reaction count and recency, and drafts a weekly digest via SendGrid. Automatically labels stale discussions as needs-triage via the GitHub REST API. Digest content is also mirrored as a pinned post to a linked Discord channel.

## Overview

Queries GitHub GraphQL API for new and unanswered Discussions, ranks them by reaction count and recency, and drafts a weekly digest via SendGrid. Automatically labels stale discussions as needs-triage via the GitHub REST API. Digest content is also mirrored as a pinned post to a linked Discord channel.

## Installation

### Any Agent

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

### Codex

```bash
npx skills add agentskillexchange/skills --skill github-discussions-community-digest -a codex
```

### OpenClaw

```bash
clawhub install github-discussions-community-digest
```

## Source

- Marketplace: https://agentskillexchange.com/skills/github-discussions-community-digest/
