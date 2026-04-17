---
name: Nginx Error Log Parser
description: Parses nginx error.log and access.log files using pattern matching for
  5xx status codes, upstream timeouts, and SSL handshake failures. Correlates error
  spikes with nginx -T configuration dumps to identify misconfigured proxy_pass and
  keepalive settings.
category: Developer Tools
framework: Custom Agents
verification: security_reviewed
source: https://github.com/nginx/nginx
tool_ecosystem:
  github_repo: nginx/nginx
  github_stars: 29930
  tool: nginx
  license: BSD-2-Clause
  maintained: true
---
# Nginx Error Log Parser
Parses nginx error.log and access.log files using pattern matching for 5xx status codes, upstream timeouts, and SSL handshake failures. Correlates error spikes with nginx -T configuration dumps to identify misconfigured proxy_pass and keepalive settings.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/nginx-error-log-parser
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/nginx-error-log-parser` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nginx-error-log-parser/)
