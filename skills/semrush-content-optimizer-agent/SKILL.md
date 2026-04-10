---
name: SEMrush Content Optimizer Agent
description: Integrates with SEMrush Writing Assistant API to analyze content against
  top-10 SERP competitors. Provides real-time readability scoring via Flesch-Kincaid,
  keyword density analysis, and semantic similarity checks using SEMrush Topic Research
  endpoints.
verification: security_reviewed
source: https://agentskillexchange.com/skills/semrush-content-optimizer-agent/
category:
- Content Writing &amp; SEO
framework:
- OpenClaw
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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semrush-content-optimizer-agent/)
