---
title: "Sentry Error Triage Assistant"
description: "Triages application errors using the Sentry Web API (/api/0/issues/) and Sentry SDK breadcrumb data. Groups issues by stack trace similarity using Sentry fingerprinting rules and queries release health via the /api/0/organizations/{org}/releases/ endpoint."
slug: "sentry-error-triage-assistant"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/sentry-error-triage-assistant/"
listed: true
---

# Sentry Error Triage Assistant

Triages application errors using the Sentry Web API (/api/0/issues/) and Sentry SDK breadcrumb data. Groups issues by stack trace similarity using Sentry fingerprinting rules and queries release health via the /api/0/organizations/{org}/releases/ endpoint.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install sentry-error-triage-assistant
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Sentry Error Triage Assistant skill automates the analysis and prioritization of application errors captured by Sentry. It queries the Sentry Web API endpoint /api/0/issues/ to retrieve issue details including event counts, user impact metrics, first and last seen timestamps, and assigned ownership based on CODEOWNERS integration.
This skill analyzes SDK-captured breadcrumb data to reconstruct user journeys leading to errors, identifying common trigger patterns across multiple error occurrences. It uses Sentry fingerprinting rules to group related issues and detect duplicate reports that may appear as separate entries due to minor stack trace variations across deployments.
Release health monitoring is provided through the /api/0/organizations/{org}/releases/ endpoint, correlating error spikes with specific release versions and identifying regression introduction points. The skill tracks crash-free session rates and adoption metrics to assess the urgency of newly introduced errors.
Triage output includes severity classifications based on user impact (unique users affected), frequency trends, and business-critical path analysis. The skill generates recommended actions including issue assignment suggestions based on code ownership, links to relevant source code via Sentry source map integration, and suggested Sentry alert rule configurations for similar future issues.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sentry-error-triage-assistant/)
