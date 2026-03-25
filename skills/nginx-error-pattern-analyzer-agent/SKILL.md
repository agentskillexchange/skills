---
name: "Nginx Error Pattern Analyzer"
description: "Analyzes Nginx error logs using GoAccess and custom regex parsers to identify recurring 502/503 patterns. Correlates upstream timeout errors with backend service health via Prometheus PromQL queries."
category: "Runbooks & Diagnostics"
framework: "Custom Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/nginx-error-pattern-analyzer-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "nginx"  # from ase_tool_match
  github_stars: 29767  # from ase_github_stars (integer, not string)
  github_repo: "nginx/nginx"  # from ase_github_repo
  license: "BSD-2-Clause"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Nginx Error Pattern Analyzer

Analyzes Nginx error logs using GoAccess and custom regex parsers to identify recurring 502/503 patterns. Correlates upstream timeout errors with backend service health via Prometheus PromQL queries.

## Overview

The Nginx Error Pattern Analyzer processes Nginx error and access logs to identify recurring failure patterns and their root causes. It combines GoAccess for real-time log parsing with custom regex-based pattern matching to categorize errors by type, frequency, and impact.

The agent focuses on critical error patterns including upstream connection timeouts, 502 Bad Gateway spikes, 503 Service Unavailable patterns, SSL handshake failures, and rate limiting events. It correlates Nginx error timestamps with backend service metrics via Prometheus PromQL queries to establish causation between upstream service degradation and frontend errors.

Advanced analysis features include request path clustering to identify which API endpoints trigger the most errors, geographic correlation using GeoIP data, and time-series anomaly detection for unusual error rate spikes. The agent generates incident-ready reports with timeline visualizations, affected endpoint summaries, and recommended Nginx configuration changes (timeout adjustments, buffer sizes, retry policies) to mitigate identified issues.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill nginx-error-pattern-analyzer-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill nginx-error-pattern-analyzer-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill nginx-error-pattern-analyzer-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill nginx-error-pattern-analyzer-agent -a codex
```

### OpenClaw

```bash
clawhub install nginx-error-pattern-analyzer-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/nginx-error-pattern-analyzer-agent/
