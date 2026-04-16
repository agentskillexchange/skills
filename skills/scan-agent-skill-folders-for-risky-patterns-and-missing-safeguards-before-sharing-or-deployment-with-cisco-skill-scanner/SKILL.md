---
title: "Scan agent skill folders for risky patterns and missing safeguards before sharing or deployment with Cisco Skill Scanner"
description: "Run a pre-trust security pass over skill packs and prompt bundles before they get shared, merged, or deployed."
verification: "listed"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-agent-skill-folders-for-risky-patterns-and-missing-safeguards-before-sharing-or-deployment-with-cisco-skill-scanner/)
