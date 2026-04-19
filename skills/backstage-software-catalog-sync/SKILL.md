---
title: "Backstage Software Catalog Sync"
description: "The Backstage Software Catalog Sync skill automates the population and maintenance of a Spotify Backstage developer portal software catalog. It discovers services across GitHub organizations, GitLab groups, and Bitbucket projects, generating catalog-info.yaml descriptor files with proper Component, API, System, and Domain entity definitions. The skill maps repository metadata, CI/CD pipeline configurations, and deployment targets into Backstage entity relationships including ownedBy, consumesApi, providesApi, and partOf hierarchies. Team ownership is resolved from CODEOWNERS files and organization membership APIs. The Backstage Catalog REST API is used for bulk entity registration, relationship validation, and orphaned entity cleanup. Tech Docs integration generates MkDocs sites from repository documentation and publishes them to the configured storage backend. The skill maintains entity annotations for monitoring dashboards, runbook links, and on-call schedule references, creating a comprehensive service directory that reduces cognitive load for developers navigating complex microservice architectures."
source: "https://github.com/backstage/backstage"
verification: "security_reviewed"
category:
  - "Templates &amp; Workflows"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "backstage/backstage"
  github_stars: 33125
---

# Backstage Software Catalog Sync

The Backstage Software Catalog Sync skill automates the population and maintenance of a Spotify Backstage developer portal software catalog. It discovers services across GitHub organizations, GitLab groups, and Bitbucket projects, generating catalog-info.yaml descriptor files with proper Component, API, System, and Domain entity definitions. The skill maps repository metadata, CI/CD pipeline configurations, and deployment targets into Backstage entity relationships including ownedBy, consumesApi, providesApi, and partOf hierarchies. Team ownership is resolved from CODEOWNERS files and organization membership APIs. The Backstage Catalog REST API is used for bulk entity registration, relationship validation, and orphaned entity cleanup. Tech Docs integration generates MkDocs sites from repository documentation and publishes them to the configured storage backend. The skill maintains entity annotations for monitoring dashboards, runbook links, and on-call schedule references, creating a comprehensive service directory that reduces cognitive load for developers navigating complex microservice architectures.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/backstage-software-catalog-sync/)
