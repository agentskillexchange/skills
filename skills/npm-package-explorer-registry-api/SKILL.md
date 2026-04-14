---
title: "NPM Package Explorer"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-explorer-registry-api/)
