---
name: "Dagster Data Pipeline Orchestrator"
description: "Orchestrate data pipelines using Dagster, the cloud-native data orchestration platform. Define data assets as Python functions with automatic lineage tracking, scheduling, and observability."
category: "Data Extraction & Transformation"
framework: "Claude Code"
verification: listed  # security_reviewed or listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/dagster-data-pipeline-orchestrator/"
---

# Dagster Data Pipeline Orchestrator

The Dagster Data Pipeline Orchestrator skill integrates Dagster, the open-source data orchestration platform with over 15,000 GitHub stars, into AI agent workflows for building, scheduling, and monitoring data pipelines. Dagster uses a declarative, asset-based programming model where data assets (tables, models, reports) are defined as Python functions with explicit dependencies.
This skill enables agents to define data pipelines where each step produces a named data asset. Dagster automatically infers the dependency graph between assets, tracks data lineage, and provides a web UI (Dagster UI, formerly Dagit) for visualization and monitoring. Agents can create pipelines that extract from APIs, transform data, load into warehouses, train ML models, and generate reports — all with built-in retry logic, partitioning, and scheduling.
The core workflow involves defining assets using the @asset decorator in Python. Each asset function declares its upstream dependencies as parameters, and Dagster resolves the execution order automatically. Agents can trigger materializations (running the pipeline to update assets), check asset health, inspect run logs, and configure schedules and sensors that react to external events.
Dagster provides a rich integration library covering major data tools: dbt for SQL transformations, Spark and Polars for data processing, Snowflake and BigQuery and Postgres for storage, Airbyte and Fivetran for ingestion, and AWS/GCP/Azure for cloud infrastructure. The framework also supports partitioned assets for incremental processing and software-defined assets for declarative data management.
Key outputs include materialized data assets, run logs with detailed step timings and metadata, asset lineage graphs, and observability metrics. Available on PyPI as dagster, licensed under Apache 2.0, with official Docker images and Helm charts for Kubernetes deployment.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill dagster-data-pipeline-orchestrator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill dagster-data-pipeline-orchestrator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill dagster-data-pipeline-orchestrator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill dagster-data-pipeline-orchestrator -a codex
```

### OpenClaw

```bash
clawhub install dagster-data-pipeline-orchestrator
```
