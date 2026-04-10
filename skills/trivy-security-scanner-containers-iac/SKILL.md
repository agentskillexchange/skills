---
title: "Trivy Security Scanner for Containers and IaC"
description: "Trivy is Aqua Security’s scanner for vulnerabilities, misconfigurations, secrets, SBOMs, and license issues. It fits security review, container hygiene, and infrastructure-as-code checks in one CLI."
slug: "trivy-security-scanner-containers-iac"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/aquasecurity/trivy"
listed: true
---

# Trivy Security Scanner for Containers and IaC

Trivy is Aqua Security’s scanner for vulnerabilities, misconfigurations, secrets, SBOMs, and license issues. It fits security review, container hygiene, and infrastructure-as-code checks in one CLI.

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
clawhub install trivy-security-scanner-containers-iac
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Trivy is a real open source security scanner from Aqua Security, built for fast checks across containers, filesystems, Git repositories, virtual machines, and Kubernetes. It looks for known CVEs, IaC misconfigurations, sensitive information, and software licenses, which makes it useful anywhere a workflow needs a quick security gate.nnUse this skill when an agent needs to inspect images before deployment, scan source trees for exposed secrets, or validate Terraform and Kubernetes manifests. Trivy ships with multiple install paths, including Homebrew, Docker, and direct release binaries, so it fits both local developer loops and CI pipelines. Its README also documents ecosystem integrations such as GitHub Actions and a Kubernetes operator, which makes it easy to plug into automated checks.nnFor ASE, Trivy maps cleanly to security verification work: container hardening, policy checks, and release-time auditing. The upstream project is actively maintained, has releases, and is backed by Aqua Security. Use it when the task is to surface concrete security findings, not to do general-purpose code review.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/trivy-security-scanner-containers-iac/)
