---
name: "Heroku Release Rollback Assistant"
description: "Uses the Heroku Platform API to identify the last stable release before a regression and execute a rollback. Compares config vars between releases to flag changes that may have caused the issue."
category: "CI/CD Integrations"
framework: "ChatGPT Agents"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/heroku-release-rollback-assistant-2/"
---

# Heroku Release Rollback Assistant

Uses the Heroku Platform API to identify the last stable release before a regression and execute a rollback. Compares config vars between releases to flag changes that may have caused the issue.

## Overview

Uses the Heroku Platform API to identify the last stable release before a regression and execute a rollback. Compares config vars between releases to flag changes that may have caused the issue.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill heroku-release-rollback-assistant-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill heroku-release-rollback-assistant-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill heroku-release-rollback-assistant-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill heroku-release-rollback-assistant-2 -a codex
```

### OpenClaw

```bash
clawhub install heroku-release-rollback-assistant-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/heroku-release-rollback-assistant-2/
