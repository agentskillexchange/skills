# Agent Skill Specification v1.2

This document defines the canonical repository and public JSON format for skills in the Agent Skill Exchange.

## Overview

A skill is a directory containing a `SKILL.md` file. The file has two parts:

1. **YAML frontmatter** — structured metadata between `---` delimiters
2. **Markdown body** — human-readable description and install instructions

## Directory Structure

```text
skills/
  <slug>/
    SKILL.md        # Required — skill definition
    references/     # Optional — supporting files
    scripts/        # Optional — automation scripts
```

The `<slug>` is a URL-safe identifier: lowercase, hyphens instead of spaces, no special characters. It must match the skill directory name.

## Canonical Frontmatter Schema

```yaml
---
title: string          # Required — display title
slug: string           # Required — stable URL/path identifier
description: string    # Required — what the skill does and when to use it
category: string       # Required — one of the valid categories
framework: string      # Required — primary framework
verification: string   # Required — listed or security_reviewed
source: string         # Optional — upstream repo, documentation, package, or canonical source URL
github_stars: number   # Optional — top-level compatibility signal when available
tool_ecosystem:        # Optional — only if backed by a real tool with verified signals
  tool: string
  github_repo: string
  github_stars: number
  npm_package: string
  npm_weekly_downloads: number
  license: string
  maintained: boolean
---
```

### Compatibility aliases

- `title` is canonical. Older generated indexes may expose `name`; new repository frontmatter and public catalog JSON should use `title`.
- `verification` is canonical for public files. WordPress may keep internal `verification_status` metadata, but exports must normalize it to the public values below.

## Field Definitions

### `title` (required, string)

The human-readable display title of the skill. Should be concise and descriptive.

**Examples**: `"Stripe Webhook Verifier"`, `"GitHub Actions Workflow Generator"`

### `slug` (required, string)

The stable URL-safe identifier. It must match the containing directory name under `skills/`.

### `description` (required, string)

A one-paragraph description of what the skill does and when to use it. It should reference specific APIs, tools, or techniques. Avoid vague language.

**Good**: `"Verifies Stripe webhook payload signatures using HMAC-SHA256 to prevent replay attacks and forged events."`

**Bad**: `"A helpful tool for working with Stripe."`

### `category` (required, string)

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
| WordPress & CMS | WordPress, theme/plugin dev, WP-CLI automation, CMS management |

### `framework` (required, string)

The primary framework this skill targets. Valid values:

- `Claude Code`
- `Claude Agents`
- `ChatGPT Agents`
- `Codex`
- `Cursor`
- `Custom Agents`
- `Gemini`
- `Google Workspace`
- `MCP`
- `Multi-Framework`
- `OpenClaw`
- `WordPress`

### `verification` (required, string)

The public trust tier of the skill.

| Value | Meaning |
|-------|---------|
| `listed` | Published — backed by a real tool, repo, package, or documented workflow |
| `security_reviewed` | Content scanned for malicious patterns, prompt injection, and unsafe instructions |

New skills enter as `listed`. Security review is handled by the marketplace team in batches.

### Internal WordPress verification mapping

WordPress may store older/internal values in `verification_status`. Public repo files and JSON indexes must normalize them as:

| Internal value | Public `verification` |
|----------------|------------------------|
| missing / empty | `listed` |
| `listed` | `listed` |
| `verified_metadata` | `listed` |
| `security_reviewed` | `security_reviewed` |

Do not expose `verified_metadata` as a separate public tier.

### `source` (optional, string)

The upstream repo, documentation, package, or canonical source URL that backs the skill. Prefer the original upstream source over the Agent Skill Exchange listing URL when both are available.

### `tool_ecosystem` (optional, object)

Only include if the skill is backed by a real tool with verifiable signals. All sub-fields are optional; include only values with real provenance.

## Canonical Public Catalog JSON

`skills.json` should use the same public naming as frontmatter:

```json
{
  "slug": "playwright-mcp-browser-automation",
  "title": "Playwright MCP Browser Automation",
  "description": "Official Playwright-powered browser control for agent workflows.",
  "category": ["Browser Automation"],
  "framework": ["Claude Code", "Cursor", "MCP", "OpenClaw"],
  "verification": "security_reviewed",
  "signals": {
    "tool": "playwright",
    "github_stars": 84874,
    "npm_weekly_downloads": 39806814,
    "license": "Apache-2.0"
  }
}
```

## Markdown Body

The body follows the frontmatter and contains:

1. **Title** — H1 heading matching the skill title
2. **Description** — One or more paragraphs explaining the skill
3. **Installation** — Commands or setup notes for supported agents

### Example

~~~markdown
---
title: Stripe Webhook Signature Verifier
slug: stripe-webhook-signature-verifier
description: Verifies Stripe webhook payload signatures using HMAC-SHA256 to prevent replay attacks and forged events.
category: Security & Verification
framework: Custom Agents
verification: listed
source: https://docs.stripe.com/webhooks/signature
---
# Stripe Webhook Signature Verifier

Verifies Stripe webhook payload signatures using HMAC-SHA256 to prevent
replay attacks and forged events. Supports both test and live mode keys.

## Installation

```bash
npx skills add agentskillexchange/skills --skill stripe-webhook-signature-verifier
```
~~~

## Validation Rules

A valid `SKILL.md` must pass the committed parser-backed validator:

```bash
python3 scripts/validate_skills.py --all
```

The validator must:

1. Parse YAML frontmatter with a real YAML parser, not grep/sed
2. Reject duplicate YAML keys
3. Include all required fields (`title`, `slug`, `description`, `category`, `framework`, `verification`)
4. Validate required field types; canonical public fields are scalar strings unless explicitly documented otherwise
5. Reject deprecated public fields (`name`, `verification_status`, `verified_metadata`)
6. Use a lowercase kebab-case `slug` matching the containing directory name
7. Use a valid category from the public category set; transitional generated buckets such as `General` and `Uncategorized` may be allowed only while the live taxonomy backlog is being cleaned
8. Use a valid framework from the public framework set
9. Use a valid public verification tier (`listed` or `security_reviewed`)
10. Validate `source` as an HTTP(S) URL when present
11. Validate numeric signal fields as numbers, not strings
12. Validate `tool_ecosystem` as an object with typed optional fields
13. Have a markdown body with an H1 heading and enough useful content
14. Emit GitHub Actions annotations in CI

## Versioning

This spec follows semantic versioning. The current version is **1.2**.

Changes to required fields or validation rules increment the major version. New optional fields increment the minor version.
