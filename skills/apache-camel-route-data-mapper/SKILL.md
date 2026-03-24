---
name: "Apache Camel Route Data Mapper"
description: "Maps and transforms data between systems using Apache Camel route definitions and the Camel Component API. Supports XSLT, JSONPath, and DataFormat transformations via camel-core SDK."
category: "Data Extraction & Transformation"
framework: "Custom Agents"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/apache-camel-route-data-mapper/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kafka"  # from ase_tool_match
  github_stars: 3987  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 2396148  # from ase_npm_downloads
  github_repo: "tulios/kafkajs"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: false  # from ase_tool_maintained
---

# Apache Camel Route Data Mapper

Maps and transforms data between systems using Apache Camel route definitions and the Camel Component API. Supports XSLT, JSONPath, and DataFormat transformations via camel-core SDK.

## Overview

The Apache Camel Route Data Mapper generates data transformation routes using the Apache Camel framework and component API. It builds route definitions that map data between disparate systems using Camel DSL in both Java and XML formats. The mapper supports XSLT transformations for XML-to-XML mappings, JSONPath expressions for JSON restructuring, and Camel DataFormat components including jackson, jaxb, and csv formatters. It validates route configurations against the Camel Component API, ensuring proper endpoint URI syntax for connectors including camel-http, camel-kafka, camel-aws2-s3, and camel-jdbc components. The skill generates type-safe POJO mappings using MapStruct integration and validates data schemas against JSON Schema and XML Schema definitions. Route testing configurations are created using the Camel Test Kit with mock endpoints, adviceWith route manipulation, and NotifyBuilder assertions for asynchronous route validation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill apache-camel-route-data-mapper
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill apache-camel-route-data-mapper -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill apache-camel-route-data-mapper -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill apache-camel-route-data-mapper -a codex
```

### OpenClaw

```bash
clawhub install apache-camel-route-data-mapper
```

## Source

- Marketplace: https://agentskillexchange.com/skills/apache-camel-route-data-mapper/
