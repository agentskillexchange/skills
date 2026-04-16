---
title: "Makefile Workflow Generator"
description: "Generates project Makefiles with standard targets using GNU Make syntax, autodeps pattern rules, and integration with package managers (npm scripts, Poetry tasks, Cargo commands). Produces .PHONY declarations and help targets."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/makefile-workflow-generator/"
category:
  - "Templates &amp; Workflows"
framework:
  - "Gemini"
---

# Makefile Workflow Generator

The Makefile Workflow Generator skill creates standardized Makefiles for software projects with consistent development workflow targets. It generates GNU Make compatible files with proper .PHONY declarations, automatic dependency tracking via pattern rules, and self-documenting help targets using grep-based comment extraction. The skill detects project type from configuration files (package.json, pyproject.toml, Cargo.toml, go.mod) and generates appropriate build, test, lint, and format targets wrapping native package manager commands. For Node.js projects, targets delegate to npm scripts with proper NODE_ENV handling. Python projects use Poetry or pip-tools with virtual environment management. Rust projects integrate Cargo commands with feature flag support. Go projects include go vet, go test with coverage, and golangci-lint integration. Common targets include: make build, make test, make lint, make fmt, make clean, make docker-build, make deploy, and make help. The generator handles multi-directory projects with recursive Make or directory-specific targets. Variable definitions support environment override via ?= assignments and .env file inclusion. Conditional logic handles OS-specific commands using uname detection. The skill also generates CI-optimized targets with verbose output, timing information, and non-interactive mode flags. Advanced features include Make function usage for file transformation, secondary expansion for dynamic prerequisites, and order-only prerequisites for directory creation.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/makefile-workflow-generator/)
