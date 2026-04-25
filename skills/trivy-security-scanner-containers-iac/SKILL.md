---
title: "Trivy Security Scanner for Containers and IaC"
description: "Trivy is Aqua Security’s scanner for vulnerabilities, misconfigurations, secrets, SBOMs, and license issues. It fits security review, container hygiene, and infrastructure-as-code checks in one CLI."
verification: "security_reviewed"
source: "https://github.com/aquasecurity/trivy"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "aquasecurity/trivy"
  github_stars: 34481
---

# Trivy Security Scanner for Containers and IaC

Trivy is a real open source security scanner from Aqua Security, built for fast checks across containers, filesystems, Git repositories, virtual machines, and Kubernetes. It looks for known CVEs, IaC misconfigurations, sensitive information, and software licenses, which makes it useful anywhere a workflow needs a quick security gate.nnUse this skill when an agent needs to inspect images before deployment, scan source trees for exposed secrets, or validate Terraform and Kubernetes manifests. Trivy ships with multiple install paths, including Homebrew, Docker, and direct release binaries, so it fits both local developer loops and CI pipelines. Its README also documents ecosystem integrations such as GitHub Actions and a Kubernetes operator, which makes it easy to plug into automated checks.nnFor ASE, Trivy maps cleanly to security verification work: container hardening, policy checks, and release-time auditing. The upstream project is actively maintained, has releases, and is backed by Aqua Security. Use it when the task is to surface concrete security findings, not to do general-purpose code review.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/trivy-security-scanner-containers-iac/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/trivy-security-scanner-containers-iac
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/trivy-security-scanner-containers-iac`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/trivy-security-scanner-containers-iac/)
