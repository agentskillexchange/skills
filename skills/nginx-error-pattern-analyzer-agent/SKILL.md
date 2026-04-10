---
name: Nginx Error Pattern Analyzer
description: Analyzes Nginx error logs using GoAccess and custom regex parsers to
  identify recurring 502/503 patterns. Correlates upstream timeout errors with backend
  service health via Prometheus PromQL queries.
verification: security_reviewed
source: https://agentskillexchange.com/skills/nginx-error-pattern-analyzer-agent/
category:
- Runbooks &amp; Diagnostics
framework:
- Custom Agents
---
# Nginx Error Pattern Analyzer

The Nginx Error Pattern Analyzer processes Nginx error and access logs to identify recurring failure patterns and their root causes. It combines GoAccess for real-time log parsing with custom regex-based pattern matching to categorize errors by type, frequency, and impact.
The agent focuses on critical error patterns including upstream connection timeouts, 502 Bad Gateway spikes, 503 Service Unavailable patterns, SSL handshake failures, and rate limiting events. It correlates Nginx error timestamps with backend service metrics via Prometheus PromQL queries to establish causation between upstream service degradation and frontend errors.
Advanced analysis features include request path clustering to identify which API endpoints trigger the most errors, geographic correlation using GeoIP data, and time-series anomaly detection for unusual error rate spikes. The agent generates incident-ready reports with timeline visualizations, affected endpoint summaries, and recommended Nginx configuration changes (timeout adjustments, buffer sizes, retry policies) to mitigate identified issues.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nginx-error-pattern-analyzer-agent/)
