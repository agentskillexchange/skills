---
name: "Render pull request architecture diagrams with PR Lens"
slug: "render-pull-request-architecture-diagrams-with-pr-lens"
description: "Have an agent turn a code diff into validated architecture and data-flow diagrams, then attach the rendered SVGs to a pull request."
github_stars: 212
verification: "security_reviewed"
source: "https://github.com/coldteadotai/pr-lens"
author: "Cold Tea"
publisher_type: "open-source project"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "coldteadotai/pr-lens"
  github_stars: 212
  npm_package: "@coldtea/pr-lens-cli"
  npm_weekly_downloads: 672
---

# Render pull request architecture diagrams with PR Lens

Have an agent turn a code diff into validated architecture and data-flow diagrams, then attach the rendered SVGs to a pull request.

## Prerequisites

Node.js 20.11+, npx/npm, Git, PR Lens CLI, GitHub CLI for PR attachment; optional GitHub App or GitHub Actions provider key

## Installation

Install or set up from the source-backed instructions:

Install the bundled agent skill with `npx skills add coldteadotai/pr-lens`. For direct CLI use, run `npx @coldtea/pr-lens-cli@latest validate .pr-lens/graph.json` and `npx @coldtea/pr-lens-cli@latest render .pr-lens/graph.json --theme dark` after the agent writes a graph document.

- Source: https://github.com/coldteadotai/pr-lens

## Documentation

- https://github.com/coldteadotai/pr-lens/tree/main/packages/agent-skill

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/render-pull-request-architecture-diagrams-with-pr-lens/)
