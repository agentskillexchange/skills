---
title: "npm Registry Analyzer"
description: "The npm Registry Analyzer skill provides comprehensive evaluation of Node.js packages through the npm registry API. It retrieves detailed package metadata including version timelines, dependency counts, bundle sizes via bundlephobia API, and maintainer activity metrics. The skill leverages the npms.io scoring endpoint for quality, popularity, and maintenance scores, providing a holistic view of package health. It integrates npm-audit for vulnerability scanning against the GitHub Advisory Database, identifying known CVEs in direct and transitive dependencies. Advanced features include comparing alternative packages side-by-side, analyzing download trends via the npm downloads API, checking TypeScript type availability, and verifying ESM/CJS dual-package support. The skill generates structured reports with actionable recommendations for package selection and dependency management decisions."
source: "https://agentskillexchange.com/skills/npm-registry-analyzer/"
verification: "security_reviewed"
category:
  - "Library &amp; API Reference"
framework:
  - "MCP"
---

# npm Registry Analyzer

The npm Registry Analyzer skill provides comprehensive evaluation of Node.js packages through the npm registry API. It retrieves detailed package metadata including version timelines, dependency counts, bundle sizes via bundlephobia API, and maintainer activity metrics. The skill leverages the npms.io scoring endpoint for quality, popularity, and maintenance scores, providing a holistic view of package health. It integrates npm-audit for vulnerability scanning against the GitHub Advisory Database, identifying known CVEs in direct and transitive dependencies. Advanced features include comparing alternative packages side-by-side, analyzing download trends via the npm downloads API, checking TypeScript type availability, and verifying ESM/CJS dual-package support. The skill generates structured reports with actionable recommendations for package selection and dependency management decisions.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-registry-analyzer/)
