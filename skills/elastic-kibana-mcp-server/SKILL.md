---
name: "Elastic / Kibana MCP Server"
description: "Use this skill when you need to query Elasticsearch indices, search logs in Kibana, or analyze data stored in the Elastic Stack via AI. It allows agents to run KQL or Lucene queries, retrieve log data, and investigate application events without direct Kibana access."
category: "Monitoring & Alerts"
framework: "MCP-compatible"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/elastic-kibana-mcp-server/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "elasticsearch"  # from ase_tool_match
  github_stars: 76387  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 1893773  # from ase_npm_downloads
  github_repo: "elastic/elasticsearch"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Elastic / Kibana MCP Server

Use this skill when you need to query Elasticsearch indices, search logs in Kibana, or analyze data stored in the Elastic Stack via AI. It allows agents to run KQL or Lucene queries, retrieve log data, and investigate application events without direct Kibana access.

## Overview

Use this skill when you need to query Elasticsearch indices, search logs in Kibana, or analyze data stored in the Elastic Stack via AI. It allows agents to run KQL or Lucene queries, retrieve log data, and investigate application events without direct Kibana access.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill elastic-kibana-mcp-server
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill elastic-kibana-mcp-server -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill elastic-kibana-mcp-server -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill elastic-kibana-mcp-server -a codex
```

### OpenClaw

```bash
clawhub install elastic-kibana-mcp-server
```

## Source

- Marketplace: https://agentskillexchange.com/skills/elastic-kibana-mcp-server/
