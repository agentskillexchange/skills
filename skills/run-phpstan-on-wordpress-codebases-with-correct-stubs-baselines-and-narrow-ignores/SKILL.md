---
name: "Run PHPStan on WordPress codebases with correct stubs baselines and narrow ignores"
slug: "run-phpstan-on-wordpress-codebases-with-correct-stubs-baselines-and-narrow-ignores"
description: "This entry turns WordPress/agent-skills' WP PHPStan guidance into a bounded agent workflow for plugin, theme, and site repositories. The agent inspects the existing PHPStan setup, adds or verifies WordPress-aware stubs, tightens config paths, and fixes or documents only the narrow ignores and baseline changes needed to get useful static-analysis output."
verification: "listed"
source: "https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-phpstan"
author: "WordPress"
publisher_type: "Open Source Project"
category: "WordPress & CMS"
framework: "Multi-Framework"
---

# Run PHPStan on WordPress codebases with correct stubs baselines and narrow ignores

This entry turns WordPress/agent-skills' WP PHPStan guidance into a bounded agent workflow for plugin, theme, and site repositories. The agent inspects the existing PHPStan setup, adds or verifies WordPress-aware stubs, tightens config paths, and fixes or documents only the narrow ignores and baseline changes needed to get useful static-analysis output.

## Prerequisites

PHP, Composer, PHPStan, and a WordPress plugin, theme, or site repository

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

- Source: https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-phpstan
- Extracted from upstream docs: https://raw.githubusercontent.com/WordPress/agent-skills/HEAD/README.md

## Documentation

- https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-phpstan

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-phpstan-on-wordpress-codebases-with-correct-stubs-baselines-and-narrow-ignores/)
