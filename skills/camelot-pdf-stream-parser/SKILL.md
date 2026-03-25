---
name: "Camelot PDF Stream Parser"
description: "Implements Camelot library for advanced PDF table detection using lattice and stream parsing algorithms. Processes complex multi-page documents with OpenCV-based edge detection and outputs normalized DataFrames with cell-level confidence scores."
category: "Data Extraction & Transformation"
framework: "Claude Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/camelot-pdf-stream-parser/"
---

# Camelot PDF Stream Parser

Implements Camelot library for advanced PDF table detection using lattice and stream parsing algorithms. Processes complex multi-page documents with OpenCV-based edge detection and outputs normalized DataFrames with cell-level confidence scores.

## Overview

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

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill camelot-pdf-stream-parser
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill camelot-pdf-stream-parser -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill camelot-pdf-stream-parser -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill camelot-pdf-stream-parser -a codex
```

### OpenClaw

```bash
clawhub install camelot-pdf-stream-parser
```

## Source

- Marketplace: https://agentskillexchange.com/skills/camelot-pdf-stream-parser/
