---
name: "WP-CLI Content Drift Auditor"
category: "WordPress & CMS"
verification: "security_reviewed"
source: "https://github.com/wp-cli/wp-cli"
tool_ecosystem:
  github_repo: "wp-cli/wp-cli"
  github_stars: 5048
---

# WP-CLI Content Drift Auditor

Audits WordPress content drift by comparing live posts, revisions, and key options using WP-CLI commands like `wp post list`, `wp post meta get`, and `wp option get`. Useful for catching accidental edits, stale templates, and mismatches between REST output and database state before they turn into site-wide regressions.

## Installation

Install this skill using one of the following methods:

```bash
# ClawHub CLI
clawhub install wp-cli-content-drift-auditor

# OpenClaw CLI
openclaw skills install wp-cli-content-drift-auditor

# Chat command
/skill install wp-cli-content-drift-auditor

# Direct download
curl -L https://agentskillexchange.com/skills/wp-cli-content-drift-auditor/download -o wp-cli-content-drift-auditor.zip

# Git clone this repo and copy the skill folder
cp -r skills/wp-cli-content-drift-auditor ~/.openclaw/workspace/skills/
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-cli-content-drift-auditor/)
