---
name: "Capture live transcripts and searchable meeting memory for agents with Minutes"
slug: "capture-live-transcripts-and-searchable-meeting-memory-for-agents-with-minutes"
description: "Stream meeting transcripts into searchable conversation memory so agents can read live or post-meeting context before drafting follow-ups or taking action."
github_stars: 1051
verification: "security_reviewed"
source: "https://github.com/silverstein/minutes"
author: "Mat Silverstein"
publisher_type: "individual"
category: "Media & Transcription"
framework: "MCP"
tool_ecosystem:
  github_repo: "silverstein/minutes"
  github_stars: 1051
  npm_package: "minutes-mcp"
  npm_weekly_downloads: 3196
---

# Capture live transcripts and searchable meeting memory for agents with Minutes

Stream meeting transcripts into searchable conversation memory so agents can read live or post-meeting context before drafting follow-ups or taking action.

## Prerequisites

Minutes app or service, minutes-mcp package, microphone or meeting audio source

## Installation

Use the upstream install or setup path that matches your environment:
- brew install --cask silverstein/tap/minutes
- brew tap silverstein/tap && brew install minutes
- cargo install minutes-cli # macOS/Linux
- cargo install minutes-cli --no-default-features # Windows (see install notes below)

Requirements and caveats from upstream:
- # Any platform — from source (requires Rust + cmake; Windows also needs LLVM)
- # Or use Mistral API (requires MISTRAL_API_KEY)

Basic usage or getting-started notes:
- Agents have run logs. Humans have conversations. **minutes** captures the human side — the decisions, the intent, the context that agents need but can't observe — and makes it queryable.
- bash
- # macOS — Desktop app (menu bar, recording UI, AI assistant)

- Source: https://github.com/silverstein/minutes
- Extracted from upstream docs: https://raw.githubusercontent.com/silverstein/minutes/HEAD/README.md

## Documentation

- https://useminutes.app

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/capture-live-transcripts-and-searchable-meeting-memory-for-agents-with-minutes/)
