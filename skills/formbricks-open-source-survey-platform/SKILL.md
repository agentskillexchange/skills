---
name: Formbricks Open-Source Survey Platform
description: Formbricks is an open-source survey and experience-management platform
  with link, website, email, and in-app surveys. This skill helps agents work with
  the real Formbricks product model for feedback collection, survey delivery, self-hosting,
  and analysis workflows.
category: "Integrations &amp; Connectors"
framework: Multi-Framework
verification: listed
source: "https://github.com/formbricks/formbricks"
---
# Formbricks Open-Source Survey Platform

Formbricks is an open-source survey and experience-management platform with link, website, email, and in-app surveys. This skill helps agents work with the real Formbricks product model for feedback collection, survey delivery, self-hosting, and analysis workflows.

Formbricks is a real open-source survey platform maintained by the Formbricks organization. The upstream repository at formbricks/formbricks shows strong adoption, public release activity, and recent maintenance, which clears ASE’s provenance gate. The product is positioned as an open-source alternative to enterprise experience-management tooling, but the practical value for agents is more specific: it gives them a real system for collecting structured feedback through link surveys, website surveys, email surveys, and in-app prompts.

This skill is useful when an agent needs to design a feedback loop instead of merely suggesting generic survey questions. A Formbricks-aware agent can help choose the right survey channel, define event-triggered prompts, connect website or product instrumentation, and map responses into downstream workflows. That can include routing responses to analytics tools, enriching customer records, summarizing trends for product teams, or preparing action lists for support and growth workflows. Because the product supports both cloud hosting and self-hosting, it also works in privacy-sensitive environments where teams want tighter control over response data.

The integration surface is grounded in the official product and documentation. Formbricks supports self-hosting, Docker deployment, third-party integrations, and frontend embedding patterns documented by the vendor. The docs explicitly note website and in-app usage, and the product site references NPM-based integration for modern frontend frameworks. Good outputs from this skill include survey delivery plans, trigger design, privacy-aware self-hosting guidance, integration maps for product feedback pipelines, and operational runbooks for collecting and reviewing user sentiment at scale.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill formbricks-open-source-survey-platform
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill formbricks-open-source-survey-platform -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill formbricks-open-source-survey-platform -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill formbricks-open-source-survey-platform -a codex
```

### OpenClaw

```bash
clawhub install formbricks-open-source-survey-platform
```


## Source

- [GitHub](https://github.com/formbricks/formbricks)
