---
title: "Semgrep Code Scanner"
description: "Semgrep Code Scanner is built around Semgrep static analysis engine. The underlying ecosystem is represented by semgrep/semgrep (14,543+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like YAML rules, semgrep –config, taint mode, SARIF, metavariables, autofix and preserving […]"
slug: "semgrep-code-scanner"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://github.com/semgrep/semgrep"
tool_ecosystem:
  github_repo: "semgrep/semgrep"
  github_stars: 14731
---

# Semgrep Code Scanner

Semgrep Code Scanner is built around Semgrep static analysis engine. The underlying ecosystem is represented by semgrep/semgrep (14,543+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like YAML rules, semgrep –config, taint mode, SARIF, metavariables, autofix and preserving […]

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
clawhub install semgrep-code-scanner
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Semgrep Code Scanner is built around Semgrep static analysis engine. The underlying ecosystem is represented by semgrep/semgrep (14,543+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like YAML rules, semgrep –config, taint mode, SARIF, metavariables, autofix and preserving the operational context that matters for real tasks.
In practice, the skill gives an agent a stable interface to semgrep so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on YAML rules, semgrep –config, taint mode, SARIF, metavariables, autofix, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.
- Accesses YAML rules, semgrep –config, taint mode, SARIF, metavariables, autofix instead of scraping a UI, which makes runs easier to audit and retry.
- Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
- Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
- Fits into broader integration points such as secure code scanning, policy enforcement, and custom code pattern checks.
In security-oriented usage, the skill emphasizes read-only discovery, evidence capture, and machine-readable output such as SARIF, JSON, or structured findings so results can flow into existing review pipelines. Key integration points include secure code scanning, policy enforcement, and custom code pattern checks. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-code-scanner/)
