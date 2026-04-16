---
title: "Docker Compose Test Harness"
description: "Scaffolds integration test environments using Docker Compose v2 CLI, testcontainers-python library, and the docker-py SDK. Manages service dependencies, health checks, and test data seeding."
verification: "security_reviewed"
source: "https://github.com/moby/moby"
category:
  - "Templates &amp; Workflows"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "moby/moby"
  github_stars: 71492
  license: "Apache-2.0"
---

# Docker Compose Test Harness

The Docker Compose Test Harness skill automates the creation and management of integration test environments using container orchestration. It generates Docker Compose v2 configuration files with proper service dependency ordering, health check definitions, and network isolation. The testcontainers-python library integration provides programmatic container lifecycle management within pytest test suites, supporting database containers (PostgreSQL, MySQL, MongoDB), message brokers (RabbitMQ, Kafka), and cache services (Redis, Memcached). The docker-py SDK handles image building, container inspection, and log collection for test debugging. The harness manages test data seeding through init containers, SQL migration scripts, and fixture loading from JSON/CSV files. Service health check configurations use appropriate strategies: TCP socket checks for databases, HTTP endpoint checks for web services, and command-based checks for custom readiness criteria. The skill supports environment variable templating, secret injection via Docker secrets, and volume mounting for test configuration files. Parallel test execution is managed through dynamic port allocation and network namespace isolation. Cleanup procedures ensure complete resource removal after test completion including orphaned volumes and networks. Output includes generated docker-compose.yml files, pytest conftest.py fixtures, and CI pipeline integration scripts.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-compose-test-harness/)
