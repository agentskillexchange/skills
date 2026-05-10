---
title: "Investigate backend-only WordPress performance bottlenecks"
slug: "investigate-backend-only-wordpress-performance-bottlenecks"
description: "This skill guides an agent through measuring, profiling, and narrowing slow WordPress behavior without relying on browser clicks. Use it when the job is to diagnose slow pages, REST endpoints, cron activity, autoload bloat, or query-heavy requests from the backend outward."
verification: "security_reviewed"
source: "https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-performance"
author: "WordPress Contributors"
publisher_type: "Open Source Project"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
---

# Investigate backend-only WordPress performance bottlenecks

This skill guides an agent through measuring, profiling, and narrowing slow WordPress behavior without relying on browser clicks. Use it when the job is to diagnose slow pages, REST endpoints, cron activity, autoload bloat, or query-heavy requests from the backend outward.

## Prerequisites

WP-CLI; curl; logs; optional Query Monitor and profiler tooling

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Clone WordPress/agent-skills, run node shared/scripts/skillpack-build.mjs --clean, then install with node shared/scripts/skillpack-install.mjs --global or --dest=<project>.
```

## Documentation

- https://github.com/WordPress/agent-skills

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/investigate-backend-only-wordpress-performance-bottlenecks/)
