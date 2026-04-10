---
title: "ShellCheck Shell Script Static Analyzer"
description: "Run static analysis on bash and shell scripts using ShellCheck to detect syntax errors, semantic pitfalls, and portability issues. Produces machine-readable diagnostics with fix suggestions."
slug: "shellcheck-shell-script-static-analyzer"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://github.com/koalaman/shellcheck"
tool_ecosystem:
  github_repo: "koalaman/shellcheck"
  github_stars: 39204
listed: true
---

# ShellCheck Shell Script Static Analyzer

Run static analysis on bash and shell scripts using ShellCheck to detect syntax errors, semantic pitfalls, and portability issues. Produces machine-readable diagnostics with fix suggestions.

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
clawhub install shellcheck-shell-script-static-analyzer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The ShellCheck Shell Script Static Analyzer skill integrates ShellCheck, a widely-adopted static analysis tool for sh, bash, dash, and ksh scripts. With over 37,000 GitHub stars and integration into dozens of CI platforms and editors, ShellCheck is the standard tool for catching bugs in shell code before they reach production.
ShellCheck operates at three levels of expertise. For beginners, it identifies syntax mistakes that produce cryptic error messages from the shell interpreter, explaining what went wrong and how to fix it. For intermediate users, it flags semantic problems where code is syntactically valid but behaves in surprising ways—like unquoted variable expansions that break on filenames with spaces, or test commands that silently do the wrong thing. For advanced users, it detects subtle corner cases and portability issues that would cause a working script to fail under different shells or edge conditions.
The skill runs ShellCheck against target scripts and interprets the output, which includes error codes (SC-prefixed), severity levels (error, warning, info, style), line numbers, and suggested fixes. Output formats include TTY-colored terminal output, GCC-compatible format for editor integration, JSON, and SARIF for security tool chains. Each diagnostic links to a wiki page with a detailed explanation and examples.
In CI/CD environments, ShellCheck uses standard exit codes: zero means no issues found, non-zero means problems were detected. This makes it drop-in compatible with Makefiles, GitHub Actions, CircleCI (via the ShellCheck Orb), Travis CI, and other build systems. The agent can configure severity thresholds, exclude specific rules via inline directives or command-line flags, and scope scans to specific directories.
ShellCheck is written in Haskell, distributed as a static binary with zero runtime dependencies, and licensed under GPLv3. It is pre-installed on GitHub Actions Linux runners and available via apt, brew, cabal, snap, and Docker. This skill is essential for any repository that includes deployment scripts, CI configuration, or developer tooling written in shell.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/shellcheck-shell-script-static-analyzer/)
