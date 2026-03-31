---
name: "npm Registry Analyzer"
description: "Queries the npm registry API and npms.io scoring endpoint to evaluate package quality, maintenance scores, and download trends. Uses npm-audit for security vulnerability detection against the GitHub Advisory Database."
category: "Library & API Reference"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/npm-registry-analyzer/"
---
# npm Registry Analyzer

Queries the npm registry API and npms.io scoring endpoint to evaluate package quality, maintenance scores, and download trends. Uses npm-audit for security vulnerability detection against the GitHub Advisory Database.

## Overview

The npm Registry Analyzer skill provides comprehensive evaluation of Node.js packages through the npm registry API. It retrieves detailed package metadata including version timelines, dependency counts, bundle sizes via bundlephobia API, and maintainer activity metrics.

The skill leverages the npms.io scoring endpoint for quality, popularity, and maintenance scores, providing a holistic view of package health. It integrates npm-audit for vulnerability scanning against the GitHub Advisory Database, identifying known CVEs in direct and transitive dependencies.

Advanced features include comparing alternative packages side-by-side, analyzing download trends via the npm downloads API, checking TypeScript type availability, and verifying ESM/CJS dual-package support. The skill generates structured reports with actionable recommendations for package selection and dependency management decisions.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill npm-registry-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill npm-registry-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill npm-registry-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill npm-registry-analyzer -a codex
```

### OpenClaw

```bash
clawhub install npm-registry-analyzer
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-registry-analyzer/)
