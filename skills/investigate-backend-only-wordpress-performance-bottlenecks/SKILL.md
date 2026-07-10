---
name: "Investigate backend-only WordPress performance bottlenecks"
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

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/WordPress/agent-skills.git

Requirements and caveats from upstream:
- node shared/scripts/skillpack-build.mjs --clean
- node shared/scripts/skillpack-install.mjs --global
- node shared/scripts/skillpack-install.mjs --global --skills=wp-playground,wp-block-development

Basic usage or getting-started notes:
- bash
- # Clone agent-skills
- cd agent-skills

- Source: https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-performance
- Extracted from upstream docs: https://raw.githubusercontent.com/WordPress/agent-skills/HEAD/README.md

## Documentation

- https://github.com/WordPress/agent-skills

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/investigate-backend-only-wordpress-performance-bottlenecks/)
