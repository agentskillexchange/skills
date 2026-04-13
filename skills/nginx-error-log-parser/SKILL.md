---
title: "Nginx Error Log Parser"
description: "Parses nginx error.log and access.log files using pattern matching for 5xx status codes, upstream timeouts, and SSL handshake failures. Correlates error spikes with nginx -T configuration dumps to identify misconfigured proxy_pass and keepalive settings."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/nginx-error-log-parser/"
category: ["Developer Tools"]
framework: ["Custom Agents"]
---

# Nginx Error Log Parser

Parses nginx error.log and access.log files using pattern matching for 5xx status codes, upstream timeouts, and SSL handshake failures. Correlates error spikes with nginx -T configuration dumps to identify misconfigured proxy_pass and keepalive settings.

## Installation

Choose the install path that fits your setup:

1. Install from the Agent Skill Exchange catalog if your agent client supports it.
2. Copy the skill folder into your local skills directory.
3. Add it as a git submodule in your shared agent-skills repo.
4. Vendor the files directly into a project-specific `.agents/skills/` or equivalent folder.
5. Keep a fork or mirror if you need local modifications or pinned revisions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nginx-error-log-parser/)
