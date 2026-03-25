---
name: "Cloud Cost Analysis"
description: "Use this skill when you need to analyze cloud spending across AWS, GCP, or Azure accounts and identify optimization opportunities. It queries cost and usage data, surfaces top spending services, highlights anomalies, and recommends rightsizing or reserved instance strategies."
category: "Developer Tools"
framework: "Claude Agents"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/cloud-cost-analysis/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "aws"  # from ase_tool_match
  github_stars: 3594  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 9204385  # from ase_npm_downloads
  github_repo: "aws/aws-sdk-js-v3"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Cloud Cost Analysis

Use this skill when you need to analyze cloud spending across AWS, GCP, or Azure accounts and identify optimization opportunities. It queries cost and usage data, surfaces top spending services, highlights anomalies, and recommends rightsizing or reserved instance strategies.

## Overview

Use this skill when you need to analyze cloud spending across AWS, GCP, or Azure accounts and identify optimization opportunities. It queries cost and usage data, surfaces top spending services, highlights anomalies, and recommends rightsizing or reserved instance strategies.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cloud-cost-analysis
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cloud-cost-analysis -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cloud-cost-analysis -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cloud-cost-analysis -a codex
```

### OpenClaw

```bash
clawhub install cloud-cost-analysis
```

## Source

- Marketplace: https://agentskillexchange.com/skills/cloud-cost-analysis/
