---
title: "watchexec File Watcher and Command Re-Runner"
slug: "watchexec-file-watcher-command-rerunner"
verification: "security_reviewed"
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

Choose the method that fits your setup:

1. Clone or download this repo and copy the skill folder into your local skills directory.
2. Install from the Agent Skill Exchange repo with your preferred Git workflow.
3. Add the skill folder as a git submodule if you manage skills as dependencies.
4. Copy the files manually into a local custom-skills directory for testing.
5. Use any marketplace or sync tooling you already have for pulling ASE skills.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/watchexec-file-watcher-command-rerunner/)
