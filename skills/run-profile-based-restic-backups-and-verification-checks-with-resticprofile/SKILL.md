---
name: "Run profile-based restic backups and verification checks with resticprofile"
slug: "run-profile-based-restic-backups-and-verification-checks-with-resticprofile"
description: "Execute named restic backup profiles with repeatable backup, retention, prune, check, and restore steps instead of hand-running one-off commands."
github_stars: 1275
verification: "listed"
source: "https://github.com/creativeprojects/resticprofile"
author: "CreativeProjects"
publisher_type: "organization"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "creativeprojects/resticprofile"
  github_stars: 1275
---

# Run profile-based restic backups and verification checks with resticprofile

Execute named restic backup profiles with repeatable backup, retention, prune, check, and restore steps instead of hand-running one-off commands.

## Prerequisites

resticprofile, restic, configured backup backend credentials

## Installation

Basic usage or getting-started notes:
- Create groups of profiles to run sequentially
- Run the forget command before or after a backup (in a section called *retention*)
- Run shell commands before or after running a profile, useful for mounting and unmounting backup disks

- Source: https://github.com/creativeprojects/resticprofile
- Extracted from upstream docs: https://raw.githubusercontent.com/creativeprojects/resticprofile/HEAD/README.md

## Documentation

- https://creativeprojects.github.io/resticprofile/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-profile-based-restic-backups-and-verification-checks-with-resticprofile/)
