---
title: "DocuSign Contract Auto-Sender with Conditional Logic"
description: "Uses the DocuSign eSignature REST API SDK to programmatically create envelope definitions with conditional routing rules based on contract value thresholds. Signers are resolved from a Salesforce SOQL query via the JSForce SDK, and envelope status updates are tracked via DocuSign Connect webhooks."
verification: "security_reviewed"
source: "https://developers.docusign.com/docs/esign-rest-api/"
category:
  - "Security & Verification"
framework:
  - "ChatGPT Agents"
---

# DocuSign Contract Auto-Sender with Conditional Logic

Uses the DocuSign eSignature REST API SDK to programmatically create envelope definitions with conditional routing rules based on contract value thresholds. Signers are resolved from a Salesforce SOQL query via the JSForce SDK, and envelope status updates are tracked via DocuSign Connect webhooks.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/docusign-contract-auto-sender/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/docusign-contract-auto-sender
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/docusign-contract-auto-sender`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docusign-contract-auto-sender/)
