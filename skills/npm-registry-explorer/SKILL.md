---
title: npm Registry Explorer
description: The npm Registry Explorer skill provides deep Node.js package intelligence
  by combining data from the npm Registry API, npms.io analyzer API, and Bundlephobia
  API. It fetches package manifests from registry.npmjs.org, resolves semver version
  ranges using the node-semver algorithm, and presents comprehensive package profiles.
  Core capabilities include dependency tree visualization with depth-limited traversal,
  detection of deprecated packages in dependency chains, and duplicate dependency
  identification across the tree. The skill queries npms.io for quality, maintenance,
  and popularity scores, and fetches bundle size data from Bundlephobia API including
  minified and gzipped sizes with dependency contribution breakdowns. Advanced features
  include license audit across entire dependency trees using SPDX expression parsing,
  npm audit integration for security vulnerability detection with severity-based filtering,
  and package comparison mode that generates side-by-side feature matrices. The skill
  monitors npm registry changes via the /-/all/since endpoint for tracking new versions
  of watched packages, supports Verdaccio private registry endpoints, and can generate
  lockfile-compatible dependency snapshots. It also provides download trend analysis
  from the npm download counts API with weekly and monthly aggregation.
verification: security_reviewed
source: https://agentskillexchange.com/skills/npm-registry-explorer/
category:
- Library &amp; API Reference
framework:
- Claude Agents
---

# npm Registry Explorer

The npm Registry Explorer skill provides deep Node.js package intelligence by combining data from the npm Registry API, npms.io analyzer API, and Bundlephobia API. It fetches package manifests from registry.npmjs.org, resolves semver version ranges using the node-semver algorithm, and presents comprehensive package profiles. Core capabilities include dependency tree visualization with depth-limited traversal, detection of deprecated packages in dependency chains, and duplicate dependency identification across the tree. The skill queries npms.io for quality, maintenance, and popularity scores, and fetches bundle size data from Bundlephobia API including minified and gzipped sizes with dependency contribution breakdowns. Advanced features include license audit across entire dependency trees using SPDX expression parsing, npm audit integration for security vulnerability detection with severity-based filtering, and package comparison mode that generates side-by-side feature matrices. The skill monitors npm registry changes via the /-/all/since endpoint for tracking new versions of watched packages, supports Verdaccio private registry endpoints, and can generate lockfile-compatible dependency snapshots. It also provides download trend analysis from the npm download counts API with weekly and monthly aggregation.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-registry-explorer/)
