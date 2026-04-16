---
title: "NPM Package Dependency Auditor"
description: "Deep-audits npm package dependency trees using the npm Registry API and Socket.dev security intelligence. Identifies supply chain risks, typosquatting, and license incompatibilities across transitive dependencies."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/npm-package-dependency-auditor/"
category:
  - "Library &amp; API Reference"
framework:
  - "MCP"
---

# NPM Package Dependency Auditor

The NPM Package Dependency Auditor performs thorough supply chain security analysis of Node.js projects by querying the npm Registry API for package metadata and cross-referencing with Socket.dev’s security intelligence platform. It goes beyond standard npm audit by examining the full transitive dependency graph for supply chain attack indicators.

The auditor checks for: typosquatting (Levenshtein distance analysis against popular package names), maintainer account takeovers (sudden ownership transfers detected via npm user API), install script abuse (preinstall/postinstall hooks executing suspicious code), dependency confusion risks (private scope names that shadow public packages), and license incompatibilities (SPDX expression parsing against your project’s license policy).

It generates a risk-scored report with CVE cross-references from the GitHub Advisory Database API, alternative package suggestions for high-risk dependencies, and lockfile integrity verification. The agent can automatically create GitHub Issues for critical findings and produce SBOM documents in CycloneDX or SPDX format for compliance workflows. Supports monorepo scanning with workspace-aware deduplication.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/npm-package-dependency-auditor/)
