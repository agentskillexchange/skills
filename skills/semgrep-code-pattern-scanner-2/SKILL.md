---
title: "Semgrep Code Pattern Scanner"
description: "Runs Semgrep against a codebase using official or custom rule registries and outputs a grouped report of security anti-patterns, deprecated API usage, and policy violations. Supports 30+ languages and produces SARIF output."
verification: "security_reviewed"
source: "https://github.com/semgrep/semgrep"
category:
  - "Code Quality & Review"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "semgrep/semgrep"
  github_stars: 14762
---

# Semgrep Code Pattern Scanner

Semgrep Code Pattern Scanner is built around Semgrep static analysis engine. The underlying ecosystem is represented by semgrep/semgrep (14,543+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like YAML rules, semgrep –config, taint mode, SARIF, metavariables, autofix and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to semgrep so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Runs Semgrep against a codebase using official or custom rule registries and outputs a grouped report of security anti-patterns, deprecated API usage, and policy violations. Supports 30+ languages and produces SARIF output. The implementation typically relies on YAML rules, semgrep –config, taint mode, SARIF, metavariables, autofix, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

- Accesses YAML rules, semgrep –config, taint mode, SARIF, metavariables, autofix instead of scraping a UI, which makes runs easier to audit and retry.

- Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

- Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

- Fits into broader integration points such as secure code scanning, policy enforcement, and custom code pattern checks.

In security-oriented usage, the skill emphasizes read-only discovery, evidence capture, and machine-readable output such as SARIF, JSON, or structured findings so results can flow into existing review pipelines. Key integration points include secure code scanning, policy enforcement, and custom code pattern checks. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/semgrep-code-pattern-scanner-2/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/semgrep-code-pattern-scanner-2
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/semgrep-code-pattern-scanner-2`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-code-pattern-scanner-2/)
