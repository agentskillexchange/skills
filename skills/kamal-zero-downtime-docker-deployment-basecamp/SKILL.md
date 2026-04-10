---
title: "Kamal Zero-Downtime Docker Deployment Tool by Basecamp"
description: "Kamal is an open-source deployment tool by Basecamp that deploys containerized web applications anywhere — from bare metal to cloud VMs — with zero downtime using Docker and SSH. It uses kamal-proxy for seamless container switching and works across multiple servers simultaneously."
slug: "kamal-zero-downtime-docker-deployment-basecamp"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/basecamp/kamal"
listed: true
---

# Kamal Zero-Downtime Docker Deployment Tool by Basecamp

Kamal is an open-source deployment tool by Basecamp that deploys containerized web applications anywhere — from bare metal to cloud VMs — with zero downtime using Docker and SSH. It uses kamal-proxy for seamless container switching and works across multiple servers simultaneously.

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
clawhub install kamal-zero-downtime-docker-deployment-basecamp
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Kamal is a deployment tool created by Basecamp (formerly known as MRSK) that enables zero-downtime deployments of containerized web applications to any server accessible via SSH. Originally built for Ruby on Rails applications, Kamal works with any web application that can be containerized with Docker, making it a versatile deployment solution for teams of all sizes.
How It Works
Kamal uses SSHKit to execute commands on remote servers over SSH. It pairs with kamal-proxy, a lightweight HTTP proxy that handles seamless request switching between old and new containers during deployments, ensuring zero downtime for end users. The entire deployment process is configured through a single deploy.yml file that defines servers, environment variables, accessories (databases, Redis, etc.), and health check settings.
Key Features
- Zero-downtime deploys: Rolling deployments with automatic container switching via kamal-proxy
- Rolling restarts: Restart running applications without interruption
- Multi-server support: Deploy to multiple servers simultaneously with role-based configuration
- Accessory management: Manage supporting services like databases, caches, and search engines alongside your app
- Asset bridging: Maintain asset availability during deployments
- Remote builds: Build Docker images on remote machines or via registry
- Lock management: Prevent concurrent deploys with built-in locking
- Hooks: Run custom scripts at various deployment lifecycle points
Agent Integration
AI coding agents can use Kamal to automate deployment workflows by generating deploy.yml configurations, running kamal setup for initial provisioning, executing kamal deploy for updates, and managing accessories. The CLI-driven interface makes it straightforward to integrate into agent pipelines for CI/CD automation without requiring complex platform-specific APIs.
Installation
gem install kamal
Or add to your Gemfile: gem "kamal". Kamal requires Docker on the deployment targets and Ruby on the machine running deployments. Configuration is done via config/deploy.yml in your project root.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kamal-zero-downtime-docker-deployment-basecamp/)
