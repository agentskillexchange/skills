---
name: "Enforce package boundaries inside a Rails monolith before coupling spreads with Packwerk"
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

Use the upstream install or setup path that matches your environment:
- gem 'packwerk'
- $ gem install packwerk

Requirements and caveats from upstream:
- This is because we rely on [Zeitwerk's conventions](https://github.com/fxn/zeitwerk#file-structure), and code that is loaded differently (like through an explicit require) often doesn't follow these conventions.

Basic usage or getting-started notes:
- Packwerk needs [Zeitwerk](https://github.com/fxn/zeitwerk) enabled, which comes with Rails 6.
- Packwerk supports MRI versions 2.7 and above.
- ## Demo

- Source: https://github.com/Shopify/packwerk
- Extracted from upstream docs: https://raw.githubusercontent.com/Shopify/packwerk/HEAD/README.md

## Documentation

- https://github.com/Shopify/packwerk

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/enforce-package-boundaries-inside-a-rails-monolith-before-coupling-spreads-with-packwerk/)
