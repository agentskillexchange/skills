---
name: "Reduce agent token burn on repo-scale coding commands with the rtk CLI proxy"
slug: "reduce-agent-token-burn-on-repo-scale-coding-commands-with-the-rtk-cli-proxy"
description: "Use rtk when an agent keeps wasting context on noisy shell output from large repos and you need smaller command responses before the model sees them."
github_stars: 25419
verification: "security_reviewed"
source: "https://github.com/rtk-ai/rtk"
author: "RTK AI"
publisher_type: "company"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "rtk-ai/rtk"
  github_stars: 25419
---

# Reduce agent token burn on repo-scale coding commands with the rtk CLI proxy

Use rtk when an agent keeps wasting context on noisy shell output from large repos and you need smaller command responses before the model sees them.

## Prerequisites

A shell-heavy coding-agent workflow, a supported agent such as Claude Code, Codex, Cursor, Gemini CLI, or Cline/Roo, and permission to install a local RTK hook or call rtk directly.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
<p>Install <code>rtk</code> with Homebrew, the upstream install script, or a Git-based install, then run <code>rtk init -g</code> or the agent-specific init flag for your tool. Restart the agent shell afterward so commands like <code>git</code>, <code>grep</code>, and test runners are routed through RTK's output filters.</p>
```

## Documentation

- https://www.rtk-ai.app/guide

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/reduce-agent-token-burn-on-repo-scale-coding-commands-with-the-rtk-cli-proxy/)
