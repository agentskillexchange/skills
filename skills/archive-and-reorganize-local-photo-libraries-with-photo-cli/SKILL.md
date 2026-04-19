---
title: "Archive and reorganize local photo libraries with photo-cli"
description: "Best for: large local photo collections that need metadata-driven cleanup, copy, or archive passes before manual review or import into another system. photo-cli is a filesystem-first photo organizer. It extracts capture time and location metadata, supports reverse geocoding, and can archive or copy media into a new folder structure with consistent naming strategies. That gives agents a concrete library-normalization job with a visible output tree. When to invoke it Invoke this skill when you want an agent to reorganize an existing media library on disk, preserve originals, and produce a cleaner archive layout before downstream cataloging or backup. Scope boundary This is not a generic photo product listing. The skill boundary is a local archive transformation pass: read metadata from files, choose an organization strategy, and write a reorganized destination tree plus local metadata records. Install notes Install photo-cli from its documented package, container, or release method. Point it at the source library and choose the archive or copy mode. Run the archive workflow to build the reorganized output folder."
source: "https://github.com/photo-cli/photo-cli"
verification: "listed"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "photo-cli/photo-cli"
  github_stars: 68
---

# Archive and reorganize local photo libraries with photo-cli

Best for: large local photo collections that need metadata-driven cleanup, copy, or archive passes before manual review or import into another system. photo-cli is a filesystem-first photo organizer. It extracts capture time and location metadata, supports reverse geocoding, and can archive or copy media into a new folder structure with consistent naming strategies. That gives agents a concrete library-normalization job with a visible output tree. When to invoke it Invoke this skill when you want an agent to reorganize an existing media library on disk, preserve originals, and produce a cleaner archive layout before downstream cataloging or backup. Scope boundary This is not a generic photo product listing. The skill boundary is a local archive transformation pass: read metadata from files, choose an organization strategy, and write a reorganized destination tree plus local metadata records. Install notes Install photo-cli from its documented package, container, or release method. Point it at the source library and choose the archive or copy mode. Run the archive workflow to build the reorganized output folder.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/archive-and-reorganize-local-photo-libraries-with-photo-cli/)
