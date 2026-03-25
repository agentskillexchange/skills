---
name: "DocuSign Contract Auto-Sender with Conditional Logic"
description: "Uses the DocuSign eSignature REST API SDK to programmatically create envelope definitions with conditional routing rules based on contract value thresholds. Signers are resolved from a Salesforce SOQL query via the JSForce SDK, and envelope status updates are tracked via DocuSign Connect webhooks."
category: "Security & Verification"
framework: "ChatGPT Agents"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/docusign-contract-auto-sender/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "salesforce"  # from ase_tool_match
  github_stars: 1452  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 804753  # from ase_npm_downloads
  github_repo: "jsforce/jsforce"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# DocuSign Contract Auto-Sender with Conditional Logic

Uses the DocuSign eSignature REST API SDK to programmatically create envelope definitions with conditional routing rules based on contract value thresholds. Signers are resolved from a Salesforce SOQL query via the JSForce SDK, and envelope status updates are tracked via DocuSign Connect webhooks.

## Overview

Uses the DocuSign eSignature REST API SDK to programmatically create envelope definitions with conditional routing rules based on contract value thresholds. Signers are resolved from a Salesforce SOQL query via the JSForce SDK, and envelope status updates are tracked via DocuSign Connect webhooks.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill docusign-contract-auto-sender
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill docusign-contract-auto-sender -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill docusign-contract-auto-sender -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill docusign-contract-auto-sender -a codex
```

### OpenClaw

```bash
clawhub install docusign-contract-auto-sender
```

## Source

- Marketplace: https://agentskillexchange.com/skills/docusign-contract-auto-sender/
