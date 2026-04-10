---
name: Trivy Container Security Scanner
description: Integrates Aqua Security Trivy CLI for comprehensive container image
  vulnerability scanning. Detects OS package CVEs, language-specific dependency vulnerabilities,
  and IaC misconfigurations with SARIF output format for CI/CD pipeline integration.
verification: security_reviewed
source: https://agentskillexchange.com/skills/trivy-container-security-scanner/
category:
- Security &amp; Verification
framework:
- Codex
---
# Trivy Container Security Scanner

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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/trivy-container-security-scanner/)
