---
name: Nginx Error Log Parser
description: Parses nginx error.log and access.log files using pattern matching for
  5xx status codes, upstream timeouts, and SSL handshake failures. Correlates error
  spikes with nginx -T configuration dumps to identify misconfigured proxy_pass and
  keepalive settings.
verification: security_reviewed
source: https://agentskillexchange.com/skills/nginx-error-log-parser/
category:
- Developer Tools
framework:
- Custom Agents
---
# Nginx Error Log Parser

Nginx Error Log Parser is built around NGINX web server and reverse proxy. The underlying ecosystem is represented by nginx/nginx (29,762+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like error.log, access.log, upstreams, proxy_pass, TLS, keepalive, config dump and preserving the operational context that matters for real tasks.
In practice, the skill gives an agent a stable interface to nginx so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Parses nginx error.log and access.log files using pattern matching for 5xx status codes, upstream timeouts, and SSL handshake failures. Correlates error spikes with nginx -T configuration dumps to identify misconfigured proxy_pass and keepalive settings. The implementation typically relies on error.log, access.log, upstreams, proxy_pass, TLS, keepalive, config dump, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses error.log, access.log, upstreams, proxy_pass, TLS, keepalive, config dump instead of scraping a UI, which makes runs easier to audit and retry.
Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
Fits into broader integration points such as traffic routing, HTTP diagnostics, and edge/server troubleshooting.

As a runbook-style skill, the value is not just tool access but operational sequencing: check the right signals first, reduce alert noise, and produce a summary that another engineer can act on immediately. Key integration points include traffic routing, HTTP diagnostics, and edge/server troubleshooting. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nginx-error-log-parser/)
