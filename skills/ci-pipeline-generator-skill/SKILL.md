---
name: "CI Pipeline Generator Skill"
description: "Use this skill to automatically generate CI/CD pipeline configurations for GitHub Actions, CircleCI, or GitLab CI based on project type, testing requirements, and deployment targets. It creates pipelines with build, test, lint, and deploy stages. Trigger when setting up CI for a new project or migrating between CI platforms."
category: "Developer Tools"
framework: "Custom Agents"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/ci-pipeline-generator-skill/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "gitlab"  # from ase_tool_match
  github_stars: 24276  # from ase_github_stars (integer, not string)
  github_repo: "gitlabhq/gitlabhq"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# CI Pipeline Generator Skill

Use this skill to automatically generate CI/CD pipeline configurations for GitHub Actions, CircleCI, or GitLab CI based on project type, testing requirements, and deployment targets. It creates pipelines with build, test, lint, and deploy stages. Trigger when setting up CI for a new project or migrating between CI platforms.

## Overview

Use this skill to automatically generate CI/CD pipeline configurations for GitHub Actions, CircleCI, or GitLab CI based on project type, testing requirements, and deployment targets. It creates pipelines with build, test, lint, and deploy stages. Trigger when setting up CI for a new project or migrating between CI platforms.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ci-pipeline-generator-skill
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ci-pipeline-generator-skill -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ci-pipeline-generator-skill -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ci-pipeline-generator-skill -a codex
```

### OpenClaw

```bash
clawhub install ci-pipeline-generator-skill
```

## Source

- Marketplace: https://agentskillexchange.com/skills/ci-pipeline-generator-skill/
