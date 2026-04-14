---
title: "Knip Unused Code and Dependency Finder"
description: "Run Knip to find and remove unused files, dependencies, and exports in JavaScript and TypeScript projects. Reduces bundle size, maintenance burden, and dependency attack surface."
verification: security_reviewed
source: "https://github.com/webpro-nl/knip"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "webpro-nl/knip"
  github_stars: 10806
  npm_package: "knip"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/knip-unused-code-dependency-finder/)
