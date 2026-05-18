---
name: "Snyk Dependency Audit Skill"
slug: "snyk-dependency-audit-skill"
description: "Uses the Snyk CLI and REST API v1 to scan package manifests for known CVEs. Cross-references findings with the GitHub Advisory Database and produces SBOM documents in CycloneDX format."
github_stars: 5496
verification: "security_reviewed"
source: "https://github.com/snyk/cli"
category: "Security & Verification"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "snyk/cli"
  github_stars: 5496
  npm_package: "snyk"
  npm_weekly_downloads: 2566112
---

# Snyk Dependency Audit Skill

Uses the Snyk CLI and REST API v1 to scan package manifests for known CVEs. Cross-references findings with the GitHub Advisory Database and produces SBOM documents in CycloneDX format.

## Installation

Requirements and caveats from upstream:
- To use the CLI, you must install it and authenticate your machine. See [Install or update the Snyk CLI](https://docs.snyk.io/snyk-cli/install-or-update-the-snyk-cli) and [Authenticate the CLI with your account](https:...
- Before you can use the CLI for Open Source scanning, you must install your package manager. The needed third-party tools, such as Gradle or Maven, must be in the PATH.
- Before using the Snyk CLI to test your Open Source Project for vulnerabilities, with limited exceptions, you must build your Project. For details, see [Open Source Projects that must be built before testing](https://d...

Basic usage or getting-started notes:
- ## Introduction to the Snyk CLI
- Snyk is a developer-first, cloud-native security tool to scan and monitor your software development projects for security vulnerabilities. Snyk scans multiple content types for security issues:
- [Snyk Open Source](https://docs.snyk.io/scan-with-snyk/snyk-open-source): Find and automatically fix open-source vulnerabilities

- Source: https://github.com/snyk/cli
- Extracted from upstream docs: https://raw.githubusercontent.com/snyk/cli/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snyk-dependency-audit-skill/)
