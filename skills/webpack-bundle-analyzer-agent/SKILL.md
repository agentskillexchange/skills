---
name: "Webpack Bundle Analyzer Agent"
description: "Analyzes webpack bundle composition using webpack-bundle-analyzer and source-map-explorer APIs. Identifies duplicate dependencies and suggests tree-shaking optimizations with specific import rewrites."
category: "Developer Tools"
framework: "Cursor"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/webpack-bundle-analyzer-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "webpack"  # from ase_tool_match
  github_stars: 66013  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 44849699  # from ase_npm_downloads
  github_repo: "webpack/webpack"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Webpack Bundle Analyzer Agent

Analyzes webpack bundle composition using webpack-bundle-analyzer and source-map-explorer APIs. Identifies duplicate dependencies and suggests tree-shaking optimizations with specific import rewrites.

## Overview

The Webpack Bundle Analyzer Agent provides deep insight into JavaScript bundle composition by integrating webpack-bundle-analyzer for visual treemap generation and source-map-explorer for precise byte-level attribution. It parses webpack stats JSON output to identify duplicate node_modules, oversized chunks, and inefficient code splitting boundaries. The agent suggests specific optimizations including dynamic import() boundaries for route-based splitting, sideEffects flags for tree-shaking, and externals configuration for CDN-loaded libraries. It monitors bundle sizes across builds using bundlesize thresholds and integrates with CI pipelines via GitHub Actions annotations. Supports webpack 4 and 5 configurations, handles multi-compiler setups, and generates actionable reports comparing bundle deltas between commits.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill webpack-bundle-analyzer-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill webpack-bundle-analyzer-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill webpack-bundle-analyzer-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill webpack-bundle-analyzer-agent -a codex
```

### OpenClaw

```bash
clawhub install webpack-bundle-analyzer-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/webpack-bundle-analyzer-agent/
