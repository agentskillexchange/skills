---
name: "OWASP ZAP Scanner"
description: "OWASP ZAP Scanner is built around OWASP security tooling ecosystem. The underlying ecosystem is represented by zaproxy/zaproxy (14,896+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like ZAP scanning, passive/active checks, auth contexts, alerts, HTTP spidering and preserving […]"
category: "Security &amp; Verification"
framework: "Custom Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/owasp-zap-scanner/"
---
# OWASP ZAP Scanner

OWASP ZAP Scanner is built around OWASP security tooling ecosystem. The underlying ecosystem is represented by zaproxy/zaproxy (14,896+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like ZAP scanning, passive/active checks, auth contexts, alerts, HTTP spidering and preserving […]

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-scanner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-scanner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-scanner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-scanner -a codex
```

### OpenClaw

```bash
clawhub install owasp-zap-scanner
```

## Details

OWASP ZAP Scanner is built around OWASP security tooling ecosystem. The underlying ecosystem is represented by zaproxy/zaproxy (14,896+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like ZAP scanning, passive/active checks, auth contexts, alerts, HTTP spidering and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to owasp so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on ZAP scanning, passive/active checks, auth contexts, alerts, HTTP spidering, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses ZAP scanning, passive/active checks, auth contexts, alerts, HTTP spidering instead of scraping a UI, which makes runs easier to audit and retry.
Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
Fits into broader integration points such as web app security review, DAST, and verification workflows.

In security-oriented usage, the skill emphasizes read-only discovery, evidence capture, and machine-readable output such as SARIF, JSON, or structured findings so results can flow into existing review pipelines. Key integration points include web app security review, DAST, and verification workflows. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-scanner/)
