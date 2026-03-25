---
name: "Airbyte Connector Config Generator"
description: "Generates Airbyte source and destination connector configurations using the Airbyte API /v1/sources/create and /v1/destinations/create endpoints. Validates connection specs against the Airbyte Protocol."
category: "Data Extraction & Transformation"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/airbyte-connector-config-generator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "terraform"  # from ase_tool_match
  github_stars: 48003  # from ase_github_stars (integer, not string)
  github_repo: "hashicorp/terraform"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Airbyte Connector Config Generator

Generates Airbyte source and destination connector configurations using the Airbyte API /v1/sources/create and /v1/destinations/create endpoints. Validates connection specs against the Airbyte Protocol.

## Overview

The Airbyte Connector Config Generator automates the creation of source and destination connector configurations for the Airbyte data integration platform. It uses the Airbyte API /v1/source_definitions/get_for_workspace endpoint to fetch available connector specifications and generates valid configuration JSON based on the connector spec schema. The generator validates configurations against the Airbyte Protocol specification, ensuring proper authentication credentials, sync mode settings, and stream selections. It supports the /v1/sources/create and /v1/destinations/create API endpoints for programmatic connector provisioning. Connection testing is automated via the /v1/sources/check_connection endpoint to verify credentials and network connectivity before deployment. The skill generates complete sync configurations including namespace mapping, cursor field selection for incremental syncs, and primary key definitions for deduplication. It also produces Airbyte Terraform provider configurations for infrastructure-as-code deployments.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill airbyte-connector-config-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill airbyte-connector-config-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill airbyte-connector-config-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill airbyte-connector-config-generator -a codex
```

### OpenClaw

```bash
clawhub install airbyte-connector-config-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/airbyte-connector-config-generator/
