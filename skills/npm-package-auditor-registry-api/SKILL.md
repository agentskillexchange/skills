---
title: "NPM Package Auditor"
description: "Audits NPM packages using the NPM Registry API with dependency tree resolution and vulnerability scanning via OSV.dev API. Generates SBOM in CycloneDX format and checks license compliance against SPDX expression parser."
verification: "security_reviewed"
source: "https://docs.npmjs.com/cli/v10/using-npm/registry/"
category:
  - "Developer Tools"
framework:
  - "MCP"
---

# NPM Package Auditor

Audits NPM packages using the NPM Registry API with dependency tree resolution and vulnerability scanning via OSV.dev API. Generates SBOM in CycloneDX format and checks license compliance against SPDX expression parser.

This skill provides a comprehensive automation layer for developers and teams who need reliable, repeatable workflows. It handles authentication, rate limiting, and error recovery automatically, so you can focus on the logic that matters. The agent monitors for changes in real time and applies incremental updates to minimize API calls and reduce latency. Configuration is handled through a simple YAML manifest that defines inputs, outputs, and trigger conditions. Built-in logging captures every action for audit trails and debugging. Supports both interactive and headless modes, making it suitable for CI/CD pipelines as well as local development. The skill includes pre-built templates for common use cases and can be extended with custom plugins. Error handling follows exponential backoff with jitter for transient failures and provides clear diagnostic messages for permanent errors. Compatible with major operating systems and containerized environments. Tested against production workloads with comprehensive integration test suites.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/npm-package-auditor-registry-api/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/npm-package-auditor-registry-api
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/npm-package-auditor-registry-api`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-auditor-registry-api/)
