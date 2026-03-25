---
name: "Semgrep Custom Rule Runner"
description: "Executes Semgrep OSS with custom YAML rule files for project-specific static analysis patterns. Supports semgrep –config and –pattern flags with metavariable constraints for detecting anti-patterns in Python, JavaScript, Go, and Java codebases."
category: "Templates & Workflows"
framework: "Cursor"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/semgrep-custom-rule-runner-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "semgrep"  # from ase_tool_match
  github_stars: 14543  # from ase_github_stars (integer, not string)
  github_repo: "semgrep/semgrep"  # from ase_github_repo
  license: "LGPL-2.1"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Semgrep Custom Rule Runner

Executes Semgrep OSS with custom YAML rule files for project-specific static analysis patterns. Supports semgrep –config and –pattern flags with metavariable constraints for detecting anti-patterns in Python, JavaScript, Go, and Java codebases.

## Overview

The Semgrep Custom Rule Runner skill provides advanced static analysis using Semgrep pattern-matching engine with custom rule definitions. It manages collections of project-specific YAML rules that encode team coding standards, security patterns, and architectural constraints beyond what standard linters catch. The skill supports full pattern syntax including metavariable comparisons, pattern-either/pattern-not compositions, and taint-mode rules for tracking data flow from sources to sinks. It can run targeted scans using semgrep –config path/to/rules/ with include and exclude filters, process results from semgrep –json output, and prioritize findings by severity and confidence. The skill maintains a local rule registry with versioning, supports rule testing via semgrep –test, and can generate baseline ignores for legacy code.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill semgrep-custom-rule-runner-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill semgrep-custom-rule-runner-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill semgrep-custom-rule-runner-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill semgrep-custom-rule-runner-2 -a codex
```

### OpenClaw

```bash
clawhub install semgrep-custom-rule-runner-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/semgrep-custom-rule-runner-2/
