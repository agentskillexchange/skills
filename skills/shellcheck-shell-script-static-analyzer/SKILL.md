---
name: "ShellCheck Shell Script Static Analyzer"
description: "Run static analysis on bash and shell scripts using ShellCheck to detect syntax errors, semantic pitfalls, and portability issues. Produces machine-readable diagnostics with fix suggestions."
category: "Code Quality & Review"
framework: "Claude Code"
verification: security_reviewed
source: "https://github.com/koalaman/shellcheck"
tool_ecosystem:
  tool: docker
  github_stars: 71560
  github_repo: moby/moby
  license: Apache-2.0
  maintained: true
---
# ShellCheck Shell Script Static Analyzer

Run static analysis on bash and shell scripts using ShellCheck to detect syntax errors, semantic pitfalls, and portability issues. Produces machine-readable diagnostics with fix suggestions.

## Overview

The ShellCheck Shell Script Static Analyzer skill integrates [ShellCheck](https://github.com/koalaman/shellcheck), a widely-adopted static analysis tool for sh, bash, dash, and ksh scripts. With over 37,000 GitHub stars and integration into dozens of CI platforms and editors, ShellCheck is the standard tool for catching bugs in shell code before they reach production.

ShellCheck operates at three levels of expertise. For beginners, it identifies syntax mistakes that produce cryptic error messages from the shell interpreter, explaining what went wrong and how to fix it. For intermediate users, it flags semantic problems where code is syntactically valid but behaves in surprising ways—like unquoted variable expansions that break on filenames with spaces, or test commands that silently do the wrong thing. For advanced users, it detects subtle corner cases and portability issues that would cause a working script to fail under different shells or edge conditions.

The skill runs ShellCheck against target scripts and interprets the output, which includes error codes (SC-prefixed), severity levels (error, warning, info, style), line numbers, and suggested fixes. Output formats include TTY-colored terminal output, GCC-compatible format for editor integration, JSON, and SARIF for security tool chains. Each diagnostic links to a wiki page with a detailed explanation and examples.

In CI/CD environments, ShellCheck uses standard exit codes: zero means no issues found, non-zero means problems were detected. This makes it drop-in compatible with Makefiles, GitHub Actions, CircleCI (via the ShellCheck Orb), Travis CI, and other build systems. The agent can configure severity thresholds, exclude specific rules via inline directives or command-line flags, and scope scans to specific directories.

ShellCheck is written in Haskell, distributed as a static binary with zero runtime dependencies, and licensed under GPLv3. It is pre-installed on GitHub Actions Linux runners and available via apt, brew, cabal, snap, and Docker. This skill is essential for any repository that includes deployment scripts, CI configuration, or developer tooling written in shell.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill shellcheck-shell-script-static-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill shellcheck-shell-script-static-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill shellcheck-shell-script-static-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill shellcheck-shell-script-static-analyzer -a codex
```

### OpenClaw

```bash
clawhub install shellcheck-shell-script-static-analyzer
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/shellcheck-shell-script-static-analyzer/)
