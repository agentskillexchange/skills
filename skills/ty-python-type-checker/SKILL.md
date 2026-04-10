---
title: "ty Ultra-Fast Python Type Checker and Language Server"
description: "ty is an extremely fast Python type checker and language server written in Rust by Astral, the creators of Ruff and uv. It delivers 10-100x faster type checking than mypy or Pyright with comprehensive diagnostics, incremental analysis, and first-class editor integrations."
slug: "ty-python-type-checker"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://github.com/astral-sh/ty"
tool_ecosystem:
  github_repo: "astral-sh/ty"
  github_stars: 18132
listed: true
---

# ty Ultra-Fast Python Type Checker and Language Server

ty is an extremely fast Python type checker and language server written in Rust by Astral, the creators of Ruff and uv. It delivers 10-100x faster type checking than mypy or Pyright with comprehensive diagnostics, incremental analysis, and first-class editor integrations.

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
clawhub install ty-python-type-checker
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

ty is an extremely fast Python type checker and language server built by Astral (the team behind Ruff and uv), written entirely in Rust for maximum performance. It provides Python developers with type checking that runs 10 to 100 times faster than established tools like mypy and Pyright, making it practical to run type checks continuously during development without disrupting workflow.
The tool delivers comprehensive diagnostics with rich contextual information, helping developers understand not just what went wrong but why. ty supports configurable rule levels, per-file overrides, and suppression comments, giving teams fine-grained control over which type errors to enforce and where. Its gradual typing support means teams can adopt ty incrementally without needing to annotate their entire codebase at once.
As a language server, ty integrates directly into code editors including VS Code, PyCharm, and Neovim. It provides code navigation, intelligent completions, code actions, auto-import suggestions, inlay hints, and on-hover documentation. The language server uses fine-grained incremental analysis designed for near-instant updates as files are edited, keeping feedback loops tight during active development.
ty includes advanced type system features such as first-class intersection types, sophisticated type narrowing, and reachability analysis based on types. It can be run standalone via the CLI with uvx ty check or integrated into CI pipelines. The tool is installable from PyPI and supports pyproject.toml configuration, fitting naturally into existing Python project structures.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ty-python-type-checker/)
