---
name: "WordPress Content Publisher"
description: "Structured publishing workflow for WordPress drafts, metadata, and content operations."
category: "WordPress & CMS"
framework: "OpenClaw"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/wordpress-content-publisher/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "wordpress"  # from ase_tool_match
  github_stars: 20973  # from ase_github_stars (integer, not string)
  github_repo: "WordPress/WordPress"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# WordPress Content Publisher

Structured publishing workflow for WordPress drafts, metadata, and content operations.

## Overview

WordPress Content Publisher helps prepare structured content packets, editorial drafts, and publishing workflows for WordPress-based sites. It works through the WordPress REST API to create, update, and manage posts and pages.

Best for

creating and updating WordPress posts and pages via REST

batch content operations and editorial workflows

structured content packaging with metadata and taxonomy assignment

Install notes

Requires a WordPress site with REST API enabled and an application password configured. Install the WordPress skills from the OpenClaw skills set and provide your site URL and credentials in the agent environment.

**Source:** OpenClaw official skills.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill wordpress-content-publisher
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill wordpress-content-publisher -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill wordpress-content-publisher -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill wordpress-content-publisher -a codex
```

### OpenClaw

```bash
clawhub install wordpress-content-publisher
```

## Source

- Marketplace: https://agentskillexchange.com/skills/wordpress-content-publisher/
