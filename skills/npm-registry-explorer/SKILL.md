---
name: "npm Registry Explorer"
description: "Queries the npm registry API and npms.io search API for package discovery, dependency analysis, and quality scoring. Resolves semver ranges, detects deprecated packages, and checks bundle sizes via Bundlephobia API."
category: "Library & API Reference"
framework: "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/npm-registry-explorer/"
---

# npm Registry Explorer

Queries the npm registry API and npms.io search API for package discovery, dependency analysis, and quality scoring. Resolves semver ranges, detects deprecated packages, and checks bundle sizes via Bundlephobia API.

## Overview

The npm Registry Explorer skill provides deep Node.js package intelligence by combining data from the npm Registry API, npms.io analyzer API, and Bundlephobia API. It fetches package manifests from registry.npmjs.org, resolves semver version ranges using the node-semver algorithm, and presents comprehensive package profiles.

Core capabilities include dependency tree visualization with depth-limited traversal, detection of deprecated packages in dependency chains, and duplicate dependency identification across the tree. The skill queries npms.io for quality, maintenance, and popularity scores, and fetches bundle size data from Bundlephobia API including minified and gzipped sizes with dependency contribution breakdowns.

Advanced features include license audit across entire dependency trees using SPDX expression parsing, npm audit integration for security vulnerability detection with severity-based filtering, and package comparison mode that generates side-by-side feature matrices. The skill monitors npm registry changes via the /-/all/since endpoint for tracking new versions of watched packages, supports Verdaccio private registry endpoints, and can generate lockfile-compatible dependency snapshots. It also provides download trend analysis from the npm download counts API with weekly and monthly aggregation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill npm-registry-explorer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill npm-registry-explorer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill npm-registry-explorer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill npm-registry-explorer -a codex
```

### OpenClaw

```bash
clawhub install npm-registry-explorer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/npm-registry-explorer/
