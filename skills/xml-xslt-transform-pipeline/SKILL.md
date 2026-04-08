---
title: XML XSLT Transform Pipeline
description: 'The XML XSLT Transform Pipeline skill provides industrial-strength XML
  transformation capabilities using a dual-engine approach: lxml (libxslt) for XSLT
  1.0 transforms and Saxon-JS for full XSLT 3.0 support including streaming transformations.
  Users define multi-stage pipelines where each stage applies an XSLT stylesheet to
  the output of the previous stage, enabling complex document transformations to be
  decomposed into manageable steps. XPath parameters can be injected at each stage
  for dynamic customization — useful for tenant-specific transforms or environment-dependent
  output. Between stages, optional XML Schema (XSD) or RelaxNG validation ensures
  intermediate documents conform to expected shapes, catching transform errors early.
  The streaming mode in Saxon-JS handles documents too large for in-memory DOM processing,
  processing them as SAX events with minimal memory footprint. Output formats include
  XML, HTML, plain text, and JSON via XSLT 3.0 json() function. The skill includes
  a library of common transform patterns: namespace stripping, element renaming, attribute-to-element
  conversion, and CDATA section handling. Batch processing with glob patterns and
  parallel execution via multiprocessing complete the feature set.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/xml-xslt-transform-pipeline/
category:
- Data Extraction &amp; Transformation
framework:
- ChatGPT Agents
---

# XML XSLT Transform Pipeline

The XML XSLT Transform Pipeline skill provides industrial-strength XML transformation capabilities using a dual-engine approach: lxml (libxslt) for XSLT 1.0 transforms and Saxon-JS for full XSLT 3.0 support including streaming transformations. Users define multi-stage pipelines where each stage applies an XSLT stylesheet to the output of the previous stage, enabling complex document transformations to be decomposed into manageable steps. XPath parameters can be injected at each stage for dynamic customization — useful for tenant-specific transforms or environment-dependent output. Between stages, optional XML Schema (XSD) or RelaxNG validation ensures intermediate documents conform to expected shapes, catching transform errors early. The streaming mode in Saxon-JS handles documents too large for in-memory DOM processing, processing them as SAX events with minimal memory footprint. Output formats include XML, HTML, plain text, and JSON via XSLT 3.0 json() function. The skill includes a library of common transform patterns: namespace stripping, element renaming, attribute-to-element conversion, and CDATA section handling. Batch processing with glob patterns and parallel execution via multiprocessing complete the feature set.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/xml-xslt-transform-pipeline/)
