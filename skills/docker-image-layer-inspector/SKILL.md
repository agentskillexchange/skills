---
title: "Docker Image Layer Inspector"
description: "Analyzes Docker image layers using the Docker Registry HTTP API v2 and Dive CLI. Identifies wasted space, duplicate files, and optimizes Dockerfile instructions for smaller builds."
verification: security_reviewed
source: "https://github.com/moby/moby"
category:
  - "CI/CD Integrations"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "moby/moby"
  github_stars: 71492
---

# Docker Image Layer Inspector

Analyzes Docker image layers using the Docker Registry HTTP API v2 and Dive CLI. Identifies wasted space, duplicate files, and optimizes Dockerfile instructions for smaller builds.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/docker-image-layer-inspector
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/docker-image-layer-inspector` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-image-layer-inspector/)
