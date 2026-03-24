---
name: "Linear Issue Triage & Sprint Planner"
description: "Queries the Linear GraphQL API to list open issues by team, priority, and cycle, then applies configurable triage rules to auto-assign or escalate. Generates sprint plan drafts scored against velocity and team capacity from Linear projectMilestone and workflowState data."
category: "Integrations & Connectors"
framework: "Claude Code"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/linear-issue-triage-sprint-planner-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "graphql"  # from ase_tool_match
  github_stars: 20335  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 32010306  # from ase_npm_downloads
  github_repo: "graphql/graphql-js"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Linear Issue Triage & Sprint Planner

Queries the Linear GraphQL API to list open issues by team, priority, and cycle, then applies configurable triage rules to auto-assign or escalate. Generates sprint plan drafts scored against velocity and team capacity from Linear projectMilestone and workflowState data.

## Overview

Queries the Linear GraphQL API to list open issues by team, priority, and cycle, then applies configurable triage rules to auto-assign or escalate. Generates sprint plan drafts scored against velocity and team capacity from Linear projectMilestone and workflowState data.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill linear-issue-triage-sprint-planner-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill linear-issue-triage-sprint-planner-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill linear-issue-triage-sprint-planner-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill linear-issue-triage-sprint-planner-2 -a codex
```

### OpenClaw

```bash
clawhub install linear-issue-triage-sprint-planner-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/linear-issue-triage-sprint-planner-2/
