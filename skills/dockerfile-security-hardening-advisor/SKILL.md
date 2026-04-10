---
name: Dockerfile Security Hardening Advisor
description: Audits Dockerfiles for security vulnerabilities using Hadolint and Trivy
  container scanner. Recommends hardening steps based on CIS Docker Benchmark and
  Snyk container advisories.
verification: security_reviewed
source: https://agentskillexchange.com/skills/dockerfile-security-hardening-advisor/
category:
- Runbooks &amp; Diagnostics
framework:
- Claude Code
---
# Dockerfile Security Hardening Advisor

The Dockerfile Security Hardening Advisor skill provides comprehensive security auditing for container images starting from the Dockerfile. It runs Hadolint for Dockerfile best practice validation and Trivy for vulnerability scanning of base images and installed packages.
The skill checks Dockerfiles against the CIS Docker Benchmark v1.5 controls, verifying that containers run as non-root users, use specific image tags instead of latest, minimize installed packages, and properly handle secrets. It queries the Snyk Container API for known vulnerabilities in base images.
Using Docker Scout API integration, the skill provides SBOM-based analysis of the final image layers, identifying which layer introduced each vulnerability. It recommends specific base image alternatives with fewer CVEs, comparing options across Alpine, Distroless, and Chainguard images.
The hardening report includes a prioritized action list with copy-paste Dockerfile modifications, estimated CVE reduction for each change, and a compliance score against organizational security policies. Output supports SARIF format for integration with GitHub Advanced Security.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dockerfile-security-hardening-advisor/)
