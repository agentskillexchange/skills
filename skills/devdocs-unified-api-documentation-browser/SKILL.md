---
title: "DevDocs Unified API Documentation Browser"
description: "What is DevDocs? DevDocs is an API documentation browser maintained by freeCodeCamp with over 38,000 GitHub stars. It combines documentation from hundreds of programming languages, frameworks, libraries, and tools into a unified interface at devdocs.io. Originally created by Thibaut Courouble, DevDocs features instant fuzzy search across all documentation sets, offline support via Service Workers, keyboard-driven navigation, a dark theme, and a mobile-optimized layout. How the Skill Works A DevDocs integration skill enables AI agents to query structured API documentation programmatically. The skill leverages DevDocs&#8217; Ruby-based scraper infrastructure that generates normalized documentation from upstream sources including MDN Web Docs, official language references, and framework documentation sites. Each documentation set includes full API signatures, parameter descriptions, code examples, and cross-references, scraped and normalized into a consistent format. The documentation scraper supports over 500 documentation sets covering JavaScript, Python, Ruby, Go, Rust, CSS, HTML, React, Node.js, Django, Rails, PostgreSQL, Redis, Docker, Kubernetes, and hundreds more. Each scraper module handles the upstream documentation&#8217;s unique HTML structure and normalizes it into DevDocs&#8217; standard format with consistent navigation, search indexing, and cross-linking. Integration Points DevDocs can be self-hosted via Docker (ghcr.io/freecodecamp/devdocs:latest) or the standard Ruby/Sinatra setup. The thorCLI commands manage documentation downloads: thor docs:download for fetching pre-generated docs, thor docs:list for available sets, and thor docs:download &#8211;installed for updates. The documentation data is stored as structured JSON, making it consumable by AI agents for context-aware code assistance and API reference lookups. What It Outputs The skill provides structured API documentation including function signatures, parameter types, return values, usage examples, and links to related entries. Search results return ranked matches across all enabled documentation sets with snippet previews and direct links to full entries."
source: "https://github.com/freeCodeCamp/devdocs"
verification: "security_reviewed"
category:
  - "Library &amp; API Reference"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "freeCodeCamp/devdocs"
  github_stars: 38655
---

# DevDocs Unified API Documentation Browser

What is DevDocs? DevDocs is an API documentation browser maintained by freeCodeCamp with over 38,000 GitHub stars. It combines documentation from hundreds of programming languages, frameworks, libraries, and tools into a unified interface at devdocs.io. Originally created by Thibaut Courouble, DevDocs features instant fuzzy search across all documentation sets, offline support via Service Workers, keyboard-driven navigation, a dark theme, and a mobile-optimized layout. How the Skill Works A DevDocs integration skill enables AI agents to query structured API documentation programmatically. The skill leverages DevDocs&#8217; Ruby-based scraper infrastructure that generates normalized documentation from upstream sources including MDN Web Docs, official language references, and framework documentation sites. Each documentation set includes full API signatures, parameter descriptions, code examples, and cross-references, scraped and normalized into a consistent format. The documentation scraper supports over 500 documentation sets covering JavaScript, Python, Ruby, Go, Rust, CSS, HTML, React, Node.js, Django, Rails, PostgreSQL, Redis, Docker, Kubernetes, and hundreds more. Each scraper module handles the upstream documentation&#8217;s unique HTML structure and normalizes it into DevDocs&#8217; standard format with consistent navigation, search indexing, and cross-linking. Integration Points DevDocs can be self-hosted via Docker (ghcr.io/freecodecamp/devdocs:latest) or the standard Ruby/Sinatra setup. The thorCLI commands manage documentation downloads: thor docs:download for fetching pre-generated docs, thor docs:list for available sets, and thor docs:download &#8211;installed for updates. The documentation data is stored as structured JSON, making it consumable by AI agents for context-aware code assistance and API reference lookups. What It Outputs The skill provides structured API documentation including function signatures, parameter types, return values, usage examples, and links to related entries. Search results return ranked matches across all enabled documentation sets with snippet previews and direct links to full entries.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/devdocs-unified-api-documentation-browser/)
