---
name: "Schedule distributed agent maintenance jobs with Dkron"
slug: "schedule-distributed-agent-maintenance-jobs-with-dkron"
description: "Use Dkron to run recurring agent maintenance, data refresh, evaluation, and cleanup jobs across a fault-tolerant cluster with a UI and API."
github_stars: 4706
verification: "security_reviewed"
source: "https://github.com/dkron-io/dkron"
author: "Dkron contributors"
publisher_type: "open_source"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "dkron-io/dkron"
  github_stars: 4706
---

# Schedule distributed agent maintenance jobs with Dkron

Use Dkron to run recurring agent maintenance, data refresh, evaluation, and cleanup jobs across a fault-tolerant cluster with a UI and API.

## Prerequisites

Dkron server and agents, Docker or native Dkron binaries, networked worker nodes, job commands or API-triggered scripts

## Installation

Use the upstream install or setup path that matches your environment:
- docker compose up -d
- docker compose up -d --scale dkron-server=4
- docker compose up -d --scale dkron-agent=10
- docker compose -f docker-compose.dev.yml up

Requirements and caveats from upstream:
- The best way to test and develop dkron is using docker, you will need [Docker](https://www.docker.com/) with Docker
- Run the docker compose:
- For testing email notifications during development, Mailpit is included in the development docker-compose setup. Mailpit provides a local SMTP server that captures outgoing emails without sending them to real recipients.

Basic usage or getting-started notes:
- Dkron runs on Linux, OSX and Windows. It can be used to run scheduled commands on a server cluster using any combination
- You can use Dkron to run the most important part of your company, scheduled jobs.
- [Installation instructions](https://dkron.io/docs/basics/installation)

- Source: https://github.com/dkron-io/dkron
- Extracted from upstream docs: https://raw.githubusercontent.com/dkron-io/dkron/HEAD/README.md

## Documentation

- https://dkron.io/docs

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/schedule-distributed-agent-maintenance-jobs-with-dkron/)
