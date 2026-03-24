---
name: "GitLab CI Pipeline Linter"
description: "Validates and optimizes .gitlab-ci.yml configurations using the GitLab CI Lint API (/api/v4/ci/lint). Checks for DAG dependency cycles, detects redundant job definitions, and suggests pipeline graph optimizations via the needs keyword."
category: "CI/CD Integrations"
framework: "Claude Agents"
verification: security_reviewed
rating: 4.9
reviews: 15
creator: "Chris Lee"
creator_handle: "@chrislee"
creator_verified: false
source: "https://agentskillexchange.com/skills/gitlab-ci-pipeline-linter/"
---
# GitLab CI Pipeline Linter

Validates and optimizes .gitlab-ci.yml configurations using the GitLab CI Lint API (/api/v4/ci/lint). Checks for DAG dependency cycles, detects redundant job definitions, and suggests pipeline graph optimizations via the needs keyword.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-linter
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-linter -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-linter -a cursor
```

### OpenClaw

```bash
clawhub install gitlab-ci-pipeline-linter
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gitlab-ci-pipeline-linter -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | CI/CD Integrations |
| Framework | Claude Agents |
| Verification | Security Reviewed |
| Rating | 4.9/5 (15 reviews) |

## Creator

**Chris Lee**
- Profile: [@chrislee](https://agentskillexchange.com/browse-skills/?creator=chrislee)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-pipeline-linter/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
