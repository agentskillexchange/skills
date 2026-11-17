---
name: "Search repository files by behavior with Localix decide"
slug: "search-repository-files-by-behavior-with-localix-decide"
description: "Narrow repository paths with ripgrep, classify each candidate with llx decide, and inspect matching or uncertain files before returning a source-grounded handoff."
github_stars: 368
verification: "security_reviewed"
source: "https://github.com/localixai/localix-cli"
author: "Localix Lab"
publisher_type: "community"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "localixai/localix-cli"
  github_stars: 368
---

# Search repository files by behavior with Localix decide

Narrow repository paths with ripgrep, classify each candidate with llx decide, and inspect matching or uncertain files before returning a source-grounded handoff.

## Prerequisites

Localix llx CLI, ripgrep, shell, OpenRouter API key; macOS or Linux

## Installation

Install or set up from the source-backed instructions:

Install the native llx binary using the upstream installation guide at https://github.com/localixai/localix-cli/blob/main/docs/install.md; the current release is v0.6.1. The documented Rust alternative is cargo install --locked --git https://github.com/localixai/localix-cli localix-cli (requires Rust 1.89 or later). Ensure llx and rg are on PATH. Supply OPENROUTER_API_KEY through the host credential environment, then run llx decide --check and llx decide --help. Optionally install the upstream agent skill with npx skills add localixai/localix-cli. No browser sign-in is needed for this decision workflow.

- Source: https://github.com/localixai/localix-cli

## Documentation

- https://github.com/localixai/localix-cli/blob/main/docs/agents.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/search-repository-files-by-behavior-with-localix-decide/)
