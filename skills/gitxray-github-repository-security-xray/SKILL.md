---
title: "Gitxray GitHub Repository Security X-Ray"
description: "Gitxray (Git X-Ray) is an open-source security tool by Kulkan Security that performs deep inspection of GitHub repositories and their contributors. It leverages public GitHub REST APIs to gather intelligence that would be extremely time-consuming to collect manually, and searches for information in unconventional places that standard GitHub interfaces do not expose. The tool serves multiple security use cases. For OSINT and threat intelligence, Gitxray can extract sensitive information from contributor profiles including data accidentally disclosed in PGP armored keys, key names, and profile metadata. It analyzes contributor behavior patterns to identify co-owned or shared accounts, and inspects public event timelines to spot fake stargazers who inflate repository popularity artificially. For repository integrity verification, Gitxray detects signs of tampering including manipulated commit dates, release assets that were updated after the release was published, and other indicators of supply chain compromise. This makes it valuable for evaluating the trustworthiness of open-source dependencies before adopting them. Forensic investigators can use Gitxray to filter results by date ranges, correlating repository events with known incident timelines. The tool generates HTML reports with structured findings, and supports text output with customizable filters for warnings, user input analysis, key associations, and starred repositories. Gitxray handles GitHub API rate limits gracefully, pausing execution when limits are reached and resuming automatically. It works without a token for public repositories, though providing a read-only fine-grained token significantly improves throughput. The tool optionally integrates with the VirusTotal API for checking identified hosts against threat intelligence databases. Gitxray is included in Kali Linux and installable via pip from PyPI."
source: "https://github.com/kulkansecurity/gitxray"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "kulkansecurity/gitxray"
  github_stars: 174
---

# Gitxray GitHub Repository Security X-Ray

Gitxray (Git X-Ray) is an open-source security tool by Kulkan Security that performs deep inspection of GitHub repositories and their contributors. It leverages public GitHub REST APIs to gather intelligence that would be extremely time-consuming to collect manually, and searches for information in unconventional places that standard GitHub interfaces do not expose. The tool serves multiple security use cases. For OSINT and threat intelligence, Gitxray can extract sensitive information from contributor profiles including data accidentally disclosed in PGP armored keys, key names, and profile metadata. It analyzes contributor behavior patterns to identify co-owned or shared accounts, and inspects public event timelines to spot fake stargazers who inflate repository popularity artificially. For repository integrity verification, Gitxray detects signs of tampering including manipulated commit dates, release assets that were updated after the release was published, and other indicators of supply chain compromise. This makes it valuable for evaluating the trustworthiness of open-source dependencies before adopting them. Forensic investigators can use Gitxray to filter results by date ranges, correlating repository events with known incident timelines. The tool generates HTML reports with structured findings, and supports text output with customizable filters for warnings, user input analysis, key associations, and starred repositories. Gitxray handles GitHub API rate limits gracefully, pausing execution when limits are reached and resuming automatically. It works without a token for public repositories, though providing a read-only fine-grained token significantly improves throughput. The tool optionally integrates with the VirusTotal API for checking identified hosts against threat intelligence databases. Gitxray is included in Kali Linux and installable via pip from PyPI.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitxray-github-repository-security-xray/)
