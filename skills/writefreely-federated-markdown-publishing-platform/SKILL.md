---
name: "WriteFreely Federated Markdown Publishing Platform with ActivityPub"
description: "WriteFreely is a clean, minimalist self-hosted publishing platform built in Go for writers. It features a distraction-free Markdown editor, ActivityPub federation for cross-platform community building, multi-blog support from a single account, and OAuth 2.0 integration for onboarding users from existing platforms."
category: "Content Writing & SEO"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/writefreely/writefreely"
tool_ecosystem:
  github_repo: "writefreely/writefreely"
  github_stars: 5117
  license: "AGPL-3.0"
---
# WriteFreely Federated Markdown Publishing Platform with ActivityPub

WriteFreely is a clean, minimalist self-hosted publishing platform built in Go for writers. It features a distraction-free Markdown editor, ActivityPub federation for cross-platform community building, multi-blog support from a single account, and OAuth 2.0 integration for onboarding users from existing platforms.

WriteFreely is a self-hosted, open-source writing and publishing platform built in Go. Designed around a plain, auto-saving Markdown editor, it provides writers with a distraction-free environment for blogging, knowledge sharing, and community building. Published content renders cleanly with a focus on readability, and the platform supports both individual blogs and multi-user instances.



Federation and Community

WriteFreely integrates with the ActivityPub protocol, enabling federated publishing across the Fediverse. Posts published on a WriteFreely instance can be followed from Mastodon, Pleroma, and other ActivityPub-compatible platforms. This allows writers to build an audience without relying on centralized social networks. Readers can follow individual blogs or entire instances using their existing Fediverse accounts.



Multi-Blog and Organization Support

Each user account can create multiple blogs with distinct identities, URLs, and content. This supports pen names, topic-focused publications, and organizational knowledge bases. Blogs can be configured as public, unlisted, or private. WriteFreely also supports pinned posts for creating static pages, hashtag-based categorization, and draft management for works in progress.



Privacy and Internationalization

WriteFreely collects minimal data by default and never publicizes more information than a writer consents to share. The platform does not track readers or inject analytics. Blog elements are localized in over 20 languages with first-class support for non-Latin scripts and right-to-left languages including Arabic and Hebrew.



Deployment and API

WriteFreely deploys as a single binary with built-in SQLite support, or can connect to MySQL or PostgreSQL databases. Pre-built binaries are available for Linux, macOS, FreeBSD, and Windows. Docker images are published to GitHub Container Registry. The platform exposes a REST API for programmatic content management, making it suitable for integration with AI agents that need to publish, edit, or manage blog content programmatically.



Installation

Download pre-built binaries from the GitHub releases page, install from the AUR on Arch Linux, or run the official Docker image. Configuration is handled through a simple INI file. The hosted version at Write.as provides managed WriteFreely instances for those who prefer not to self-host.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill writefreely-federated-markdown-publishing-platform
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill writefreely-federated-markdown-publishing-platform -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill writefreely-federated-markdown-publishing-platform -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill writefreely-federated-markdown-publishing-platform -a codex
```

### OpenClaw

```bash
clawhub install writefreely-federated-markdown-publishing-platform
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/writefreely-federated-markdown-publishing-platform/)
