---
title: "Normalize article metadata from URLs before generating link previews or content briefs"
description: "Uses metascraper to turn a URL plus its fetched HTML into normalized fields such as title, description, author, date, publisher, and lead image. This is useful when an agent needs reliable preview or briefing data from a page without building a custom parser for every site."
verification: "security_reviewed"
source: "https://github.com/microlinkhq/metascraper"
author: "microlinkhq"
publisher_type: "Organization"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "microlinkhq/metascraper"
  github_stars: 2660
---

# Normalize article metadata from URLs before generating link previews or content briefs

Uses metascraper to turn a URL plus its fetched HTML into normalized fields such as title, description, author, date, publisher, and lead image. This is useful when an agent needs reliable preview or briefing data from a page without building a custom parser for every site.

## Prerequisites

Node.js and an HTML retrieval step such as fetch, Playwright, or browserless

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
npm install metascraper
```

## Documentation

- https://metascraper.js.org

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/normalize-article-metadata-from-urls-before-generating-link-previews-or-content-briefs/)
