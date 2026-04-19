---
title: "npm Registry Explorer"
description: "The npm Registry Explorer skill provides deep Node.js package intelligence by combining data from the npm Registry API, npms.io analyzer API, and Bundlephobia API. It fetches package manifests from registry.npmjs.org, resolves semver version ranges using the node-semver algorithm, and presents comprehensive package profiles. Core capabilities include dependency tree visualization with depth-limited traversal, detection of deprecated packages in dependency chains, and duplicate dependency identification across the tree. The skill queries npms.io for quality, maintenance, and popularity scores, and fetches bundle size data from Bundlephobia API including minified and gzipped sizes with dependency contribution breakdowns. Advanced features include license audit across entire dependency trees using SPDX expression parsing, npm audit integration for security vulnerability detection with severity-based filtering, and package comparison mode that generates side-by-side feature matrices. The skill monitors npm registry changes via the /-/all/since endpoint for tracking new versions of watched packages, supports Verdaccio private registry endpoints, and can generate lockfile-compatible dependency snapshots. It also provides download trend analysis from the npm download counts API with weekly and monthly aggregation."
source: "https://agentskillexchange.com/skills/npm-registry-explorer/"
verification: "security_reviewed"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Agents"
---

# npm Registry Explorer

The npm Registry Explorer skill provides deep Node.js package intelligence by combining data from the npm Registry API, npms.io analyzer API, and Bundlephobia API. It fetches package manifests from registry.npmjs.org, resolves semver version ranges using the node-semver algorithm, and presents comprehensive package profiles. Core capabilities include dependency tree visualization with depth-limited traversal, detection of deprecated packages in dependency chains, and duplicate dependency identification across the tree. The skill queries npms.io for quality, maintenance, and popularity scores, and fetches bundle size data from Bundlephobia API including minified and gzipped sizes with dependency contribution breakdowns. Advanced features include license audit across entire dependency trees using SPDX expression parsing, npm audit integration for security vulnerability detection with severity-based filtering, and package comparison mode that generates side-by-side feature matrices. The skill monitors npm registry changes via the /-/all/since endpoint for tracking new versions of watched packages, supports Verdaccio private registry endpoints, and can generate lockfile-compatible dependency snapshots. It also provides download trend analysis from the npm download counts API with weekly and monthly aggregation.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-registry-explorer/)
