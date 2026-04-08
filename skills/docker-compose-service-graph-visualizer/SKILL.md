---
title: Docker Compose Service Graph Visualizer
description: The Docker Compose Service Graph Visualizer skill transforms docker-compose.yml
  files into interactive visual dependency graphs. Using PyYAML for YAML parsing and
  Graphviz (via pygraphviz) for graph layout, it creates comprehensive views of multi-service
  architectures. Each service node displays its image, exposed ports, resource limits,
  and health check configuration. Edges represent depends_on relationships with condition
  annotations (service_started, service_healthy, service_completed_successfully).
  Network topology is rendered as subgraph clusters, showing which services share
  networks and their internal DNS names. Volume mounts are displayed as shared storage
  nodes connecting dependent services. The D3.js interactive mode enables pan, zoom,
  click-to-inspect service details, and real-time status overlay when connected to
  a running Docker daemon via the Docker SDK for Python. Additional features include
  diff mode (compare two compose files to visualize architecture changes), merge mode
  (overlay multiple compose files as they would resolve with extends and override),
  and export to SVG, PNG, or Mermaid diagram syntax for embedding in documentation.
  Supports Compose v2 and v3 specification formats with full extension field handling.
verification: security_reviewed
source: https://github.com/docker/compose
category:
- Developer Tools
framework:
- Claude Code
- Multi-Framework
tool_ecosystem:
  github_repo: docker/compose
  github_stars: 37211
---

# Docker Compose Service Graph Visualizer

The Docker Compose Service Graph Visualizer skill transforms docker-compose.yml files into interactive visual dependency graphs. Using PyYAML for YAML parsing and Graphviz (via pygraphviz) for graph layout, it creates comprehensive views of multi-service architectures. Each service node displays its image, exposed ports, resource limits, and health check configuration. Edges represent depends_on relationships with condition annotations (service_started, service_healthy, service_completed_successfully). Network topology is rendered as subgraph clusters, showing which services share networks and their internal DNS names. Volume mounts are displayed as shared storage nodes connecting dependent services. The D3.js interactive mode enables pan, zoom, click-to-inspect service details, and real-time status overlay when connected to a running Docker daemon via the Docker SDK for Python. Additional features include diff mode (compare two compose files to visualize architecture changes), merge mode (overlay multiple compose files as they would resolve with extends and override), and export to SVG, PNG, or Mermaid diagram syntax for embedding in documentation. Supports Compose v2 and v3 specification formats with full extension field handling.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-compose-service-graph-visualizer/)
