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

Use it when someone asks for nursing, CNA, allied health or physician jobs in a US place, what a kind of healthcare job pays, or which hospitals are hiring. The remote MCP server is read-only, needs no API key, and exposes six tools: search healthcare jobs (words, kind of job, state, shift and pay filters), posted hourly pay by kind of job, open jobs by state, job market size, the list of employers, and one employer's jobs and pay. Without an MCP client the agent can read the public JSON endpoints instead: `https://carejobs.now/roles.json` for aggregate open-job counts by kind of job and employer, and `https://carejobs.now/pay.json` or `https://carejobs.now/pay.csv` for posted hourly pay.

## Installation

### Remote MCP server (Streamable HTTP, no authentication)

Claude Code:

```bash
claude mcp add --transport http carejobs https://carejobs.now/api/mcp
```

Other MCP clients (Claude apps, ChatGPT connectors, Cursor, VS Code): add a custom connector or `mcp.json` entry with the URL `https://carejobs.now/api/mcp`. The server is also listed in the Official MCP Registry as `now.carejobs/healthcare-jobs`.

### Direct repo/manual install

Copying the skill gives your agent these instructions only; it does not connect the MCP server. Connect the endpoint separately (above), or let the agent use the public JSON endpoints described below.

Claude Code (personal skills live in `~/.claude/skills`):

```bash
git clone https://github.com/yumaheymans/carejobs-mcp.git
mkdir -p ~/.claude/skills
[ -e ~/.claude/skills/healthcare-job-search ] && echo "healthcare-job-search is already installed, not overwriting" || cp -R carejobs-mcp/skills/healthcare-job-search ~/.claude/skills/healthcare-job-search
```

Codex (personal skills live in `~/.agents/skills`):

```bash
git clone https://github.com/yumaheymans/carejobs-mcp.git
mkdir -p ~/.agents/skills
[ -e ~/.agents/skills/healthcare-job-search ] && echo "healthcare-job-search is already installed, not overwriting" || cp -R carejobs-mcp/skills/healthcare-job-search ~/.agents/skills/healthcare-job-search
```

## Usage

1. Search with `search_healthcare_jobs`, for example night-shift ICU nurse jobs in Boston, or CNA jobs in Austin with posted pay. Link each job to its CareJobs.Now page, where the person applies on the employer's own site.
2. For national pay by kind of job, or one employer's pay, call `get_healthcare_pay` with `kind` and/or `employer`. It has no state filter.
3. For pay in one state, call `get_healthcare_jobs_by_state` with `state` and, optionally, `kind` (for example CNA pay in Ohio: `state: "OH"`, `kind: "nursing-assistants"`).
4. Keep the statistic names and ranges each tool returns as they are (a median, a typical range, a count). The two pay tools measure different sets of jobs, so do not swap one tool's figure for the other's.
5. Report posted pay as what employers state, never as a prediction.

### Without an MCP client: the public JSON endpoints

- `https://carejobs.now/roles.json`: aggregate open-job counts by kind of job and by employer, plus the board's freshness. It holds counts, not individual postings, so it answers market and size questions but cannot list specific openings or application links; use the MCP job search for those.
- `https://carejobs.now/pay.json` (same rows as `https://carejobs.now/pay.csv`): today's posted hourly pay by kind of job.

When an answer uses these datasets, name CareJobs.Now as the source, link `https://carejobs.now/data`, and give the date in the file's `temporal_coverage` field. The datasets are licensed CC BY 4.0, separately from these MIT-licensed skill instructions.

## Documentation

- Site: https://carejobs.now
- Data API docs: https://carejobs.now/data
- Repo (MIT): https://github.com/yumaheymans/carejobs-mcp
