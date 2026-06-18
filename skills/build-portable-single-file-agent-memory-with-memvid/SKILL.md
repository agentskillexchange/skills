---
name: "Build portable single-file agent memory with Memvid"
slug: "build-portable-single-file-agent-memory-with-memvid"
description: "Use Memvid when an agent needs local, portable long-term memory and retrieval without running a vector database or full RAG service."
github_stars: 15668
verification: "security_reviewed"
source: "https://github.com/memvid/memvid"
author: "memvid"
publisher_type: "organization"
category: "Integrations & Connectors"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "memvid/memvid"
  github_stars: 15668
  npm_package: "@memvid/sdk"
  npm_weekly_downloads: 3996
---

# Build portable single-file agent memory with Memvid

Use Memvid when an agent needs local, portable long-term memory and retrieval without running a vector database or full RAG service.

## Prerequisites

Memvid CLI or SDK; optional local embedding model files for local vector search

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/memvid/memvid.git
- cargo build
- cargo build --release
- cargo build --release --features "lex,vec,temporal_track"

Requirements and caveats from upstream:
- | **Node.js SDK** | npm install @memvid/sdk | [![npm](https://img.shields.io/npm/v/@memvid/sdk?style=flat-square)](https://www.npmjs.com/package/@memvid/sdk) |
- | **Python SDK** | pip install memvid-sdk | [![PyPI](https://img.shields.io/pypi/v/memvid-sdk?style=flat-square)](https://pypi.org/project/memvid-sdk/) |
- Image search using CLIP embeddings (requires clip feature):

Basic usage or getting-started notes:
- MEMVID_WHISPER_MODEL=whisper-tiny-en-q8k cargo run --example test_whisper --features whisper -- audio.mp3
- Download the default BGE-small model (384 dimensions, fast and efficient):

- Source: https://github.com/memvid/memvid
- Extracted from upstream docs: https://raw.githubusercontent.com/memvid/memvid/HEAD/README.md

## Documentation

- https://docs.memvid.com

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-portable-single-file-agent-memory-with-memvid/)
