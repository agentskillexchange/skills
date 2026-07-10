---
name: "Scan project dependencies for supply-chain vulnerabilities with MurphySec"
slug: "scan-project-dependencies-for-supply-chain-vulnerabilities-with-murphysec"
description: "Run MurphySec CLI against a project before release or dependency approval to detect vulnerable direct and transitive dependencies."
github_stars: 1746
verification: "security_reviewed"
source: "https://github.com/murphysecurity/murphysec"
author: "MurphySecurity"
publisher_type: "Open-source vendor"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "murphysecurity/murphysec"
  github_stars: 1746
---

# Scan project dependencies for supply-chain vulnerabilities with MurphySec

Run MurphySec CLI against a project before release or dependency approval to detect vulnerable direct and transitive dependencies.

## Prerequisites

MurphySec CLI; MurphySec account access token for authentication

## Installation

Requirements and caveats from upstream:
- MurphySec CLI requires an access token from your MurphySec account for authentication to work properly. [What is an access token?](https://www.murphysec.com/docs/faqs/project-management/access-token.html)
- --log-level string specify log level, must be silent|error|warn|info|debug

Basic usage or getting-started notes:
- [Getting Started](#getting-started)
- Visit the [GitHub Releases](https://github.com/murphysecurity/murphysec/releases/latest) page to download the latest version of MurphySec CLI, or install it by running:
- wget -q https://s.murphysec.com/release/install.sh -O - | /bin/bash

- Source: https://github.com/murphysecurity/murphysec
- Extracted from upstream docs: https://raw.githubusercontent.com/murphysecurity/murphysec/HEAD/README.md

## Documentation

- https://github.com/murphysecurity/murphysec

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-project-dependencies-for-supply-chain-vulnerabilities-with-murphysec/)
