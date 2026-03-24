---
name: "Semgrep Code Pattern Scanner"
description: "Runs Semgrep against a codebase using official or custom rule registries and outputs a grouped report of security anti-patterns, deprecated API usage, and policy violations. Supports 30+ languages and produces SARIF output."
category: "Code Quality & Review"
framework: "Codex"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/semgrep-code-pattern-scanner-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "semgrep"  # from ase_tool_match
  github_stars: 14543  # from ase_github_stars (integer, not string)
  github_repo: "semgrep/semgrep"  # from ase_github_repo
  license: "LGPL-2.1"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Semgrep Code Pattern Scanner

Runs Semgrep against a codebase using official or custom rule registries and outputs a grouped report of security anti-patterns, deprecated API usage, and policy violations. Supports 30+ languages and produces SARIF output.

## Overview

Runs Semgrep against a codebase using official or custom rule registries and outputs a grouped report of security anti-patterns, deprecated API usage, and policy violations. Supports 30+ languages and produces SARIF output.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill semgrep-code-pattern-scanner-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill semgrep-code-pattern-scanner-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill semgrep-code-pattern-scanner-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill semgrep-code-pattern-scanner-2 -a codex
```

### OpenClaw

```bash
clawhub install semgrep-code-pattern-scanner-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/semgrep-code-pattern-scanner-2/
