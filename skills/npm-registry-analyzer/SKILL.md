---
title: "npm Registry Analyzer"
description: "Queries the npm registry API and npms.io scoring endpoint to evaluate package quality, maintenance scores, and download trends. Uses npm-audit for security vulnerability detection against the GitHub Advisory Database."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/npm-registry-analyzer/"
category:
  - "Library &amp; API Reference"
framework:
  - "MCP"
---

# npm Registry Analyzer

The npm Registry Analyzer skill provides comprehensive evaluation of Node.js packages through the npm registry API. It retrieves detailed package metadata including version timelines, dependency counts, bundle sizes via bundlephobia API, and maintainer activity metrics.

The skill leverages the npms.io scoring endpoint for quality, popularity, and maintenance scores, providing a holistic view of package health. It integrates npm-audit for vulnerability scanning against the GitHub Advisory Database, identifying known CVEs in direct and transitive dependencies.

Advanced features include comparing alternative packages side-by-side, analyzing download trends via the npm downloads API, checking TypeScript type availability, and verifying ESM/CJS dual-package support. The skill generates structured reports with actionable recommendations for package selection and dependency management decisions.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-registry-analyzer/)
