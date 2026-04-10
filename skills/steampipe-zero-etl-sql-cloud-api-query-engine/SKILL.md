---
title: "Steampipe Zero-ETL SQL Cloud API Query Engine"
description: "Query cloud APIs, SaaS services, and infrastructure with standard SQL using Steampipe. Maps over 150 data sources (AWS, Azure, GCP, GitHub, Slack, and more) to PostgreSQL tables — no ETL pipelines needed."
slug: "steampipe-zero-etl-sql-cloud-api-query-engine"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://github.com/turbot/steampipe"
tool_ecosystem:
  github_repo: "turbot/steampipe"
  github_stars: 7745
---

# Steampipe Zero-ETL SQL Cloud API Query Engine

Query cloud APIs, SaaS services, and infrastructure with standard SQL using Steampipe. Maps over 150 data sources (AWS, Azure, GCP, GitHub, Slack, and more) to PostgreSQL tables — no ETL pipelines needed.

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
clawhub install steampipe-zero-etl-sql-cloud-api-query-engine
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Steampipe from Turbot is an open-source tool that lets you query cloud APIs and services using standard SQL. It exposes APIs as PostgreSQL foreign tables, so you can run SELECT queries against live data from AWS, Azure, GCP, Kubernetes, GitHub, Slack, Jira, and 150+ other services without building ETL pipelines or managing data warehouses.
Under the hood, Steampipe bundles an embedded PostgreSQL instance and translates your SQL queries into API calls in real time. Each data source is handled by a plugin that defines the available tables and columns. For example, the AWS plugin provides tables like aws_s3_bucket, aws_ec2_instance, and aws_iam_user, each mapping directly to the corresponding AWS API. Queries are parallelized and cached for performance, delivering results faster than most hand-written API scripts.
The plugin ecosystem covers major cloud providers, developer platforms (GitHub, GitLab, Bitbucket), communication tools (Slack, Microsoft Teams), security services (Shodan, VirusTotal), DNS providers, and more. Community-contributed plugins extend coverage to niche APIs. Steampipe also ships as SQLite extensions and Postgres FDWs, so you can embed its query capabilities in existing database workflows.
This skill lets agents run SQL queries against live cloud infrastructure and service APIs. Agents can audit AWS IAM policies, inventory Kubernetes resources, check GitHub repository settings, correlate data across multiple cloud providers in a single query with JOINs, and generate compliance reports. The skill outputs query results as structured tables that can be further processed or rendered as reports.
Steampipe integrates with Grafana for dashboards, works in CI/CD for policy-as-code checks (via Steampipe mods), and supports multi-account/multi-region queries. It is distributed as a single binary installable via Homebrew on macOS or a curl-based installer on Linux. The project is actively maintained under the AGPL-3.0 license with 7,700+ GitHub stars.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/steampipe-zero-etl-sql-cloud-api-query-engine/)
