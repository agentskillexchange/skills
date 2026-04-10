---
title: "publint Package Export Validation Skill for npm Release Checks"
description: "Use this skill when an agent needs to lint a package before publish, catch broken exports or manifest issues, and explain exactly what will fail for consumers. It is a pre-publish validation workflow centered on publint, not a generic listing for the tool itself."
slug: "publint-package-export-validation-skill-npm-release-checks"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/publint/publint"
tool_ecosystem:
  github_repo: "publint/publint"
  github_stars: 1252
  npm_package: "publint"
  npm_weekly_downloads: 551109
listed: true
---

# publint Package Export Validation Skill for npm Release Checks

Use this skill when an agent needs to lint a package before publish, catch broken exports or manifest issues, and explain exactly what will fail for consumers. It is a pre-publish validation workflow centered on publint, not a generic listing for the tool itself.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install publint-package-export-validation-skill-npm-release-checks
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill teaches an agent how to use publint as a release gate for JavaScript and TypeScript packages. The concrete job is to inspect a package before publish, run publint against the built output, interpret warnings around exports, conditions, module formats, and entry points, and then suggest the smallest safe fix in package.json or build configuration. That is valuable when a package “works on my machine” but breaks for consumers because the published exports map, types entry, or dual ESM and CommonJS setup is wrong.
Invoke this skill when a user is preparing an npm release, debugging broken package consumption in downstream apps, or cleaning up a monorepo package that has accumulated confusing export settings. In those cases the user does not need a broad package-management overview. They need an agent that can run a precise publish-readiness check and translate publint’s findings into concrete release fixes.
The scope boundary is narrow by design. This is not a general npm registry listing, and it is not a generic bundler or TypeScript skill. It is specifically about using publint to validate publish artifacts and package metadata before release. The agent stays focused on exported entry points, type resolution, package conditions, and distribution structure. Common integration points include CI publish jobs, changeset or semantic-release pipelines, library monorepos, and prepublish scripts that should fail fast before a bad package reaches the registry.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/publint-package-export-validation-skill-npm-release-checks/)
