---
title: "Apache Tika Document Extractor"
description: "Wraps Apache Tika Server REST API for extracting structured text from PDFs, DOCX, PPTX, and 1,200+ file formats. Outputs clean markdown with metadata preservation using Tika /rmeta/text endpoint and recursive parsing mode."
verification: "security_reviewed"
source: "https://github.com/apache/tika"
category:
  - "Data Extraction & Transformation"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "apache/tika"
  github_stars: 3695
  license: "Apache-2.0"
---

# Apache Tika Document Extractor

Wraps Apache Tika Server REST API for extracting structured text from PDFs, DOCX, PPTX, and 1,200+ file formats. Outputs clean markdown with metadata preservation using Tika /rmeta/text endpoint and recursive parsing mode.


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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-tika-document-extractor/)
