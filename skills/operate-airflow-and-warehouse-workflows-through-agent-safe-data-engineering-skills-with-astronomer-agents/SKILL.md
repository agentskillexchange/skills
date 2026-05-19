---
name: "Operate Airflow and warehouse workflows through agent-safe data engineering skills with Astronomer Agents"
slug: "operate-airflow-and-warehouse-workflows-through-agent-safe-data-engineering-skills-with-astronomer-agents"
description: "Give agents structured Airflow, lineage, dbt, and warehouse workflows through installable skills and an Airflow MCP surface instead of loose shell access."
github_stars: 337
verification: "security_reviewed"
source: "https://github.com/astronomer/agents"
author: "Astronomer"
publisher_type: "organization"
category: "Data Extraction & Transformation"
framework: "MCP"
tool_ecosystem:
  github_repo: "astronomer/agents"
  github_stars: 337
---

# Operate Airflow and warehouse workflows through agent-safe data engineering skills with Astronomer Agents

Give agents structured Airflow, lineage, dbt, and warehouse workflows through installable skills and an Airflow MCP surface instead of loose shell access.

## Prerequisites

Python or uvx, Airflow 2.x or 3.x REST API access or Astro project, optional data warehouse credentials, MCP-compatible client or supported coding agent

## Installation

Use the upstream install or setup path that matches your environment:
- npx skills add astronomer/agents --skill '*'
- npx skills add astronomer/agents --skill '*' -a cursor
- For open-source Airflow, use Docker Compose for local dev and the Helm chart for production (see deploying-airflow) instead of Astro setup skills.
- git clone https://github.com/astronomer/agents.git

Requirements and caveats from upstream:
- | [deploying-airflow](./skills/deploying-airflow/) | Deploy Airflow DAGs and projects (Astro, Docker Compose, Kubernetes) |
- The account field requires your Snowflake **account identifier** (e.g., orgname-accountname or xy12345.us-east-1), not your account name. Find this in your Snowflake console under Admin > Accounts.

Basic usage or getting-started notes:
- <!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
- [Quick Start](#quick-start)
- [Usage](#usage)

- Source: https://github.com/astronomer/agents
- Extracted from upstream docs: https://raw.githubusercontent.com/astronomer/agents/HEAD/README.md

## Documentation

- https://github.com/astronomer/agents

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/operate-airflow-and-warehouse-workflows-through-agent-safe-data-engineering-skills-with-astronomer-agents/)
