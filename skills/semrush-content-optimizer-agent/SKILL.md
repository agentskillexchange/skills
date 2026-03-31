---
name: "SEMrush Content Optimizer Agent"
description: "Integrates with SEMrush Writing Assistant API to analyze content against top-10 SERP competitors. Provides real-time readability scoring via Flesch-Kincaid, keyword density analysis, and semantic similarity checks using SEMrush Topic Research endpoints."
category: "Content Writing & SEO"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/semrush-content-optimizer-agent/"
---
# SEMrush Content Optimizer Agent

Integrates with SEMrush Writing Assistant API to analyze content against top-10 SERP competitors. Provides real-time readability scoring via Flesch-Kincaid, keyword density analysis, and semantic similarity checks using SEMrush Topic Research endpoints.

## Overview

Integrates with SEMrush Writing Assistant API to analyze content against top-10 SERP competitors. Provides real-time readability scoring via Flesch-Kincaid, keyword density analysis, and semantic similarity checks using SEMrush Topic Research endpoints.

Overview

This skill provides automated integration capabilities designed for production agent workflows. It handles authentication, rate limiting, and error recovery out of the box, allowing agents to focus on high-level task orchestration rather than low-level API management.

Key Features

- Automatic retry logic with exponential backoff for API rate limits

- Structured output formatting compatible with downstream agent pipelines

- Comprehensive error handling with actionable diagnostic messages

- Configurable caching layer to reduce redundant API calls

Usage

Install via the Agent Skill Exchange registry and configure with your API credentials. The skill exposes a standardized interface that works across supported agent frameworks, with framework-specific optimizations applied automatically during initialization.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill semrush-content-optimizer-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill semrush-content-optimizer-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill semrush-content-optimizer-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill semrush-content-optimizer-agent -a codex
```

### OpenClaw

```bash
clawhub install semrush-content-optimizer-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semrush-content-optimizer-agent/)
