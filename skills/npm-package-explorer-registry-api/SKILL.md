---
name: "NPM Package Explorer"
description: "Explores the npm registry using the Registry API and npms.io scoring API. Analyzes package quality, dependency trees, and bundle sizes via bundlephobia API."
category: "Library & API Reference"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/npm-package-explorer-registry-api/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "snyk"  # from ase_tool_match
  github_stars: 5458  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 601684  # from ase_npm_downloads
  github_repo: "snyk/cli"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# NPM Package Explorer

Explores the npm registry using the Registry API and npms.io scoring API. Analyzes package quality, dependency trees, and bundle sizes via bundlephobia API.

## Overview

NPM Package Explorer queries the npm Registry API to provide deep analysis of npm packages and their ecosystems. It retrieves package metadata, version histories, and maintainer information directly from the registry. Integration with the npms.io API provides quality, popularity, and maintenance scores for informed package selection. Bundle size analysis uses the bundlephobia API to estimate the impact of adding packages to frontend projects, including tree-shaking support detection. The tool builds comprehensive dependency trees using the npm resolve algorithm, identifying duplicate packages and version conflicts. License compliance scanning detects incompatible license combinations across dependency chains. It tracks download statistics via the npm downloads API with trend analysis and comparison charts. Security audit integration cross-references with npm audit advisories and Snyk vulnerability database for real-time risk assessment.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill npm-package-explorer-registry-api
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill npm-package-explorer-registry-api -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill npm-package-explorer-registry-api -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill npm-package-explorer-registry-api -a codex
```

### OpenClaw

```bash
clawhub install npm-package-explorer-registry-api
```

## Source

- Marketplace: https://agentskillexchange.com/skills/npm-package-explorer-registry-api/
