---
title: "OWASP ZAP Security Audit Skill"
description: "Wraps OWASP ZAP API for automated web application security testing including active scan, spider crawl, and ajax spider endpoints. Generates structured findings reports with CWE classifications and OWASP Top 10 category mapping."
verification: "security_reviewed"
source: "https://github.com/zaproxy/zaproxy"
category:
  - "Security &amp; Verification"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "zaproxy/zaproxy"
  github_stars: 14991
  license: "Apache-2.0"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-security-audit-skill/)
