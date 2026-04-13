---
title: "Regression-test prompts, agents, and RAG outputs before shipping changes"
description: "Use promptfoo when an agent needs to evaluate prompt, agent, or RAG behavior against saved assertions before a change goes live. The value here is the repeatable evaluation workflow, not a generic AI tooling catalog entry."
verification: "security_reviewed"
source: "https://github.com/promptfoo/promptfoo"
category: ["Code Quality &amp; Review"]
framework: ["Multi-Framework"]
tool_ecosystem:
  github_repo: "promptfoo/promptfoo"
  github_stars: 20007
---

# Regression-test prompts, agents, and RAG outputs before shipping changes

Use promptfoo when an agent needs to evaluate prompt, agent, or RAG behavior against saved assertions before a change goes live. The value here is the repeatable evaluation workflow, not a generic AI tooling catalog entry.

## Installation

Choose the install path that fits your setup:

1. Install from the Agent Skill Exchange catalog if your agent client supports it.
2. Copy the skill folder into your local skills directory.
3. Add it as a git submodule in your shared agent-skills repo.
4. Vendor the files directly into a project-specific `.agents/skills/` or equivalent folder.
5. Keep a fork or mirror if you need local modifications or pinned revisions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/regression-test-prompts-agents-and-rag-outputs-before-shipping-changes/)
