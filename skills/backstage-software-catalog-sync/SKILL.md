---
title: Backstage Software Catalog Sync
description: The Backstage Software Catalog Sync skill automates the population and
  maintenance of a Spotify Backstage developer portal software catalog. It discovers
  services across GitHub organizations, GitLab groups, and Bitbucket projects, generating
  catalog-info.yaml descriptor files with proper Component, API, System, and Domain
  entity definitions. The skill maps repository metadata, CI/CD pipeline configurations,
  and deployment targets into Backstage entity relationships including ownedBy, consumesApi,
  providesApi, and partOf hierarchies. Team ownership is resolved from CODEOWNERS
  files and organization membership APIs. The Backstage Catalog REST API is used for
  bulk entity registration, relationship validation, and orphaned entity cleanup.
  Tech Docs integration generates MkDocs sites from repository documentation and publishes
  them to the configured storage backend. The skill maintains entity annotations for
  monitoring dashboards, runbook links, and on-call schedule references, creating
  a comprehensive service directory that reduces cognitive load for developers navigating
  complex microservice architectures.
verification: security_reviewed
source: https://agentskillexchange.com/skills/backstage-software-catalog-sync/
category:
- Templates &amp; Workflows
framework:
- Cursor
---

# Backstage Software Catalog Sync

The Backstage Software Catalog Sync skill automates the population and maintenance of a Spotify Backstage developer portal software catalog. It discovers services across GitHub organizations, GitLab groups, and Bitbucket projects, generating catalog-info.yaml descriptor files with proper Component, API, System, and Domain entity definitions. The skill maps repository metadata, CI/CD pipeline configurations, and deployment targets into Backstage entity relationships including ownedBy, consumesApi, providesApi, and partOf hierarchies. Team ownership is resolved from CODEOWNERS files and organization membership APIs. The Backstage Catalog REST API is used for bulk entity registration, relationship validation, and orphaned entity cleanup. Tech Docs integration generates MkDocs sites from repository documentation and publishes them to the configured storage backend. The skill maintains entity annotations for monitoring dashboards, runbook links, and on-call schedule references, creating a comprehensive service directory that reduces cognitive load for developers navigating complex microservice architectures.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/backstage-software-catalog-sync/)
