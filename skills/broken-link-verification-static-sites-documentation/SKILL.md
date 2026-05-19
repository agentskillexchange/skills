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

Use the upstream install or setup path that matches your environment:
- docker run -v $(pwd):/test --rm wjdp/htmltest
- docker run -v $(pwd):/test --rm wjdp/htmltest -l 3 -s

Requirements and caveats from upstream:
- ### :whale: Docker

Basic usage or getting-started notes:
- You'll be prompted for your password. After simply do htmltest to run.
- By default this will install htmltest into ./bin of your current directory, to run do bin/htmltest. Rather suitable for CI environments.
- If you need more arguments to the test run it like this:

- Source: https://github.com/wjdp/htmltest
- Extracted from upstream docs: https://raw.githubusercontent.com/wjdp/htmltest/HEAD/README.md

## Documentation

- https://github.com/wjdp/htmltest

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/broken-link-verification-static-sites-documentation/)
