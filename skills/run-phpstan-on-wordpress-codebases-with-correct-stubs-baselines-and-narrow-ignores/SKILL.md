---
title: "Run PHPStan on WordPress codebases with correct stubs baselines and narrow ignores"
description: "This entry turns WordPress/agent-skills’ WP PHPStan guidance into a bounded agent workflow for plugin, theme, and site repositories. The agent inspects the existing PHPStan setup, adds or verifies WordPress-aware stubs, tightens config paths, and fixes or documents only the narrow ignores and baseline changes needed to get useful static-analysis output."
verification: "security_reviewed"
source: "https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-phpstan"
category:
  - "WordPress &amp; CMS"
framework:
  - "Multi-Framework"
---

# Run PHPStan on WordPress codebases with correct stubs baselines and narrow ignores

This entry is built around the official WP PHPStan skill in the WordPress agent-skills repository. The upstream guidance is not just a description of PHPStan as a product. It is a concrete operator workflow for getting static analysis to behave in real WordPress codebases, especially when plugins, themes, REST callbacks, hooks, and third-party integrations produce noisy or misleading type errors. The agent’s job here is to inspect the repository’s current PHPStan entrypoints, verify or add WordPress-aware stubs, review phpstan.neon and any baseline file, and then make the smallest safe changes that turn the report into something actionable.

You invoke this when a WordPress repository has static-analysis debt, when a new plugin or theme is adopting PHPStan, or when CI is failing because WordPress types are unresolved. It is useful for setting up a clean configuration, shrinking an overgrown baseline, fixing WordPress-specific PHPDoc, and handling third-party plugin classes with targeted stubs or narrow ignore rules. It is not a generic PHP static-analysis catalog card and it is not a generic “use PHPStan” entry. The scope boundary is strict: WordPress-specific PHPStan configuration, baseline management, and error repair only.

Integration points are Composer, vendor/bin/phpstan or existing Composer scripts, phpstan.neon, phpstan-baseline.neon, WordPress stubs such as szepeviktor/phpstan-wordpress or php-stubs/wordpress-stubs, and CI jobs that need deterministic analysis results. If the repository already has conventions, the agent follows them. If a dependency version or new Composer package cannot be verified, the workflow pauses instead of inventing types. That makes the entry skill-shaped, source-backed, and operationally narrow enough to be useful on its own.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-phpstan-on-wordpress-codebases-with-correct-stubs-baselines-and-narrow-ignores/)
