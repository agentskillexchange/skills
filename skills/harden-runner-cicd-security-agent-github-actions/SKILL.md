---
title: "Harden-Runner CI/CD Security Agent for GitHub Actions"
description: "Harden-Runner by StepSecurity is a CI/CD security agent that works like an EDR for GitHub Actions runners. It monitors network egress, file integrity, and process activity in real-time, detecting supply chain attacks such as the tj-actions and Codecov compromises."
slug: "harden-runner-cicd-security-agent-github-actions"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://github.com/step-security/harden-runner"
tool_ecosystem:
  github_repo: "step-security/harden-runner"
  github_stars: 1055
listed: true
---

# Harden-Runner CI/CD Security Agent for GitHub Actions

Harden-Runner by StepSecurity is a CI/CD security agent that works like an EDR for GitHub Actions runners. It monitors network egress, file integrity, and process activity in real-time, detecting supply chain attacks such as the tj-actions and Codecov compromises.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install harden-runner-cicd-security-agent-github-actions
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Harden-Runner is a CI/CD security monitoring tool developed by StepSecurity that provides endpoint detection and response capabilities specifically designed for GitHub Actions runners. With over 1,000 GitHub stars and deployment across 18 million workflow runs per week, it addresses a critical gap in software supply chain security: the lack of runtime monitoring on ephemeral CI/CD infrastructure.
Traditional EDR solutions are ineffective for CI/CD runners because of their ephemeral nature and inability to correlate events with specific workflow runs. Harden-Runner solves this by operating as a GitHub Action that instruments the runner at the start of each job. It monitors outbound network connections, file system changes, and process activity, building a baseline of expected behavior over time. When anomalous activity occurs, such as connections to unexpected domains or unauthorized file modifications, it flags the deviation in real time.
The tool has a proven track record of detecting major supply chain compromises. It identified the tj-actions/changed-files attack (CVE-2025-30066), detected command-and-control connections in the compromised NX build system package, caught a supply chain attack in Google’s open-source Flank project, and identified anomalous behavior in Microsoft’s Azure Karpenter Provider. It also detected outbound C2 connections across 12,000+ public repositories during the Trivy supply chain compromise.
Integration requires adding a single step at the beginning of each workflow job. In audit mode (egress-policy: audit), it logs all network, file, and process activity without blocking. In block mode, it enforces an allowlist of permitted network destinations, actively preventing exfiltration. The tool supports Linux, Windows, and macOS runners, including self-hosted configurations. Used by projects from Microsoft, Google, and CISA, Harden-Runner is available on the GitHub Marketplace and maintained at github.com/step-security/harden-runner under the Apache-2.0 license.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/harden-runner-cicd-security-agent-github-actions/)
