---
name: Sentry Error Triage Assistant
description: Triages application errors using the Sentry Web API (/api/0/issues/) and Sentry SDK breadcrumb data. Groups issues by stack trace similarity using Sentry fingerprinting rules and queries release health via the /api/0/organizations/{org}/releases/ endpoint.
category: Runbooks &amp; Diagnostics
framework: Any Agent
verification: security_reviewed
rating: 4.4
reviews: 14
source: https://agentskillexchange.com/skill/sentry-error-triage-assistant/
---

# Sentry Error Triage Assistant

Triages application errors using the Sentry Web API (/api/0/issues/) and Sentry SDK breadcrumb data. Groups issues by stack trace similarity using Sentry fingerprinting rules and queries release health via the /api/0/organizations/{org}/releases/ endpoint.

## Overview

Triages application errors using the Sentry Web API (/api/0/issues/) and Sentry SDK breadcrumb data. Groups issues by stack trace similarity using Sentry fingerprinting rules and queries release health via the /api/0/organizations/{org}/releases/ endpoint.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill sentry-error-triage-assistant
```

### OpenClaw

```bash
clawhub install sentry-error-triage-assistant
```

### Claude Code

```bash
claude mcp add sentry-error-triage-assistant
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/sentry-error-triage-assistant/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: Runbooks &amp; Diagnostics
- **Framework**: Any Agent
- **Rating**: 4.4/5 (14 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/sentry-error-triage-assistant/)
