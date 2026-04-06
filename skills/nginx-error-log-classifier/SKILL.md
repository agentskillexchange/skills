---
name: Nginx Error Log Classifier
description: Classifies and prioritizes Nginx error log entries using pattern matching
  against known error signatures and the GoAccess real-time log analyzer. Maps upstream
  timeout patterns to specific backend service degradation.
category: "Runbooks &amp; Diagnostics"
framework: Cursor
verification: security_reviewed
source: "https://agentskillexchange.com/skills/nginx-error-log-classifier/"
---
# Nginx Error Log Classifier

Classifies and prioritizes Nginx error log entries using pattern matching against known error signatures and the GoAccess real-time log analyzer. Maps upstream timeout patterns to specific backend service degradation.

The Nginx Error Log Classifier skill processes Nginx error logs to identify, classify, and prioritize issues affecting web application delivery. It parses error.log entries using regex patterns matched against a curated database of known Nginx error signatures, categorizing them into upstream failures, SSL/TLS errors, configuration issues, and resource exhaustion events.

The skill integrates with GoAccess for real-time log analysis and can process access.log entries to correlate error spikes with traffic patterns. It maps upstream timeout and connection refused patterns to specific backend services by cross-referencing Nginx upstream block configurations, helping identify which microservice is degraded.

Advanced capabilities include SSL handshake failure diagnosis by inspecting certificate chains via OpenSSL s_client, worker process crash analysis through core dump inspection, and rate limiting effectiveness evaluation by analyzing limit_req and limit_conn zone statistics. The skill generates actionable Nginx configuration snippets for resolving detected issues, including buffer size adjustments, keepalive tuning, and proxy timeout optimization.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-classifier
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-classifier -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-classifier -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-classifier -a codex
```

### OpenClaw

```bash
clawhub install nginx-error-log-classifier
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nginx-error-log-classifier/)
