---
name: "Gitxray GitHub Repository Security X-Ray"
description: "A multifaceted OSINT and forensics tool for GitHub repositories that detects fake stargazers, tampered commits, infected releases, leaked PGP keys, and suspicious contributor behavior using public GitHub REST APIs."
category: "Security & Verification"
framework: "Claude Code"
verification: security_reviewed
source: "https://github.com/kulkansecurity/gitxray"
---
# Gitxray GitHub Repository Security X-Ray

A multifaceted OSINT and forensics tool for GitHub repositories that detects fake stargazers, tampered commits, infected releases, leaked PGP keys, and suspicious contributor behavior using public GitHub REST APIs.

## Overview

Gitxray (Git X-Ray) is an open-source security tool by Kulkan Security that performs deep inspection of GitHub repositories and their contributors. It leverages public GitHub REST APIs to gather intelligence that would be extremely time-consuming to collect manually, and searches for information in unconventional places that standard GitHub interfaces do not expose.

The tool serves multiple security use cases. For OSINT and threat intelligence, Gitxray can extract sensitive information from contributor profiles including data accidentally disclosed in PGP armored keys, key names, and profile metadata. It analyzes contributor behavior patterns to identify co-owned or shared accounts, and inspects public event timelines to spot fake stargazers who inflate repository popularity artificially.

For repository integrity verification, Gitxray detects signs of tampering including manipulated commit dates, release assets that were updated after the release was published, and other indicators of supply chain compromise. This makes it valuable for evaluating the trustworthiness of open-source dependencies before adopting them.

Forensic investigators can use Gitxray to filter results by date ranges, correlating repository events with known incident timelines. The tool generates HTML reports with structured findings, and supports text output with customizable filters for warnings, user input analysis, key associations, and starred repositories.

Gitxray handles GitHub API rate limits gracefully, pausing execution when limits are reached and resuming automatically. It works without a token for public repositories, though providing a read-only fine-grained token significantly improves throughput. The tool optionally integrates with the VirusTotal API for checking identified hosts against threat intelligence databases. Gitxray is included in Kali Linux and installable via pip from PyPI.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gitxray-github-repository-security-xray
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gitxray-github-repository-security-xray -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gitxray-github-repository-security-xray -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gitxray-github-repository-security-xray -a codex
```

### OpenClaw

```bash
clawhub install gitxray-github-repository-security-xray
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitxray-github-repository-security-xray/)
