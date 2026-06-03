---
name: "Staff Engineer Mode"
slug: "staff-engineer-mode"
description: "Routes engineering design, delivery, reliability, security, operations, and maintenance prompts to one native router skill backed by specialist guidance for Claude Code, Codex, Cursor, OpenCode, Copilot, and Gemini."
category: "Developer Tools"
framework: "Multi-Framework"
verification: listed
source: "https://github.com/sirmarkz/staff-engineer-mode"
---

# Staff Engineer Mode

Staff Engineer Mode packages major-outage lessons as one router skill for AI
coding agents. Use it when engineering prompts need production judgment across
architecture, reliability, security, delivery, operations, maintenance,
documentation lifecycle, platform, data, or release work. The upstream repo
exposes one native `staff-engineer-mode` router instead of 54 separate installed
skills. The router classifies the artifact and phase, then loads one primary
specialist from the repo's `specialists/` directory. That keeps startup context
small while preserving targeted guidance for design reviews, incident handling,
release readiness, security checks, API compatibility, SLOs, migration work, and
operational documentation. The project includes `.claude-plugin` and
`.codex-plugin` manifests plus install paths for Cursor, OpenCode, GitHub
Copilot CLI, and Gemini CLI.

Install from the upstream repository so the router can load its specialist
files. Copying only this catalog entry will not include the specialist guidance.

## Installation

### Claude Code

```bash
claude plugin marketplace add https://github.com/sirmarkz/staff-engineer-mode.git
claude plugin install staff-engineer-mode@staff-engineer-mode
```

### Codex

```bash
codex plugin marketplace add https://github.com/sirmarkz/staff-engineer-mode.git
codex plugin add staff-engineer-mode@staff-engineer-mode
```

### Direct Repo

```bash
git clone https://github.com/sirmarkz/staff-engineer-mode.git
```

See the upstream README for Cursor, OpenCode, GitHub Copilot CLI, and Gemini CLI
installation commands.
