---
title: "Backstage Software Catalog Sync"
description: "Synchronizes service metadata into Spotify Backstage catalog using catalog-info.yaml generation and the Backstage Catalog REST API. Manages component, API, and system entity relationships across teams."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/backstage-software-catalog-sync/"
category:
  - "Templates &amp; Workflows"
framework:
  - "Cursor"
---

# Backstage Software Catalog Sync

The Backstage Software Catalog Sync skill automates the population and maintenance of a Spotify Backstage developer portal software catalog. It discovers services across GitHub organizations, GitLab groups, and Bitbucket projects, generating catalog-info.yaml descriptor files with proper Component, API, System, and Domain entity definitions. The skill maps repository metadata, CI/CD pipeline configurations, and deployment targets into Backstage entity relationships including ownedBy, consumesApi, providesApi, and partOf hierarchies. Team ownership is resolved from CODEOWNERS files and organization membership APIs. The Backstage Catalog REST API is used for bulk entity registration, relationship validation, and orphaned entity cleanup. Tech Docs integration generates MkDocs sites from repository documentation and publishes them to the configured storage backend. The skill maintains entity annotations for monitoring dashboards, runbook links, and on-call schedule references, creating a comprehensive service directory that reduces cognitive load for developers navigating complex microservice architectures.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/backstage-software-catalog-sync/)
