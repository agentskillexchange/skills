---
title: "semantic-release Automated Versioning and Release Publishing"
description: "semantic-release automates version calculation, changelog generation, tagging, and package publishing from conventional commits and CI runs. It fits agent workflows that need repeatable release automation across npm and other release targets without manual version bumps."
slug: "semantic-release-automated-versioning-and-release-publishing"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/semantic-release/semantic-release"
listed: true
---

# semantic-release Automated Versioning and Release Publishing

semantic-release automates version calculation, changelog generation, tagging, and package publishing from conventional commits and CI runs. It fits agent workflows that need repeatable release automation across npm and other release targets without manual version bumps.

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
clawhub install semantic-release-automated-versioning-and-release-publishing
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

semantic-release is an open source release automation tool that turns commit history into repeatable package releases. In a skill context, it is a strong fit for agents that need to inspect a repository, verify commit conventions, prepare release configuration, and trigger a release pipeline without manually choosing a version number. The project analyzes conventional commits, determines whether the next release is major, minor, or patch, generates release notes, creates tags, and publishes through configured plugins.
This skill is useful in CI/CD pipelines where an agent needs to standardize release operations across repositories. An agent can validate that a project has a Git repository, a supported Node.js runtime, CI credentials, and a semantic-release configuration, then generate or update configuration files, check branch rules, and explain why a given commit set will or will not produce a release. Because semantic-release supports plugin-driven publishing and notifications, it also integrates well with GitHub releases, npm publishing, changelog generation, and downstream notification steps.
Upstream documentation highlights release workflow support, shareable configurations, and plugin extensibility. That makes it practical for agentic use cases like repository onboarding, release troubleshooting, migration from manual versioning, and organization-wide release policy enforcement. A good implementation can output a proposed configuration, validate commit messages, run dry diagnostics in CI, and document the expected release behavior before publishing.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semantic-release-automated-versioning-and-release-publishing/)
