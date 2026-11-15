---
name: "Operate Kubernetes and OpenShift clusters through MCP"
slug: "operate-kubernetes-and-openshift-clusters-through-mcp"
description: "Expose Kubernetes and OpenShift cluster operations to MCP clients with native API-backed tools for resources, pods, events, Helm, Tekton, and diagnostics."
github_stars: 1607
verification: "security_reviewed"
source: "https://github.com/containers/kubernetes-mcp-server"
author: "containers"
publisher_type: "organization"
category: "Runbooks & Diagnostics"
framework: "MCP"
tool_ecosystem:
  github_repo: "containers/kubernetes-mcp-server"
  github_stars: 1607
  npm_package: "kubernetes-mcp-server"
  npm_weekly_downloads: 7270
---

# Operate Kubernetes and OpenShift clusters through MCP

Expose Kubernetes and OpenShift cluster operations to MCP clients with native API-backed tools for resources, pods, events, Helm, Tekton, and diagnostics.

## Prerequisites

Access to a Kubernetes or OpenShift cluster, kubeconfig or in-cluster configuration, MCP-compatible client, optional npm, Python, Docker, or native binary install path

## Installation

Use the upstream install or setup path that matches your environment:
- npx kubernetes-mcp-server@latest --help
- make build
- npx @modelcontextprotocol/inspector@latest $(pwd)/kubernetes-mcp-server

Requirements and caveats from upstream:
- If you're using the native binaries you don't need to have Node or Python installed on your system.
- **✅ Cross-Platform**: Available as a native binary for Linux, macOS, and Windows, as well as an npm package, a Python package, and container/Docker image.
- # Run the Kubernetes MCP server using npx (in case you have npm and node installed)

Basic usage or getting-started notes:
- [✨ Features](#features) | [🚀 Getting Started](#getting-started) | [🎥 Demos](#demos) | [⚙️ Configuration](#configuration) | [🛠️ Tools](#tools-and-functionalities) | [💬 Community](#community) | [🧑‍💻 Development](#develo...
- **Top** gets resource usage metrics for all pods or a specific pod in the specified namespace.
- **Exec** into a pod and run a command.

- Source: https://github.com/containers/kubernetes-mcp-server
- Extracted from upstream docs: https://raw.githubusercontent.com/containers/kubernetes-mcp-server/HEAD/README.md

## Documentation

- https://github.com/containers/kubernetes-mcp-server

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/operate-kubernetes-and-openshift-clusters-through-mcp/)
