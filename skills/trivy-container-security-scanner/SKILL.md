---
name: "Trivy Container Security Scanner"
description: "Integrates Aqua Security Trivy CLI for comprehensive container image vulnerability scanning. Detects OS package CVEs, language-specific dependency vulnerabilities, and IaC misconfigurations with SARIF output format for CI/CD pipeline integration."
category: "Security & Verification"
framework: "Codex"
verification: security_reviewed
source: "https://github.com/aquasecurity/trivy"
tool_ecosystem:
  tool: trivy
  github_stars: 34053
  github_repo: aquasecurity/trivy
  license: Apache-2.0
  maintained: true
---

# Trivy Container Security Scanner

Integrates Aqua Security Trivy CLI for comprehensive container image vulnerability scanning. Detects OS package CVEs, language-specific dependency vulnerabilities, and IaC misconfigurations with SARIF output format for CI/CD pipeline integration.

## Overview

Integrates Aqua Security Trivy CLI for comprehensive container image vulnerability scanning. Detects OS package CVEs, language-specific dependency vulnerabilities, and IaC misconfigurations with SARIF output format for CI/CD pipeline integration.

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
npx skills add agentskillexchange/skills --skill trivy-container-security-scanner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill trivy-container-security-scanner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill trivy-container-security-scanner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill trivy-container-security-scanner -a codex
```

### OpenClaw

```bash
clawhub install trivy-container-security-scanner
```

## Source

- Marketplace: https://agentskillexchange.com/skills/trivy-container-security-scanner/
