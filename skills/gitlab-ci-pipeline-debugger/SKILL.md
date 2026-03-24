---
name: "GitLab CI Pipeline Debugger"
description: "Debugs failed GitLab CI/CD pipelines by parsing .gitlab-ci.yml and fetching job logs via GitLab REST API v4. Identifies runner misconfigurations, artifact dependency issues, and suggests targeted fixes."
category: "CI/CD Integrations"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/gitlab-ci-pipeline-debugger/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "gitlab"  # from ase_tool_match
  github_stars: 24276  # from ase_github_stars (integer, not string)
  github_repo: "gitlabhq/gitlabhq"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# GitLab CI Pipeline Debugger

Debugs failed GitLab CI/CD pipelines by parsing .gitlab-ci.yml and fetching job logs via GitLab REST API v4. Identifies runner misconfigurations, artifact dependency issues, and suggests targeted fixes.

## Overview

The GitLab CI Pipeline Debugger agent provides intelligent troubleshooting for failed GitLab CI/CD pipelines. It connects to your GitLab instance via the REST API v4, fetching pipeline details, job logs, and runner configurations to diagnose build failures quickly and accurately.

When a pipeline fails, the agent parses your .gitlab-ci.yml file to understand the pipeline structure including stages, jobs, dependencies, and rules. It then fetches the specific job logs using the GitLab Jobs API, applying pattern matching to identify common failure modes such as missing dependencies, Docker image pull failures, artifact expiration issues, and runner tag mismatches.

The debugger understands GitLab-specific concepts like DAG dependencies with needs keyword, dynamic child pipelines, merge request pipelines vs branch pipelines, and protected variable scoping. It can trace failures across multi-project pipelines by following trigger relationships. Recommendations include specific .gitlab-ci.yml fixes with line references, runner configuration adjustments, and cache optimization strategies using the GitLab cache API.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-debugger
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-debugger -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-debugger -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-debugger -a codex
```

### OpenClaw

```bash
clawhub install gitlab-ci-pipeline-debugger
```

## Source

- Marketplace: https://agentskillexchange.com/skills/gitlab-ci-pipeline-debugger/
