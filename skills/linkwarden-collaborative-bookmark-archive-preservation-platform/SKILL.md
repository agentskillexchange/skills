---
title: "Linkwarden Collaborative Bookmark Archive and Preservation Platform"
description: "Linkwarden is an open source bookmark and web archiving platform for saving, organizing, and preserving research material. It captures screenshots, PDFs, and archived page copies, adds reader and annotation features, and supports shared collections for teams."
verification: security_reviewed
source: "https://github.com/linkwarden/linkwarden"
category:
  - "Research &amp; Scraping"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "linkwarden/linkwarden"
  github_stars: 17869
---

# Linkwarden Collaborative Bookmark Archive and Preservation Platform

Linkwarden is the core project behind linkwarden/linkwarden, a self-hosted bookmark manager that focuses on long-term preservation instead of just storing URLs. When a link is saved, the platform can capture a screenshot, generate a PDF, and keep a preserved copy of the page so teams can still access information even after the original source changes or disappears.

That makes Linkwarden a strong fit for research, competitive monitoring, knowledge capture, and any workflow where agents or human operators need stable references instead of fragile bookmarks. The project also adds reader mode, text highlighting, annotations, tagging, collections, collaboration controls, and API keys. Its documentation highlights optional integrations such as Wayback Machine snapshots, local AI tagging, browser extensions, browser synchronization, and upload flows from SingleFile.

In an agent ecosystem, Linkwarden can act as a durable memory layer for sourced research. A skill built around it can collect articles, product pages, issue threads, and documentation pages, then preserve and organize them for later review. Because it supports multi-user collaboration and public or private sharing, it also maps well to research assistants, editorial workflows, and internal knowledge operations.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/linkwarden-collaborative-bookmark-archive-preservation-platform/)
