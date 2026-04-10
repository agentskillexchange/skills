---
title: "Makefile Workflow Generator"
description: "Generates project Makefiles with standard targets using GNU Make syntax, autodeps pattern rules, and integration with package managers (npm scripts, Poetry tasks, Cargo commands). Produces .PHONY declarations and help targets."
slug: "makefile-workflow-generator"
category:
  - "Templates &amp; Workflows"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/makefile-workflow-generator/"
listed: true
---

# Makefile Workflow Generator

Generates project Makefiles with standard targets using GNU Make syntax, autodeps pattern rules, and integration with package managers (npm scripts, Poetry tasks, Cargo commands). Produces .PHONY declarations and help targets.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install makefile-workflow-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Makefile Workflow Generator skill creates standardized Makefiles for software projects with consistent development workflow targets. It generates GNU Make compatible files with proper .PHONY declarations, automatic dependency tracking via pattern rules, and self-documenting help targets using grep-based comment extraction. The skill detects project type from configuration files (package.json, pyproject.toml, Cargo.toml, go.mod) and generates appropriate build, test, lint, and format targets wrapping native package manager commands. For Node.js projects, targets delegate to npm scripts with proper NODE_ENV handling. Python projects use Poetry or pip-tools with virtual environment management. Rust projects integrate Cargo commands with feature flag support. Go projects include go vet, go test with coverage, and golangci-lint integration. Common targets include: make build, make test, make lint, make fmt, make clean, make docker-build, make deploy, and make help. The generator handles multi-directory projects with recursive Make or directory-specific targets. Variable definitions support environment override via ?= assignments and .env file inclusion. Conditional logic handles OS-specific commands using uname detection. The skill also generates CI-optimized targets with verbose output, timing information, and non-interactive mode flags. Advanced features include Make function usage for file transformation, secondary expansion for dynamic prerequisites, and order-only prerequisites for directory creation.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/makefile-workflow-generator/)
