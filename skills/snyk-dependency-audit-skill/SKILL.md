---
title: "Snyk Dependency Audit Skill"
description: "Uses the Snyk CLI and REST API v1 to scan package manifests for known CVEs. Cross-references findings with the GitHub Advisory Database and produces SBOM documents in CycloneDX format."
verification: security_reviewed
source: "https://github.com/snyk/cli"
category:
  - "Security & Verification"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "snyk/cli"
  github_stars: 5496
---

# Snyk Dependency Audit Skill

Uses the Snyk CLI and REST API v1 to scan package manifests for known CVEs. Cross-references findings with the GitHub Advisory Database and produces SBOM documents in CycloneDX format.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/snyk-dependency-audit-skill
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/snyk-dependency-audit-skill` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snyk-dependency-audit-skill/)
