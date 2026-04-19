---
title: "Trivy Security Scanner for Containers and IaC"
description: "Trivy is a real open source security scanner from Aqua Security, built for fast checks across containers, filesystems, Git repositories, virtual machines, and Kubernetes. It looks for known CVEs, IaC misconfigurations, sensitive information, and software licenses, which makes it useful anywhere a workflow needs a quick security gate.nnUse this skill when an agent needs to inspect images before deployment, scan source trees for exposed secrets, or validate Terraform and Kubernetes manifests. Trivy ships with multiple install paths, including Homebrew, Docker, and direct release binaries, so it fits both local developer loops and CI pipelines. Its README also documents ecosystem integrations such as GitHub Actions and a Kubernetes operator, which makes it easy to plug into automated checks.nnFor ASE, Trivy maps cleanly to security verification work: container hardening, policy checks, and release-time auditing. The upstream project is actively maintained, has releases, and is backed by Aqua Security. Use it when the task is to surface concrete security findings, not to do general-purpose code review."
source: "https://github.com/aquasecurity/trivy"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "aquasecurity/trivy"
  github_stars: 34481
---

# Trivy Security Scanner for Containers and IaC

Trivy is a real open source security scanner from Aqua Security, built for fast checks across containers, filesystems, Git repositories, virtual machines, and Kubernetes. It looks for known CVEs, IaC misconfigurations, sensitive information, and software licenses, which makes it useful anywhere a workflow needs a quick security gate.nnUse this skill when an agent needs to inspect images before deployment, scan source trees for exposed secrets, or validate Terraform and Kubernetes manifests. Trivy ships with multiple install paths, including Homebrew, Docker, and direct release binaries, so it fits both local developer loops and CI pipelines. Its README also documents ecosystem integrations such as GitHub Actions and a Kubernetes operator, which makes it easy to plug into automated checks.nnFor ASE, Trivy maps cleanly to security verification work: container hardening, policy checks, and release-time auditing. The upstream project is actively maintained, has releases, and is backed by Aqua Security. Use it when the task is to surface concrete security findings, not to do general-purpose code review.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/trivy-security-scanner-containers-iac/)
