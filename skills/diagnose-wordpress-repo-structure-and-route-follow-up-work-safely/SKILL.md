---
title: "Diagnose WordPress repo structure and route follow-up work safely"
description: "This entry is based on the wp-project-triage skill from the official WordPress/agent-skills repository. The agent behavior is narrow and practical: inspect a WordPress repository, classify what kind of codebase it is, surface tooling and version hints, and produce a structured report that tells the next skill what guardrails to follow. That makes it useful before editing code, running tests, or invoking more specialized WordPress workflows. Use this when a user drops an unfamiliar WordPress repo into an agent session and wants safe next steps. It is the right invocation when the question is not yet “build a block” or “debug a REST route,” but “what exactly is this repo and what workflows fit it?” The skill is valuable because it reduces wrong assumptions. A plugin repo, a block theme, a Gutenberg checkout, and a full site each need different commands, conventions, and risk boundaries. The scope boundary is clear. This is not a listing for WordPress itself, a generic repo scanner, or a general framework card. The agent is not being asked to “use WordPress normally.” It is being asked to run deterministic detection, interpret project signals, and route follow-up work safely. Integration points include filesystem inspection, Node-based detector scripts, downstream WordPress skills, and any agent workflow that needs a trustworthy project-kind report before it acts."
source: "https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-project-triage"
verification: "security_reviewed"
category:
  - "WordPress &amp; CMS"
framework:
  - "Multi-Framework"
---

# Diagnose WordPress repo structure and route follow-up work safely

This entry is based on the wp-project-triage skill from the official WordPress/agent-skills repository. The agent behavior is narrow and practical: inspect a WordPress repository, classify what kind of codebase it is, surface tooling and version hints, and produce a structured report that tells the next skill what guardrails to follow. That makes it useful before editing code, running tests, or invoking more specialized WordPress workflows. Use this when a user drops an unfamiliar WordPress repo into an agent session and wants safe next steps. It is the right invocation when the question is not yet “build a block” or “debug a REST route,” but “what exactly is this repo and what workflows fit it?” The skill is valuable because it reduces wrong assumptions. A plugin repo, a block theme, a Gutenberg checkout, and a full site each need different commands, conventions, and risk boundaries. The scope boundary is clear. This is not a listing for WordPress itself, a generic repo scanner, or a general framework card. The agent is not being asked to “use WordPress normally.” It is being asked to run deterministic detection, interpret project signals, and route follow-up work safely. Integration points include filesystem inspection, Node-based detector scripts, downstream WordPress skills, and any agent workflow that needs a trustworthy project-kind report before it acts.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diagnose-wordpress-repo-structure-and-route-follow-up-work-safely/)
