---
title: "OpenMetadata Data Catalog and Governance Platform for Agent Discovery"
description: "OpenMetadata provides a central metadata layer for data discovery, lineage, quality, ownership, and governance. This skill helps agents answer questions about tables, dashboards, pipelines, and data health from one searchable control plane instead of jumping between isolated tools."
slug: "openmetadata-data-catalog-governance-platform-agent-discovery"
category:
  - "Library &amp; API Reference"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/open-metadata/OpenMetadata"
tool_ecosystem:
  github_repo: "open-metadata/OpenMetadata"
  github_stars: 9965
---

# OpenMetadata Data Catalog and Governance Platform for Agent Discovery

OpenMetadata provides a central metadata layer for data discovery, lineage, quality, ownership, and governance. This skill helps agents answer questions about tables, dashboards, pipelines, and data health from one searchable control plane instead of jumping between isolated tools.

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
clawhub install openmetadata-data-catalog-governance-platform-agent-discovery
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

OpenMetadata is an open-source metadata platform designed to index and organize the assets that matter in modern data stacks: databases, tables, dashboards, pipelines, tests, ownership information, and lineage. For agent workflows, that is a strong foundation because the agent can use one system to answer questions like “where does this metric come from?”, “who owns this pipeline?”, or “what downstream dashboards will break if this table changes?” without stitching together custom logic across multiple tools. The job to be done is discovery and governance, not just storage.
An OpenMetadata-oriented skill is especially useful for data engineering, analytics, and platform teams that want an agent to act as a reliable catalog assistant. The agent can search assets, surface descriptions and tags, reason about lineage, and support incident triage when a schema or job changes. Because OpenMetadata also tracks data quality and observability signals, it can anchor workflows where the agent summarizes health issues, routes the right owner, or generates documentation from existing metadata rather than guessing.
This kind of skill fits best when you already have multiple data tools and need a trustworthy inventory layer. Instead of connecting an assistant separately to warehouse schemas, BI dashboards, and pipeline systems, OpenMetadata becomes the reference system the agent consults first. That makes the resulting workflows more explainable and easier to maintain. It is a practical building block for catalog search, data governance copilots, lineage-aware runbooks, and documentation automation across multi-tool data environments.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openmetadata-data-catalog-governance-platform-agent-discovery/)
