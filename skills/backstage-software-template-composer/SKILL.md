---
title: "Backstage Software Template Composer"
description: "Creates Spotify Backstage software templates using template.yaml definitions with Scaffolder actions including fetch:template, publish:github, and catalog:register. Manages the Backstage Software Catalog via its REST API."
slug: "backstage-software-template-composer"
category:
  - "Templates &amp; Workflows"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://github.com/backstage/backstage"
tool_ecosystem:
  github_repo: "backstage/backstage"
  github_stars: 33052
---

# Backstage Software Template Composer

Creates Spotify Backstage software templates using template.yaml definitions with Scaffolder actions including fetch:template, publish:github, and catalog:register. Manages the Backstage Software Catalog via its REST API.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install backstage-software-template-composer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Backstage Software Template Composer builds and manages software templates within Spotify Backstage developer portals. Templates are defined using template.yaml with the backstage.io/v1beta3 schema, specifying multi-step scaffolding workflows that combine user input collection, code generation, repository creation, and catalog registration. Built-in Scaffolder actions including fetch:template for Nunjucks-based file rendering, publish:github for automated repository creation with branch protection and team access configuration, and catalog:register for adding new components to the Backstage Software Catalog are orchestrated into coherent workflows. The skill manages template parameters with JSON Schema validation, conditional step execution based on user selections, and custom UI picker components for selecting existing catalog entities. Integration with the Backstage Software Catalog REST API enables querying existing components, systems, and domains to maintain consistent naming and ownership across the organization. Template testing uses the Scaffolder dry-run mode to validate template rendering without creating external resources. Custom Scaffolder actions are developed using the @backstage/plugin-scaffolder-node SDK for organization-specific workflows like Jira project creation, Slack channel provisioning, or PagerDuty service registration.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/backstage-software-template-composer/)
