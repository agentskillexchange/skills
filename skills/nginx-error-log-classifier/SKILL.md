---
title: "Nginx Error Log Classifier"
description: "Classifies and prioritizes Nginx error log entries using pattern matching against known error signatures and the GoAccess real-time log analyzer. Maps upstream timeout patterns to specific backend service degradation."
verification: security_reviewed
source: "https://github.com/nginx/nginx"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "nginx/nginx"
  github_stars: 29930
---

# Nginx Error Log Classifier

The Nginx Error Log Classifier skill processes Nginx error logs to identify, classify, and prioritize issues affecting web application delivery. It parses error.log entries using regex patterns matched against a curated database of known Nginx error signatures, categorizing them into upstream failures, SSL/TLS errors, configuration issues, and resource exhaustion events.

The skill integrates with GoAccess for real-time log analysis and can process access.log entries to correlate error spikes with traffic patterns. It maps upstream timeout and connection refused patterns to specific backend services by cross-referencing Nginx upstream block configurations, helping identify which microservice is degraded.

Advanced capabilities include SSL handshake failure diagnosis by inspecting certificate chains via OpenSSL s_client, worker process crash analysis through core dump inspection, and rate limiting effectiveness evaluation by analyzing limit_req and limit_conn zone statistics. The skill generates actionable Nginx configuration snippets for resolving detected issues, including buffer size adjustments, keepalive tuning, and proxy timeout optimization.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nginx-error-log-classifier/)
