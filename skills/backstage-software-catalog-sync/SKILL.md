---
name: "Backstage Software Catalog Sync"
description: "Synchronizes service metadata into Spotify Backstage catalog using catalog-info.yaml generation and the Backstage Catalog REST API. Manages component, API, and system entity relationships across teams."
category: "Templates & Workflows"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/backstage-software-catalog-sync/"
tool_ecosystem:
  tool: gitlab
  github_stars: 24278
  github_repo: gitlabhq/gitlabhq
  maintained: true
---

# Backstage Software Catalog Sync

Synchronizes service metadata into Spotify Backstage catalog using catalog-info.yaml generation and the Backstage Catalog REST API. Manages component, API, and system entity relationships across teams.

## Overview

The Backstage Software Catalog Sync skill automates the population and maintenance of a Spotify Backstage developer portal software catalog. It discovers services across GitHub organizations, GitLab groups, and Bitbucket projects, generating catalog-info.yaml descriptor files with proper Component, API, System, and Domain entity definitions. The skill maps repository metadata, CI/CD pipeline configurations, and deployment targets into Backstage entity relationships including ownedBy, consumesApi, providesApi, and partOf hierarchies. Team ownership is resolved from CODEOWNERS files and organization membership APIs. The Backstage Catalog REST API is used for bulk entity registration, relationship validation, and orphaned entity cleanup. Tech Docs integration generates MkDocs sites from repository documentation and publishes them to the configured storage backend. The skill maintains entity annotations for monitoring dashboards, runbook links, and on-call schedule references, creating a comprehensive service directory that reduces cognitive load for developers navigating complex microservice architectures.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill backstage-software-catalog-sync
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill backstage-software-catalog-sync -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill backstage-software-catalog-sync -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill backstage-software-catalog-sync -a codex
```

### OpenClaw

```bash
clawhub install backstage-software-catalog-sync
```

## Source

- Marketplace: https://agentskillexchange.com/skills/backstage-software-catalog-sync/
