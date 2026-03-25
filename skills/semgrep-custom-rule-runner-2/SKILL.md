---
name: "Semgrep Custom Rule Runner"
description: "Executes Semgrep OSS with custom YAML rule files for project-specific static analysis patterns. Supports semgrep –config and –pattern flags with metavariable constraints for detecting anti-patterns in Python, JavaScript, Go, and Java codebases."
category: "Templates & Workflows"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/semgrep-custom-rule-runner-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "semgrep"  # from ase_tool_match
  github_stars: 14551  # from ase_github_stars (integer, not string)
  github_repo: "semgrep/semgrep"  # from ase_github_repo
  license: "LGPL-2.1"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Semgrep Custom Rule Runner

Executes Semgrep OSS with custom YAML rule files for project-specific static analysis patterns. Supports semgrep –config and –pattern flags with metavariable constraints for detecting anti-patterns in Python, JavaScript, Go, and Java codebases.

## Overview

**Semgrep Custom Rule Runner** is built around Semgrep static analysis engine. The underlying ecosystem is represented by `semgrep/semgrep` (14,543+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like YAML rules, semgrep –config, taint mode, SARIF, metavariables, autofix and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to semgrep so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Executes Semgrep OSS with custom YAML rule files for project-specific static analysis patterns. Supports semgrep –config and –pattern flags with metavariable constraints for detecting anti-patterns in Python, JavaScript, Go, and Java codebases. The implementation typically relies on YAML rules, semgrep –config, taint mode, SARIF, metavariables, autofix, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses YAML rules, semgrep –config, taint mode, SARIF, metavariables, autofix instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as secure code scanning, policy enforcement, and custom code pattern checks.

Key integration points include secure code scanning, policy enforcement, and custom code pattern checks. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

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
