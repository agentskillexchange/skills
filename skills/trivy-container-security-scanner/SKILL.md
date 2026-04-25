---
title: "Trivy Container Security Scanner"
description: "Integrates Aqua Security Trivy CLI for comprehensive container image vulnerability scanning. Detects OS package CVEs, language-specific dependency vulnerabilities, and IaC misconfigurations with SARIF output format for CI/CD pipeline integration."
verification: "security_reviewed"
source: "https://github.com/aquasecurity/trivy"
category:
  - "Security & Verification"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "aquasecurity/trivy"
  github_stars: 34488
---

# Trivy Container Security Scanner

Integrates Aqua Security Trivy CLI for comprehensive container image vulnerability scanning. Detects OS package CVEs, language-specific dependency vulnerabilities, and IaC misconfigurations with SARIF output format for CI/CD pipeline integration.

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

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/trivy-container-security-scanner/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/trivy-container-security-scanner
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/trivy-container-security-scanner`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/trivy-container-security-scanner/)
