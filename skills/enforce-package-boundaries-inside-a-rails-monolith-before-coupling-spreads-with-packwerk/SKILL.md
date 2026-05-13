---
title: "Enforce package boundaries inside a Rails monolith before coupling spreads with Packwerk"
slug: "enforce-package-boundaries-inside-a-rails-monolith-before-coupling-spreads-with-packwerk"
description: "Check a Rails codebase for dependency and visibility violations so domain boundaries stay reviewable instead of dissolving over time."
github_stars: 1858
verification: "security_reviewed"
source: "https://github.com/Shopify/packwerk"
author: "Shopify"
publisher_type: "organization"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "Shopify/packwerk"
  github_stars: 1858
---

# Enforce package boundaries inside a Rails monolith before coupling spreads with Packwerk

Check a Rails codebase for dependency and visibility violations so domain boundaries stay reviewable instead of dissolving over time.

## Prerequisites

Ruby, Bundler, a Rails application with Zeitwerk enabled, Packwerk gem installation, and repository access to the monolith being analyzed

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Add Packwerk to the target Rails application's Gemfile or install it as documented upstream, generate the configuration with the provided init command, then run Packwerk against the codebase to report package dependency and privacy violations.
```

## Documentation

- https://github.com/Shopify/packwerk

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/enforce-package-boundaries-inside-a-rails-monolith-before-coupling-spreads-with-packwerk/)
