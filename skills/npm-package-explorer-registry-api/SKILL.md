---
title: "NPM Package Explorer"
description: "Explores the npm registry using the Registry API and npms.io scoring API. Analyzes package quality, dependency trees, and bundle sizes via bundlephobia API."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/npm-package-explorer-registry-api/"
category:
  - "Library & API Reference"
framework:
  - "Cursor"
---

# NPM Package Explorer

NPM Package Explorer queries the npm Registry API to provide deep analysis of npm packages and their ecosystems. It retrieves package metadata, version histories, and maintainer information directly from the registry. Integration with the npms.io API provides quality, popularity, and maintenance scores for informed package selection. Bundle size analysis uses the bundlephobia API to estimate the impact of adding packages to frontend projects, including tree-shaking support detection. The tool builds comprehensive dependency trees using the npm resolve algorithm, identifying duplicate packages and version conflicts. License compliance scanning detects incompatible license combinations across dependency chains. It tracks download statistics via the npm downloads API with trend analysis and comparison charts. Security audit integration cross-references with npm audit advisories and Snyk vulnerability database for real-time risk assessment.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/npm-package-explorer-registry-api
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/npm-package-explorer-registry-api` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-explorer-registry-api/)
