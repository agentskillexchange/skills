---
title: "Trivy Security Scanner for Containers and IaC"
description: "Trivy is Aqua Security’s scanner for vulnerabilities, misconfigurations, secrets, SBOMs, and license issues. It fits security review, container hygiene, and infrastructure-as-code checks in one CLI."
verification: security_reviewed
source: "https://github.com/aquasecurity/trivy"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/trivy-security-scanner-containers-iac/)
