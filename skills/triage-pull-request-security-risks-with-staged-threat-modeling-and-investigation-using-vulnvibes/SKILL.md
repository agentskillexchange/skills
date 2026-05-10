---
title: "Triage pull request security risks with staged threat modeling and investigation using VulnVibes"
slug: "triage-pull-request-security-risks-with-staged-threat-modeling-and-investigation-using-vulnvibes"
description: "Analyze a GitHub pull request for security impact, run targeted vulnerability-investigation skills when Stage 1 finds credible threats, and return a structured verdict instead of doing an ad hoc manual review."
github_stars: 17
verification: "security_reviewed"
source: "https://github.com/anshumanbh/vulnvibes"
author: "anshumanbh"
publisher_type: "individual"
category: "Security & Verification"
framework: "Claude Agents"
tool_ecosystem:
  github_repo: "anshumanbh/vulnvibes"
  github_stars: 17
---

# Triage pull request security risks with staged threat modeling and investigation using VulnVibes

Analyze a GitHub pull request for security impact, run targeted vulnerability-investigation skills when Stage 1 finds credible threats, and return a structured verdict instead of doing an ad hoc manual review.

## Prerequisites

GitHub token, Anthropic API key, access to the target GitHub pull request

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
git clone https://github.com/anshumanbh/vulnvibes.git && cd vulnvibes && pip install -e ".[dev]"; set GITHUB_TOKEN and ANTHROPIC_API_KEY; run `vulnvibes pr analyze <PR_URL>`
```

## Documentation

- https://github.com/anshumanbh/vulnvibes

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/triage-pull-request-security-risks-with-staged-threat-modeling-and-investigation-using-vulnvibes/)
