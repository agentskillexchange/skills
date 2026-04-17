---
title: "Investigate backend-only WordPress performance bottlenecks"
description: "This skill guides an agent through measuring, profiling, and narrowing slow WordPress behavior without relying on browser clicks. Use it when the job is to diagnose slow pages, REST endpoints, cron activity, autoload bloat, or query-heavy requests from the backend outward."
verification: security_reviewed
source: "https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-performance"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "wordpress/agent-skills"
  github_stars: 1219
---

# Investigate backend-only WordPress performance bottlenecks

This entry is based on the wp-performance skill from the official WordPress/agent-skills repository. The tool behavior is strongly skill-shaped: the agent measures a reproducible target, inspects available profiling tools, and then works through a bounded troubleshooting flow for backend performance issues. It prioritizes WP-CLI, logs, headers, and profiling data over UI guessing, which makes it well suited for coding agents and ops-oriented sessions.

Invoke this when a user reports that a WordPress page, admin screen, REST route, or cron path is slow and wants an agent to diagnose the bottleneck safely. It is specifically useful when the user needs a profiling plan, a backend-only report, and a fix path organized by likely root cause, such as database queries, autoloaded options, object cache misses, remote HTTP calls, or due-now cron spikes.

The scope boundary keeps it from collapsing into a plain product listing. This is not “WP-CLI” as a generic command-line tool, and it is not WordPress as a platform card. The value is the operator playbook: baseline first, inspect capabilities, choose one dominant bottleneck category, verify the delta, and avoid risky production changes without approval. Integration points include WP-CLI profile and doctor commands, Query Monitor headers, curl-based timing, PHP logs, and downstream code changes once the slow path is isolated.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/investigate-backend-only-wordpress-performance-bottlenecks
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/investigate-backend-only-wordpress-performance-bottlenecks` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/investigate-backend-only-wordpress-performance-bottlenecks/)
