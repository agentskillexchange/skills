---
title: "Dagster Data Pipeline Orchestrator"
description: "Orchestrate data pipelines using Dagster, the cloud-native data orchestration platform. Define data assets as Python functions with automatic lineage tracking, scheduling, and observability."
verification: security_reviewed
source: "https://github.com/dagster-io/dagster"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Claude Code"
  - "OpenClaw"
tool_ecosystem:
  github_repo: "dagster-io/dagster"
  github_stars: 15257
---

# Dagster Data Pipeline Orchestrator

The Dagster Data Pipeline Orchestrator skill integrates Dagster, the open-source data orchestration platform with over 15,000 GitHub stars, into AI agent workflows for building, scheduling, and monitoring data pipelines. Dagster uses a declarative, asset-based programming model where data assets (tables, models, reports) are defined as Python functions with explicit dependencies.

This skill enables agents to define data pipelines where each step produces a named data asset. Dagster automatically infers the dependency graph between assets, tracks data lineage, and provides a web UI (Dagster UI, formerly Dagit) for visualization and monitoring. Agents can create pipelines that extract from APIs, transform data, load into warehouses, train ML models, and generate reports — all with built-in retry logic, partitioning, and scheduling.

The core workflow involves defining assets using the @asset decorator in Python. Each asset function declares its upstream dependencies as parameters, and Dagster resolves the execution order automatically. Agents can trigger materializations (running the pipeline to update assets), check asset health, inspect run logs, and configure schedules and sensors that react to external events.

Dagster provides a rich integration library covering major data tools: dbt for SQL transformations, Spark and Polars for data processing, Snowflake and BigQuery and Postgres for storage, Airbyte and Fivetran for ingestion, and AWS/GCP/Azure for cloud infrastructure. The framework also supports partitioned assets for incremental processing and software-defined assets for declarative data management.

Key outputs include materialized data assets, run logs with detailed step timings and metadata, asset lineage graphs, and observability metrics. Available on PyPI as dagster, licensed under Apache 2.0, with official Docker images and Helm charts for Kubernetes deployment.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dagster-data-pipeline-orchestrator/)
