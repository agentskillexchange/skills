---
title: "Diagnose WordPress repo structure and route follow-up work safely"
description: "This skill inspects a WordPress codebase, identifies what kind of project it is, and returns the signals an agent needs before touching files or running tools. Use it when you need a deterministic first pass instead of guessing whether a repo is a plugin, block theme, site, core checkout, or mixed workspace."
verification: "security_reviewed"
source: "https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-project-triage"
category:
  - "WordPress & CMS"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "wordpress/agent-skills"
  github_stars: 1219
---

# Diagnose WordPress repo structure and route follow-up work safely

This entry is based on the wp-project-triage skill from the official WordPress/agent-skills repository. The agent behavior is narrow and practical: inspect a WordPress repository, classify what kind of codebase it is, surface tooling and version hints, and produce a structured report that tells the next skill what guardrails to follow. That makes it useful before editing code, running tests, or invoking more specialized WordPress workflows.

Use this when a user drops an unfamiliar WordPress repo into an agent session and wants safe next steps. It is the right invocation when the question is not yet “build a block” or “debug a REST route,” but “what exactly is this repo and what workflows fit it?” The skill is valuable because it reduces wrong assumptions. A plugin repo, a block theme, a Gutenberg checkout, and a full site each need different commands, conventions, and risk boundaries.

The scope boundary is clear. This is not a listing for WordPress itself, a generic repo scanner, or a general framework card. The agent is not being asked to “use WordPress normally.” It is being asked to run deterministic detection, interpret project signals, and route follow-up work safely. Integration points include filesystem inspection, Node-based detector scripts, downstream WordPress skills, and any agent workflow that needs a trustworthy project-kind report before it acts.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/diagnose-wordpress-repo-structure-and-route-follow-up-work-safely/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/diagnose-wordpress-repo-structure-and-route-follow-up-work-safely
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/diagnose-wordpress-repo-structure-and-route-follow-up-work-safely`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diagnose-wordpress-repo-structure-and-route-follow-up-work-safely/)
