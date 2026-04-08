---
title: Kamal Zero-Downtime Docker Deployment Tool by Basecamp
description: 'Kamal is a deployment tool created by Basecamp (formerly known as MRSK)
  that enables zero-downtime deployments of containerized web applications to any
  server accessible via SSH. Originally built for Ruby on Rails applications, Kamal
  works with any web application that can be containerized with Docker, making it
  a versatile deployment solution for teams of all sizes. How It Works Kamal uses
  SSHKit to execute commands on remote servers over SSH. It pairs with kamal-proxy,
  a lightweight HTTP proxy that handles seamless request switching between old and
  new containers during deployments, ensuring zero downtime for end users. The entire
  deployment process is configured through a single deploy.yml file that defines servers,
  environment variables, accessories (databases, Redis, etc.), and health check settings.
  Key Features Zero-downtime deploys : Rolling deployments with automatic container
  switching via kamal-proxy Rolling restarts : Restart running applications without
  interruption Multi-server support : Deploy to multiple servers simultaneously with
  role-based configuration Accessory management : Manage supporting services like
  databases, caches, and search engines alongside your app Asset bridging : Maintain
  asset availability during deployments Remote builds : Build Docker images on remote
  machines or via registry Lock management : Prevent concurrent deploys with built-in
  locking Hooks : Run custom scripts at various deployment lifecycle points Agent
  Integration AI coding agents can use Kamal to automate deployment workflows by generating
  deploy.yml configurations, running kamal setup for initial provisioning, executing
  kamal deploy for updates, and managing accessories. The CLI-driven interface makes
  it straightforward to integrate into agent pipelines for CI/CD automation without
  requiring complex platform-specific APIs. Installation gem install kamal Or add
  to your Gemfile: gem "kamal" . Kamal requires Docker on the deployment targets and
  Ruby on the machine running deployments. Configuration is done via config/deploy.yml
  in your project root.'
verification: security_reviewed
source: https://github.com/basecamp/kamal
category:
- CI/CD Integrations
framework:
- Multi-Framework
---

# Kamal Zero-Downtime Docker Deployment Tool by Basecamp

Kamal is a deployment tool created by Basecamp (formerly known as MRSK) that enables zero-downtime deployments of containerized web applications to any server accessible via SSH. Originally built for Ruby on Rails applications, Kamal works with any web application that can be containerized with Docker, making it a versatile deployment solution for teams of all sizes. How It Works Kamal uses SSHKit to execute commands on remote servers over SSH. It pairs with kamal-proxy, a lightweight HTTP proxy that handles seamless request switching between old and new containers during deployments, ensuring zero downtime for end users. The entire deployment process is configured through a single deploy.yml file that defines servers, environment variables, accessories (databases, Redis, etc.), and health check settings. Key Features Zero-downtime deploys : Rolling deployments with automatic container switching via kamal-proxy Rolling restarts : Restart running applications without interruption Multi-server support : Deploy to multiple servers simultaneously with role-based configuration Accessory management : Manage supporting services like databases, caches, and search engines alongside your app Asset bridging : Maintain asset availability during deployments Remote builds : Build Docker images on remote machines or via registry Lock management : Prevent concurrent deploys with built-in locking Hooks : Run custom scripts at various deployment lifecycle points Agent Integration AI coding agents can use Kamal to automate deployment workflows by generating deploy.yml configurations, running kamal setup for initial provisioning, executing kamal deploy for updates, and managing accessories. The CLI-driven interface makes it straightforward to integrate into agent pipelines for CI/CD automation without requiring complex platform-specific APIs. Installation gem install kamal Or add to your Gemfile: gem "kamal" . Kamal requires Docker on the deployment targets and Ruby on the machine running deployments. Configuration is done via config/deploy.yml in your project root.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kamal-zero-downtime-docker-deployment-basecamp/)
