---
name: "Reconcile OmniGet Download Receipts and Diagnose Failed Jobs over MCP"
slug: "reconcile-omniget-download-receipts-and-diagnose-failed-jobs-over-mcp"
description: "Turn an explicit media URL batch into per-job completion evidence and a bounded failure handoff through OmniGet’s local MCP server."
github_stars: 14505
verification: "security_reviewed"
source: "https://github.com/tonhowtf/omniget"
author: "tonhowtf"
publisher_type: "community"
category: "Media & Transcription"
framework: "MCP"
tool_ecosystem:
  github_repo: "tonhowtf/omniget"
  github_stars: 14505
---

# Reconcile OmniGet Download Receipts and Diagnose Failed Jobs over MCP

Turn an explicit media URL batch into per-job completion evidence and a bounded failure handoff through OmniGet’s local MCP server.

## Prerequisites

OmniGet desktop app; an HTTP MCP client; local connection token; built-in download engine

## Installation

Install or set up from the source-backed instructions:

Download the appropriate release from https://getomniget.com/download or https://github.com/tonhowtf/omniget/releases and verify its published SHA-256. Open OmniGet, create a connection under Settings → AI & agents → Connect to other apps, and use the generated MCP configuration. Default URL: http://127.0.0.1:47720/mcp; retain the private token locally. Restart the MCP client and inspect its available download tools.

- Source: https://github.com/tonhowtf/omniget

## Documentation

- https://github.com/tonhowtf/omniget/blob/main/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/reconcile-omniget-download-receipts-and-diagnose-failed-jobs-over-mcp/)
