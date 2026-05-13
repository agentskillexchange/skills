---
title: "Scan agent skill folders for risky patterns and missing safeguards before sharing or deployment with Cisco Skill Scanner"
slug: "scan-agent-skill-folders-for-risky-patterns-and-missing-safeguards-before-sharing-or-deployment-with-cisco-skill-scanner"
description: "Run a pre-trust security pass over skill packs and prompt bundles before they get shared, merged, or deployed."
github_stars: 1767
verification: "security_reviewed"
source: "https://github.com/cisco-ai-defense/skill-scanner"
author: "Cisco AI Defense"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "cisco-ai-defense/skill-scanner"
  github_stars: 1767
---

# Scan agent skill folders for risky patterns and missing safeguards before sharing or deployment with Cisco Skill Scanner

Run a pre-trust security pass over skill packs and prompt bundles before they get shared, merged, or deployed.

## Prerequisites

Python 3.10+, skill-scanner package, optional LLM provider credentials for semantic analyzers, and access to the target skill repository or archive

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install cisco-ai-skill-scanner with uv or pip, set any optional analyzer credentials you plan to use, then run the scanner against the target skill folder or repository and review the reported findings before release.
```

## Documentation

- https://cisco-ai-defense.github.io/docs/skill-scanner

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-agent-skill-folders-for-risky-patterns-and-missing-safeguards-before-sharing-or-deployment-with-cisco-skill-scanner/)
