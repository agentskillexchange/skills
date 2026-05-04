---
title: "Operate Airflow and warehouse workflows through agent-safe data engineering skills with Astronomer Agents"
description: "Give agents structured Airflow, lineage, dbt, and warehouse workflows through installable skills and an Airflow MCP surface instead of loose shell access."
verification: "listed"
source: "https://github.com/astronomer/agents"
author: "Astronomer"
publisher_type: "organization"
category:
  - "Data Extraction & Transformation"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "astronomer/agents"
  github_stars: 337
---

# Operate Airflow and warehouse workflows through agent-safe data engineering skills with Astronomer Agents

Give agents structured Airflow, lineage, dbt, and warehouse workflows through installable skills and an Airflow MCP surface instead of loose shell access.

## Prerequisites

Python or uvx, Airflow 2.x or 3.x REST API access or Astro project, optional data warehouse credentials, MCP-compatible client or supported coding agent

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the skills with `npx skills add astronomer/agents --skill '*'` for a supported coding agent, or run the Airflow MCP server with `uvx astro-airflow-mcp --transport stdio` and configure it in your MCP client.
```

## Documentation

- https://github.com/astronomer/agents

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/operate-airflow-and-warehouse-workflows-through-agent-safe-data-engineering-skills-with-astronomer-agents/)
