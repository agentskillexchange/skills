---
name: "Diagnose WordPress repo structure and route follow-up work safely"
description: "This skill inspects a WordPress codebase, identifies what kind of project it is, and returns the signals an agent needs before touching files or running tools. Use it when you need a deterministic first pass instead of guessing whether a repo is a plugin, block theme, site, core checkout, or mixed workspace."
verification: listed
source: "https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-project-triage"
category:
  - "WordPress &amp; CMS"
framework:
  - "Multi-Framework"
---

# Diagnose WordPress repo structure and route follow-up work safely

This entry is based on the wp-project-triage skill from the official WordPress/agent-skills repository. The agent behavior is narrow and practical: inspect a WordPress repository, classify what kind of codebase it is, surface tooling and version hints, and produce a structured report that tells the next skill what guardrails to follow. That makes it useful before editing code, running tests, or invoking more specialized WordPress workflows.
Use this when a user drops an unfamiliar WordPress repo into an agent session and wants safe next steps. It is the right invocation when the question is not yet “build a block” or “debug a REST route,” but “what exactly is this repo and what workflows fit it?” The skill is valuable because it reduces wrong assumptions. A plugin repo, a block theme, a Gutenberg checkout, and a full site each need different commands, conventions, and risk boundaries.
The scope boundary is clear. This is not a listing for WordPress itself, a generic repo scanner, or a general framework card. The agent is not being asked to “use WordPress normally.” It is being asked to run deterministic detection, interpret project signals, and route follow-up work safely. Integration points include filesystem inspection, Node-based detector scripts, downstream WordPress skills, and any agent workflow that needs a trustworthy project-kind report before it acts.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diagnose-wordpress-repo-structure-and-route-follow-up-work-safely/)
