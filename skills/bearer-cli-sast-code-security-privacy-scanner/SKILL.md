---
title: "Bearer CLI SAST Code Security and Privacy Scanner"
description: "Bearer CLI is a free, open-source static application security testing tool developed by Cycode that scans source code and analyzes data flows to identify security vulnerabilities and privacy risks. Unlike generic scanners, Bearer tracks how sensitive data moves through an application, enabling it to detect issues that pattern-matching tools miss. The scanner covers the OWASP Top 10 and CWE Top 25 vulnerability categories with built-in rules for access control failures (path traversal, open redirects), cryptographic weaknesses, injection flaws (SQL injection, XSS, XPath), security misconfigurations, authentication failures, data integrity issues, SSRF, and more. All rules and their code patterns are documented and open source, allowing teams to audit exactly what the tool checks. Beyond security scanning, Bearer includes a privacy analysis capability that detects sensitive data flows including PII and PHI usage throughout the codebase. It identifies which components process sensitive data, including databases and third-party APIs like OpenAI and Sentry, producing reports suitable for Privacy Impact Assessments, Data Protection Impact Assessments, and GDPR compliance Records of Processing Activities. The CLI supports Go, Java, JavaScript, TypeScript, PHP, Python, and Ruby out of the box. Installation is available through Homebrew (bearer/tap/bearer), APT and RPM repositories, Docker images, and a curl-based install script. Scanning a project is as simple as running bearer scan ./my-project, which produces a detailed security report with findings, their locations in the codebase, and explanations of why each pattern is risky. Output formats include JSON, HTML, SARIF for CI integration, and a default human-readable report. The project lives at github.com/Bearer/bearer under the Elastic License 2.0, with an active community and regular releases."
source: "https://github.com/Bearer/bearer"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "Bearer/bearer"
  github_stars: 2610
---

# Bearer CLI SAST Code Security and Privacy Scanner

Bearer CLI is a free, open-source static application security testing tool developed by Cycode that scans source code and analyzes data flows to identify security vulnerabilities and privacy risks. Unlike generic scanners, Bearer tracks how sensitive data moves through an application, enabling it to detect issues that pattern-matching tools miss. The scanner covers the OWASP Top 10 and CWE Top 25 vulnerability categories with built-in rules for access control failures (path traversal, open redirects), cryptographic weaknesses, injection flaws (SQL injection, XSS, XPath), security misconfigurations, authentication failures, data integrity issues, SSRF, and more. All rules and their code patterns are documented and open source, allowing teams to audit exactly what the tool checks. Beyond security scanning, Bearer includes a privacy analysis capability that detects sensitive data flows including PII and PHI usage throughout the codebase. It identifies which components process sensitive data, including databases and third-party APIs like OpenAI and Sentry, producing reports suitable for Privacy Impact Assessments, Data Protection Impact Assessments, and GDPR compliance Records of Processing Activities. The CLI supports Go, Java, JavaScript, TypeScript, PHP, Python, and Ruby out of the box. Installation is available through Homebrew (bearer/tap/bearer), APT and RPM repositories, Docker images, and a curl-based install script. Scanning a project is as simple as running bearer scan ./my-project, which produces a detailed security report with findings, their locations in the codebase, and explanations of why each pattern is risky. Output formats include JSON, HTML, SARIF for CI integration, and a default human-readable report. The project lives at github.com/Bearer/bearer under the Elastic License 2.0, with an active community and regular releases.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bearer-cli-sast-code-security-privacy-scanner/)
