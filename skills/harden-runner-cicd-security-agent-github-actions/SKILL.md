---
name: "Harden-Runner CI/CD Security Agent for GitHub Actions"
description: "Harden-Runner by StepSecurity is a CI/CD security agent that works like an EDR for GitHub Actions runners. It monitors network egress, file integrity, and process activity in real-time, detecting supply chain attacks such as the tj-actions and Codecov compromises."
category: "CI/CD Integrations"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/harden-runner-cicd-security-agent-github-actions/"
---

# Harden-Runner CI/CD Security Agent for GitHub Actions

Harden-Runner by StepSecurity is a CI/CD security agent that works like an EDR for GitHub Actions runners. It monitors network egress, file integrity, and process activity in real-time, detecting supply chain attacks such as the tj-actions and Codecov compromises.

## Overview

Harden-Runner is a CI/CD security monitoring tool developed by StepSecurity that provides endpoint detection and response capabilities specifically designed for GitHub Actions runners. With over 1,000 GitHub stars and deployment across 18 million workflow runs per week, it addresses a critical gap in software supply chain security: the lack of runtime monitoring on ephemeral CI/CD infrastructure.

Traditional EDR solutions are ineffective for CI/CD runners because of their ephemeral nature and inability to correlate events with specific workflow runs. Harden-Runner solves this by operating as a GitHub Action that instruments the runner at the start of each job. It monitors outbound network connections, file system changes, and process activity, building a baseline of expected behavior over time. When anomalous activity occurs, such as connections to unexpected domains or unauthorized file modifications, it flags the deviation in real time.

The tool has a proven track record of detecting major supply chain compromises. It identified the tj-actions/changed-files attack (CVE-2025-30066), detected command-and-control connections in the compromised NX build system package, caught a supply chain attack in Google’s open-source Flank project, and identified anomalous behavior in Microsoft’s Azure Karpenter Provider. It also detected outbound C2 connections across 12,000+ public repositories during the Trivy supply chain compromise.

Integration requires adding a single step at the beginning of each workflow job. In audit mode (egress-policy: audit), it logs all network, file, and process activity without blocking. In block mode, it enforces an allowlist of permitted network destinations, actively preventing exfiltration. The tool supports Linux, Windows, and macOS runners, including self-hosted configurations. Used by projects from Microsoft, Google, and CISA, Harden-Runner is available on the GitHub Marketplace and maintained at github.com/step-security/harden-runner under the Apache-2.0 license.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill harden-runner-cicd-security-agent-github-actions
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill harden-runner-cicd-security-agent-github-actions -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill harden-runner-cicd-security-agent-github-actions -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill harden-runner-cicd-security-agent-github-actions -a codex
```

### OpenClaw

```bash
clawhub install harden-runner-cicd-security-agent-github-actions
```

## Source

- Marketplace: https://agentskillexchange.com/skills/harden-runner-cicd-security-agent-github-actions/
