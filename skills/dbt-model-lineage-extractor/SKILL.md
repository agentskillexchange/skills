---
name: "dbt Model Lineage Extractor"
description: "Parses dbt project manifests and extracts full model lineage graphs using the dbt Core Python API and manifest.json. Identifies orphaned models, circular dependencies, and models missing tests using the dbt Graph API. Outputs a lineage report and optionally pushes graph data to Atlan or DataHub via their REST APIs."
category: "Data Extraction & Transformation"
framework: "Claude Code"
verification: verified_metadata
rating: 4.7
reviews: 54
creator: "David Kim"
creator_handle: "@dkim"
creator_verified: false
source: "https://agentskillexchange.com/skills/dbt-model-lineage-extractor/"
---
# dbt Model Lineage Extractor

Parses dbt project manifests and extracts full model lineage graphs using the dbt Core Python API and manifest.json. Identifies orphaned models, circular dependencies, and models missing tests using the dbt Graph API. Outputs a lineage report and optionally pushes graph data to Atlan or DataHub via their REST APIs.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill dbt-model-lineage-extractor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill dbt-model-lineage-extractor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill dbt-model-lineage-extractor -a cursor
```

### OpenClaw

```bash
clawhub install dbt-model-lineage-extractor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill dbt-model-lineage-extractor -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Data Extraction & Transformation |
| Framework | Claude Code |
| Verification | Verified Metadata |
| Rating | 4.7/5 (54 reviews) |

## Creator

**David Kim**
- Profile: [@dkim](https://agentskillexchange.com/browse-skills/?creator=dkim)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-model-lineage-extractor/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
