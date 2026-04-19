---
title: "Investigate backend-only WordPress performance bottlenecks"
description: "This entry is based on the wp-performance skill from the official WordPress/agent-skills repository. The tool behavior is strongly skill-shaped: the agent measures a reproducible target, inspects available profiling tools, and then works through a bounded troubleshooting flow for backend performance issues. It prioritizes WP-CLI, logs, headers, and profiling data over UI guessing, which makes it well suited for coding agents and ops-oriented sessions. Invoke this when a user reports that a WordPress page, admin screen, REST route, or cron path is slow and wants an agent to diagnose the bottleneck safely. It is specifically useful when the user needs a profiling plan, a backend-only report, and a fix path organized by likely root cause, such as database queries, autoloaded options, object cache misses, remote HTTP calls, or due-now cron spikes. The scope boundary keeps it from collapsing into a plain product listing. This is not “WP-CLI” as a generic command-line tool, and it is not WordPress as a platform card. The value is the operator playbook: baseline first, inspect capabilities, choose one dominant bottleneck category, verify the delta, and avoid risky production changes without approval. Integration points include WP-CLI profile and doctor commands, Query Monitor headers, curl-based timing, PHP logs, and downstream code changes once the slow path is isolated."
source: "https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-performance"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Multi-Framework"
---

# Investigate backend-only WordPress performance bottlenecks

This entry is based on the wp-performance skill from the official WordPress/agent-skills repository. The tool behavior is strongly skill-shaped: the agent measures a reproducible target, inspects available profiling tools, and then works through a bounded troubleshooting flow for backend performance issues. It prioritizes WP-CLI, logs, headers, and profiling data over UI guessing, which makes it well suited for coding agents and ops-oriented sessions. Invoke this when a user reports that a WordPress page, admin screen, REST route, or cron path is slow and wants an agent to diagnose the bottleneck safely. It is specifically useful when the user needs a profiling plan, a backend-only report, and a fix path organized by likely root cause, such as database queries, autoloaded options, object cache misses, remote HTTP calls, or due-now cron spikes. The scope boundary keeps it from collapsing into a plain product listing. This is not “WP-CLI” as a generic command-line tool, and it is not WordPress as a platform card. The value is the operator playbook: baseline first, inspect capabilities, choose one dominant bottleneck category, verify the delta, and avoid risky production changes without approval. Integration points include WP-CLI profile and doctor commands, Query Monitor headers, curl-based timing, PHP logs, and downstream code changes once the slow path is isolated.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/investigate-backend-only-wordpress-performance-bottlenecks/)
