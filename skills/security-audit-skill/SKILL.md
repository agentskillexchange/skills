---
title: "Security Audit Skill"
description: "Security Audit Skill is built around OWASP security tooling ecosystem. The underlying ecosystem is represented by zaproxy/zaproxy (14,896+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like ZAP scanning, passive/active checks, auth contexts, alerts, HTTP spidering and preserving […]"
slug: "security-audit-skill"
category:
  - "Security &amp; Verification"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/security-audit-skill/"
listed: true
---

# Security Audit Skill

Security Audit Skill is built around OWASP security tooling ecosystem. The underlying ecosystem is represented by zaproxy/zaproxy (14,896+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like ZAP scanning, passive/active checks, auth contexts, alerts, HTTP spidering and preserving […]

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
clawhub install security-audit-skill
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Security Audit Skill is built around OWASP security tooling ecosystem. The underlying ecosystem is represented by zaproxy/zaproxy (14,896+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like ZAP scanning, passive/active checks, auth contexts, alerts, HTTP spidering and preserving the operational context that matters for real tasks.
In practice, the skill gives an agent a stable interface to owasp so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on ZAP scanning, passive/active checks, auth contexts, alerts, HTTP spidering, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.
- Accesses ZAP scanning, passive/active checks, auth contexts, alerts, HTTP spidering instead of scraping a UI, which makes runs easier to audit and retry.
- Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
- Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
- Fits into broader integration points such as web app security review, DAST, and verification workflows.
In security-oriented usage, the skill emphasizes read-only discovery, evidence capture, and machine-readable output such as SARIF, JSON, or structured findings so results can flow into existing review pipelines. Key integration points include web app security review, DAST, and verification workflows. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/security-audit-skill/)
