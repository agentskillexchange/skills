---
name: "Backstage Software Catalog Sync"
description: "Synchronizes service metadata into Spotify Backstage catalog using catalog-info.yaml generation and the Backstage Catalog REST API. Manages component, API, and system entity relationships across teams."
category: "Templates & Workflows"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/backstage-software-catalog-sync/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "gitlab"  # from ase_tool_match
  github_stars: 24276  # from ase_github_stars (integer, not string)
  github_repo: "gitlabhq/gitlabhq"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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
