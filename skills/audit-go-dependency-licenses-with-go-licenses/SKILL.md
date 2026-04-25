---
title: "Audit Go dependency licenses with go-licenses"
description: "Produce a license inventory for Go module dependencies before release, procurement review, or open-source due diligence."
verification: "listed"
source: "https://github.com/google/go-licenses"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "google/go-licenses"
  github_stars: 992
---

# Audit Go dependency licenses with go-licenses

Use this skill when an agent needs to inspect the licenses of Go dependencies before a release or policy review. It works well for repositories that need a fast report of transitive modules and their license obligations. Invoke it instead of using go-licenses as a raw product when the job is bounded: scan the Go module graph, produce the license report, and flag dependencies whose terms need review before shipping. This is skill-shaped because the boundary is concrete and narrow, audit Go dependency licenses. It is not a general package-management or legal-tech listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/audit-go-dependency-licenses-with-go-licenses/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/audit-go-dependency-licenses-with-go-licenses
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/audit-go-dependency-licenses-with-go-licenses`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-go-dependency-licenses-with-go-licenses/)
