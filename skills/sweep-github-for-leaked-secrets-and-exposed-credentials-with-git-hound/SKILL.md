---
title: "Sweep GitHub for leaked secrets and exposed credentials with git-hound"
description: "Search public GitHub broadly for leaked secrets and triage exposures when the workflow is recon and remediation, not generic secret scanning."
verification: listed
source: "https://github.com/tillson/git-hound"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "tillson/git-hound"
  github_stars: 1400
---

# Sweep GitHub for leaked secrets and exposed credentials with git-hound

Use git-hound when the real task is external secret exposure hunting across public GitHub, especially before incident response, key rotation, or partner notification work. Its scope boundary is crisp: run GitHub dork based searches, inspect matches with contextual detection and history digging, and surface likely credential leaks for follow-up. That makes it skill-shaped and distinct from a generic security product card. The operator is invoking a focused reconnaissance workflow, not browsing a general security platform or SDK.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/sweep-github-for-leaked-secrets-and-exposed-credentials-with-git-hound
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/sweep-github-for-leaked-secrets-and-exposed-credentials-with-git-hound` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sweep-github-for-leaked-secrets-and-exposed-credentials-with-git-hound/)
