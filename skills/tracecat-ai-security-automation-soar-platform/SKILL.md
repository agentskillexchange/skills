---
name: "Tracecat AI-Native Security Automation and SOAR Platform"
slug: "tracecat-ai-security-automation-soar-platform"
description: "Tracecat is an open-source, AI-native security automation platform built as a self-hosted alternative to Tines and Splunk SOAR. It combines agents, workflows, case management, and lookup tables in one platform with sandboxed execution powered by Temporal and nsjail."
github_stars: 3546
verification: "security_reviewed"
source: "https://github.com/TracecatHQ/tracecat"
author: "Tracecat"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "TracecatHQ/tracecat"
  github_stars: 3546
---

# Tracecat AI-Native Security Automation and SOAR Platform

Tracecat is an open-source, AI-native security automation platform built as a self-hosted alternative to Tines and Splunk SOAR. It combines agents, workflows, case management, and lookup tables in one platform with sandboxed execution powered by Temporal and nsjail.

## Installation

Requirements and caveats from upstream:
- **Code-native**: sync custom Python scripts from your Git repo into Tracecat.
- **Self-host anywhere**: Docker, Kubernetes, AWS Fargate.
- **Custom registry**: turn custom Python scripts into agent tools and workflow steps

Basic usage or getting-started notes:
- Sandboxed-by-default with [nsjail](https://github.com/google/nsjail) and run on [Temporal](https://temporal.io) for security, reliability, and scale.
- **Sandboxed**: run untrusted code and agents within nsjail sandboxes or pid runtimes.

- Source: https://github.com/TracecatHQ/tracecat
- Extracted from upstream docs: https://raw.githubusercontent.com/TracecatHQ/tracecat/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tracecat-ai-security-automation-soar-platform/)
