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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semrush-content-optimizer-agent/)
