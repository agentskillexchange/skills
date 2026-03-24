---
name: "GitLab CI Pipeline Linter"
description: "Validates and optimizes .gitlab-ci.yml configurations using the GitLab CI Lint API (/api/v4/ci/lint). Checks for DAG dependency cycles, detects redundant job definitions, and suggests pipeline graph optimizations via the needs keyword."
category: "CI/CD Integrations"
framework: "Claude Agents"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/gitlab-ci-pipeline-linter/"
tool_ecosystem:
  tool: "gitlab"
  github_stars: 24276
  npm_weekly_downloads: 0
  github_repo: "gitlabhq/gitlabhq"
  license: "NOASSERTION"
  maintained: true
---

# GitLab CI Pipeline Linter

Validates and optimizes .gitlab-ci.yml configurations using the GitLab CI Lint API (/api/v4/ci/lint). Checks for DAG dependency cycles, detects redundant job definitions, and suggests pipeline graph optimizations via the needs keyword.

## Installation

### Any Agent (npx)
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

| | |
|---|---|
| **Category** | CI/CD Integrations |
| **Framework** | Claude Agents |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [gitlab](https://github.com/gitlabhq/gitlabhq) — ⭐ 24.3k · NOASSERTION |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/gitlab-ci-pipeline-linter/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
