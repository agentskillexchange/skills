---
title: "Airbyte Connector Config Generator"
description: "Generates Airbyte source and destination connector configurations using the Airbyte API /v1/sources/create and /v1/destinations/create endpoints. Validates connection specs against the Airbyte Protocol."
verification: security_reviewed
source: "https://github.com/airbytehq/airbyte"
category:
  - "Data Extraction & Transformation"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "airbytehq/airbyte"
  github_stars: 21088
---

# Airbyte Connector Config Generator

The Airbyte Connector Config Generator automates the creation of source and destination connector configurations for the Airbyte data integration platform. It uses the Airbyte API /v1/source_definitions/get_for_workspace endpoint to fetch available connector specifications and generates valid configuration JSON based on the connector spec schema. The generator validates configurations against the Airbyte Protocol specification, ensuring proper authentication credentials, sync mode settings, and stream selections. It supports the /v1/sources/create and /v1/destinations/create API endpoints for programmatic connector provisioning. Connection testing is automated via the /v1/sources/check_connection endpoint to verify credentials and network connectivity before deployment. The skill generates complete sync configurations including namespace mapping, cursor field selection for incremental syncs, and primary key definitions for deduplication. It also produces Airbyte Terraform provider configurations for infrastructure-as-code deployments.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/airbyte-connector-config-generator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/airbyte-connector-config-generator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/airbyte-connector-config-generator/)
