---
name: "Checkmate Open Source Uptime and Infrastructure Monitoring"
slug: "checkmate-open-source-uptime-infrastructure-monitoring"
description: "An ASE skill built on Checkmate, the open source self-hosted monitoring platform for uptime, incidents, response times, and infrastructure visibility. It fits agent workflows that need recurring checks, incident context, and operational dashboards with optional server telemetry via the companion Capture agent."
github_stars: 9576
verification: "listed"
source: "https://github.com/bluewave-labs/Checkmate"
author: "bluewave-labs"
publisher_type: "Open Source Project"
category: "Monitoring & Alerts"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "bluewave-labs/Checkmate"
  github_stars: 9576
---

# Checkmate Open Source Uptime and Infrastructure Monitoring

An ASE skill built on Checkmate, the open source self-hosted monitoring platform for uptime, incidents, response times, and infrastructure visibility. It fits agent workflows that need recurring checks, incident context, and operational dashboards with optional server telemetry via the companion Capture agent.

## Prerequisites

Docker, Git, and optionally the Capture agent for server telemetry

## Installation

Requirements and caveats from upstream:
- [Docker](https://www.docker.com/) installed
- If you need to monitor internal HTTPS endpoints with certificates from private Certificate Authorities (like Smallstep), see our [Custom CA Trust Guide](./docs/custom-ca-trust.md) for Docker configuration options.
- Thanks to extensive optimizations, Checkmate operates with an exceptionally small memory footprint, requiring minimal memory and CPU resources. Here’s the memory usage of a Node.js instance running on a server that mo...

Basic usage or getting-started notes:
- [![Run on PikaPods](https://www.pikapods.com/static/run-button.svg)](https://www.pikapods.com/pods?run=checkmate)
- Checkmate also has an agent, called [Capture](https://github.com/bluewave-labs/capture), to retrieve data from remote servers. While Capture is not required to run Checkmate, it provides additional insights about your...
- [Git](https://git-scm.com/) installed

- Source: https://github.com/bluewave-labs/Checkmate
- Extracted from upstream docs: https://raw.githubusercontent.com/bluewave-labs/Checkmate/HEAD/README.md

## Documentation

- https://checkmate.so/docs

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/checkmate-open-source-uptime-infrastructure-monitoring/)
