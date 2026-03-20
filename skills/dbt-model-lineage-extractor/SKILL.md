---
name: dbt Model Lineage Extractor
description: Parses dbt project manifests and extracts full model lineage graphs using the dbt Core Python API and manifest.json. Identifies orphaned models, circular dependencies, and models missing tests using the dbt Graph API. Outputs a lineage report and optionally pushes graph data to Atlan or DataHub via their REST APIs.
category: Data Extraction &amp; Transformation
framework: Any Agent
verification: verified_metadata
rating: 4.7
reviews: 54
source: https://agentskillexchange.com/skill/dbt-model-lineage-extractor/
---

# dbt Model Lineage Extractor

Parses dbt project manifests and extracts full model lineage graphs using the dbt Core Python API and manifest.json. Identifies orphaned models, circular dependencies, and models missing tests using the dbt Graph API. Outputs a lineage report and optionally pushes graph data to Atlan or DataHub via their REST APIs.

## Overview

Parses dbt project manifests and extracts full model lineage graphs using the dbt Core Python API and manifest.json. Identifies orphaned models, circular dependencies, and models missing tests using the dbt Graph API. Outputs a lineage report and optionally pushes graph data to Atlan or DataHub via their REST APIs.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill dbt-model-lineage-extractor
```

### OpenClaw

```bash
clawhub install dbt-model-lineage-extractor
```

### Claude Code

```bash
claude mcp add dbt-model-lineage-extractor
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/dbt-model-lineage-extractor/) for detailed installation instructions.

## Verification

- **Status**: verified_metadata
- **Category**: Data Extraction &amp; Transformation
- **Framework**: Any Agent
- **Rating**: 4.7/5 (54 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/dbt-model-lineage-extractor/)
