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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Download git-hound from GitHub Releases, configure the required GitHub access in config.yml, then run dork or keyword searches to scan matching repositories and histories for leaked secrets.
```

## Documentation

- https://github.com/tillson/git-hound#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sweep-github-for-leaked-secrets-and-exposed-credentials-with-git-hound/)
