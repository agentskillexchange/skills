---
name: "Investigate repository failures with an evidence-backed Archon workflow"
slug: "investigate-repository-failures-evidence-backed-archon-workflow"
description: "Run Archon’s bounded investigation workflow to reproduce a repository failure, establish its cause and hand off a saved evidence report before implementation."
github_stars: 23908
verification: "security_reviewed"
source: "https://github.com/coleam00/Archon"
author: "coleam00"
publisher_type: "open_source"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "coleam00/Archon"
  github_stars: 23908
---

# Investigate repository failures with an evidence-backed Archon workflow

Run Archon’s bounded investigation workflow to reproduce a repository failure, establish its cause and hand off a saved evidence report before implementation.

## Prerequisites

Git; Archon; configured Claude Code, Codex or Pi provider; project reproduction dependencies

## Installation

Install or set up from the source-backed instructions:

Install Archon using the upstream platform guide; the documented Homebrew route is brew install coleam00/archon/archon, followed by archon setup. Configure an authenticated Claude Code, Codex or Pi provider. In the target repository, use archon workflow list and confirm archon-investigate is available. Use a version containing the cited investigation contract; the inspected dev commit is 086aff57836fd0ba087f7ffeb5625a4c8a67c53e, and released versions may differ. Optional archon skill add installs agent guidance. No installation was executed during metadata review.

- Source: https://github.com/coleam00/Archon

## Documentation

- https://github.com/coleam00/Archon/blob/086aff57836fd0ba087f7ffeb5625a4c8a67c53e/.archon/workflows/sdlc/investigate/archon-investigate.yaml

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/investigate-repository-failures-evidence-backed-archon-workflow/)
