---
name: "Review SQL Server execution plans through an MCP-compatible analysis workflow with Performance Studio"
slug: "review-sql-server-execution-plans-through-an-mcp-compatible-analysis-workflow-with-performance-studio"
description: "Use Performance Studio when an MCP-compatible agent needs to parse SQL Server .sqlplan files, surface performance warnings, inspect missing-index suggestions, and turn execution-plan evidence into a reviewable tuning workflow."
github_stars: 175
verification: "security_reviewed"
source: "https://github.com/erikdarlingdata/PerformanceStudio"
author: "Erik Darling Data"
publisher_type: "company"
category: "Runbooks & Diagnostics"
framework: "MCP"
tool_ecosystem:
  github_repo: "erikdarlingdata/PerformanceStudio"
  github_stars: 175
---

# Review SQL Server execution plans through an MCP-compatible analysis workflow with Performance Studio

Use Performance Studio when an MCP-compatible agent needs to parse SQL Server .sqlplan files, surface performance warnings, inspect missing-index suggestions, and turn execution-plan evidence into a reviewable tuning workflow.

## Prerequisites

Performance Studio via its built-in MCP server or CLI, plus SQL Server execution plan files or a reachable SQL Server environment.

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/erikdarlingdata/PerformanceStudio.git
- docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=YourPassword123" \

Requirements and caveats from upstream:
- Each warning includes severity (Info, Warning, or Critical), the operator node ID, and enough context to act on immediately.
- Docker (optional — macOS/Linux users can run SQL Server locally via Docker)
- [Critical] Parallelism (Node 0): Estimated 1 rows, actual 2,889 (2889x underestimated).

Basic usage or getting-started notes:
- **Missing indexes** — extracts SQL Server's index suggestions with ready-to-run CREATE statements
- [.NET 8 SDK](https://dotnet.microsoft.com/download/dotnet/8.0) (required to build and run)
- SQL Server instance (optional — only needed for live plan capture; file analysis works without one)

- Source: https://github.com/erikdarlingdata/PerformanceStudio
- Extracted from upstream docs: https://raw.githubusercontent.com/erikdarlingdata/PerformanceStudio/HEAD/README.md

## Documentation

- https://github.com/erikdarlingdata/PerformanceStudio

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/review-sql-server-execution-plans-through-an-mcp-compatible-analysis-workflow-with-performance-studio/)
