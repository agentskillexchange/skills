---
title: "NPM Package Explorer"
description: "Explores the npm registry using the Registry API and npms.io scoring API. Analyzes package quality, dependency trees, and bundle sizes via bundlephobia API."
slug: "npm-package-explorer-registry-api"
category:
  - "Library &amp; API Reference"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/npm-package-explorer-registry-api/"
listed: true
---

# NPM Package Explorer

Explores the npm registry using the Registry API and npms.io scoring API. Analyzes package quality, dependency trees, and bundle sizes via bundlephobia API.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install npm-package-explorer-registry-api
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

NPM Package Explorer queries the npm Registry API to provide deep analysis of npm packages and their ecosystems. It retrieves package metadata, version histories, and maintainer information directly from the registry. Integration with the npms.io API provides quality, popularity, and maintenance scores for informed package selection. Bundle size analysis uses the bundlephobia API to estimate the impact of adding packages to frontend projects, including tree-shaking support detection. The tool builds comprehensive dependency trees using the npm resolve algorithm, identifying duplicate packages and version conflicts. License compliance scanning detects incompatible license combinations across dependency chains. It tracks download statistics via the npm downloads API with trend analysis and comparison charts. Security audit integration cross-references with npm audit advisories and Snyk vulnerability database for real-time risk assessment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-explorer-registry-api/)
