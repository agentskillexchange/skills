---
name: Apache Camel Route Data Mapper
description: Maps and transforms data between systems using Apache Camel route definitions
  and the Camel Component API. Supports XSLT, JSONPath, and DataFormat transformations
  via camel-core SDK.
verification: security_reviewed
source: https://agentskillexchange.com/skills/apache-camel-route-data-mapper/
category:
- Data Extraction &amp; Transformation
framework:
- Custom Agents
---
# Apache Camel Route Data Mapper

The Apache Camel Route Data Mapper generates data transformation routes using the Apache Camel framework and component API. It builds route definitions that map data between disparate systems using Camel DSL in both Java and XML formats. The mapper supports XSLT transformations for XML-to-XML mappings, JSONPath expressions for JSON restructuring, and Camel DataFormat components including jackson, jaxb, and csv formatters. It validates route configurations against the Camel Component API, ensuring proper endpoint URI syntax for connectors including camel-http, camel-kafka, camel-aws2-s3, and camel-jdbc components. The skill generates type-safe POJO mappings using MapStruct integration and validates data schemas against JSON Schema and XML Schema definitions. Route testing configurations are created using the Camel Test Kit with mock endpoints, adviceWith route manipulation, and NotifyBuilder assertions for asynchronous route validation.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-camel-route-data-mapper/)
