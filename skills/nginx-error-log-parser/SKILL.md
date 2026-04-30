---
title: "Nginx Error Log Parser"
description: "Parses nginx error.log and access.log files using pattern matching for 5xx status codes, upstream timeouts, and SSL handshake failures. Correlates error spikes with nginx -T configuration dumps to identify misconfigured proxy_pass and keepalive settings."
verification: "security_reviewed"
source: "https://github.com/nginx/nginx"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "nginx/nginx"
  github_stars: 29930
---

# Nginx Error Log Parser

Parses nginx error.log and access.log files using pattern matching for 5xx status codes, upstream timeouts, and SSL handshake failures. Correlates error spikes with nginx -T configuration dumps to identify misconfigured proxy_pass and keepalive settings.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nginx-error-log-parser/)
