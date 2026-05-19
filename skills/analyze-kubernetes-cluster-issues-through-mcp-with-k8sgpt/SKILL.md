---
name: "Analyze Kubernetes cluster issues through MCP with K8sGPT"
slug: "analyze-kubernetes-cluster-issues-through-mcp-with-k8sgpt"
description: "Run K8sGPT as an MCP server so an agent can scan a Kubernetes cluster, explain unhealthy resources, and return prioritized remediation clues in natural language."
github_stars: 7687
verification: "security_reviewed"
source: "https://github.com/k8sgpt-ai/k8sgpt"
author: "K8sGPT Authors"
publisher_type: "organization"
category: "Runbooks & Diagnostics"
framework: "MCP"
tool_ecosystem:
  github_repo: "k8sgpt-ai/k8sgpt"
  github_stars: 7687
---

# Analyze Kubernetes cluster issues through MCP with K8sGPT

Run K8sGPT as an MCP server so an agent can scan a Kubernetes cluster, explain unhealthy resources, and return prioritized remediation clues in natural language.

## Prerequisites

A reachable Kubernetes cluster, K8sGPT, and an MCP-compatible client

## Installation

Use the upstream install or setup path that matches your environment:
- brew install k8sgpt
- brew tap k8sgpt-ai/k8sgpt
- built from the source. k8sgpt Install Clang or run brew install gcc.

Requirements and caveats from upstream:
- K8sGPT can be integrated with Claude Desktop to provide AI-powered Kubernetes cluster analysis. This integration requires K8sGPT v0.4.14 or later.
- Analyzer Node took 160.109833ms
- Node

Basic usage or getting-started notes:
- [Quick Start](#quick-start)
- If you install gcc as suggested, the problem will persist. Therefore, you need to install the build-essential package.
- Currently, the default AI provider is OpenAI, you will need to generate an API key from [OpenAI](https://openai.com)

- Source: https://github.com/k8sgpt-ai/k8sgpt
- Extracted from upstream docs: https://raw.githubusercontent.com/k8sgpt-ai/k8sgpt/HEAD/README.md

## Documentation

- https://docs.k8sgpt.ai/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/analyze-kubernetes-cluster-issues-through-mcp-with-k8sgpt/)
