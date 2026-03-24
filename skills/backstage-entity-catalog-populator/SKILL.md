---
name: "Backstage Entity Catalog Populator"
description: "Populates Spotify Backstage software catalogs by generating catalog-info.yaml entity descriptors for services, APIs, and resources. Discovers repositories via the GitHub API and produces Component, API, and System entities conforming to the Backstage entity model."
category: "Templates & Workflows"
framework: "Gemini"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/backstage-entity-catalog-populator/"
---

# Backstage Entity Catalog Populator

Populates Spotify Backstage software catalogs by generating catalog-info.yaml entity descriptors for services, APIs, and resources. Discovers repositories via the GitHub API and produces Component, API, and System entities conforming to the Backstage entity model.

## Overview

Overview

The Backstage Entity Catalog Populator skill automates the population of Spotify Backstage software catalogs by generating `catalog-info.yaml` entity descriptor files that conform to the Backstage Entity Model specification. Instead of manually writing YAML for every microservice, API, and infrastructure resource, this skill discovers repositories across a GitHub organization and produces properly typed entity definitions that Backstage’s catalog backend can ingest via its entity provider pipeline.

How It Works

The agent queries the GitHub REST API at `/orgs/{org}/repos` with pagination to enumerate all repositories. For each repo, it inspects the file tree via `/repos/{owner}/{repo}/contents/` to detect the technology stack — checking for `package.json` (Node.js), `go.mod` (Go), `Cargo.toml` (Rust), `Dockerfile` (containerized), and `openapi.yaml` / `asyncapi.yaml` (API definitions). Based on detection, it generates a `catalog-info.yaml` with `apiVersion: backstage.io/v1alpha1`, `kind: Component` (for services), `kind: API` (for OpenAPI/AsyncAPI specs), or `kind: Resource` (for databases and infrastructure). Each entity includes metadata labels, spec.type, spec.lifecycle, spec.owner, and annotations for `github.com/project-slug`, `backstage.io/techdocs-ref`, and CI/CD links.

Output and Integration

Produces catalog-info.yaml files committed directly to each repository’s root via the GitHub Contents API (PUT), or generates a single monorepo-style `all.yaml` with Location entities pointing to each repo’s descriptor. Supports System and Domain entities for grouping related components. Handles the `spec.providesApis` and `spec.consumesApis` relationships by scanning import statements and API client configurations. Generates TechDocs `mkdocs.yml` stubs for automatic documentation discovery. All YAML output validates against the Backstage entity JSON schema and passes `backstage-cli catalog-info validate`.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill backstage-entity-catalog-populator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill backstage-entity-catalog-populator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill backstage-entity-catalog-populator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill backstage-entity-catalog-populator -a codex
```

### OpenClaw

```bash
clawhub install backstage-entity-catalog-populator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/backstage-entity-catalog-populator/
