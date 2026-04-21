---
title: "Sentry Error Triage Assistant"
slug: "sentry-error-triage-assistant"
description: "Triages application errors using the Sentry Web API (/api/0/issues/) and Sentry SDK breadcrumb data. Groups issues by stack trace similarity using Sentry fingerprinting rules and queries release health via the /api/0/organizations/{org}/releases/ endpoint."
verification: security_reviewed
source: "https://github.com/getsentry/sentry"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "getsentry/sentry"
  github_stars: 43576
---

# Sentry Error Triage Assistant

Triages application errors using the Sentry Web API (/api/0/issues/) and Sentry SDK breadcrumb data. Groups issues by stack trace similarity using Sentry fingerprinting rules and queries release health via the /api/0/organizations/{org}/releases/ endpoint.

## Installation

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sentry-error-triage-assistant/)
