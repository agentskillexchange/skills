---
name: "Extract reviewable relationship timelines from chat exports with Afterglow"
slug: "extract-relationship-timelines-from-chat-exports-with-afterglow"
description: "Analyze supplied chat exports into resumable JSON and Markdown relationship timelines, with block coverage and skipped-input diagnostics."
github_stars: 317
verification: "security_reviewed"
source: "https://github.com/kldhsh123/Afterglow"
author: "Afterglow Contributors"
publisher_type: "community"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "kldhsh123/Afterglow"
  github_stars: 317
---

# Extract reviewable relationship timelines from chat exports with Afterglow

Analyze supplied chat exports into resumable JSON and Markdown relationship timelines, with block coverage and skipped-input diagnostics.

## Prerequisites

Git, Python 3.12.x, uv, Afterglow xuwen CLI, configured analysis block/final model endpoints, authorized chat export files

## Installation

Install or set up from the source-backed instructions:

Install Python 3.12.x, uv and Git. Clone https://github.com/kldhsh123/Afterglow, enter Afterglow/backend, and run uv sync --extra dev. Follow the upstream configuration guide to configure the analysis block and final model endpoints/credentials in backend/.env; empty ANALYSIS_* settings fall back to the main chat model. Use local endpoints for both stages if offline processing is required. Supply authorized chat exports for one target person. From backend/, inspect the selection with uv run xuwen analyze chat.json --list-blocks --language en, then run uv run xuwen analyze chat.json --timeline-only --language en. No companion server or automatic messaging is needed for this CLI workflow.

- Source: https://github.com/kldhsh123/Afterglow

## Documentation

- https://kldhsh123.github.io/Afterglow/en/advanced.html

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/extract-relationship-timelines-from-chat-exports-with-afterglow/)
