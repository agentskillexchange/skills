---
title: "Airbyte Connector Config Generator"
description: "Generates Airbyte source and destination connector configurations using the Airbyte API /v1/sources/create and /v1/destinations/create endpoints. Validates connection specs against the Airbyte Protocol."
slug: "airbyte-connector-config-generator"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/airbyte-connector-config-generator/"
---

# Airbyte Connector Config Generator

Generates Airbyte source and destination connector configurations using the Airbyte API /v1/sources/create and /v1/destinations/create endpoints. Validates connection specs against the Airbyte Protocol.

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
clawhub install airbyte-connector-config-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Airbyte Connector Config Generator automates the creation of source and destination connector configurations for the Airbyte data integration platform. It uses the Airbyte API /v1/source_definitions/get_for_workspace endpoint to fetch available connector specifications and generates valid configuration JSON based on the connector spec schema. The generator validates configurations against the Airbyte Protocol specification, ensuring proper authentication credentials, sync mode settings, and stream selections. It supports the /v1/sources/create and /v1/destinations/create API endpoints for programmatic connector provisioning. Connection testing is automated via the /v1/sources/check_connection endpoint to verify credentials and network connectivity before deployment. The skill generates complete sync configurations including namespace mapping, cursor field selection for incremental syncs, and primary key definitions for deduplication. It also produces Airbyte Terraform provider configurations for infrastructure-as-code deployments.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/airbyte-connector-config-generator/)
