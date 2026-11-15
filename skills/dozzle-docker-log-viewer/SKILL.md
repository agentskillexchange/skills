---
name: "Dozzle Real-Time Docker Container Log Viewer"
slug: "dozzle-docker-log-viewer"
description: "Dozzle is a lightweight, web-based real-time log viewer for Docker containers. It supports Docker standalone, Swarm mode, and Kubernetes, provides fuzzy search, regex and SQL log queries, multi-host agent mode, and split-screen log viewing — all in a 7 MB container."
github_stars: 12360
verification: "security_reviewed"
source: "https://github.com/amir20/dozzle"
author: "Amir Raminfar"
category: "Monitoring & Alerts"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "amir20/dozzle"
  github_stars: 12360
---

# Dozzle Real-Time Docker Container Log Viewer

Dozzle is a lightweight, web-based real-time log viewer for Docker containers. It supports Docker standalone, Swarm mode, and Kubernetes, provides fuzzy search, regex and SQL log queries, multi-host agent mode, and split-screen log viewing — all in a 7 MB container.

## Installation

Use the upstream install or setup path that matches your environment:
- $ docker pull amir20/dozzle:latest
- $ docker run --name dozzle -d --volume=/var/run/docker.sock:/var/run/docker.sock -v dozzle_data:/data -p 8080:8080 amir20/dozzle:latest
- $ docker service create --name dozzle --env DOZZLE_MODE=swarm --mode global --mount type=bind,source=/var/run/docker.sock,target=/var/run/docker.sock -p 8080:8080 amir20/dozzle:latest
- $ docker run -v /var/run/docker.sock:/var/run/docker.sock -p 7007:7007 amir20/dozzle:latest agent

Requirements and caveats from upstream:
- Dozzle is a lightweight, web-based application for monitoring Docker logs in real time. It doesn't store any log files—it's designed purely for live log viewing.
- [![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/amir20/dozzle)](https://hub.docker.com/r/amir20/dozzle/)
- [![Docker Pulls](https://img.shields.io/docker/pulls/amir20/dozzle.svg)](https://hub.docker.com/r/amir20/dozzle/)

Basic usage or getting-started notes:
- Live stats with memory and CPU usage
- Dozzle is a small container (7 MB compressed). Pull the latest release with:
- ### Running Dozzle

- Source: https://github.com/amir20/dozzle
- Extracted from upstream docs: https://raw.githubusercontent.com/amir20/dozzle/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dozzle-docker-log-viewer/)
