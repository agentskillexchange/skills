---
title: "Run self-hosted media research and RAG workflows with tldw_server"
description: "Use tldw_server when an agent workflow needs to ingest video, audio, documents, and web pages into a local research layer with RAG, evals, OpenAI-compatible APIs, and MCP access."
verification: "security_reviewed"
source: "https://github.com/rmusser01/tldw_server"
author: "rmusser01"
publisher_type: "independent_open_source"
category:
  - "Research & Scraping"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "rmusser01/tldw_server"
  github_stars: 1410
---

# Run self-hosted media research and RAG workflows with tldw_server

Use tldw_server when an agent workflow needs to ingest video, audio, documents, and web pages into a local research layer with RAG, evals, OpenAI-compatible APIs, and MCP access.

## Prerequisites

Python 3.10+, ffmpeg, Docker or local Python setup, tldw_server, optional LLM/STT/TTS providers, optional MCP client

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Follow the upstream Start Here guide. Run the prerequisite check, choose the Docker single-user or local single-user profile, configure authentication and provider settings, start the FastAPI service, verify the health endpoint, and test ingestion plus retrieval before connecting MCP clients.
```

## Documentation

- https://tldwproject.com

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-self-hosted-media-research-and-rag-workflows-with-tldw-server/)
