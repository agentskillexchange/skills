---
title: "Backstage Software Catalog Sync"
description: "Synchronizes service metadata into Spotify Backstage catalog using catalog-info.yaml generation and the Backstage Catalog REST API. Manages component, API, and system entity relationships across teams."
slug: "backstage-software-catalog-sync"
category:
  - "Templates &amp; Workflows"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/backstage-software-catalog-sync/"
listed: true
---

# Backstage Software Catalog Sync

Synchronizes service metadata into Spotify Backstage catalog using catalog-info.yaml generation and the Backstage Catalog REST API. Manages component, API, and system entity relationships across teams.

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
clawhub install backstage-software-catalog-sync
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Backstage Software Catalog Sync skill automates the population and maintenance of a Spotify Backstage developer portal software catalog. It discovers services across GitHub organizations, GitLab groups, and Bitbucket projects, generating catalog-info.yaml descriptor files with proper Component, API, System, and Domain entity definitions. The skill maps repository metadata, CI/CD pipeline configurations, and deployment targets into Backstage entity relationships including ownedBy, consumesApi, providesApi, and partOf hierarchies. Team ownership is resolved from CODEOWNERS files and organization membership APIs. The Backstage Catalog REST API is used for bulk entity registration, relationship validation, and orphaned entity cleanup. Tech Docs integration generates MkDocs sites from repository documentation and publishes them to the configured storage backend. The skill maintains entity annotations for monitoring dashboards, runbook links, and on-call schedule references, creating a comprehensive service directory that reduces cognitive load for developers navigating complex microservice architectures.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/backstage-software-catalog-sync/)
