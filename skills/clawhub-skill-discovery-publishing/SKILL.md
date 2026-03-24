---
name: "ClawHub Skill Discovery & Publishing"
description: "Search, install, update, and publish OpenClaw skills from the command line. The package manager for the OpenClaw skill ecosystem."
category: "Integrations & Connectors"
framework: "OpenClaw"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/clawhub-skill-discovery-publishing/"
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

Install globally via `npm i -g clawhub`. For publishing, authenticate with `clawhub login`. Default registry: clawhub.com. Override with `CLAWHUB_REGISTRY` env var.

**Source:** [OpenClaw skills/clawhub](https://github.com/openclaw/openclaw/tree/main/skills/clawhub)

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill clawhub-skill-discovery-publishing
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill clawhub-skill-discovery-publishing -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill clawhub-skill-discovery-publishing -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill clawhub-skill-discovery-publishing -a codex
```

### OpenClaw

```bash
clawhub install clawhub-skill-discovery-publishing
```

## Source

- Marketplace: https://agentskillexchange.com/skills/clawhub-skill-discovery-publishing/
