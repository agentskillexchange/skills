---
name: "Backstage Software Template Composer"
description: "Creates Spotify Backstage software templates using template.yaml definitions with Scaffolder actions including fetch:template, publish:github, and catalog:register. Manages the Backstage Software Catalog via its REST API."
category: "Templates & Workflows"
framework: "Codex"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/backstage-software-template-composer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "pagerduty"  # from ase_tool_match
  github_stars: 69  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 210829  # from ase_npm_downloads
  github_repo: "PagerDuty/pdjs"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: false  # from ase_tool_maintained
---

# Backstage Software Template Composer

Creates Spotify Backstage software templates using template.yaml definitions with Scaffolder actions including fetch:template, publish:github, and catalog:register. Manages the Backstage Software Catalog via its REST API.

## Overview

The Backstage Software Template Composer builds and manages software templates within Spotify Backstage developer portals. Templates are defined using template.yaml with the backstage.io/v1beta3 schema, specifying multi-step scaffolding workflows that combine user input collection, code generation, repository creation, and catalog registration. Built-in Scaffolder actions including fetch:template for Nunjucks-based file rendering, publish:github for automated repository creation with branch protection and team access configuration, and catalog:register for adding new components to the Backstage Software Catalog are orchestrated into coherent workflows. The skill manages template parameters with JSON Schema validation, conditional step execution based on user selections, and custom UI picker components for selecting existing catalog entities. Integration with the Backstage Software Catalog REST API enables querying existing components, systems, and domains to maintain consistent naming and ownership across the organization. Template testing uses the Scaffolder dry-run mode to validate template rendering without creating external resources. Custom Scaffolder actions are developed using the @backstage/plugin-scaffolder-node SDK for organization-specific workflows like Jira project creation, Slack channel provisioning, or PagerDuty service registration.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill backstage-software-template-composer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill backstage-software-template-composer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill backstage-software-template-composer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill backstage-software-template-composer -a codex
```

### OpenClaw

```bash
clawhub install backstage-software-template-composer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/backstage-software-template-composer/
