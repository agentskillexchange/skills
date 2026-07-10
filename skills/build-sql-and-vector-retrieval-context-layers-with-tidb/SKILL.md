---
title: "Build SQL and vector retrieval context layers with TiDB"
description: "Use TiDB when an agent needs one transactional SQL store that can also hold embeddings and serve vector retrieval for RAG, memory, or app-context workflows."
verification: "listed"
source: "https://github.com/pingcap/tidb"
author: "PingCAP"
publisher_type: "organization"
category:
  - "Data Extraction & Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "pingcap/tidb"
  github_stars: 40235
---

# Build SQL and vector retrieval context layers with TiDB

Use TiDB when an agent needs one transactional SQL store that can also hold embeddings and serve vector retrieval for RAG, memory, or app-context workflows.

## Prerequisites

TiDB or TiDB Cloud, an embedding model, SQL client or application connector, source documents or application records

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Use TiDB Cloud Serverless for the shortest setup path, or install a local TiDB test cluster with the current TiUP instructions from PingCAP's documentation. Create vector columns for embeddings, load source rows, add vector indexes where appropriate, and query with SQL filters plus vector similarity functions from the TiDB vector search docs.
```

## Documentation

- https://docs.pingcap.com/tidb/stable/vector-search-overview/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-sql-and-vector-retrieval-context-layers-with-tidb/)
