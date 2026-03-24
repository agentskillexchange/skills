---
name: "GitHub Actions Workflow Linter"
description: "Validates GitHub Actions workflow YAML files using actionlint and checks for security anti-patterns like script injection via ${{ github.event }}. Suggests pinned action versions using SHA hashes from the GitHub API."
category: "CI/CD Integrations"
framework: "Cursor"
verification: security_reviewed
rating: 4.3
reviews: 25
creator: "Tom Anderson"
creator_handle: "@tanderson"
creator_verified: false
source: "https://agentskillexchange.com/skills/github-actions-workflow-linter/"
---
# GitHub Actions Workflow Linter

Validates GitHub Actions workflow YAML files using actionlint and checks for security anti-patterns like script injection via ${{ github.event }}. Suggests pinned action versions using SHA hashes from the GitHub API.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill github-actions-workflow-linter
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill github-actions-workflow-linter -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill github-actions-workflow-linter -a cursor
```

### OpenClaw

```bash
clawhub install github-actions-workflow-linter
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill github-actions-workflow-linter -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | CI/CD Integrations |
| Framework | Cursor |
| Verification | Security Reviewed |
| Rating | 4.3/5 (25 reviews) |

## Creator

**Tom Anderson**
- Profile: [@tanderson](https://agentskillexchange.com/browse-skills/?creator=tanderson)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/github-actions-workflow-linter/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
