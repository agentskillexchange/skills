---
title: "XML XSLT Transform Pipeline"
description: "Applies chained XSLT transformations to XML documents using lxml and Saxon-JS. Supports XSLT 3.0 streaming, XPath parameter injection, and multi-stage transform pipelines with intermediate validation."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/xml-xslt-transform-pipeline/"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "ChatGPT Agents"
---

# XML XSLT Transform Pipeline

The XML XSLT Transform Pipeline skill provides industrial-strength XML transformation capabilities using a dual-engine approach: lxml (libxslt) for XSLT 1.0 transforms and Saxon-JS for full XSLT 3.0 support including streaming transformations. Users define multi-stage pipelines where each stage applies an XSLT stylesheet to the output of the previous stage, enabling complex document transformations to be decomposed into manageable steps. XPath parameters can be injected at each stage for dynamic customization — useful for tenant-specific transforms or environment-dependent output. Between stages, optional XML Schema (XSD) or RelaxNG validation ensures intermediate documents conform to expected shapes, catching transform errors early. The streaming mode in Saxon-JS handles documents too large for in-memory DOM processing, processing them as SAX events with minimal memory footprint. Output formats include XML, HTML, plain text, and JSON via XSLT 3.0 json() function. The skill includes a library of common transform patterns: namespace stripping, element renaming, attribute-to-element conversion, and CDATA section handling. Batch processing with glob patterns and parallel execution via multiprocessing complete the feature set.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/xml-xslt-transform-pipeline/)
