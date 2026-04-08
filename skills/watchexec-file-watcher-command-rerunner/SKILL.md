---
title: "watchexec File Watcher and Command Re-Runner"
slug: "watchexec-file-watcher-command-rerunner"
verification: "security_reviewed"
description: "watchexec is a standalone file-watching tool written in Rust that automatically executes commands when it detects file modifications. It respects .gitignore rules, coalesces rapid filesystem events, and works cross-platform without requiring any language runtime."
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
source: "https://github.com/watchexec/watchexec"
tool_ecosystem:
  github_repo: "watchexec/watchexec"
  github_stars: 6882
---

# watchexec File Watcher and Command Re-Runner

watchexec is a standalone file-watching tool written in Rust that automatically executes commands when it detects file modifications. It respects .gitignore rules, coalesces rapid filesystem events, and works cross-platform without requiring any language runtime.

## Installation

Choose the setup path that fits your environment:

1. Clone or download this skill into your local skills workspace.
2. Install it with ClawHub if it is available there.
3. Copy the folder into your OpenClaw or AgentSkills directory manually.
4. Add it as a git submodule if you manage skills as pinned dependencies.
5. Vendor it directly into a project repo when you need a fixed internal copy.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/watchexec-file-watcher-command-rerunner/)
