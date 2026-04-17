---
title: "Backstage Software Template Composer"
description: "The Backstage Software Template Composer builds and manages software templates within Spotify Backstage developer portals. Templates are defined using template.yaml with the backstage.io/v1beta3 schema, specifying multi-step scaffolding workflows that combine user input collection, code generation, repository creation, and catalog registration. Built-in Scaffolder actions including fetch:template for Nunjucks-based file rendering, publish:github for automated repository creation with branch protection and team access configuration, and catalog:register for adding new components to the Backstage Software Catalog are orchestrated into coherent workflows. The skill manages template parameters with JSON Schema validation, conditional step execution based on user selections, and custom UI picker components for selecting existing catalog entities. Integration with the Backstage Software Catalog REST API enables querying existing components, systems, and domains to maintain consistent naming and ownership across the organization. Template testing uses the Scaffolder dry-run mode to validate template rendering without creating external resources. Custom Scaffolder actions are developed using the @backstage/plugin-scaffolder-node SDK for organization-specific workflows like Jira project creation, Slack channel provisioning, or PagerDuty service registration."
verification: security_reviewed
source: "https://github.com/backstage/backstage"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "backstage/backstage"
  github_stars: 33052
---

# Backstage Software Template Composer

The Backstage Software Template Composer builds and manages software templates within Spotify Backstage developer portals. Templates are defined using template.yaml with the backstage.io/v1beta3 schema, specifying multi-step scaffolding workflows that combine user input collection, code generation, repository creation, and catalog registration. Built-in Scaffolder actions including fetch:template for Nunjucks-based file rendering, publish:github for automated repository creation with branch protection and team access configuration, and catalog:register for adding new components to the Backstage Software Catalog are orchestrated into coherent workflows. The skill manages template parameters with JSON Schema validation, conditional step execution based on user selections, and custom UI picker components for selecting existing catalog entities. Integration with the Backstage Software Catalog REST API enables querying existing components, systems, and domains to maintain consistent naming and ownership across the organization. Template testing uses the Scaffolder dry-run mode to validate template rendering without creating external resources. Custom Scaffolder actions are developed using the @backstage/plugin-scaffolder-node SDK for organization-specific workflows like Jira project creation, Slack channel provisioning, or PagerDuty service registration.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/backstage-software-template-composer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/backstage-software-template-composer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/backstage-software-template-composer/)
