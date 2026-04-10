---
name: Gitxray GitHub Repository Security X-Ray
description: A multifaceted OSINT and forensics tool for GitHub repositories that
  detects fake stargazers, tampered commits, infected releases, leaked PGP keys, and
  suspicious contributor behavior using public GitHub REST APIs.
verification: security_reviewed
source: https://github.com/kulkansecurity/gitxray
category:
- Security &amp; Verification
framework:
- Claude Code
tool_ecosystem:
  github_repo: kulkansecurity/gitxray
  github_stars: 174
---
# Gitxray GitHub Repository Security X-Ray

Gitxray (Git X-Ray) is an open-source security tool by Kulkan Security that performs deep inspection of GitHub repositories and their contributors. It leverages public GitHub REST APIs to gather intelligence that would be extremely time-consuming to collect manually, and searches for information in unconventional places that standard GitHub interfaces do not expose.
The tool serves multiple security use cases. For OSINT and threat intelligence, Gitxray can extract sensitive information from contributor profiles including data accidentally disclosed in PGP armored keys, key names, and profile metadata. It analyzes contributor behavior patterns to identify co-owned or shared accounts, and inspects public event timelines to spot fake stargazers who inflate repository popularity artificially.
For repository integrity verification, Gitxray detects signs of tampering including manipulated commit dates, release assets that were updated after the release was published, and other indicators of supply chain compromise. This makes it valuable for evaluating the trustworthiness of open-source dependencies before adopting them.
Forensic investigators can use Gitxray to filter results by date ranges, correlating repository events with known incident timelines. The tool generates HTML reports with structured findings, and supports text output with customizable filters for warnings, user input analysis, key associations, and starred repositories.
Gitxray handles GitHub API rate limits gracefully, pausing execution when limits are reached and resuming automatically. It works without a token for public repositories, though providing a read-only fine-grained token significantly improves throughput. The tool optionally integrates with the VirusTotal API for checking identified hosts against threat intelligence databases. Gitxray is included in Kali Linux and installable via pip from PyPI.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitxray-github-repository-security-xray/)
