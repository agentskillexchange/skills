---
title: "Develop and harden WordPress plugins with lifecycle and security guardrails"
description: "Use Automattic’s official wp-plugin-development skill when an agent needs to build, refactor, secure, or package a WordPress plugin with correct activation hooks, settings handling, uninstall behavior, and data hygiene. This is a plugin engineering playbook, not a generic WordPress listing."
verification: security_reviewed
source: "https://github.com/Automattic/agent-skills/tree/trunk/skills/wp-plugin-development"
category:
  - "WordPress &amp; CMS"
framework:
  - "Multi-Framework"
---

# Develop and harden WordPress plugins with lifecycle and security guardrails

Tool name: WP Plugin Development, from Automattic’s official agent-skills repository.

This entry qualifies because it maps to a bounded operator workflow: designing, refactoring, and hardening WordPress plugins with repeatable architectural and security guardrails. The upstream skill is not just describing WordPress as a platform. It gives the agent a concrete sequence: detect plugin entry points, follow a predictable bootstrap and hook architecture, implement activation and uninstall safely, build admin settings via the Settings API, enforce nonce and capability checks, and verify data storage, cron behavior, and packaging before release.

Invoke this when a user wants an agent to create a plugin skeleton, clean up a messy plugin, add hooks, ship an admin settings page, fix activation or uninstall bugs, tighten sanitization and escaping, or prepare a release artifact. It is the right choice when the request is about plugin engineering work. It is not for using WordPress normally, browsing plugins, running editorial workflows, or reading CMS marketing pages.

The scope boundary keeps it from collapsing into a product listing. This is not “WordPress” in general and not even all developer work inside WordPress. It is specifically about plugin development lifecycle concerns: bootstrap structure, activation and deactivation behavior, migrations, settings registration, SQL safety, cron idempotency, and release packaging. Theme work, block-only work, REST controller work, or general site administration belong in different entries.

Integration points include filesystem-based WordPress repos, plugin folders under wp-content/plugins or mu-plugins, WP-CLI assisted verification, and plugin release workflows. Evidence is source-backed through the official Automattic repo, readable skill docs, repository license, and recent maintenance.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/develop-and-harden-wordpress-plugins-with-lifecycle-and-security-guardrails/)
