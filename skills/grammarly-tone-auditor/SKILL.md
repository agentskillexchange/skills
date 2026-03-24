---
name: "Grammarly Business Tone Consistency Auditor"
description: "Integrates with the Grammarly Text Editor SDK to batch-audit marketing copy for tone deviations using the /analyze endpoint with the tone_detector feature flag. Outputs a structured JSON report of flagged sentences with suggested rewrites, logged to Google Sheets via the Sheets API v4."
category: "Content Writing & SEO"
framework: "Cursor"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/grammarly-tone-auditor/"
---

# Grammarly Business Tone Consistency Auditor

Integrates with the Grammarly Text Editor SDK to batch-audit marketing copy for tone deviations using the /analyze endpoint with the tone_detector feature flag. Outputs a structured JSON report of flagged sentences with suggested rewrites, logged to Google Sheets via the Sheets API v4.

## Overview

Integrates with the Grammarly Text Editor SDK to batch-audit marketing copy for tone deviations using the /analyze endpoint with the tone_detector feature flag. Outputs a structured JSON report of flagged sentences with suggested rewrites, logged to Google Sheets via the Sheets API v4.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill grammarly-tone-auditor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill grammarly-tone-auditor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill grammarly-tone-auditor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill grammarly-tone-auditor -a codex
```

### OpenClaw

```bash
clawhub install grammarly-tone-auditor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/grammarly-tone-auditor/
