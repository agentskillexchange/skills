---
title: "Harden-Runner CI/CD Security Agent for GitHub Actions"
description: "Harden-Runner is a CI/CD security monitoring tool developed by StepSecurity that provides endpoint detection and response capabilities specifically designed for GitHub Actions runners. With over 1,000 GitHub stars and deployment across 18 million workflow runs per week, it addresses a critical gap in software supply chain security: the lack of runtime monitoring on ephemeral CI/CD infrastructure. Traditional EDR solutions are ineffective for CI/CD runners because of their ephemeral nature and inability to correlate events with specific workflow runs. Harden-Runner solves this by operating as a GitHub Action that instruments the runner at the start of each job. It monitors outbound network connections, file system changes, and process activity, building a baseline of expected behavior over time. When anomalous activity occurs, such as connections to unexpected domains or unauthorized file modifications, it flags the deviation in real time. The tool has a proven track record of detecting major supply chain compromises. It identified the tj-actions/changed-files attack (CVE-2025-30066), detected command-and-control connections in the compromised NX build system package, caught a supply chain attack in Google&#8217;s open-source Flank project, and identified anomalous behavior in Microsoft&#8217;s Azure Karpenter Provider. It also detected outbound C2 connections across 12,000+ public repositories during the Trivy supply chain compromise. Integration requires adding a single step at the beginning of each workflow job. In audit mode (egress-policy: audit), it logs all network, file, and process activity without blocking. In block mode, it enforces an allowlist of permitted network destinations, actively preventing exfiltration. The tool supports Linux, Windows, and macOS runners, including self-hosted configurations. Used by projects from Microsoft, Google, and CISA, Harden-Runner is available on the GitHub Marketplace and maintained at github.com/step-security/harden-runner under the Apache-2.0 license."
source: "https://github.com/step-security/harden-runner"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "step-security/harden-runner"
  github_stars: 1055
---

# Harden-Runner CI/CD Security Agent for GitHub Actions

Harden-Runner is a CI/CD security monitoring tool developed by StepSecurity that provides endpoint detection and response capabilities specifically designed for GitHub Actions runners. With over 1,000 GitHub stars and deployment across 18 million workflow runs per week, it addresses a critical gap in software supply chain security: the lack of runtime monitoring on ephemeral CI/CD infrastructure. Traditional EDR solutions are ineffective for CI/CD runners because of their ephemeral nature and inability to correlate events with specific workflow runs. Harden-Runner solves this by operating as a GitHub Action that instruments the runner at the start of each job. It monitors outbound network connections, file system changes, and process activity, building a baseline of expected behavior over time. When anomalous activity occurs, such as connections to unexpected domains or unauthorized file modifications, it flags the deviation in real time. The tool has a proven track record of detecting major supply chain compromises. It identified the tj-actions/changed-files attack (CVE-2025-30066), detected command-and-control connections in the compromised NX build system package, caught a supply chain attack in Google&#8217;s open-source Flank project, and identified anomalous behavior in Microsoft&#8217;s Azure Karpenter Provider. It also detected outbound C2 connections across 12,000+ public repositories during the Trivy supply chain compromise. Integration requires adding a single step at the beginning of each workflow job. In audit mode (egress-policy: audit), it logs all network, file, and process activity without blocking. In block mode, it enforces an allowlist of permitted network destinations, actively preventing exfiltration. The tool supports Linux, Windows, and macOS runners, including self-hosted configurations. Used by projects from Microsoft, Google, and CISA, Harden-Runner is available on the GitHub Marketplace and maintained at github.com/step-security/harden-runner under the Apache-2.0 license.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/harden-runner-cicd-security-agent-github-actions/)
