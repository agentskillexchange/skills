---
name: "Sweep GitHub for leaked secrets and exposed credentials with git-hound"
slug: "sweep-github-for-leaked-secrets-and-exposed-credentials-with-git-hound"
description: "Search public GitHub broadly for leaked secrets and triage exposures when the workflow is recon and remediation, not generic secret scanning."
github_stars: 1400
verification: "security_reviewed"
source: "https://github.com/tillson/git-hound"
author: "tillson"
publisher_type: "GitHub repository"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "tillson/git-hound"
  github_stars: 1400
---

# Sweep GitHub for leaked secrets and exposed credentials with git-hound

Search public GitHub broadly for leaked secrets and triage exposures when the workflow is recon and remediation, not generic secret scanning.

## Prerequisites

git-hound binary, GitHub token or code search access, and operator-defined dork queries

## Installation

Use the upstream install or setup path that matches your environment:
- docker build -t my-githound-container .
- docker run -v /path/to/config.yaml:/root/.githound/config.yaml -v $(pwd)/data:/data my-githound-container --subdomain-file /data/subdomains.txt

Requirements and caveats from upstream:
- ## Building the Docker Image
- To build the Docker image for Git-Hound, use the following command:
- This command builds the Docker image with the tag my-githound-container. You can change the tag name to your preference.

Basic usage or getting-started notes:
- Example config.yaml:
- Use the following command to run the container with your configuration and input files:

- Source: https://github.com/tillson/git-hound
- Extracted from upstream docs: https://raw.githubusercontent.com/tillson/git-hound/HEAD/README.md

## Documentation

- https://github.com/tillson/git-hound#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sweep-github-for-leaked-secrets-and-exposed-credentials-with-git-hound/)
