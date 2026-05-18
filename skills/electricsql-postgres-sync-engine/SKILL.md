---
name: "ElectricSQL Real-Time Postgres Sync Engine"
slug: "electricsql-postgres-sync-engine"
description: "ElectricSQL is a read-path sync engine for PostgreSQL that handles partial replication, data delivery, and fan-out. It syncs data out of Postgres in real time using an HTTP API that integrates with CDNs, with Shapes for managing partial replication and client libraries for React and TypeScript."
github_stars: 10069
verification: "listed"
source: "https://github.com/electric-sql/electric"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "electric-sql/electric"
  github_stars: 10069
---

# ElectricSQL Real-Time Postgres Sync Engine

ElectricSQL is a read-path sync engine for PostgreSQL that handles partial replication, data delivery, and fan-out. It syncs data out of Postgres in real time using an HTTP API that integrates with CDNs, with Shapes for managing partial replication and client libraries for React and TypeScript.

## Installation

Use the upstream install or setup path that matches your environment:
- docker compose -f .support/docker-compose.yml up
- brew install asdf
- pnpm install
- pnpm test

Requirements and caveats from upstream:
- For example, using [Docker Compose](https://docs.docker.com/compose/) from the root of this repo:
- We use [asdf](https://asdf-vm.com/) to install Elixir, Erlang, and Node.js. Versions are defined in [.tool-versions](.tool-versions).
- This starts a Docker Compose setup with Postgres configured for logical replication on port 54321.

Basic usage or getting-started notes:
- [Getting Started](#getting-started)
- See the [Quickstart guide](https://electric-sql.com/docs/quickstart) to get up and running. In short, you need to:
- have a Postgres database with logical replication enabled; and then to

- Source: https://github.com/electric-sql/electric
- Extracted from upstream docs: https://raw.githubusercontent.com/electric-sql/electric/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/electricsql-postgres-sync-engine/)
