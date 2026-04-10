---
title: "Semgrep Code Pattern Scanner"
description: "Runs Semgrep against a codebase using official or custom rule registries and outputs a grouped report of security anti-patterns, deprecated API usage, and policy violations. Supports 30+ languages and produces SARIF output."
slug: "semgrep-code-pattern-scanner-2"
category:
  - "Code Quality &amp; Review"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/semgrep-code-pattern-scanner-2/"
listed: true
---

# Semgrep Code Pattern Scanner

Runs Semgrep against a codebase using official or custom rule registries and outputs a grouped report of security anti-patterns, deprecated API usage, and policy violations. Supports 30+ languages and produces SARIF output.

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
clawhub install semgrep-code-pattern-scanner-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Semgrep Code Pattern Scanner is built around Semgrep static analysis engine. The underlying ecosystem is represented by semgrep/semgrep (14,543+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like YAML rules, semgrep –config, taint mode, SARIF, metavariables, autofix and preserving the operational context that matters for real tasks.
In practice, the skill gives an agent a stable interface to semgrep so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Runs Semgrep against a codebase using official or custom rule registries and outputs a grouped report of security anti-patterns, deprecated API usage, and policy violations. Supports 30+ languages and produces SARIF output. The implementation typically relies on YAML rules, semgrep –config, taint mode, SARIF, metavariables, autofix, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.
- Accesses YAML rules, semgrep –config, taint mode, SARIF, metavariables, autofix instead of scraping a UI, which makes runs easier to audit and retry.
- Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
- Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
- Fits into broader integration points such as secure code scanning, policy enforcement, and custom code pattern checks.
In security-oriented usage, the skill emphasizes read-only discovery, evidence capture, and machine-readable output such as SARIF, JSON, or structured findings so results can flow into existing review pipelines. Key integration points include secure code scanning, policy enforcement, and custom code pattern checks. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-code-pattern-scanner-2/)
