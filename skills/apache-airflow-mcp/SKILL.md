---
name: "Apache Airflow MCP"
description: "Expose Apache Airflow DAGs, task logs, and run history to AI agents via MCP, enabling conversational DAG management and troubleshooting. Agents can trigger DAG runs, inspect task states, and retrieve XCom values without direct Airflow UI access."
category: "Data Extraction & Transformation"
framework: "MCP-compatible"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/apache-airflow-mcp/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "airflow"  # from ase_tool_match
  github_stars: 44767  # from ase_github_stars (integer, not string)
  github_repo: "apache/airflow"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Apache Airflow MCP

Expose Apache Airflow DAGs, task logs, and run history to AI agents via MCP, enabling conversational DAG management and troubleshooting. Agents can trigger DAG runs, inspect task states, and retrieve XCom values without direct Airflow UI access.

## Overview

Expose Apache Airflow DAGs, task logs, and run history to AI agents via MCP, enabling conversational DAG management and troubleshooting. Agents can trigger DAG runs, inspect task states, and retrieve XCom values without direct Airflow UI access.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill apache-airflow-mcp
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill apache-airflow-mcp -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill apache-airflow-mcp -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill apache-airflow-mcp -a codex
```

### OpenClaw

```bash
clawhub install apache-airflow-mcp
```

## Source

- Marketplace: https://agentskillexchange.com/skills/apache-airflow-mcp/
