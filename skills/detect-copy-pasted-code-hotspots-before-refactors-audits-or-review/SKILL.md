---
title: "Detect copy-pasted code hotspots before refactors, audits, or review"
description: "Use jscpd when an agent needs to scan a codebase for duplicated blocks and turn clone findings into a focused cleanup or review queue. The skill is about duplication detection and hotspot reporting, not general linting, testing, or automated refactoring by itself."
verification: security_reviewed
source: "https://www.npmjs.com/package/jscpd"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  npm_package: "jscpd"
  npm_weekly_downloads: 703581
---

# Detect copy-pasted code hotspots before refactors, audits, or review

Tool: jscpd. This skill is for agents that need to inspect a repository and find duplicated code blocks before humans waste time reviewing the same logic in three places or refactoring the wrong area first. jscpd tokenizes source files, compares them across many languages and formats, and returns concrete clone reports that an agent can rank, summarize, or route into a cleanup plan.

When to use it: invoke this skill before a large refactor, during a technical-debt audit, ahead of a code review, or when an agent is trying to explain why a codebase feels harder to change than it should. Without the skill, a user would have to eyeball similar files, depend on vague intuition, or run a generic quality suite that does not isolate duplication as its own maintenance risk. With jscpd, the agent can hand back exact files, repeated fragments, and a prioritized list of hotspots worth deduplicating first.

Scope boundary: this is not a full static-analysis platform, secure-code scanner, or automatic refactoring engine. It does not prove correctness, find vulnerabilities, or rewrite the code for you. Its boundary is tighter and more useful: detect copy-paste duplication and make that duplication visible early enough for a human or downstream tool to act on it.

Integration points: local repository scans, CI checks, pull-request review workflows, architecture audits, and AI-assisted refactor loops. Upstream evidence includes the official jscpd repository, the published npm package, active maintenance, and current package adoption.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/detect-copy-pasted-code-hotspots-before-refactors-audits-or-review
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/detect-copy-pasted-code-hotspots-before-refactors-audits-or-review` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/detect-copy-pasted-code-hotspots-before-refactors-audits-or-review/)
