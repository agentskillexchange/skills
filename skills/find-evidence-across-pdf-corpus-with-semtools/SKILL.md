---
name: "Find evidence across a PDF corpus with Semtools"
slug: "find-evidence-across-pdf-corpus-with-semtools"
description: "Parse a selected PDF batch, search the cached Markdown locally, and return an agent answer backed by inspected passages and explicit coverage limits."
github_stars: 1888
verification: "security_reviewed"
source: "https://github.com/run-llama/semtools"
author: "run-llama"
publisher_type: "organization"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "run-llama/semtools"
  github_stars: 1888
  npm_package: "@llamaindex/semtools"
  npm_weekly_downloads: 146
---

# Find evidence across a PDF corpus with Semtools

Parse a selected PDF batch, search the cached Markdown locally, and return an agent answer backed by inspected passages and explicit coverage limits.

## Prerequisites

Terminal-capable agent, Semtools CLI, LlamaParse API key for parsing; Node.js/npm for npm installation, Rust/Cargo if a prebuilt binary is unavailable

## Installation

Install or set up from the source-backed instructions:

Install with npm install -g @llamaindex/semtools@3.0.1 and verify semtools --help. Upstream also supports cargo install semtools. Configure LLAMA_CLOUD_API_KEY through the environment for the default cloud parsing backend. Obtain authorization for document upload and parsing charges before semtools parse. Search only the returned Markdown paths with semtools search; search is local. Follow the upstream coding-agent guide to provide the CLI usage instructions to your agent.

- Source: https://github.com/run-llama/semtools

## Documentation

- https://github.com/run-llama/semtools/blob/main/examples/use_with_coding_agents.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/find-evidence-across-pdf-corpus-with-semtools/)
