---
title: "Camelot PDF Stream Parser"
description: "Implements Camelot library for advanced PDF table detection using lattice and stream parsing algorithms. Processes complex multi-page documents with OpenCV-based edge detection and outputs normalized DataFrames with cell-level confidence scores."
verification: "security_reviewed"
source: "https://github.com/camelot-dev/camelot"
category:
  - "Data Extraction & Transformation"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "camelot-dev/camelot"
  github_stars: 3673
---

# Camelot PDF Stream Parser

Implements Camelot library for advanced PDF table detection using lattice and stream parsing algorithms. Processes complex multi-page documents with OpenCV-based edge detection and outputs normalized DataFrames with cell-level confidence scores. Overview This skill provides automated integration capabilities designed for production agent workflows. It handles authentication, rate limiting, and error recovery out of the box, allowing agents to focus on high-level task orchestration rather than low-level API management. Key Features Automatic retry logic with exponential backoff for API rate limits Structured output formatting compatible with downstream agent pipelines Comprehensive error handling with actionable diagnostic messages Configurable caching layer to reduce redundant API calls Usage Install via the Agent Skill Exchange registry and configure with your API credentials. The skill exposes a standardized interface that works across supported agent frameworks, with framework-specific optimizations applied automatically during initialization.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/camelot-pdf-stream-parser/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/camelot-pdf-stream-parser
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/camelot-pdf-stream-parser`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/camelot-pdf-stream-parser/)
