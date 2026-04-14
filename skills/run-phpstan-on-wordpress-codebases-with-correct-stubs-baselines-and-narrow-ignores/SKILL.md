---
title: "Run PHPStan on WordPress codebases with correct stubs baselines and narrow ignores"
description: "This entry turns WordPress/agent-skills’ WP PHPStan guidance into a bounded agent workflow for plugin, theme, and site repositories. The agent inspects the existing PHPStan setup, adds or verifies WordPress-aware stubs, tightens config paths, and fixes or documents only the narrow ignores and baseline changes needed to get useful static-analysis output."
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

This entry is built around the official WP PHPStan skill in the WordPress agent-skills repository. The upstream guidance is not just a description of PHPStan as a product. It is a concrete operator workflow for getting static analysis to behave in real WordPress codebases, especially when plugins, themes, REST callbacks, hooks, and third-party integrations produce noisy or misleading type errors. The agent’s job here is to inspect the repository’s current PHPStan entrypoints, verify or add WordPress-aware stubs, review phpstan.neon and any baseline file, and then make the smallest safe changes that turn the report into something actionable.

You invoke this when a WordPress repository has static-analysis debt, when a new plugin or theme is adopting PHPStan, or when CI is failing because WordPress types are unresolved. It is useful for setting up a clean configuration, shrinking an overgrown baseline, fixing WordPress-specific PHPDoc, and handling third-party plugin classes with targeted stubs or narrow ignore rules. It is not a generic PHP static-analysis catalog card and it is not a generic “use PHPStan” entry. The scope boundary is strict: WordPress-specific PHPStan configuration, baseline management, and error repair only.

Integration points are Composer, vendor/bin/phpstan or existing Composer scripts, phpstan.neon, phpstan-baseline.neon, WordPress stubs such as szepeviktor/phpstan-wordpress or php-stubs/wordpress-stubs, and CI jobs that need deterministic analysis results. If the repository already has conventions, the agent follows them. If a dependency version or new Composer package cannot be verified, the workflow pauses instead of inventing types. That makes the entry skill-shaped, source-backed, and operationally narrow enough to be useful on its own.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-phpstan-on-wordpress-codebases-with-correct-stubs-baselines-and-narrow-ignores/)
