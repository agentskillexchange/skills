---
title: "Pagefind Static Low-Bandwidth Search Engine"
description: "Pagefind is a static search library written in Rust that indexes your built site and adds a search bundle requiring no server infrastructure. It performs well on large sites while using minimal bandwidth."
verification: "security_reviewed"
source: "https://github.com/Pagefind/pagefind"
category:
  - "Research & Scraping"
framework:
  - "Multi-Framework"
---

# Pagefind Static Low-Bandwidth Search Engine

Pagefind is a fully static search library that aims to perform well on large sites while using as little bandwidth as possible and without requiring any hosted infrastructure. Originally created by Liam Bigelow at CloudCannon, Pagefind has become a popular choice for adding search to static sites with over 5,000 GitHub stars.


How It Works
Pagefind operates in two phases. First, you run the pagefind CLI against your built static site (the output directory of Hugo, Astro, Eleventy, Jekyll, or any other generator). It indexes all HTML pages, creating a compressed search index. Second, Pagefind adds a small JavaScript search bundle to your site that loads index fragments on demand as users type, keeping bandwidth low even for sites with thousands of pages.


Search Features
Pagefind supports full-text search with multilingual stemming, filtering by metadata attributes, sorting by custom data attributes, substring matching, and result highlighting. The search index is split into chunks, so only relevant portions are loaded for each query. A typical search uses under 100KB of bandwidth even on sites with tens of thousands of pages.


Prebuilt UI and JavaScript API
Pagefind ships with a prebuilt search UI component that can be dropped into any page with minimal configuration. For custom implementations, a JavaScript API allows programmatic search queries, result fetching, and filter management. Both approaches work without any server-side code.


Agent Integration
Agents can invoke the pagefind CLI to index a site after building (npx pagefind –site public), configure search behavior via data attributes in HTML, and integrate the search UI or API into page templates. Pagefind is installable via npm (npx pagefind) or as a standalone binary, and works with any static site generator that outputs HTML files.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagefind-static-low-bandwidth-search-engine/)
