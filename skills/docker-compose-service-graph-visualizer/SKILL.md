---
title: "Docker Compose Service Graph Visualizer"
description: "Parses docker-compose.yml files using PyYAML and generates interactive dependency graphs with Graphviz and D3.js. Shows port mappings, volume mounts, network topology, and health check status."
slug: "docker-compose-service-graph-visualizer"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/docker/compose"
tool_ecosystem:
  github_repo: "docker/compose"
  github_stars: 37227
---

# Docker Compose Service Graph Visualizer

Parses docker-compose.yml files using PyYAML and generates interactive dependency graphs with Graphviz and D3.js. Shows port mappings, volume mounts, network topology, and health check status.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install docker-compose-service-graph-visualizer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Docker Compose Service Graph Visualizer skill transforms docker-compose.yml files into interactive visual dependency graphs. Using PyYAML for YAML parsing and Graphviz (via pygraphviz) for graph layout, it creates comprehensive views of multi-service architectures. Each service node displays its image, exposed ports, resource limits, and health check configuration. Edges represent depends_on relationships with condition annotations (service_started, service_healthy, service_completed_successfully). Network topology is rendered as subgraph clusters, showing which services share networks and their internal DNS names. Volume mounts are displayed as shared storage nodes connecting dependent services. The D3.js interactive mode enables pan, zoom, click-to-inspect service details, and real-time status overlay when connected to a running Docker daemon via the Docker SDK for Python. Additional features include diff mode (compare two compose files to visualize architecture changes), merge mode (overlay multiple compose files as they would resolve with extends and override), and export to SVG, PNG, or Mermaid diagram syntax for embedding in documentation. Supports Compose v2 and v3 specification formats with full extension field handling.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-compose-service-graph-visualizer/)
