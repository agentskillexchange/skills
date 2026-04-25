---
title: "Archive and reorganize local photo libraries with photo-cli"
description: "Use photo-cli when an agent needs to normalize a local photo archive by reading capture metadata, reverse geocoding locations, and rebuilding a cleaner folder structure without moving into a hosted photo platform."
verification: "security_reviewed"
source: "https://github.com/photo-cli/photo-cli"
category:
  - "Image & Creative Automation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "photo-cli/photo-cli"
  github_stars: 68
---

# Archive and reorganize local photo libraries with photo-cli

Best for: large local photo collections that need metadata-driven cleanup, copy, or archive passes before manual review or import into another system.

photo-cli is a filesystem-first photo organizer. It extracts capture time and location metadata, supports reverse geocoding, and can archive or copy media into a new folder structure with consistent naming strategies. That gives agents a concrete library-normalization job with a visible output tree.

When to invoke it
Invoke this skill when you want an agent to reorganize an existing media library on disk, preserve originals, and produce a cleaner archive layout before downstream cataloging or backup.

Scope boundary
This is not a generic photo product listing. The skill boundary is a local archive transformation pass: read metadata from files, choose an organization strategy, and write a reorganized destination tree plus local metadata records.

Install notes

Install photo-cli from its documented package, container, or release method.
Point it at the source library and choose the archive or copy mode.
Run the archive workflow to build the reorganized output folder.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/archive-and-reorganize-local-photo-libraries-with-photo-cli/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/archive-and-reorganize-local-photo-libraries-with-photo-cli
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/archive-and-reorganize-local-photo-libraries-with-photo-cli`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/archive-and-reorganize-local-photo-libraries-with-photo-cli/)
