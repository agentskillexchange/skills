---
title: "npm Registry Explorer"
description: "Queries the npm registry API and npms.io search API for package discovery, dependency analysis, and quality scoring. Resolves semver ranges, detects deprecated packages, and checks bundle sizes via Bundlephobia API."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/npm-registry-explorer/"
category:
  - "Library & API Reference"
framework:
  - "Claude Agents"
---

# npm Registry Explorer

The npm Registry Explorer skill provides deep Node.js package intelligence by combining data from the npm Registry API, npms.io analyzer API, and Bundlephobia API. It fetches package manifests from registry.npmjs.org, resolves semver version ranges using the node-semver algorithm, and presents comprehensive package profiles.


Core capabilities include dependency tree visualization with depth-limited traversal, detection of deprecated packages in dependency chains, and duplicate dependency identification across the tree. The skill queries npms.io for quality, maintenance, and popularity scores, and fetches bundle size data from Bundlephobia API including minified and gzipped sizes with dependency contribution breakdowns.


Advanced features include license audit across entire dependency trees using SPDX expression parsing, npm audit integration for security vulnerability detection with severity-based filtering, and package comparison mode that generates side-by-side feature matrices. The skill monitors npm registry changes via the /-/all/since endpoint for tracking new versions of watched packages, supports Verdaccio private registry endpoints, and can generate lockfile-compatible dependency snapshots. It also provides download trend analysis from the npm download counts API with weekly and monthly aggregation.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-registry-explorer/)
