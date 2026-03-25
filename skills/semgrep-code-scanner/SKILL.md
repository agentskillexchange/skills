---
name: "Semgrep Code Scanner"
description: "Runs Semgrep static analysis for security vulnerabilities, bug patterns, and custom code rules. Supports 30+ languages and custom rule creation. Integrates with CI for automated scanning on every commit."
category: "Code Quality & Review"
framework: "Claude Code"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/semgrep-code-scanner/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "semgrep"  # from ase_tool_match
  github_stars: 14543  # from ase_github_stars (integer, not string)
  github_repo: "semgrep/semgrep"  # from ase_github_repo
  license: "LGPL-2.1"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Semgrep Code Scanner

Runs Semgrep static analysis for security vulnerabilities, bug patterns, and custom code rules. Supports 30+ languages and custom rule creation. Integrates with CI for automated scanning on every commit.

## Overview

Runs Semgrep static analysis for security vulnerabilities, bug patterns, and custom code rules. Supports 30+ languages and custom rule creation. Integrates with CI for automated scanning on every commit.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill semgrep-code-scanner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill semgrep-code-scanner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill semgrep-code-scanner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill semgrep-code-scanner -a codex
```

### OpenClaw

```bash
clawhub install semgrep-code-scanner
```

## Source

- Marketplace: https://agentskillexchange.com/skills/semgrep-code-scanner/
