---
title: ty Ultra-Fast Python Type Checker and Language Server
description: ty is an extremely fast Python type checker and language server built
  by Astral (the team behind Ruff and uv), written entirely in Rust for maximum performance.
  It provides Python developers with type checking that runs 10 to 100 times faster
  than established tools like mypy and Pyright, making it practical to run type checks
  continuously during development without disrupting workflow. The tool delivers comprehensive
  diagnostics with rich contextual information, helping developers understand not
  just what went wrong but why. ty supports configurable rule levels, per-file overrides,
  and suppression comments, giving teams fine-grained control over which type errors
  to enforce and where. Its gradual typing support means teams can adopt ty incrementally
  without needing to annotate their entire codebase at once. As a language server,
  ty integrates directly into code editors including VS Code, PyCharm, and Neovim.
  It provides code navigation, intelligent completions, code actions, auto-import
  suggestions, inlay hints, and on-hover documentation. The language server uses fine-grained
  incremental analysis designed for near-instant updates as files are edited, keeping
  feedback loops tight during active development. ty includes advanced type system
  features such as first-class intersection types, sophisticated type narrowing, and
  reachability analysis based on types. It can be run standalone via the CLI with
  uvx ty check or integrated into CI pipelines. The tool is installable from PyPI
  and supports pyproject.toml configuration, fitting naturally into existing Python
  project structures.
verification: security_reviewed
source: https://github.com/astral-sh/ty
category:
- Code Quality &amp; Review
framework:
- Claude Code
tool_ecosystem:
  github_repo: astral-sh/ty
  github_stars: 18132
---

# ty Ultra-Fast Python Type Checker and Language Server

ty is an extremely fast Python type checker and language server built by Astral (the team behind Ruff and uv), written entirely in Rust for maximum performance. It provides Python developers with type checking that runs 10 to 100 times faster than established tools like mypy and Pyright, making it practical to run type checks continuously during development without disrupting workflow. The tool delivers comprehensive diagnostics with rich contextual information, helping developers understand not just what went wrong but why. ty supports configurable rule levels, per-file overrides, and suppression comments, giving teams fine-grained control over which type errors to enforce and where. Its gradual typing support means teams can adopt ty incrementally without needing to annotate their entire codebase at once. As a language server, ty integrates directly into code editors including VS Code, PyCharm, and Neovim. It provides code navigation, intelligent completions, code actions, auto-import suggestions, inlay hints, and on-hover documentation. The language server uses fine-grained incremental analysis designed for near-instant updates as files are edited, keeping feedback loops tight during active development. ty includes advanced type system features such as first-class intersection types, sophisticated type narrowing, and reachability analysis based on types. It can be run standalone via the CLI with uvx ty check or integrated into CI pipelines. The tool is installable from PyPI and supports pyproject.toml configuration, fitting naturally into existing Python project structures.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ty-python-type-checker/)
