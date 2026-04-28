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

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/snyk-dependency-audit-skill/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/snyk-dependency-audit-skill
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/snyk-dependency-audit-skill`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snyk-dependency-audit-skill/)
