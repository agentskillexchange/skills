# Agent Skill Specification v1.1

This document defines the format for skills in the Agent Skill Exchange.

## Overview

A skill is a directory containing a `SKILL.md` file. The file has two parts:

1. **YAML frontmatter** — structured metadata between `---` delimiters
2. **Markdown body** — human-readable description and install instructions

## Directory Structure

```
skills/
  <slug>/
    SKILL.md        # Required — skill definition
    references/     # Optional — supporting files
    scripts/        # Optional — automation scripts
```

The `<slug>` is a URL-safe identifier: lowercase, hyphens instead of spaces, no special characters.

## Frontmatter Schema

```yaml
---
name: string            # Required — display name
description: string     # Required — what the skill does and when to use it
category: string        # Required — one of the valid categories
framework: string       # Required — primary framework
verification: string    # Required — listed or security_reviewed
source: string          # Optional — URL to skill on agentskillexchange.com
tool_ecosystem:         # Optional — only if backed by a real tool
  tool: string          # Tool identifier
  github_stars: number  # Stars on the tool's repo
  npm_weekly_downloads: number  # npm weekly downloads
  github_repo: string   # owner/repo
  license: string       # SPDX license identifier
  maintained: boolean   # Whether the tool is actively maintained
---
```

### Field Definitions

#### `name` (required, string)

The human-readable display name of the skill. Should be concise and descriptive.

**Examples**: `"Stripe Webhook Verifier"`, `"GitHub Actions Workflow Generator"`

#### `description` (required, string)

A one-paragraph description of what the skill does and when to use it. Should reference specific APIs, tools, or techniques. Avoid vague language.

**Good**: `"Verifies Stripe webhook payload signatures using HMAC-SHA256 to prevent replay attacks and forged events."`

**Bad**: `"A helpful tool for working with Stripe."`

#### `category` (required, string)

One of the 17 valid categories. Must match exactly.

| Category | Description |
|----------|-------------|
| Browser Automation | Navigation, login flows, form handling, screenshots |
| Calendar, Email & Productivity | Calendar, email, scheduling, productivity tools |
| CI/CD Integrations | Pipelines, workflows, deployment, CI templates |
| Code Quality & Review | Linters, reviewers, test generators, coverage |
| Content Writing & SEO | SEO, content generation, editorial workflows |
| Data Extraction & Transformation | Schema validation, ETL, data mapping, conversion |
| Developer Tools | Coding agents, repo tools, scaffolders, terminal |
| Image & Creative Automation | Image generation, editing, design automation |
| Integrations & Connectors | Third-party connectors, webhooks, API bridges |
| Library & API Reference | SDK docs, API parsers, symbol resolvers |
| Media & Transcription | Audio transcription, video processing, media tools |
| Monitoring & Alerts | Error tracking, uptime, alerting, observability |
| Research & Scraping | Web research, content discovery, data collection |
| Runbooks & Diagnostics | Incident response, diagnostics, troubleshooting |
| Security & Verification | Vulnerability scanning, signature verification |
| Templates & Workflows | Scaffolders, boilerplate generators, automation |
| WordPress & CMS | WordPress, theme/plugin dev, CMS automation |

#### `framework` (required, string)

The primary framework this skill targets. Valid values:

- `Claude Code`
- `Claude Agents`
- `ChatGPT Agents`
- `Codex`
- `Cursor`
- `Custom Agents`
- `Gemini`
- `Google Workspace`
- `MCP-compatible`
- `OpenClaw`
- `WordPress`

#### `verification` (required, string)

The trust tier of the skill.

| Value | Meaning |
|-------|---------|
| `listed` | Published — backed by a real tool, repo, or package |
| `security_reviewed` | Content scanned for malicious patterns — safe to use |

New skills enter as `listed`. Security review is handled by the marketplace team in batches.

#### `source` (optional, string)

URL to the skill's page on agentskillexchange.com. Uses `/skills/` path.

#### `tool_ecosystem` (optional, object)

Only include if the skill is backed by a real tool with verifiable signals. All sub-fields are optional — include only those with real data.

## Markdown Body

The body follows the frontmatter and contains:

1. **Title** — H1 heading matching the skill name
2. **Description** — One or more paragraphs explaining the skill
3. **Installation** — Commands for supported agents

### Example

```markdown
# Stripe Webhook Signature Verifier

Verifies Stripe webhook payload signatures using HMAC-SHA256 to prevent
replay attacks and forged events. Supports both test and live mode keys.

## Installation

### Any Agent

\`\`\`bash
npx skills add agentskillexchange/skills --skill stripe-webhook-verifier
\`\`\`

### Claude Code

\`\`\`bash
npx skills add agentskillexchange/skills --skill stripe-webhook-verifier -a claude-code
\`\`\`

### OpenClaw

\`\`\`bash
clawhub install stripe-webhook-verifier
\`\`\`
```

## Validation Rules

A valid SKILL.md must:

1. Have valid YAML frontmatter between `---` delimiters
2. Include all required fields (`name`, `description`, `category`, `framework`, `verification`)
3. Use a valid category from the list above
4. Use a valid framework from the list above
5. Use a valid verification tier (`listed` or `security_reviewed`)
6. Have a markdown body with at least a title and description

## Versioning

This spec follows semantic versioning. The current version is **1.1**.

Changes to required fields or validation rules increment the major version. New optional fields increment the minor version.
