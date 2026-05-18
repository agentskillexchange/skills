---
name: "Back up GitHub, GitLab, Bitbucket, and Forgejo repositories with gitbackup"
slug: "back-up-github-gitlab-bitbucket-and-forgejo-repositories-with-gitbackup"
description: "Run repeatable cross-forge repository backup jobs from one config instead of hand-scripting clone and export steps per provider."
github_stars: 218
verification: "security_reviewed"
source: "https://github.com/amitsaha/gitbackup"
author: "Amit Saha"
publisher_type: "individual"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "amitsaha/gitbackup"
  github_stars: 218
---

# Back up GitHub, GitLab, Bitbucket, and Forgejo repositories with gitbackup

Run repeatable cross-forge repository backup jobs from one config instead of hand-scripting clone and export steps per provider.

## Prerequisites

gitbackup binary or container image, forge access tokens, backup storage

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Download a release binary or use the published container image, provide the needed provider token and backup directory, then run gitbackup against the target service using the documented flags or config file.
```

## Documentation

- https://github.com/amitsaha/gitbackup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/back-up-github-gitlab-bitbucket-and-forgejo-repositories-with-gitbackup/)
