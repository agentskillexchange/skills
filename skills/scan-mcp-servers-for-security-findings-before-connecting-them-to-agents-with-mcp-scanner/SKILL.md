---
name: "Scan MCP servers for security findings before connecting them to agents with MCP Scanner"
slug: "scan-mcp-servers-for-security-findings-before-connecting-them-to-agents-with-mcp-scanner"
description: "Run MCP Scanner against a remote or local MCP server before trusting it, so the agent gets a bounded security review of tools, prompts, resources, dependencies, and supply-chain risk."
github_stars: 889
verification: "security_reviewed"
source: "https://github.com/cisco-ai-defense/mcp-scanner"
author: "Cisco AI Defense"
publisher_type: "open_source_project"
category: "Security & Verification"
framework: "MCP"
tool_ecosystem:
  github_repo: "cisco-ai-defense/mcp-scanner"
  github_stars: 889
---

# Scan MCP servers for security findings before connecting them to agents with MCP Scanner

Run MCP Scanner against a remote or local MCP server before trusting it, so the agent gets a bounded security review of tools, prompts, resources, dependencies, and supply-chain risk.

## Prerequisites

Python 3.11+, uv, optional Cisco AI Defense API key, optional LLM provider key, optional VirusTotal API key

## Installation

Use the upstream install or setup path that matches your environment:
- uv tool install --python 3.13 cisco-ai-mcp-scanner
- uv tool install --python 3.13 --from git+https://github.com/cisco-ai-defense/mcp-scanner cisco-ai-mcp-scanner
- git clone https://github.com/cisco-ai-defense/mcp-scanner
- uv sync --python 3.13

Requirements and caveats from upstream:
- [![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
- A Python tool for scanning MCP (Model Context Protocol) servers and tools for potential security findings. The MCP Scanner combines Cisco AI Defense inspect API, YARA rules and LLM-as-a-judge to detect malicious MCP t...
- **Vulnerable Packages Scanning**: Scan Python dependencies for known vulnerabilities (CVE/PYSEC/GHSA) using pip-audit integration.

Basic usage or getting-started notes:
- **Multiple Modes:** Run scanner as a stand-alone CLI tool or REST API server
- A valid Cisco AI Defense API Key (optional)
- LLM Provider API Key (optional)

- Source: https://github.com/cisco-ai-defense/mcp-scanner
- Extracted from upstream docs: https://raw.githubusercontent.com/cisco-ai-defense/mcp-scanner/HEAD/README.md

## Documentation

- https://blogs.cisco.com/ai/securing-the-ai-agent-supply-chain-with-ciscos-open-source-mcp-scanner

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-mcp-servers-for-security-findings-before-connecting-them-to-agents-with-mcp-scanner/)
