---
name: Airbyte Connector Config Generator
description: Generates Airbyte source and destination connector configurations using
  the Airbyte API /v1/sources/create and /v1/destinations/create endpoints. Validates
  connection specs against the Airbyte Protocol.
verification: security_reviewed
source: https://agentskillexchange.com/skills/airbyte-connector-config-generator/
category:
- Data Extraction &amp; Transformation
framework:
- Cursor
---
# Airbyte Connector Config Generator

The Airbyte Connector Config Generator automates the creation of source and destination connector configurations for the Airbyte data integration platform. It uses the Airbyte API /v1/source_definitions/get_for_workspace endpoint to fetch available connector specifications and generates valid configuration JSON based on the connector spec schema. The generator validates configurations against the Airbyte Protocol specification, ensuring proper authentication credentials, sync mode settings, and stream selections. It supports the /v1/sources/create and /v1/destinations/create API endpoints for programmatic connector provisioning. Connection testing is automated via the /v1/sources/check_connection endpoint to verify credentials and network connectivity before deployment. The skill generates complete sync configurations including namespace mapping, cursor field selection for incremental syncs, and primary key definitions for deduplication. It also produces Airbyte Terraform provider configurations for infrastructure-as-code deployments.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/airbyte-connector-config-generator/)
