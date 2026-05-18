---
name: "Run PHPStan on WordPress codebases with correct stubs baselines and narrow ignores"
slug: "run-phpstan-on-wordpress-codebases-with-correct-stubs-baselines-and-narrow-ignores"
description: "This entry turns WordPress/agent-skills' WP PHPStan guidance into a bounded agent workflow for plugin, theme, and site repositories. The agent inspects the existing PHPStan setup, adds or verifies WordPress-aware stubs, tightens config paths, and fixes or documents only the narrow ignores and baseline changes needed to get useful static-analysis output."
verification: "security_reviewed"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Use a Composer-based PHPStan setup and load WordPress-aware stubs such as szepeviktor/phpstan-wordpress or php-stubs/wordpress-stubs before analysis.
```

## Documentation

- https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-phpstan

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-phpstan-on-wordpress-codebases-with-correct-stubs-baselines-and-narrow-ignores/)
