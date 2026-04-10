---
name: "DevDocs Unified API Documentation Browser"
description: "DevDocs aggregates 500+ API documentation sets into a single searchable interface with instant fuzzy search, offline support, and keyboard navigation. Maintained by freeCodeCamp with 38,000+ GitHub stars, it serves as a comprehensive reference for programming languages, frameworks, and tools."
verification: security_reviewed
source: "https://github.com/freeCodeCamp/devdocs"
category:
  - "Library &amp; API Reference"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "freeCodeCamp/devdocs"
  github_stars: 38655
---

# DevDocs Unified API Documentation Browser

What is DevDocs?
DevDocs is an API documentation browser maintained by freeCodeCamp with over 38,000 GitHub stars. It combines documentation from hundreds of programming languages, frameworks, libraries, and tools into a unified interface at devdocs.io. Originally created by Thibaut Courouble, DevDocs features instant fuzzy search across all documentation sets, offline support via Service Workers, keyboard-driven navigation, a dark theme, and a mobile-optimized layout.
How the Skill Works
A DevDocs integration skill enables AI agents to query structured API documentation programmatically. The skill leverages DevDocs' Ruby-based scraper infrastructure that generates normalized documentation from upstream sources including MDN Web Docs, official language references, and framework documentation sites. Each documentation set includes full API signatures, parameter descriptions, code examples, and cross-references, scraped and normalized into a consistent format.
The documentation scraper supports over 500 documentation sets covering JavaScript, Python, Ruby, Go, Rust, CSS, HTML, React, Node.js, Django, Rails, PostgreSQL, Redis, Docker, Kubernetes, and hundreds more. Each scraper module handles the upstream documentation's unique HTML structure and normalizes it into DevDocs' standard format with consistent navigation, search indexing, and cross-linking.
Integration Points
DevDocs can be self-hosted via Docker (ghcr.io/freecodecamp/devdocs:latest) or the standard Ruby/Sinatra setup. The thorCLI commands manage documentation downloads: thor docs:download for fetching pre-generated docs, thor docs:list for available sets, and thor docs:download -installed for updates. The documentation data is stored as structured JSON, making it consumable by AI agents for context-aware code assistance and API reference lookups.
What It Outputs
The skill provides structured API documentation including function signatures, parameter types, return values, usage examples, and links to related entries. Search results return ranked matches across all enabled documentation sets with snippet previews and direct links to full entries.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/devdocs-unified-api-documentation-browser/)
