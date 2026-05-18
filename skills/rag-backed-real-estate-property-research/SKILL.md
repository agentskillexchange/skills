---
name: "Research real estate properties with RAG-backed market analysis"
slug: "rag-backed-real-estate-property-research"
description: "Guide an agent through property search, buyer/renter preference capture, and evidence-backed shortlist notes from structured listing data."
github_stars: 170
verification: "security_reviewed"
source: "https://github.com/AleksNeStu/ai-real-estate-assistant"
author: "AleksNeStu"
publisher_type: "individual"
category: "Research & Scraping"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "AleksNeStu/ai-real-estate-assistant"
  github_stars: 170
---

# Research real estate properties with RAG-backed market analysis

Guide an agent through property search, buyer/renter preference capture, and evidence-backed shortlist notes from structured listing data.

## Prerequisites

Python 3.11+, Streamlit, LangChain, OpenAI GPT or Llama model access, Pandas, FastEmbed, DocArrayInMemorySearch or ChromaDB, Poetry

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/AleksNeStu/ai-real-estate-assistant.git
- docker compose -f deploy/compose/docker-compose.yml up --build
- uv pip install -e ".[dev]" && python -m uvicorn api.main:app --reload --port 8000

Requirements and caveats from upstream:
- [![Python](https://img.shields.io/badge/Python-3.12+-blue?style=flat&logo=python&logoColor=white)](https://python.org)
- **Note:** The demo uses simulated AI responses for instant exploration. Production deployment requires API keys.
- | **Lines of Code** | 60,000+ (27K Python + 34K TypeScript) |

Basic usage or getting-started notes:
- [Quick Start](#-quick-start)
- <img src="docs/screenshots/usage.png" alt="Usage statistics dashboard" width="320" style="border-radius: 8px;" />
- <p><strong>Usage Dashboard</strong></p>

- Source: https://github.com/AleksNeStu/ai-real-estate-assistant
- Extracted from upstream docs: https://raw.githubusercontent.com/AleksNeStu/ai-real-estate-assistant/HEAD/README.md

## Documentation

- https://github.com/AleksNeStu/ai-real-estate-assistant/blob/main/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rag-backed-real-estate-property-research/)
