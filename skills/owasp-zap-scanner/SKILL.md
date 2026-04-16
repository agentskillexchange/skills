---
title: "OWASP ZAP Scanner"
description: "OWASP ZAP Scanner is built around OWASP security tooling ecosystem. The underlying ecosystem is represented by zaproxy/zaproxy (14,896+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like ZAP scanning, passive/active checks, auth contexts, alerts, HTTP spidering and preserving […]"
verification: "security_reviewed"
source: "https://github.com/zaproxy/zaproxy"
category:
  - "Security & Verification"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "zaproxy/zaproxy"
  github_stars: 14978
---

# OWASP ZAP Scanner

OWASP ZAP Scanner is built around OWASP security tooling ecosystem. The underlying ecosystem is represented by zaproxy/zaproxy (14,896+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like ZAP scanning, passive/active checks, auth contexts, alerts, HTTP spidering and preserving the operational context that matters for real tasks.


In practice, the skill gives an agent a stable interface to owasp so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on ZAP scanning, passive/active checks, auth contexts, alerts, HTTP spidering, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.



Accesses ZAP scanning, passive/active checks, auth contexts, alerts, HTTP spidering instead of scraping a UI, which makes runs easier to audit and retry.
Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
Fits into broader integration points such as web app security review, DAST, and verification workflows.

In security-oriented usage, the skill emphasizes read-only discovery, evidence capture, and machine-readable output such as SARIF, JSON, or structured findings so results can flow into existing review pipelines. Key integration points include web app security review, DAST, and verification workflows. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-scanner/)
