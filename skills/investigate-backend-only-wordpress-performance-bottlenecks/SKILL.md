---
title: "Investigate backend-only WordPress performance bottlenecks"
description: "This skill guides an agent through measuring, profiling, and narrowing slow WordPress behavior without relying on browser clicks. Use it when the job is to diagnose slow pages, REST endpoints, cron activity, autoload bloat, or query-heavy requests from the backend outward."
verification: security_reviewed
source: "https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-performance"
category:
  - "Runbooks &amp; Diagnostics"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/investigate-backend-only-wordpress-performance-bottlenecks/)
