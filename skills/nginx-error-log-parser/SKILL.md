---
title: Nginx Error Log Parser
description: Parses nginx error.log and access.log files using pattern matching for
  5xx status codes, upstream timeouts, and SSL handshake failures. Correlates error
  spikes with nginx -T configuration dumps to identify misconfigured proxy_pass and
  keepalive settings.
verification: security_reviewed
source: https://github.com/nginx/nginx
category:
- Developer Tools
framework:
- Custom Agents
tool_ecosystem:
  github_repo: nginx/nginx
  github_stars: 29930
---

# Nginx Error Log Parser

Parses nginx error.log and access.log files using pattern matching for 5xx status codes, upstream timeouts, and SSL handshake failures. Correlates error spikes with nginx -T configuration dumps to identify misconfigured proxy_pass and keepalive settings.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/nginx-error-log-parser/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/nginx-error-log-parser
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/nginx-error-log-parser`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nginx-error-log-parser/)
