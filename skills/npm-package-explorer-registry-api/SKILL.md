---
name: "NPM Package Explorer"
description: "Explores the npm registry using the Registry API and npms.io scoring API. Analyzes package quality, dependency trees, and bundle sizes via bundlephobia API."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/npm-package-explorer-registry-api/"
category:
  - "Library &amp; API Reference"
framework:
  - "Cursor"
---

# NPM Package Explorer

NPM Package Explorer queries the npm Registry API to provide deep analysis of npm packages and their ecosystems. It retrieves package metadata, version histories, and maintainer information directly from the registry. Integration with the npms.io API provides quality, popularity, and maintenance scores for informed package selection. Bundle size analysis uses the bundlephobia API to estimate the impact of adding packages to frontend projects, including tree-shaking support detection. The tool builds comprehensive dependency trees using the npm resolve algorithm, identifying duplicate packages and version conflicts. License compliance scanning detects incompatible license combinations across dependency chains. It tracks download statistics via the npm downloads API with trend analysis and comparison charts. Security audit integration cross-references with npm audit advisories and Snyk vulnerability database for real-time risk assessment.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-explorer-registry-api/)
