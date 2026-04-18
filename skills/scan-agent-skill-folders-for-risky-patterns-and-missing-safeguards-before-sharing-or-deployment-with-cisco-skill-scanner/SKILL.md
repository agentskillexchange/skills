---
title: "Scan agent skill folders for risky patterns and missing safeguards before sharing or deployment with Cisco Skill Scanner"
description: "Run a pre-trust security pass over skill packs and prompt bundles before they get shared, merged, or deployed."
verification: listed
source: "https://github.com/cisco-ai-defense/skill-scanner"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "cisco-ai-defense/skill-scanner"
  github_stars: 1767
---

# Scan agent skill folders for risky patterns and missing safeguards before sharing or deployment with Cisco Skill Scanner

Use Cisco Skill Scanner when the job is to inspect an agent skill package for prompt injection, exfiltration patterns, malicious code, or other risky content before publication or rollout, not to browse a generic security platform. The invoke moment is narrow and repeatable: point the scanner at a skill or prompt-pack repo, run the analyzers, and review findings before trusting the artifact. That boundary, pre-distribution security review for agent skills, makes this a real operator workflow instead of a plain vendor or product card.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/scan-agent-skill-folders-for-risky-patterns-and-missing-safeguards-before-sharing-or-deployment-with-cisco-skill-scanner
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/scan-agent-skill-folders-for-risky-patterns-and-missing-safeguards-before-sharing-or-deployment-with-cisco-skill-scanner` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-agent-skill-folders-for-risky-patterns-and-missing-safeguards-before-sharing-or-deployment-with-cisco-skill-scanner/)
