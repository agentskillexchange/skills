---
title: "Run PHPStan on WordPress codebases with correct stubs baselines and narrow ignores"
slug: "run-phpstan-on-wordpress-codebases-with-correct-stubs-baselines-and-narrow-ignores"
verification: security_reviewed
source: "https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-phpstan"
category:
  - "WordPress &amp; CMS"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "wordpress/agent-skills"
  github_stars: 1219
---
# Run PHPStan on WordPress codebases with correct stubs baselines and narrow ignores

This entry turns WordPress/agent-skills' WP PHPStan guidance into a bounded agent workflow for plugin, theme, and site repositories. The agent inspects the existing PHPStan setup, adds or verifies WordPress-aware stubs, tightens config paths, and fixes or documents only the narrow ignores and baseline changes needed to get useful static-analysis output.

## Installation

Choose the method that fits your setup:

1. Install from Agent Skill Exchange
2. Clone or download the upstream project
3. Install with the upstream package manager
4. Add the skill to your local skills directory
5. Follow the upstream documentation for environment-specific setup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-phpstan-on-wordpress-codebases-with-correct-stubs-baselines-and-narrow-ignores/)
