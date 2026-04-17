---
title: "Dozzle Real-Time Docker Container Log Viewer"
description: "Overview\nDozzle is a lightweight, open-source application for monitoring Docker container logs in real time through a clean web interface. Written in Go with a Vue.js frontend, the entire application ships as a 7 MB compressed Docker image. Dozzle does not store any log files — it is designed purely for live log streaming and analysis, making it complementary to full-featured log aggregation platforms.\nKey Features\nDozzle provides intelligent fuzzy search for container names, regex-based log search, and a unique SQL query engine for structured log analysis. It offers split-screen viewing for monitoring multiple containers simultaneously, live CPU and memory stats overlays, dark mode, and multi-user authentication with forward proxy authorization support. The interface includes log level highlighting and automatic JSON formatting.\nDocker Swarm and Multi-Host Support\nDozzle runs natively in Docker Swarm mode as a global service, providing unified log access across all swarm nodes. For non-Swarm setups, the agent mode allows monitoring multiple Docker hosts from a single Dozzle instance. Each remote host runs Dozzle in agent mode on port 7007, and the main instance aggregates logs from all connected agents.\nAgent Integration Points\nAgents can deploy Dozzle via Docker CLI or Docker Compose to instantly gain log visibility across containerized environments. The simple deployment command (docker run -v /var/run/docker.sock:/var/run/docker.sock -p 8080:8080 amir20/dozzle:latest) makes it trivially automatable. Dozzle also works with Podman and Colima through automatic API negotiation, extending its usefulness across container runtimes.\nUse Cases\nReal-time debugging of containerized applications, monitoring deployment rollouts, tracking error patterns across microservices, quick log inspection during incident response, and providing development teams with lightweight log access without the overhead of a full ELK or Loki stack. With over 12,000 GitHub stars, Dozzle is widely trusted in the self-hosting community."
verification: security_reviewed
source: "https://github.com/amir20/dozzle"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "amir20/dozzle"
  github_stars: 12360
---

# Dozzle Real-Time Docker Container Log Viewer

Overview
Dozzle is a lightweight, open-source application for monitoring Docker container logs in real time through a clean web interface. Written in Go with a Vue.js frontend, the entire application ships as a 7 MB compressed Docker image. Dozzle does not store any log files — it is designed purely for live log streaming and analysis, making it complementary to full-featured log aggregation platforms.
Key Features
Dozzle provides intelligent fuzzy search for container names, regex-based log search, and a unique SQL query engine for structured log analysis. It offers split-screen viewing for monitoring multiple containers simultaneously, live CPU and memory stats overlays, dark mode, and multi-user authentication with forward proxy authorization support. The interface includes log level highlighting and automatic JSON formatting.
Docker Swarm and Multi-Host Support
Dozzle runs natively in Docker Swarm mode as a global service, providing unified log access across all swarm nodes. For non-Swarm setups, the agent mode allows monitoring multiple Docker hosts from a single Dozzle instance. Each remote host runs Dozzle in agent mode on port 7007, and the main instance aggregates logs from all connected agents.
Agent Integration Points
Agents can deploy Dozzle via Docker CLI or Docker Compose to instantly gain log visibility across containerized environments. The simple deployment command (docker run -v /var/run/docker.sock:/var/run/docker.sock -p 8080:8080 amir20/dozzle:latest) makes it trivially automatable. Dozzle also works with Podman and Colima through automatic API negotiation, extending its usefulness across container runtimes.
Use Cases
Real-time debugging of containerized applications, monitoring deployment rollouts, tracking error patterns across microservices, quick log inspection during incident response, and providing development teams with lightweight log access without the overhead of a full ELK or Loki stack. With over 12,000 GitHub stars, Dozzle is widely trusted in the self-hosting community.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/dozzle-docker-log-viewer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/dozzle-docker-log-viewer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dozzle-docker-log-viewer/)
