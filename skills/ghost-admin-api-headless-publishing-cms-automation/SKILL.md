---
name: Ghost Admin API Headless Publishing and CMS Automation
description: The Ghost Admin API exposes authenticated operations for posts, pages,
  tags, members, offers, and newsletter publishing. This skill gives agents a concrete
  workflow for structured publishing and operational automation in Ghost-backed sites.
category: "WordPress &amp; CMS"
framework: Custom Agents
verification: security_reviewed
source: "https://ghost.org/docs/admin-api/"
---
# Ghost Admin API Headless Publishing and CMS Automation

The Ghost Admin API exposes authenticated operations for posts, pages, tags, members, offers, and newsletter publishing. This skill gives agents a concrete workflow for structured publishing and operational automation in Ghost-backed sites.

The Ghost Admin API is the authenticated API surface for managing content and operational objects inside Ghost. This skill uses the Ghost Admin API and the official JavaScript client library to help agents create drafts, update posts, schedule publication, manage tags, inspect members-related data, and automate editorial workflows without relying on brittle browser clicks. It is especially useful for teams running Ghost as a headless CMS, newsletter platform, or publishing system where repeatable API calls matter more than manual dashboard work.

A typical workflow starts with API authentication, then moves into concrete content operations such as listing posts, creating a draft, updating the lexical or HTML content payload, assigning authors or tags, and publishing or scheduling the item. The skill can also help interpret the difference between Ghost’s content APIs and admin APIs, explain authentication requirements, and map an editorial request into the correct resource operation. Because Ghost powers memberships and newsletters as well as standard publishing, the skill is relevant for automations that connect content release, campaign workflows, and CMS administration.

Expected outputs include valid request shapes, draft or post lifecycle steps, structured mutation plans, troubleshooting notes for auth or payload errors, and reusable examples for posts, pages, tags, and members-related flows. Integration points include server-side scripts, webhook-triggered automations, AI writing pipelines, and editorial review tools. Technical terms central to the skill include Admin API keys, JWT authentication, posts endpoints, tags, members, newsletters, scheduling, and headless publishing. Anchoring the workflow to the Ghost Admin API gives the agent a precise, source-backed way to operate Ghost rather than hand-waving around generic CMS publishing tasks.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ghost-admin-api-headless-publishing-cms-automation
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ghost-admin-api-headless-publishing-cms-automation -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ghost-admin-api-headless-publishing-cms-automation -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ghost-admin-api-headless-publishing-cms-automation -a codex
```

### OpenClaw

```bash
clawhub install ghost-admin-api-headless-publishing-cms-automation
```


## Source

- [ghost.org](https://ghost.org/docs/admin-api/)
