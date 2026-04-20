---
title: "Nginx Error Log Classifier"
description: "Classifies and prioritizes Nginx error log entries using pattern matching against known error signatures and the GoAccess real-time log analyzer. Maps upstream timeout patterns to specific backend service degradation."
verification: security_reviewed
source: "https://github.com/nginx/nginx"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "nginx/nginx"
  github_stars: 29930
---

# Nginx Error Log Classifier

Classifies and prioritizes Nginx error log entries using pattern matching against known error signatures and the GoAccess real-time log analyzer. Maps upstream timeout patterns to specific backend service degradation.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/nginx-error-log-classifier/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/nginx-error-log-classifier
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/nginx-error-log-classifier`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nginx-error-log-classifier/)
