---
title: "Develop and harden WordPress plugins with lifecycle and security guardrails"
description: "Use Automattic&#8217;s official wp-plugin-development skill when an agent needs to build, refactor, secure, or package a WordPress plugin with correct activation hooks, settings handling, uninstall behavior, and data hygiene. This is a plugin engineering playbook, not a generic WordPress listing."
verification: security_reviewed
source: "https://github.com/Automattic/agent-skills/tree/trunk/skills/wp-plugin-development"
category:
  - "WordPress &amp; CMS"
---

# Develop and harden WordPress plugins with lifecycle and security guardrails

Use Automattic&#8217;s official wp-plugin-development skill when an agent needs to build, refactor, secure, or package a WordPress plugin with correct activation hooks, settings handling, uninstall behavior, and data hygiene. This is a plugin engineering playbook, not a generic WordPress listing.

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
