---
name: "Run private RAG and MCP skill workspaces with Yuxi"
slug: "run-private-rag-and-mcp-skill-workspaces-with-yuxi"
description: "Deploy Yuxi when an agent team needs a private, multi-tenant knowledge workspace that combines document RAG, knowledge graphs, MCP tools, skills, sandboxes, and permissions."
github_stars: 7036
verification: "security_reviewed"
source: "https://github.com/xerrors/Yuxi"
author: "xerrors"
publisher_type: "individual"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "xerrors/Yuxi"
  github_stars: 7036
---

# Run private RAG and MCP skill workspaces with Yuxi

Deploy Yuxi when an agent team needs a private, multi-tenant knowledge workspace that combines document RAG, knowledge graphs, MCP tools, skills, sandboxes, and permissions.

## Prerequisites

Docker Engine, Docker Compose, LLM API key, PostgreSQL, Redis, MinIO, Milvus, Neo4j

## Installation

Install or set up from the source-backed instructions:

Clone the repository at the documented release branch, run the initialization script to create environment settings and secrets, start the stack with docker compose up --build -d, confirm readiness at /api/system/ready, then open the local web app and initialize the administrator account.

- Source: https://github.com/xerrors/Yuxi

## Documentation

- https://xerrors.github.io/Yuxi/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-private-rag-and-mcp-skill-workspaces-with-yuxi/)
