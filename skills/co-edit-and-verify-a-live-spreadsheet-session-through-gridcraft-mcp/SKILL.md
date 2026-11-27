---
name: "Co-edit and verify a live spreadsheet session through GridCraft MCP"
slug: "co-edit-and-verify-a-live-spreadsheet-session-through-gridcraft-mcp"
description: "Connect an agent to the GridCraft workbook open on a user’s desktop, make scoped edits, and return formula readbacks plus a screenshot for review."
github_stars: 6208
verification: "security_reviewed"
source: "https://github.com/storytold/gridcraft"
author: "ArtCraft team (storytold)"
publisher_type: "organization"
category: "Data Extraction & Transformation"
framework: "MCP"
tool_ecosystem:
  github_repo: "storytold/gridcraft"
  github_stars: 6208
---

# Co-edit and verify a live spreadsheet session through GridCraft MCP

Connect an agent to the GridCraft workbook open on a user’s desktop, make scoped edits, and return formula readbacks plus a screenshot for review.

## Prerequisites

GridCraft desktop, gridcraft-cli, local stdio MCP client, workbook copy and output path; Rust/Cargo for source builds

## Installation

Install or set up from the source-backed instructions:

Obtain the matching desktop and CLI builds from the official GitHub release and verify the supplied checksums. Alternatively clone https://github.com/storytold/gridcraft.git, check out reviewed revision a1c84547e3485606a5d8b6fab07dd3a072aa6c52, and follow the README source-build prerequisites: cargo install --path apps/gridcraft-cli; launch the desktop with cargo run --release -p gridcraft -- --control 7979. Open a workbook copy, then configure the MCP client command gridcraft-cli with args ["mcp", "--connect", "7979"]. Confirm inspect_workbook identifies the intended session before editing.

- Source: https://github.com/storytold/gridcraft

## Documentation

- https://github.com/storytold/gridcraft/blob/a1c84547e3485606a5d8b6fab07dd3a072aa6c52/docs/mcp.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/co-edit-and-verify-a-live-spreadsheet-session-through-gridcraft-mcp/)
