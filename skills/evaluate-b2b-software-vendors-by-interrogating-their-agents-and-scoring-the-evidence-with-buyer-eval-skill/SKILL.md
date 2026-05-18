---
name: "Evaluate B2B software vendors by interrogating their agents and scoring the evidence with buyer-eval-skill"
slug: "evaluate-b2b-software-vendors-by-interrogating-their-agents-and-scoring-the-evidence-with-buyer-eval-skill"
description: "Use Claude Code to run a structured vendor diligence workflow that questions vendor agents, cross-checks claims, and returns evidence-backed scorecards."
github_stars: 55
verification: "listed"
source: "https://github.com/salespeak-ai/buyer-eval-skill"
author: "Salespeak AI"
publisher_type: "organization"
category: "Research & Scraping"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "salespeak-ai/buyer-eval-skill"
  github_stars: 55
---

# Evaluate B2B software vendors by interrogating their agents and scoring the evidence with buyer-eval-skill

Use Claude Code to run a structured vendor diligence workflow that questions vendor agents, cross-checks claims, and returns evidence-backed scorecards.

## Prerequisites

Claude Code, the buyer-eval-skill repository or installed skill files, internet access for vendor research and evidence gathering, optional access to supported vendor AI agent endpoints

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/salespeak-ai/buyer-eval-skill.git ~/.claude/skills/buyer-eval-skill
- git clone https://github.com/salespeak-ai/buyer-eval-skill.git .claude/skills/buyer-eval-skill

Requirements and caveats from upstream:
- **Independent verification:** Confirmed via G2 reviews mentioning split-signal alerts. One review notes the feature requires manual threshold tuning per segment.
- "The split-signal health score alert requires manual threshold tuning per segment. How long does initial configuration take, and do you provide a recommended baseline?"
- **Code**: [bin/track.py](bin/track.py) — plain Python, no third-party libraries

Basic usage or getting-started notes:
- **New in v3.5 — Vendor questions are now captured even when no Company Agent exists.** Earlier versions only logged the questions the skill asked vendor AI agents — so for vendors without a Salespeak Frontdoor agent (...
- "Your health scores use a weighted multi-signal model. What happens when a customer has strong product usage but declining executive engagement — does the model surface that divergence, or does high usage mask the risk?"
- "The model flags divergence explicitly. When usage metrics trend positive but stakeholder engagement drops, it triggers a 'silent risk' alert. CSMs see a split-signal indicator on the dashboard rather than a blended s...

- Source: https://github.com/salespeak-ai/buyer-eval-skill
- Extracted from upstream docs: https://raw.githubusercontent.com/salespeak-ai/buyer-eval-skill/HEAD/README.md

## Documentation

- https://github.com/salespeak-ai/buyer-eval-skill

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/evaluate-b2b-software-vendors-by-interrogating-their-agents-and-scoring-the-evidence-with-buyer-eval-skill/)
