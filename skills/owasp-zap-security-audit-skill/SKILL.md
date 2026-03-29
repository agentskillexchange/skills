---
name: "OWASP ZAP Security Audit Skill"
description: "Wraps OWASP ZAP API for automated web application security testing including active scan, spider crawl, and ajax spider endpoints. Generates structured findings reports with CWE classifications and OWASP Top 10 category mapping."
category: "Security & Verification"
framework: "Claude Code"
verification: security_reviewed
source: "https://github.com/zaproxy/zaproxy"
tool_ecosystem:
  tool: owasp
  github_stars: 14900
  github_repo: zaproxy/zaproxy
  license: Apache-2.0
  maintained: true
---
# OWASP ZAP Security Audit Skill

Wraps OWASP ZAP API for automated web application security testing including active scan, spider crawl, and ajax spider endpoints. Generates structured findings reports with CWE classifications and OWASP Top 10 category mapping.

## Overview

Wraps OWASP ZAP API for automated web application security testing including active scan, spider crawl, and ajax spider endpoints. Generates structured findings reports with CWE classifications and OWASP Top 10 category mapping.

Overview

This skill provides automated integration capabilities designed for production agent workflows. It handles authentication, rate limiting, and error recovery out of the box, allowing agents to focus on high-level task orchestration rather than low-level API management.

Key Features

Automatic retry logic with exponential backoff for API rate limits

Structured output formatting compatible with downstream agent pipelines

Comprehensive error handling with actionable diagnostic messages

Configurable caching layer to reduce redundant API calls

Usage

Install via the Agent Skill Exchange registry and configure with your API credentials. The skill exposes a standardized interface that works across supported agent frameworks, with framework-specific optimizations applied automatically during initialization.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-security-audit-skill
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-security-audit-skill -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-security-audit-skill -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill owasp-zap-security-audit-skill -a codex
```

### OpenClaw

```bash
clawhub install owasp-zap-security-audit-skill
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-security-audit-skill/)
