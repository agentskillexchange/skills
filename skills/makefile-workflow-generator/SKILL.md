---
name: "Makefile Workflow Generator"
description: "Generates project Makefiles with standard targets using GNU Make syntax, autodeps pattern rules, and integration with package managers (npm scripts, Poetry tasks, Cargo commands). Produces .PHONY declarations and help targets."
category: "Templates & Workflows"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/makefile-workflow-generator/"
---
# Makefile Workflow Generator

Generates project Makefiles with standard targets using GNU Make syntax, autodeps pattern rules, and integration with package managers (npm scripts, Poetry tasks, Cargo commands). Produces .PHONY declarations and help targets.

## Overview

The Makefile Workflow Generator skill creates standardized Makefiles for software projects with consistent development workflow targets. It generates GNU Make compatible files with proper .PHONY declarations, automatic dependency tracking via pattern rules, and self-documenting help targets using grep-based comment extraction. The skill detects project type from configuration files (package.json, pyproject.toml, Cargo.toml, go.mod) and generates appropriate build, test, lint, and format targets wrapping native package manager commands. For Node.js projects, targets delegate to npm scripts with proper NODE_ENV handling. Python projects use Poetry or pip-tools with virtual environment management. Rust projects integrate Cargo commands with feature flag support. Go projects include go vet, go test with coverage, and golangci-lint integration. Common targets include: make build, make test, make lint, make fmt, make clean, make docker-build, make deploy, and make help. The generator handles multi-directory projects with recursive Make or directory-specific targets. Variable definitions support environment override via ?= assignments and .env file inclusion. Conditional logic handles OS-specific commands using uname detection. The skill also generates CI-optimized targets with verbose output, timing information, and non-interactive mode flags. Advanced features include Make function usage for file transformation, secondary expansion for dynamic prerequisites, and order-only prerequisites for directory creation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill makefile-workflow-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill makefile-workflow-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill makefile-workflow-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill makefile-workflow-generator -a codex
```

### OpenClaw

```bash
clawhub install makefile-workflow-generator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/makefile-workflow-generator/)
