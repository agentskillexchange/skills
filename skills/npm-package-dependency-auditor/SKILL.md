---
title: "NPM Package Dependency Auditor"
description: "The NPM Package Dependency Auditor performs thorough supply chain security analysis of Node.js projects by querying the npm Registry API for package metadata and cross-referencing with Socket.dev&#8217;s security intelligence platform. It goes beyond standard npm audit by examining the full transitive dependency graph for supply chain attack indicators. The auditor checks for: typosquatting (Levenshtein distance analysis against popular package names), maintainer account takeovers (sudden ownership transfers detected via npm user API), install script abuse (preinstall/postinstall hooks executing suspicious code), dependency confusion risks (private scope names that shadow public packages), and license incompatibilities (SPDX expression parsing against your project&#8217;s license policy). It generates a risk-scored report with CVE cross-references from the GitHub Advisory Database API, alternative package suggestions for high-risk dependencies, and lockfile integrity verification. The agent can automatically create GitHub Issues for critical findings and produce SBOM documents in CycloneDX or SPDX format for compliance workflows. Supports monorepo scanning with workspace-aware deduplication."
source: "https://agentskillexchange.com/skills/npm-package-dependency-auditor/"
verification: "security_reviewed"
category:
  - "Library &amp; API Reference"
framework:
  - "MCP"
---

# NPM Package Dependency Auditor

The NPM Package Dependency Auditor performs thorough supply chain security analysis of Node.js projects by querying the npm Registry API for package metadata and cross-referencing with Socket.dev&#8217;s security intelligence platform. It goes beyond standard npm audit by examining the full transitive dependency graph for supply chain attack indicators. The auditor checks for: typosquatting (Levenshtein distance analysis against popular package names), maintainer account takeovers (sudden ownership transfers detected via npm user API), install script abuse (preinstall/postinstall hooks executing suspicious code), dependency confusion risks (private scope names that shadow public packages), and license incompatibilities (SPDX expression parsing against your project&#8217;s license policy). It generates a risk-scored report with CVE cross-references from the GitHub Advisory Database API, alternative package suggestions for high-risk dependencies, and lockfile integrity verification. The agent can automatically create GitHub Issues for critical findings and produce SBOM documents in CycloneDX or SPDX format for compliance workflows. Supports monorepo scanning with workspace-aware deduplication.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-dependency-auditor/)
