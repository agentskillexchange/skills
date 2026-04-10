---
name: uv Ultra-Fast Python Package and Project Manager
description: uv is an extremely fast Python package and project manager written in
  Rust by Astral (creators of Ruff). It replaces pip, pip-tools, pipx, poetry, pyenv,
  virtualenv, and twine with a single tool that resolves and installs packages 10-100x
  faster.
verification: security_reviewed
source: https://github.com/astral-sh/uv
category:
- Developer Tools
framework:
- Claude Code
tool_ecosystem:
  github_repo: astral-sh/uv
  github_stars: 82442
---
# uv Ultra-Fast Python Package and Project Manager

uv is an open-source Python package and project manager written in Rust, developed by Astral — the same team behind the Ruff linter and the ty type checker. It is designed as a drop-in replacement for the entire Python packaging toolchain: pip, pip-tools, pipx, poetry, pyenv, virtualenv, and twine, unified into a single binary that runs 10 to 100 times faster than traditional Python package managers.
The speed advantage comes from Rust-native dependency resolution and parallel download/install operations. Installing a project's dependencies with a warm cache completes in milliseconds rather than seconds. uv supports the full pip interface (uv pip install, uv pip compile, uv pip sync) so migration from existing pip-based workflows requires minimal changes — just prefix commands with uv.
Beyond package installation, uv provides comprehensive Python project management. It handles Python version management (install and switch between Python versions without pyenv), virtual environment creation and management, dependency locking with cross-platform lockfiles, project scaffolding with uv init, script execution with inline dependency metadata via uv run, and tool installation via uv tool install (replacing pipx). The uv.lock format produces deterministic, cross-platform lockfiles.
uv integrates well into CI/CD pipelines where install speed directly impacts build times. In GitHub Actions, replacing pip with uv can cut dependency installation from minutes to seconds. The tool also supports workspaces for monorepo setups, build backend integration for publishing packages, and pip-compatible requirements.txt file handling.
Installation is available via curl, pip, Homebrew, conda, Docker, and direct binary download — it does not require Rust or Python to be pre-installed. uv runs on macOS, Linux, and Windows, supports both x86_64 and ARM architectures, and is licensed under Apache 2.0 / MIT dual license. The project is one of the fastest-growing developer tools on GitHub with tens of thousands of stars.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/uv-ultra-fast-python-package-project-manager/)
