---
title: "Export live HTML slide decks to PDF handouts before review or archival"
description: "This ASE entry is built around DeckTape , the open source CLI from astefanutti/decktape that exports HTML presentations to PDF and can also capture slide screenshots. The agent behavior here is concrete: take a live or locally hosted slide deck URL, detect the presentation format, wait for the deck to load, and produce a distributable artifact that reviewers, approvers, or archive systems can consume without opening the presentation runtime. That makes it a strong fit for release packets, executive review loops, offline backups, conference submission bundles, and compliance archives where “open the deck in a browser” is not a dependable final step. Use this when the slides already exist and an agent needs to package them for someone else. DeckTape supports multiple presentation engines, exposes viewport and timing controls, lets an operator pass custom headers for protected decks, and can export selected slide ranges instead of the whole presentation. In practice, an agent can run it after a Marp, Slidev, Reveal.js, or internal HTML deck build, then attach the resulting PDF to a ticket, upload screenshots to a review thread, or stash the output in artifact storage from CI. The scope boundary is what keeps this skill from collapsing into a product listing. DeckTape is not a slide authoring tool, a design platform, or a generic browser automation framework. It solves the narrow operational problem of rendering already-built HTML presentations into portable review artifacts. That bounded export step, plus clean integrations with Node scripts, Docker, and CI runners, makes it skill-shaped enough for ASE."
source: "https://github.com/astefanutti/decktape"
verification: "security_reviewed"
category:
  - "Templates &amp; Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "astefanutti/decktape"
  github_stars: 2361
---

# Export live HTML slide decks to PDF handouts before review or archival

This ASE entry is built around DeckTape , the open source CLI from astefanutti/decktape that exports HTML presentations to PDF and can also capture slide screenshots. The agent behavior here is concrete: take a live or locally hosted slide deck URL, detect the presentation format, wait for the deck to load, and produce a distributable artifact that reviewers, approvers, or archive systems can consume without opening the presentation runtime. That makes it a strong fit for release packets, executive review loops, offline backups, conference submission bundles, and compliance archives where “open the deck in a browser” is not a dependable final step. Use this when the slides already exist and an agent needs to package them for someone else. DeckTape supports multiple presentation engines, exposes viewport and timing controls, lets an operator pass custom headers for protected decks, and can export selected slide ranges instead of the whole presentation. In practice, an agent can run it after a Marp, Slidev, Reveal.js, or internal HTML deck build, then attach the resulting PDF to a ticket, upload screenshots to a review thread, or stash the output in artifact storage from CI. The scope boundary is what keeps this skill from collapsing into a product listing. DeckTape is not a slide authoring tool, a design platform, or a generic browser automation framework. It solves the narrow operational problem of rendering already-built HTML presentations into portable review artifacts. That bounded export step, plus clean integrations with Node scripts, Docker, and CI runners, makes it skill-shaped enough for ASE.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/export-live-html-slide-decks-to-pdf-handouts-before-review-or-archival/)
