---
title: "Knip Unused Code and Dependency Finder"
description: "Run Knip to find and remove unused files, dependencies, and exports in JavaScript and TypeScript projects. Reduces bundle size, maintenance burden, and dependency attack surface."
verification: "security_reviewed"
source: "https://github.com/webpro-nl/knip"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "webpro-nl/knip"
  github_stars: 10806
  ase_npm_package: "knip"
  npm_weekly_downloads: 6061385
---

# Knip Unused Code and Dependency Finder

Overview

Knip is a static analysis tool that finds unused files, dependencies, and exports in JavaScript and TypeScript projects. The name comes from the Dutch word for “cut” — the idea is to knip (cut) dead code before you ship it. By identifying what’s not actually used, Knip helps teams reduce bundle sizes, lower maintenance costs, and shrink their dependency attack surface.

Knip goes beyond simple unused import detection. It traces the full dependency graph of a project, understanding entry points, configuration files, and plugin systems to determine which files, exports, and npm dependencies are truly unreachable. It understands workspaces, monorepos, and the plugin systems of popular tools like ESLint, Jest, Webpack, Next.js, and dozens more.

How It Works

Agents invoke Knip via npx knip in a project directory. Knip analyzes the project structure, reads configuration from knip.json or knip.ts, and produces a report of unused items categorized by type: unused files, unused dependencies, unused devDependencies, unused exports, unused types, and duplicate exports. Each finding includes the file path and specific identifier.

Knip supports all major package managers (npm, pnpm, Yarn, Bun) and understands monorepo workspace configurations. It has built-in compilers for non-standard file types and plugin support for over 100 tools and frameworks, automatically detecting which configuration files to analyze.

Output and Integration

Knip outputs results in multiple formats including human-readable terminal output, JSON for programmatic consumption, and compact mode for CI summaries. It supports auto-fix with --fix for safe removals like unused dependencies in package.json. The project has over 10,000 GitHub stars on GitHub, is MIT licensed, and receives active maintenance with frequent releases. It integrates well into CI/CD pipelines as a code quality gate.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/knip-unused-code-dependency-finder/)
