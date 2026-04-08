---
title: npm Registry Analyzer
description: The npm Registry Analyzer skill provides comprehensive evaluation of
  Node.js packages through the npm registry API. It retrieves detailed package metadata
  including version timelines, dependency counts, bundle sizes via bundlephobia API,
  and maintainer activity metrics. The skill leverages the npms.io scoring endpoint
  for quality, popularity, and maintenance scores, providing a holistic view of package
  health. It integrates npm-audit for vulnerability scanning against the GitHub Advisory
  Database, identifying known CVEs in direct and transitive dependencies. Advanced
  features include comparing alternative packages side-by-side, analyzing download
  trends via the npm downloads API, checking TypeScript type availability, and verifying
  ESM/CJS dual-package support. The skill generates structured reports with actionable
  recommendations for package selection and dependency management decisions.
verification: security_reviewed
source: https://agentskillexchange.com/skills/npm-registry-analyzer/
category:
- Library &amp; API Reference
framework:
- MCP
---

# npm Registry Analyzer

The npm Registry Analyzer skill provides comprehensive evaluation of Node.js packages through the npm registry API. It retrieves detailed package metadata including version timelines, dependency counts, bundle sizes via bundlephobia API, and maintainer activity metrics. The skill leverages the npms.io scoring endpoint for quality, popularity, and maintenance scores, providing a holistic view of package health. It integrates npm-audit for vulnerability scanning against the GitHub Advisory Database, identifying known CVEs in direct and transitive dependencies. Advanced features include comparing alternative packages side-by-side, analyzing download trends via the npm downloads API, checking TypeScript type availability, and verifying ESM/CJS dual-package support. The skill generates structured reports with actionable recommendations for package selection and dependency management decisions.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-registry-analyzer/)
