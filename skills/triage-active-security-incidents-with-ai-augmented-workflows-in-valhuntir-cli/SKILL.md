---
name: "Triage active security incidents with AI-augmented workflows in Valhuntir CLI"
slug: "triage-active-security-incidents-with-ai-augmented-workflows-in-valhuntir-cli"
description: "Guide live digital-forensics and incident-response work with human approval gates when the job is evidence review and triage, not general MCP setup."
github_stars: 40
verification: "security_reviewed"
source: "https://github.com/AppliedIR/Valhuntir"
author: "AppliedIR"
publisher_type: "GitHub repository"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "AppliedIR/Valhuntir"
  github_stars: 40
---

# Triage active security incidents with AI-augmented workflows in Valhuntir CLI

Guide live digital-forensics and incident-response work with human approval gates when the job is evidence review and triage, not general MCP setup.

## Prerequisites

Valhuntir CLI and gateway components, forensic artifacts, and an MCP-compatible local client under human analyst control

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/AppliedIR/sift-mcp.git && cd sift-mcp
- git clone https://github.com/AppliedIR/wintools-mcp.git; cd wintools-mcp
- git clone https://github.com/AppliedIR/sift-mcp.git

Requirements and caveats from upstream:
- OSD["OpenSearch<br/>Docker :9200"]
- The **Examiner Portal** (vhir portal) is the primary review interface — an 8-tab browser UI where examiners review, edit, approve, and reject findings and timeline events. The Commit button requires the examiner's pas...
- | OpenSearch | SIFT (Docker) | 9200 | Evidence search engine. Local or remote. Optional. |

Basic usage or getting-started notes:
- Valhuntir is **LLM client agnostic** — connect any locally installed MCP-compatible client through the gateway. Supported clients include Claude Code, Claude Desktop, Cherry Studio, self-hosted LibreChat, and any clie...
- With [opensearch-mcp](https://github.com/AppliedIR/opensearch-mcp), evidence is parsed programmatically and indexed into OpenSearch, giving the LLM 17 purpose-built query tools instead of consuming billions of tokens...
- | **Valhuntir + OpenSearch** | Above + evidence indexing | 32 GB | 32 GB | 100 GB + evidence/extractions/indices | OpenSearch JVM 6 GB, container 8 GB. Can run on separate host. |

- Source: https://github.com/AppliedIR/Valhuntir
- Extracted from upstream docs: https://raw.githubusercontent.com/AppliedIR/Valhuntir/HEAD/README.md

## Documentation

- https://github.com/AppliedIR/Valhuntir#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/triage-active-security-incidents-with-ai-augmented-workflows-in-valhuntir-cli/)
