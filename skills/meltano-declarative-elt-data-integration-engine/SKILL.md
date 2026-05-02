---
title: "Meltano Declarative ELT Data Integration Engine"
description: "Meltano is an open-source, CLI-first ELT platform built on the Singer specification. It provides declarative, code-first data integration with 600+ connectors through Singer taps and targets, orchestrating data movement from APIs, databases, and files to warehouses and lakes."
verification: "security_reviewed"
source: "https://github.com/meltano/meltano"
category:
  - "Data Extraction & Transformation"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "meltano/meltano"
  github_stars: 2403
---

# Meltano Declarative ELT Data Integration Engine

Meltano (github.com/meltano/meltano) is an open-source, declarative data integration engine maintained by an active community. It follows the Singer specification for data extraction and loading, which standardizes how data connectors (called taps and targets) exchange data through a well-defined JSON protocol over stdout/stdin.

The platform provides a CLI that manages the full lifecycle of data pipelines: initializing projects, adding and configuring plugins, running extraction and loading jobs, and scheduling pipeline executions. Meltano projects are defined through a meltano.yml configuration file that specifies which taps (data sources) and targets (destinations) to use, along with their configuration parameters. This code-first approach means entire pipeline definitions can be version-controlled, reviewed, and deployed through standard Git workflows.

The Meltano Hub (hub.meltano.com) serves as the central registry for discovering connectors. It hosts hundreds of Singer taps and targets covering APIs like Salesforce, Stripe, and GitHub, databases like PostgreSQL, MySQL, and MongoDB, and file formats like CSV and Parquet. When a connector is not available, the Meltano Singer SDK provides a Python framework for building custom taps and targets with minimal boilerplate code.

Meltano handles plugin isolation through separate Python virtual environments for each connector, preventing dependency conflicts between different taps and targets. It provides Docker images (slim and full variants) for containerized deployment, and supports integration with dbt for data transformation, making it a complete ELT solution. The engine also includes built-in job scheduling, state management for incremental replication, and catalog-based schema selection.

Available on PyPI and Docker Hub, Meltano is licensed under MIT and backed by a community of over 2,500 data professionals on Slack. It represents a shift toward declarative, GitOps-style data integration where pipelines are defined as code rather than configured through visual interfaces.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/meltano-declarative-elt-data-integration-engine/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/meltano-declarative-elt-data-integration-engine
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/meltano-declarative-elt-data-integration-engine`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/meltano-declarative-elt-data-integration-engine/)
