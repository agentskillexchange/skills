---
name: "Nginx Error Log Runbook Agent"
slug: "nginx-error-log-runbook-agent"
description: "Automates Nginx error diagnosis using nginx -T configuration dump, error.log pattern matching, and the Nginx Plus REST API /api/8/http/upstreams endpoint. Resolves 502 Bad Gateway, SSL handshake failures, and upstream timeout issues."
github_stars: 29930
verification: "security_reviewed"
source: "https://github.com/nginx/nginx"
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
tool_ecosystem:
  github_repo: "nginx/nginx"
  github_stars: 29930
---

# Nginx Error Log Runbook Agent

Automates Nginx error diagnosis using nginx -T configuration dump, error.log pattern matching, and the Nginx Plus REST API /api/8/http/upstreams endpoint. Resolves 502 Bad Gateway, SSL handshake failures, and upstream timeout issues.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nginx-error-log-runbook-agent/)
