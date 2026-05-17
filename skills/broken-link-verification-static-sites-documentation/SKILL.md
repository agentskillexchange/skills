---
name: "Broken Link Verification for Static Sites and Documentation"
slug: "broken-link-verification-static-sites-documentation"
description: "Uses htmltest to crawl generated documentation or static site output, detect broken internal and external links, and return a link-focused validation report before deploy. This is a narrow docs QA skill for agents validating already-built HTML, not a generic site generator or crawler listing."
github_stars: 371
verification: "security_reviewed"
source: "https://github.com/wjdp/htmltest"
author: "wjdp"
publisher_type: "Open Source Project"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "wjdp/htmltest"
  github_stars: 371
---

# Broken Link Verification for Static Sites and Documentation

Uses htmltest to crawl generated documentation or static site output, detect broken internal and external links, and return a link-focused validation report before deploy. This is a narrow docs QA skill for agents validating already-built HTML, not a generic site generator or crawler listing.

## Prerequisites

Go or prebuilt htmltest binary and generated HTML output

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install htmltest with go install github.com/wjdp/htmltest@latest or download a release binary
```

## Documentation

- https://github.com/wjdp/htmltest

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/broken-link-verification-static-sites-documentation/)
