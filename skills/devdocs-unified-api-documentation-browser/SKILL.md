---
name: "DevDocs Unified API Documentation Browser"
slug: "devdocs-unified-api-documentation-browser"
description: "DevDocs aggregates 500+ API documentation sets into a single searchable interface with instant fuzzy search, offline support, and keyboard navigation. Maintained by freeCodeCamp with 38,000+ GitHub stars, it serves as a comprehensive reference for programming languages, frameworks, and tools."
github_stars: 38655
verification: "security_reviewed"
source: "https://github.com/freeCodeCamp/devdocs"
category: "Library & API Reference"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "freeCodeCamp/devdocs"
  github_stars: 38655
---

# DevDocs Unified API Documentation Browser

DevDocs aggregates 500+ API documentation sets into a single searchable interface with instant fuzzy search, offline support, and keyboard navigation. Maintained by freeCodeCamp, it serves as a comprehensive reference for programming languages, frameworks, and tools.

## Installation

Use the upstream install or setup path that matches your environment:
- docker run --name devdocs -d -p 9292:9292 ghcr.io/freecodecamp/devdocs:latest
- git clone https://github.com/freeCodeCamp/devdocs.git && cd devdocs
- docker build -t devdocs .
- docker run --name devdocs -d -p 9292:9292 devdocs

Requirements and caveats from upstream:
- ### Using Docker (Recommended)
- The easiest way to run DevDocs locally is using Docker:
- DevDocs requires Ruby 3.4.1 (defined in [Gemfile](./Gemfile)), libcurl, and a JavaScript runtime supported by [ExecJS](https://github.com/rails/execjs#readme) (included in OS X and Windows; [Node.js](https://nodejs.or...

Basic usage or getting-started notes:
- Unless you wish to contribute to the project, we recommend using the hosted version at [devdocs.io](https://devdocs.io). It's up-to-date and works offline out-of-the-box.

- Source: https://github.com/freeCodeCamp/devdocs
- Extracted from upstream docs: https://raw.githubusercontent.com/freeCodeCamp/devdocs/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/devdocs-unified-api-documentation-browser/)
