---
title: "Bearer CLI SAST Code Security and Privacy Scanner"
description: "Bearer CLI is an open-source static application security testing (SAST) tool that scans source code to identify, filter, and prioritize security vulnerabilities and privacy risks. Covers OWASP Top 10 and CWE Top 25 with data flow analysis across multiple languages."
slug: "bearer-cli-sast-code-security-privacy-scanner"
category:
  - "Security &amp; Verification"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://github.com/Bearer/bearer"
tool_ecosystem:
  github_repo: "Bearer/bearer"
  github_stars: 2610
---

# Bearer CLI SAST Code Security and Privacy Scanner

Bearer CLI is an open-source static application security testing (SAST) tool that scans source code to identify, filter, and prioritize security vulnerabilities and privacy risks. Covers OWASP Top 10 and CWE Top 25 with data flow analysis across multiple languages.

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
clawhub install bearer-cli-sast-code-security-privacy-scanner
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Bearer CLI is a free, open-source static application security testing tool developed by Cycode that scans source code and analyzes data flows to identify security vulnerabilities and privacy risks. Unlike generic scanners, Bearer tracks how sensitive data moves through an application, enabling it to detect issues that pattern-matching tools miss.
The scanner covers the OWASP Top 10 and CWE Top 25 vulnerability categories with built-in rules for access control failures (path traversal, open redirects), cryptographic weaknesses, injection flaws (SQL injection, XSS, XPath), security misconfigurations, authentication failures, data integrity issues, SSRF, and more. All rules and their code patterns are documented and open source, allowing teams to audit exactly what the tool checks.
Beyond security scanning, Bearer includes a privacy analysis capability that detects sensitive data flows including PII and PHI usage throughout the codebase. It identifies which components process sensitive data, including databases and third-party APIs like OpenAI and Sentry, producing reports suitable for Privacy Impact Assessments, Data Protection Impact Assessments, and GDPR compliance Records of Processing Activities.
The CLI supports Go, Java, JavaScript, TypeScript, PHP, Python, and Ruby out of the box. Installation is available through Homebrew (bearer/tap/bearer), APT and RPM repositories, Docker images, and a curl-based install script. Scanning a project is as simple as running bearer scan ./my-project, which produces a detailed security report with findings, their locations in the codebase, and explanations of why each pattern is risky. Output formats include JSON, HTML, SARIF for CI integration, and a default human-readable report. The project lives at github.com/Bearer/bearer under the Elastic License 2.0, with an active community and regular releases.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bearer-cli-sast-code-security-privacy-scanner/)
