---
title: "Camelot PDF Stream Parser"
description: "Implements Camelot library for advanced PDF table detection using lattice and stream parsing algorithms. Processes complex multi-page documents with OpenCV-based edge detection and outputs normalized DataFrames with cell-level confidence scores."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/camelot-pdf-stream-parser/"
category:
  - "Data Extraction &amp; Transformation"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/camelot-pdf-stream-parser/)
