---
name: "Audit cloud accounts for security misconfigurations with Prowler"
slug: "audit-cloud-accounts-for-security-misconfigurations-with-prowler"
description: "Run targeted AWS, Azure, or GCP security and compliance audits when an agent needs actionable cloud findings instead of a generic cloud-security platform overview."
github_stars: 13635
verification: "listed"
source: "https://github.com/prowler-cloud/prowler"
author: "Prowler Cloud"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "prowler-cloud/prowler"
  github_stars: 13635
---

# Audit cloud accounts for security misconfigurations with Prowler

Run targeted AWS, Azure, or GCP security and compliance audits when an agent needs actionable cloud findings instead of a generic cloud-security platform overview.

## Prerequisites

Python or Docker runtime, cloud account credentials, optional AWS CLI or equivalent cloud auth setup

## Installation

Use the upstream install or setup path that matches your environment:
- docker compose up -d
- git clone https://github.com/prowler-cloud/prowler
- uv sync
- docker compose up postgres valkey -d

Requirements and caveats from upstream:
- <a href="https://pypi.org/project/prowler/"><img alt="Python Version" src="https://img.shields.io/pypi/v/prowler.svg"></a>
- <a href="https://pypi.python.org/pypi/prowler/"><img alt="Python Version" src="https://img.shields.io/pypi/pyversions/prowler.svg"></a>
- <a href="https://hub.docker.com/r/toniblyx/prowler"><img alt="Docker Pulls" src="https://img.shields.io/docker/pulls/toniblyx/prowler"></a>

Basic usage or getting-started notes:
- For detailed instructions on using Prowler App, refer to the [Prowler App Usage Guide](https://docs.prowler.com/projects/prowler-open-source/en/latest/tutorials/prowler-app/).
- If you want to use AWS role assumption (e.g., with the "Connect assuming IAM Role" option), you may need to mount your local .aws directory into the container as a volume (e.g., - "${HOME}/.aws:/home/prowler/.aws:ro")...
- **Commands to run the API**

- Source: https://github.com/prowler-cloud/prowler
- Extracted from upstream docs: https://raw.githubusercontent.com/prowler-cloud/prowler/HEAD/README.md

## Documentation

- https://github.com/prowler-cloud/prowler#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-cloud-accounts-for-security-misconfigurations-with-prowler/)
