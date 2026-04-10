---
name: Dozzle Real-Time Docker Container Log Viewer
description: Dozzle is a lightweight, web-based real-time log viewer for Docker containers.
  It supports Docker standalone, Swarm mode, and Kubernetes, provides fuzzy search,
  regex and SQL log queries, multi-host agent mode, and split-screen log viewing —
  all in a 7 MB container.
verification: security_reviewed
source: https://github.com/amir20/dozzle
category:
- Monitoring &amp; Alerts
framework:
- Multi-Framework
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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dozzle-docker-log-viewer/)
