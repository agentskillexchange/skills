---
title: "Apache Camel Route Data Mapper"
description: "Maps and transforms data between systems using Apache Camel route definitions and the Camel Component API. Supports XSLT, JSONPath, and DataFormat transformations via camel-core SDK."
slug: "apache-camel-route-data-mapper"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/apache-camel-route-data-mapper/"
listed: true
---

# Apache Camel Route Data Mapper

Maps and transforms data between systems using Apache Camel route definitions and the Camel Component API. Supports XSLT, JSONPath, and DataFormat transformations via camel-core SDK.

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
clawhub install apache-camel-route-data-mapper
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Apache Camel Route Data Mapper generates data transformation routes using the Apache Camel framework and component API. It builds route definitions that map data between disparate systems using Camel DSL in both Java and XML formats. The mapper supports XSLT transformations for XML-to-XML mappings, JSONPath expressions for JSON restructuring, and Camel DataFormat components including jackson, jaxb, and csv formatters. It validates route configurations against the Camel Component API, ensuring proper endpoint URI syntax for connectors including camel-http, camel-kafka, camel-aws2-s3, and camel-jdbc components. The skill generates type-safe POJO mappings using MapStruct integration and validates data schemas against JSON Schema and XML Schema definitions. Route testing configurations are created using the Camel Test Kit with mock endpoints, adviceWith route manipulation, and NotifyBuilder assertions for asynchronous route validation.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-camel-route-data-mapper/)
