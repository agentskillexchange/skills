---
name: "Docker Compose Service Graph Visualizer"
description: "Parses docker-compose.yml files using PyYAML and generates interactive dependency graphs with Graphviz and D3.js. Shows port mappings, volume mounts, network topology, and health check status."
category: "Developer Tools"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/docker-compose-service-graph-visualizer/"
---
# Docker Compose Service Graph Visualizer

Parses docker-compose.yml files using PyYAML and generates interactive dependency graphs with Graphviz and D3.js. Shows port mappings, volume mounts, network topology, and health check status.

The Docker Compose Service Graph Visualizer skill transforms docker-compose.yml files into interactive visual dependency graphs. Using PyYAML for YAML parsing and Graphviz (via pygraphviz) for graph layout, it creates comprehensive views of multi-service architectures. Each service node displays its image, exposed ports, resource limits, and health check configuration. Edges represent depends_on relationships with condition annotations (service_started, service_healthy, service_completed_successfully). Network topology is rendered as subgraph clusters, showing which services share networks and their internal DNS names. Volume mounts are displayed as shared storage nodes connecting dependent services. The D3.js interactive mode enables pan, zoom, click-to-inspect service details, and real-time status overlay when connected to a running Docker daemon via the Docker SDK for Python. Additional features include diff mode (compare two compose files to visualize architecture changes), merge mode (overlay multiple compose files as they would resolve with extends and override), and export to SVG, PNG, or Mermaid diagram syntax for embedding in documentation. Supports Compose v2 and v3 specification formats with full extension field handling.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill docker-compose-service-graph-visualizer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill docker-compose-service-graph-visualizer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill docker-compose-service-graph-visualizer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill docker-compose-service-graph-visualizer -a codex
```

### OpenClaw

```bash
clawhub install docker-compose-service-graph-visualizer
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-compose-service-graph-visualizer/)
