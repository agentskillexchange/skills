---
title: "npm Registry Analyzer"
description: "Queries the npm registry API and npms.io scoring endpoint to evaluate package quality, maintenance scores, and download trends. Uses npm-audit for security vulnerability detection against the GitHub Advisory Database."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/npm-registry-analyzer/"
category:
  - "Library & API Reference"
framework:
  - "MCP"
---

# npm Registry Analyzer

The npm Registry Analyzer skill provides comprehensive evaluation of Node.js packages through the npm registry API. It retrieves detailed package metadata including version timelines, dependency counts, bundle sizes via bundlephobia API, and maintainer activity metrics.

The skill leverages the npms.io scoring endpoint for quality, popularity, and maintenance scores, providing a holistic view of package health. It integrates npm-audit for vulnerability scanning against the GitHub Advisory Database, identifying known CVEs in direct and transitive dependencies.

Advanced features include comparing alternative packages side-by-side, analyzing download trends via the npm downloads API, checking TypeScript type availability, and verifying ESM/CJS dual-package support. The skill generates structured reports with actionable recommendations for package selection and dependency management decisions.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/npm-registry-analyzer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/npm-registry-analyzer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/npm-registry-analyzer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-registry-analyzer/)
