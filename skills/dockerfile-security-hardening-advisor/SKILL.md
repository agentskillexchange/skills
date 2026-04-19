---
title: "Dockerfile Security Hardening Advisor"
description: "The Dockerfile Security Hardening Advisor skill provides comprehensive security auditing for container images starting from the Dockerfile. It runs Hadolint for Dockerfile best practice validation and Trivy for vulnerability scanning of base images and installed packages. The skill checks Dockerfiles against the CIS Docker Benchmark v1.5 controls, verifying that containers run as non-root users, use specific image tags instead of latest, minimize installed packages, and properly handle secrets. It queries the Snyk Container API for known vulnerabilities in base images. Using Docker Scout API integration, the skill provides SBOM-based analysis of the final image layers, identifying which layer introduced each vulnerability. It recommends specific base image alternatives with fewer CVEs, comparing options across Alpine, Distroless, and Chainguard images. The hardening report includes a prioritized action list with copy-paste Dockerfile modifications, estimated CVE reduction for each change, and a compliance score against organizational security policies. Output supports SARIF format for integration with GitHub Advanced Security."
source: "https://agentskillexchange.com/skills/dockerfile-security-hardening-advisor/"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Code"
---

# Dockerfile Security Hardening Advisor

The Dockerfile Security Hardening Advisor skill provides comprehensive security auditing for container images starting from the Dockerfile. It runs Hadolint for Dockerfile best practice validation and Trivy for vulnerability scanning of base images and installed packages. The skill checks Dockerfiles against the CIS Docker Benchmark v1.5 controls, verifying that containers run as non-root users, use specific image tags instead of latest, minimize installed packages, and properly handle secrets. It queries the Snyk Container API for known vulnerabilities in base images. Using Docker Scout API integration, the skill provides SBOM-based analysis of the final image layers, identifying which layer introduced each vulnerability. It recommends specific base image alternatives with fewer CVEs, comparing options across Alpine, Distroless, and Chainguard images. The hardening report includes a prioritized action list with copy-paste Dockerfile modifications, estimated CVE reduction for each change, and a compliance score against organizational security policies. Output supports SARIF format for integration with GitHub Advanced Security.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dockerfile-security-hardening-advisor/)
