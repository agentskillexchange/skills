---
title: "Run terminal-native repo analysis, edits, and command loops with Gemini in a bounded CLI workflow with Gemini CLI"
description: "Lets an agent use Gemini from the terminal to inspect repositories, edit files, run shell commands, and ground work with built-in search and local context."
verification: listed
source: "https://github.com/google-gemini/gemini-cli"
category:
  - "Developer Tools"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "google-gemini/gemini-cli"
  github_stars: 101569
---

# Run terminal-native repo analysis, edits, and command loops with Gemini in a bounded CLI workflow with Gemini CLI

Use Gemini CLI when an agent needs a terminal-first Gemini workflow for repo inspection, edits, shell actions, and multimodal or search-grounded inputs without leaving the command line. It fits large-context codebase analysis, shell-assisted debugging, and turning local artifacts into implementation work.

Invoke this instead of using Gemini normally in a web app or raw API flow when the agent must stay inside a bounded terminal loop over local files and commands. This is skill-shaped because the scope boundary is specific: repo and shell work through Gemini CLI. It is not a generic Gemini product, model API, or broad chat listing.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/run-terminal-native-repo-analysis-edits-and-command-loops-with-gemini-in-a-bounded-cli-workflow-with-gemini-cli
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/run-terminal-native-repo-analysis-edits-and-command-loops-with-gemini-in-a-bounded-cli-workflow-with-gemini-cli` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-terminal-native-repo-analysis-edits-and-command-loops-with-gemini-in-a-bounded-cli-workflow-with-gemini-cli/)
