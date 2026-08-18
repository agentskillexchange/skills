---
name: "Run local document RAG with citations over MCP using Haiku.RAG"
slug: "run-local-document-rag-with-citations-over-mcp-using-haiku-rag"
description: "Index local or self-hosted documents, search them with hybrid and multimodal retrieval, and answer agent questions through an MCP server with citations."
github_stars: 581
verification: "security_reviewed"
source: "https://github.com/ggozad/haiku.rag"
author: "Yiorgis Gozadinos"
publisher_type: "individual"
category: "Data Extraction & Transformation"
framework: "MCP"
tool_ecosystem:
  github_repo: "ggozad/haiku.rag"
  github_stars: 581
---

# Run local document RAG with citations over MCP using Haiku.RAG

Index local or self-hosted documents, search them with hybrid and multimodal retrieval, and answer agent questions through an MCP server with citations.

## Prerequisites

Python 3.12+, haiku.rag or haiku.rag-slim, an embedding provider such as Ollama/OpenAI/VoyageAI/Cohere/LM Studio/vLLM, and an MCP-compatible client

## Installation

Install or set up from the source-backed instructions:

Install with `pip install haiku.rag` or `uv pip install haiku.rag`, index documents with commands such as `haiku-rag add-src paper.pdf`, then expose the knowledge base to an MCP client with `haiku-rag mcp --stdio`. Use `haiku-rag --read-only mcp --stdio` when the agent should only search and ask questions.

- Source: https://github.com/ggozad/haiku.rag

## Documentation

- https://ggozad.github.io/haiku.rag/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-local-document-rag-with-citations-over-mcp-using-haiku-rag/)
