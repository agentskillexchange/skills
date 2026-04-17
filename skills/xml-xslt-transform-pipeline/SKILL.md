---
title: "XML XSLT Transform Pipeline"
description: "Applies chained XSLT transformations to XML documents using lxml and Saxon-JS. Supports XSLT 3.0 streaming, XPath parameter injection, and multi-stage transform pipelines with intermediate validation."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/xml-xslt-transform-pipeline/"
category:
  - "Data Extraction & Transformation"
framework:
  - "ChatGPT Agents"
---

# XML XSLT Transform Pipeline

The XML XSLT Transform Pipeline skill provides industrial-strength XML transformation capabilities using a dual-engine approach: lxml (libxslt) for XSLT 1.0 transforms and Saxon-JS for full XSLT 3.0 support including streaming transformations. Users define multi-stage pipelines where each stage applies an XSLT stylesheet to the output of the previous stage, enabling complex document transformations to be decomposed into manageable steps. XPath parameters can be injected at each stage for dynamic customization — useful for tenant-specific transforms or environment-dependent output. Between stages, optional XML Schema (XSD) or RelaxNG validation ensures intermediate documents conform to expected shapes, catching transform errors early. The streaming mode in Saxon-JS handles documents too large for in-memory DOM processing, processing them as SAX events with minimal memory footprint. Output formats include XML, HTML, plain text, and JSON via XSLT 3.0 json() function. The skill includes a library of common transform patterns: namespace stripping, element renaming, attribute-to-element conversion, and CDATA section handling. Batch processing with glob patterns and parallel execution via multiprocessing complete the feature set.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/xml-xslt-transform-pipeline
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/xml-xslt-transform-pipeline` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/xml-xslt-transform-pipeline/)
