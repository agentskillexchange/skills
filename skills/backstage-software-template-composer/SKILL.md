---
title: "Backstage Software Template Composer"
description: "Creates Spotify Backstage software templates using template.yaml definitions with Scaffolder actions including fetch:template, publish:github, and catalog:register. Manages the Backstage Software Catalog via its REST API."
verification: "security_reviewed"
source: "https://github.com/backstage/backstage"
category:
  - "Templates &amp; Workflows"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "backstage/backstage"
  github_stars: 33052
---

# Backstage Software Template Composer

The Backstage Software Template Composer builds and manages software templates within Spotify Backstage developer portals. Templates are defined using template.yaml with the backstage.io/v1beta3 schema, specifying multi-step scaffolding workflows that combine user input collection, code generation, repository creation, and catalog registration. Built-in Scaffolder actions including fetch:template for Nunjucks-based file rendering, publish:github for automated repository creation with branch protection and team access configuration, and catalog:register for adding new components to the Backstage Software Catalog are orchestrated into coherent workflows. The skill manages template parameters with JSON Schema validation, conditional step execution based on user selections, and custom UI picker components for selecting existing catalog entities. Integration with the Backstage Software Catalog REST API enables querying existing components, systems, and domains to maintain consistent naming and ownership across the organization. Template testing uses the Scaffolder dry-run mode to validate template rendering without creating external resources. Custom Scaffolder actions are developed using the @backstage/plugin-scaffolder-node SDK for organization-specific workflows like Jira project creation, Slack channel provisioning, or PagerDuty service registration.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/backstage-software-template-composer/)
