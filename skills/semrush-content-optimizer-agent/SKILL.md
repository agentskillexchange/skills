---
title: "SEMrush Content Optimizer Agent"
description: "Integrates with SEMrush Writing Assistant API to analyze content against top-10 SERP competitors. Provides real-time readability scoring via Flesch-Kincaid, keyword density analysis, and semantic similarity checks using SEMrush Topic Research endpoints."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/semrush-content-optimizer-agent/"
category:
  - "Content Writing & SEO"
framework:
  - "OpenClaw"
---

# SEMrush Content Optimizer Agent

Integrates with SEMrush Writing Assistant API to analyze content against top-10 SERP competitors. Provides real-time readability scoring via Flesch-Kincaid, keyword density analysis, and semantic similarity checks using SEMrush Topic Research endpoints.

Overview
This skill provides automated integration capabilities designed for production agent workflows. It handles authentication, rate limiting, and error recovery out of the box, allowing agents to focus on high-level task orchestration rather than low-level API management.

Key Features

Automatic retry logic with exponential backoff for API rate limits
Structured output formatting compatible with downstream agent pipelines
Comprehensive error handling with actionable diagnostic messages
Configurable caching layer to reduce redundant API calls

Usage
Install via the Agent Skill Exchange registry and configure with your API credentials. The skill exposes a standardized interface that works across supported agent frameworks, with framework-specific optimizations applied automatically during initialization.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/semrush-content-optimizer-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/semrush-content-optimizer-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/semrush-content-optimizer-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semrush-content-optimizer-agent/)
