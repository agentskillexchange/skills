---
name: "Cross-validate research with SandBase Multi-Source Search"
slug: "cross-validate-research-with-sandbase-multi-source-search"
description: "Use SandBase Multi-Source Search to fact-check claims across independent web and academic sources, record disagreements, score confidence, and validate a structured evidence ledger offline."
verification: "listed"
source: "https://github.com/sandbaseai/sandbase-skills/tree/main/research/multi-source-search"
author: "SandBase"
publisher_type: "organization"
category: "Research & Scraping"
framework: "Multi-Framework"
---

# Cross-validate research with SandBase Multi-Source Search

Use the open-source SandBase `multi-source-search` Agent Skill when a decision or
fact-check needs more than one independent perspective. The workflow starts with
search and page-reading tools already available to the host agent, so a SandBase
account is not required. If SandBase tools are connected, it can add Tavily for
time-sensitive results, Exa for semantic discovery, Scholar for academic coverage,
and Cloudsway for broader web coverage. It treats retrieved pages as untrusted
evidence, traces derivative reporting back to common origins, keeps citations next
to claims, and explicitly records missing coverage and conflicting findings.

The Skill produces a JSON evidence ledger with source IDs, providers, claims,
supporting and contradicting evidence, confidence levels, and research gaps. Its
bundled offline validator checks URL shape, unique identifiers, provider diversity,
source references, and whether a confidence rating is supported by the declared
number of independent sources. This validates structural consistency rather than
asserting that a source is true. Use it for market research, technical comparisons,
current-event verification, or any report that must show how evidence supports each
conclusion.

## Installation

No source-backed install or usage instructions could be extracted automatically. Review the upstream project before running this skill in a sensitive workflow.

- Source: https://github.com/sandbaseai/sandbase-skills/tree/main/research/multi-source-search

## Source

- [SandBase Skills repository](https://github.com/sandbaseai/sandbase-skills)
- [Multi-Source Search Skill](https://github.com/sandbaseai/sandbase-skills/tree/main/research/multi-source-search)
- [Worked evidence-ledger example](https://github.com/sandbaseai/sandbase-skills/blob/main/examples/branch-protection-research.md)
