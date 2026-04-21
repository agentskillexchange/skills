---
title: "DocuSign Contract Auto-Sender with Conditional Logic"
description: "Uses the DocuSign eSignature REST API SDK to programmatically create envelope definitions with conditional routing rules based on contract value thresholds. Signers are resolved from a Salesforce SOQL query via the JSForce SDK, and envelope status updates are tracked via DocuSign Connect webhooks."
verification: security_reviewed
source: "https://developers.docusign.com/docs/esign-rest-api/"
category:
  - "Security &amp; Verification"
framework:
  - "ChatGPT Agents"
---

# DocuSign Contract Auto-Sender with Conditional Logic

Uses the DocuSign eSignature REST API SDK to programmatically create envelope definitions with conditional routing rules based on contract value thresholds. Signers are resolved from a Salesforce SOQL query via the JSForce SDK, and envelope status updates are tracked via DocuSign Connect webhooks.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/docusign-contract-auto-sender
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/docusign-contract-auto-sender` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docusign-contract-auto-sender/)
