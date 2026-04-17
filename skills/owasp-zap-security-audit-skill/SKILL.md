---
title: "OWASP ZAP Security Audit Skill"
description: "Wraps OWASP ZAP API for automated web application security testing including active scan, spider crawl, and ajax spider endpoints. Generates structured findings reports with CWE classifications and OWASP Top 10 category mapping.\nOverview\nThis skill provides automated integration capabilities designed for production agent workflows. It handles authentication, rate limiting, and error recovery out of the box, allowing agents to focus on high-level task orchestration rather than low-level API management.\nKey Features\n\nAutomatic retry logic with exponential backoff for API rate limits\nStructured output formatting compatible with downstream agent pipelines\nComprehensive error handling with actionable diagnostic messages\nConfigurable caching layer to reduce redundant API calls\n\nUsage\nInstall via the Agent Skill Exchange registry and configure with your API credentials. The skill exposes a standardized interface that works across supported agent frameworks, with framework-specific optimizations applied automatically during initialization."
verification: security_reviewed
source: "https://github.com/zaproxy/zaproxy"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "zaproxy/zaproxy"
  github_stars: 14991
---

# OWASP ZAP Security Audit Skill

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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/owasp-zap-security-audit-skill
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/owasp-zap-security-audit-skill` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-security-audit-skill/)
