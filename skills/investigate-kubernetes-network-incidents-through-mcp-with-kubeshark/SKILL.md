---
name: "Investigate Kubernetes network incidents through MCP with Kubeshark"
slug: "investigate-kubernetes-network-incidents-through-mcp-with-kubeshark"
description: "Query live and historical Kubernetes network traffic through Kubeshark's MCP server when an agent needs packet-level evidence, API payloads, or service-path traces for incident response."
github_stars: 11873
verification: "listed"
source: "https://github.com/kubeshark/kubeshark"
author: "Kubeshark"
publisher_type: "organization"
category: "Monitoring & Alerts"
framework: "MCP"
tool_ecosystem:
  github_repo: "kubeshark/kubeshark"
  github_stars: 11873
---

# Investigate Kubernetes network incidents through MCP with Kubeshark

Query live and historical Kubernetes network traffic through Kubeshark's MCP server when an agent needs packet-level evidence, API payloads, or service-path traces for incident response.

## Prerequisites

Kubeshark deployed in the target Kubernetes cluster and an MCP-compatible client

## Installation

Use the upstream install or setup path that matches your environment:
- brew install kubeshark

Requirements and caveats from upstream:
- <a href="https://hub.docker.com/r/kubeshark/worker"><img alt="Docker pulls" src="https://img.shields.io/docker/pulls/kubeshark/worker?color=%23099cec&logo=Docker&style=flat-square"></a>

Basic usage or getting-started notes:
- A visual map of how workloads communicate, showing dependencies, traffic volume, and protocol usage across the cluster.
- | Method | Command |
- |--------|---------|

- Source: https://github.com/kubeshark/kubeshark
- Extracted from upstream docs: https://raw.githubusercontent.com/kubeshark/kubeshark/HEAD/README.md

## Documentation

- https://docs.kubeshark.com/en/mcp

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/investigate-kubernetes-network-incidents-through-mcp-with-kubeshark/)
