---
title: "NPM Package Explorer"
description: "Explores the npm registry using the Registry API and npms.io scoring API. Analyzes package quality, dependency trees, and bundle sizes via bundlephobia API."
verification: "security_reviewed"
source: "https://docs.npmjs.com/"
category:
  - "Library & API Reference"
framework:
  - "Cursor"
---

# NPM Package Explorer

NPM Package Explorer queries the npm Registry API to provide deep analysis of npm packages and their ecosystems. It retrieves package metadata, version histories, and maintainer information directly from the registry. Integration with the npms.io API provides quality, popularity, and maintenance scores for informed package selection. Bundle size analysis uses the bundlephobia API to estimate the impact of adding packages to frontend projects, including tree-shaking support detection. The tool builds comprehensive dependency trees using the npm resolve algorithm, identifying duplicate packages and version conflicts. License compliance scanning detects incompatible license combinations across dependency chains. It tracks download statistics via the npm downloads API with trend analysis and comparison charts. Security audit integration cross-references with npm audit advisories and Snyk vulnerability database for real-time risk assessment.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/npm-package-explorer-registry-api/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/npm-package-explorer-registry-api
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/npm-package-explorer-registry-api`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-explorer-registry-api/)
