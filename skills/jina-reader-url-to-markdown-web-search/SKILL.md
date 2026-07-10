---
name: "Jina Reader URL-to-Markdown Converter and Web Search API"
slug: "jina-reader-url-to-markdown-web-search"
description: "Jina Reader converts any URL to LLM-friendly markdown by prefixing https://r.jina.ai/ to any web address. It also provides a search endpoint at https://s.jina.ai/ that returns web search results in clean markdown format for RAG and agent workflows."
github_stars: 10559
verification: "security_reviewed"
source: "https://github.com/jina-ai/reader"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "jina-ai/reader"
  github_stars: 10559
---

# Jina Reader URL-to-Markdown Converter and Web Search API

Jina Reader converts any URL to LLM-friendly markdown by prefixing https://r.jina.ai/ to any web address. It also provides a search endpoint at https://s.jina.ai/ that returns web search results in clean markdown format for RAG and agent workflows.

## Installation

Use the upstream install or setup path that matches your environment:
- docker pull ghcr.io/jina-ai/reader:oss
- docker run --rm -p 3000:8081 ghcr.io/jina-ai/reader:oss
- docker run --rm -p 3000:8080 -p 3001:8081 ghcr.io/jina-ai/reader:oss
- docker run --rm -p 3000:8081 \

Requirements and caveats from upstream:
- ## Self-host with Docker
- Docker *(optional — only if you want a local MinIO bucket cache)*

Basic usage or getting-started notes:
- **2026-04** — Re-synchronized the open source branch with the SaaS code. The MongoDB-backed storage layer is stripped; the oss branch runs in stateless mode out of the box, with optional MinIO/S3-compatible bucket cac...
- **2025-03** — Major refactor: Reader is no longer a Firebase application. The SaaS migrated off Firestore + Cloud Functions to a Cloud Run image with MongoDB Atlas, removing the platform-coupled bits and unblocking th...
- ### Using r.jina.ai for single URL fetching

- Source: https://github.com/jina-ai/reader
- Extracted from upstream docs: https://raw.githubusercontent.com/jina-ai/reader/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jina-reader-url-to-markdown-web-search/)
