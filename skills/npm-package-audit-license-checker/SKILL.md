---
title: NPM Package Audit & License Checker
description: 'The NPM Package Audit & License Checker skill performs comprehensive
  security and compliance analysis of Node.js project dependencies. It combines npm
  audit for vulnerability scanning, license-checker-rspack for license extraction,
  and direct npm registry API (registry.npmjs.org/-/v1/search, registry.npmjs.org/{package})
  queries for package health metrics. Security analysis includes: CVE vulnerability
  reports with CVSS v3.1 scores and vector strings, transitive dependency vulnerability
  tracing showing the full dependency chain, exploit availability indicators from
  GitHub Advisory Database (GHSA) cross-references, and fix availability status with
  recommended semver-compatible upgrade paths. License compliance generates: a full
  dependency license matrix (MIT, Apache-2.0, ISC, BSD, GPL variants), compatibility
  analysis against your project license, SPDX expression parsing for dual-licensed
  packages, and flagging of packages with no license field or custom/proprietary licenses.
  Package health metrics from the registry API include: weekly download trends (flagging
  >50% decline as potential abandonment), last publish date (warning if >2 years),
  maintainer count and bus factor analysis, and GitHub stars/issues ratio as a maintenance
  indicator. The skill outputs actionable reports with prioritized remediation steps:
  critical CVE patches, license violation resolutions, and suggested replacements
  for abandoned packages.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/npm-package-audit-license-checker/
category:
- Library &amp; API Reference
framework:
- Claude Code
---

# NPM Package Audit & License Checker

The NPM Package Audit & License Checker skill performs comprehensive security and compliance analysis of Node.js project dependencies. It combines npm audit for vulnerability scanning, license-checker-rspack for license extraction, and direct npm registry API (registry.npmjs.org/-/v1/search, registry.npmjs.org/{package}) queries for package health metrics. Security analysis includes: CVE vulnerability reports with CVSS v3.1 scores and vector strings, transitive dependency vulnerability tracing showing the full dependency chain, exploit availability indicators from GitHub Advisory Database (GHSA) cross-references, and fix availability status with recommended semver-compatible upgrade paths. License compliance generates: a full dependency license matrix (MIT, Apache-2.0, ISC, BSD, GPL variants), compatibility analysis against your project license, SPDX expression parsing for dual-licensed packages, and flagging of packages with no license field or custom/proprietary licenses. Package health metrics from the registry API include: weekly download trends (flagging >50% decline as potential abandonment), last publish date (warning if >2 years), maintainer count and bus factor analysis, and GitHub stars/issues ratio as a maintenance indicator. The skill outputs actionable reports with prioritized remediation steps: critical CVE patches, license violation resolutions, and suggested replacements for abandoned packages.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-audit-license-checker/)
