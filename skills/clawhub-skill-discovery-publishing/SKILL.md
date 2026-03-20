---
name: ClawHub Skill Discovery & Publishing
description: Search, install, update, and publish OpenClaw skills from the command line. The package manager for the OpenClaw skill ecosystem.
category: Integrations & Connectors
framework: OpenClaw
verification: security_reviewed
rating: 4.8
reviews: 52
source: https://agentskillexchange.com/skill/clawhub-skill-discovery-publishing/
---

# ClawHub Skill Discovery & Publishing

Search, install, update, and publish OpenClaw skills from the command line. The package manager for the OpenClaw skill ecosystem.

## Overview

The ClawHub CLI connects to the skill registry and provides five core operations: search by keyword, install skills by slug with optional version pinning, update one or all installed skills, list local skills and versions, and publish skill folders with version and changelog.
Best for

Discovering new skills from the registry
Keeping installed skills current with hash-based version matching
Publishing custom skills to the community or your team
Managing skill versions across workspaces

Install notes
Install globally via npm i -g clawhub. For publishing, authenticate with clawhub login. Default registry: clawhub.com. Override with CLAWHUB_REGISTRY env var.
Source: OpenClaw skills/clawhub

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill clawhub-skill-discovery-publishing
```

### OpenClaw

```bash
openclaw install clawhub-skill-discovery-publishing
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | Integrations & Connectors |
| Framework | OpenClaw |
| Verification | Security Reviewed |
| Rating | ⭐⭐⭐⭐ 4.8/5.0 (52 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/clawhub-skill-discovery-publishing/)*
