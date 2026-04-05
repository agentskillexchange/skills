---
name: "Great Expectations Data Validation Pipeline"
description: "Validate data quality using the Great Expectations Python library. Define expectations as unit tests for your data, run validation suites, and generate human-readable data quality reports."
category: "Code Quality & Review"
framework: "Claude Code"
verification: security_reviewed
source: "https://github.com/great-expectations/great_expectations"
tool_ecosystem:
  tool: pagerduty
  github_repo: great-expectations/great_expectations
  github_stars: 11321
---
# Great Expectations Data Validation Pipeline

Validate data quality using the Great Expectations Python library. Define expectations as unit tests for your data, run validation suites, and generate human-readable data quality reports.

## Overview

The Great Expectations Data Validation Pipeline skill uses Great Expectations (GX), the open-source Python framework with over 11,000 GitHub stars, to bring rigorous data quality testing to AI agent workflows. Great Expectations lets you define “expectations” — declarative assertions about what your data should look like — and then validate real data against those expectations.

This skill enables agents to set up data validation pipelines that catch data quality issues before they propagate through downstream systems. Agents can create expectation suites that check column types, value ranges, null rates, uniqueness, referential integrity, distribution shapes, and custom business rules. Each expectation is a testable statement like “this column should never be null” or “values should be between 0 and 100.”

The workflow proceeds in three phases. First, the agent connects to a data source — this could be a Pandas DataFrame, a SQL database (PostgreSQL, Snowflake, BigQuery, Redshift, Databricks, and more), or a Spark DataFrame. Second, the agent defines or loads an expectation suite, either by profiling existing data to auto-generate expectations or by specifying custom expectations. Third, the agent runs validation and inspects the results.

Great Expectations produces rich validation output including pass/fail status per expectation, observed values, unexpected values counts and samples, and success percentages. The framework also generates “Data Docs” — auto-generated HTML documentation of your data quality results that can be served locally or pushed to cloud storage.

Integration points include dbt for post-transformation validation, Airflow and Dagster for orchestrating validation checkpoints in data pipelines, and Slack or PagerDuty for alerting on validation failures. Available on PyPI as the `great-expectations` package, licensed under Apache 2.0.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill great-expectations-data-validation-pipeline
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill great-expectations-data-validation-pipeline -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill great-expectations-data-validation-pipeline -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill great-expectations-data-validation-pipeline -a codex
```

### OpenClaw

```bash
clawhub install great-expectations-data-validation-pipeline
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/great-expectations-data-validation-pipeline/)
