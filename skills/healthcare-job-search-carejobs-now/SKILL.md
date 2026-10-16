---
name: "Healthcare Job Search (US) with CareJobs.Now"
slug: "healthcare-job-search-carejobs-now"
description: "Lets an agent find open US healthcare jobs and the hourly pay employers post, through the free CareJobs.Now remote MCP server or its public JSON endpoints. Covers nursing, CNA, allied health, therapy, imaging, pharmacy and physician jobs, with filters for kind of job, state, shift and pay, plus posted pay by job kind and open jobs per employer and state."
verification: "listed"
source: "https://github.com/yumaheymans/carejobs-mcp/tree/main/skills/healthcare-job-search"
license: "MIT"
author: "CareJobs.Now"
category: "Library & API Reference"
framework: "MCP"
---

# Healthcare Job Search (US) with CareJobs.Now

CareJobs.Now is a free US healthcare job board that reads the career sites of hundreds of hospitals, health systems, clinic groups and care companies every day, with more than 170,000 open jobs and the pay each employer posts. This skill teaches an agent to answer healthcare job and pay questions from that data, and to always give the person a link to the job page where they apply on the employer's own site.

Use it when someone asks for nursing, CNA, allied health or physician jobs in a US place, what a kind of healthcare job pays, or which hospitals are hiring. The remote MCP server is read-only, needs no API key, and exposes six tools: search healthcare jobs (words, kind of job, state, shift and pay filters), posted hourly pay by kind of job, open jobs by state, job market size, the list of employers, and one employer's jobs and pay. Without an MCP client the agent can read the public JSON endpoints instead: `roles.json` for open jobs by kind and employer, and `pay.json` or `pay.csv` for posted hourly pay.

## Installation

### Remote MCP server (Streamable HTTP, no authentication)

Claude Code:

```bash
claude mcp add --transport http carejobs https://carejobs.now/api/mcp
```

Other MCP clients (Claude apps, ChatGPT connectors, Cursor, VS Code): add a custom connector or `mcp.json` entry with the URL `https://carejobs.now/api/mcp`. The server is also listed in the Official MCP Registry as `now.carejobs/healthcare-jobs`.

### Direct repo/manual install

```bash
git clone https://github.com/yumaheymans/carejobs-mcp.git
cp -R carejobs-mcp/skills/healthcare-job-search ~/.agent-skills/healthcare-job-search
```

## Usage

1. Search with the job-search tool, for example night-shift ICU nurse jobs in Boston, or CNA jobs in Austin with posted pay.
2. Ask the pay tool for the median and typical posted hourly range of a kind of job, optionally within a state.
3. Report posted pay as what employers state, never as a prediction, and link each job to its CareJobs.Now page.

## Documentation

- Site: https://carejobs.now
- Data API docs: https://carejobs.now/data
- Repo (MIT): https://github.com/yumaheymans/carejobs-mcp
