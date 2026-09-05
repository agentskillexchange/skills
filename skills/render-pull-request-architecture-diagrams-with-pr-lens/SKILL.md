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

Node.js 20.11+, npm/npx, Git, a repository with a bounded code change, and a coding agent capable of writing the upstream graph format. GitHub authentication is needed only for posting to a pull request, not local validation/rendering. The agent-authored path does not require a separate PR Lens model API key.

## Installation

In the project where you want to review a change, install the upstream skill and CLI packages at the reviewed versions:

```bash
npm install --save-dev --save-exact @coldtea/pr-lens-agent-skill@0.1.5 @coldtea/pr-lens-cli@0.2.0
```

For Claude Code, copy both the instructions and their references into the project skill directory:

```bash
mkdir -p .claude/skills/pr-lens
cp node_modules/@coldtea/pr-lens-agent-skill/SKILL.md .claude/skills/pr-lens/
cp -R node_modules/@coldtea/pr-lens-agent-skill/references .claude/skills/pr-lens/
```

For another coding agent, use its documented instruction-loading mechanism to reference the installed `SKILL.md` and accompanying `references` directory; the Claude Code destination is not a universal runtime path. This route uses PR Lens's own packages, not the separate third-party `skills` installer.

- Source: https://github.com/coldteadotai/pr-lens

## Usage and Verification

Ask the agent to read the selected diff and the installed `references/graph-document.md`, then write `.pr-lens/graph.json` describing only that change. Do not run validation before this file exists. Request local diagrams only; do not post or modify a pull request yet.

```bash
npx --no-install pr-lens validate .pr-lens/graph.json
npx --no-install pr-lens render .pr-lens/graph.json --theme dark
```

Fix reported validation errors before rendering. Confirm both commands exit successfully, the generated SVG files open locally, and the depicted components and relationships match the actual diff. Rendering also produces `manifest.json` and `drawn.graph.json` in the output directory. Validation checks the graph contract, not whether the architecture claims are true.

Review package/lockfile changes and generated artifacts. Obtain human approval before attaching diagrams or posting comments to a PR. The separate CLI `analyze` path sends a diff to the configured model provider; it is not required for this agent-authored workflow.

## Documentation

- https://github.com/coldteadotai/pr-lens/tree/main/packages/agent-skill

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/render-pull-request-architecture-diagrams-with-pr-lens/)
