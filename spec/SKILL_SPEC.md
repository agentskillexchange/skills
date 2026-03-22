# Agent Skill Specification v1.0

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
verification: string    # Required — verification tier
rating: number          # Optional — community rating (1.0–5.0)
reviews: number         # Optional — number of reviews
creator: string         # Required — creator display name
creator_handle: string  # Optional — GitHub or marketplace handle
creator_verified: bool  # Optional — whether creator is verified
source: string          # Optional — URL to skill on agentskillexchange.com
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

The verification tier of the skill. Set by the marketplace, not by contributors.

| Value | Meaning |
|-------|---------|
| `listed` | Published and indexed. Basic format validation only. |
| `verified_metadata` | Frontmatter, source links, and install instructions confirmed accurate. |
| `security_reviewed` | Content reviewed for prompt injection, data exfiltration, and malicious patterns. |

#### `rating` (optional, number)

Community rating from 1.0 to 5.0. Set by the marketplace based on user reviews. Contributors should not set this field.

#### `reviews` (optional, number)

Total number of user reviews. Set by the marketplace.

#### `creator` (required, string)

Display name of the skill creator.

#### `creator_handle` (optional, string)

GitHub username or marketplace handle of the creator.

#### `creator_verified` (optional, boolean)

Whether the creator has been verified on the marketplace. Default: `false`.

#### `source` (optional, string)

URL to the skill's page on agentskillexchange.com.

## Markdown Body

The body follows the frontmatter and contains:

1. **Title** — H1 heading matching the skill name
2. **Description** — One or more paragraphs explaining the skill
3. **Installation** — Commands for supported agents
4. **Creator** (optional) — Attribution line

### Example

```markdown
# Stripe Webhook Signature Verifier

Verifies Stripe webhook payload signatures using HMAC-SHA256 to prevent
replay attacks and forged events. Supports both test and live mode keys.

## Installation

### Any agent (npx skills)

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

---

*Created by [Creator Name](https://agentskillexchange.com/creator/handle)*
```

## Validation Rules

A valid SKILL.md must:

1. Have valid YAML frontmatter between `---` delimiters
2. Include all required fields (`name`, `description`, `category`, `framework`, `verification`, `creator`)
3. Use a valid category from the list above
4. Use a valid framework from the list above
5. Use a valid verification tier (`listed`, `verified_metadata`, `security_reviewed`)
6. Have `rating` between 1.0 and 5.0 if present
7. Have a markdown body with at least a title and description

## Versioning

This spec follows semantic versioning. The current version is **1.0**.

Changes to required fields or validation rules increment the major version. New optional fields increment the minor version.
