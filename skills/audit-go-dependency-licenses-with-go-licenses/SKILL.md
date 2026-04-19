---
title: "Audit Go dependency licenses with go-licenses"
description: "Use this skill when an agent needs to inspect the licenses of Go dependencies before a release or policy review. It works well for repositories that need a fast report of transitive modules and their license obligations. Invoke it instead of using go-licenses as a raw product when the job is bounded: scan the Go module graph, produce the license report, and flag dependencies whose terms need review before shipping. This is skill-shaped because the boundary is concrete and narrow, audit Go dependency licenses. It is not a general package-management or legal-tech listing."
source: "https://github.com/google/go-licenses"
verification: "listed"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "google/go-licenses"
  github_stars: 992
---

# Audit Go dependency licenses with go-licenses

Use this skill when an agent needs to inspect the licenses of Go dependencies before a release or policy review. It works well for repositories that need a fast report of transitive modules and their license obligations. Invoke it instead of using go-licenses as a raw product when the job is bounded: scan the Go module graph, produce the license report, and flag dependencies whose terms need review before shipping. This is skill-shaped because the boundary is concrete and narrow, audit Go dependency licenses. It is not a general package-management or legal-tech listing.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-go-dependency-licenses-with-go-licenses/)
