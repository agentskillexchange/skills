---
title: "Camelot PDF Stream Parser"
description: "Implements Camelot library for advanced PDF table detection using lattice and stream parsing algorithms. Processes complex multi-page documents with OpenCV-based edge detection and outputs normalized DataFrames with cell-level confidence scores."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/camelot-pdf-stream-parser/"
category:
  - "Data Extraction & Transformation"
framework:
  - "Claude Agents"
---

# Camelot PDF Stream Parser

Implements Camelot library for advanced PDF table detection using lattice and stream parsing algorithms. Processes complex multi-page documents with OpenCV-based edge detection and outputs normalized DataFrames with cell-level confidence scores.

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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/camelot-pdf-stream-parser
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/camelot-pdf-stream-parser` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/camelot-pdf-stream-parser/)
