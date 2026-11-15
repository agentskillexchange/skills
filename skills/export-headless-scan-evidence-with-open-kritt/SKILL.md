---
name: "Export complete or partial headless scan evidence with open·kritt"
slug: "export-headless-scan-evidence-with-open-kritt"
description: "Inspect an existing scan from a private headless host and export a review bundle that clearly distinguishes complete findings from partial results."
github_stars: 2431
verification: "security_reviewed"
source: "https://github.com/Kritt-ai/open-kritt"
author: "Kritt-ai"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "Kritt-ai/open-kritt"
  github_stars: 2431
---

# Export complete or partial headless scan evidence with open·kritt

Inspect an existing scan from a private headless host and export a review bundle that clearly distinguishes complete findings from partial results.

## Prerequisites

Node.js >=20; matching open·kritt repository checkout and running private backend; approved existing scan ID; writable approved export destination; ZIP inspection tools

## Installation

Install or set up from the source-backed instructions:

Use the same checkout as the existing backend; reviewed source commit ab240adc8d5731a45f8a8218ff03a6a3ac382e6e. For a new dedicated host, upstream setup is git clone https://github.com/Kritt-ai/open-kritt, cd open-kritt, ./kritt setup, then ./kritt start; this host setup is outside the export task. The repository-local ./kritt-headless client requires Node.js >=20 and no npm install. Connect privately and use scan show and scan export for an existing approved ID.

- Source: https://github.com/Kritt-ai/open-kritt

## Documentation

- https://github.com/Kritt-ai/open-kritt/blob/ab240adc8d5731a45f8a8218ff03a6a3ac382e6e/docs-site/getting-started/headless-cli.mdx

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/export-headless-scan-evidence-with-open-kritt/)
