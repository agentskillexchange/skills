---
name: "SSL Certificate Auditor"
slug: "ssl-certificate-auditor-agent"
description: "Audits TLS/SSL configurations using sslyze Python library and SSL Labs API v3. Checks certificate chain validity, HSTS headers, and OCSP stapling status with Certificate Transparency log verification."
github_stars: 3755
verification: "security_reviewed"
source: "https://github.com/nabla-c0d3/sslyze"
author: "nabla-c0d3"
category: "Security & Verification"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "nabla-c0d3/sslyze"
  github_stars: 3755
---

# SSL Certificate Auditor

Audits TLS/SSL configurations using sslyze Python library and SSL Labs API v3. Checks certificate chain validity, HSTS headers, and OCSP stapling status with Certificate Transparency log verification.

## Installation

Use the upstream install or setup path that matches your environment:
- $ pip install --upgrade pip setuptools wheel
- $ pip install --upgrade sslyze
- $ docker run --rm -it nablac0d3/sslyze:6.1.0 www.google.com
- $ pip install -e .

Requirements and caveats from upstream:
- [![Python version](https://img.shields.io/pypi/pyversions/sslyze.svg)](https://pypi.org/project/sslyze/)
- SSLyze is a fast and powerful SSL/TLS scanning tool and Python library.
- Fully documented [Python API](https://nabla-c0d3.github.io/sslyze/documentation/) to run scans directly from any

Basic usage or getting-started notes:
- ![Run Tests](https://github.com/nabla-c0d3/sslyze/workflows/Run%20Tests/badge.svg)
- Easy to operationalize: SSLyze can be directly run from CI/CD, in order to continuously check a server against
- -----------

- Source: https://github.com/nabla-c0d3/sslyze
- Extracted from upstream docs: https://raw.githubusercontent.com/nabla-c0d3/sslyze/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ssl-certificate-auditor-agent/)
