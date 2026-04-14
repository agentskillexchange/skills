---
title: "Decap CMS Git-Based Content Management System for Static Sites"
description: "Decap CMS is a Git-based content management system for static site generators. It provides an admin UI at /admin, authenticates against Git-backed backends, and lets teams edit structured content in repositories without building a custom editorial interface from scratch."
verification: security_reviewed
source: "https://github.com/decaporg/decap-cms"
category:
  - "WordPress &amp; CMS"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "decaporg/decap-cms"
  github_stars: 18995
---

# Decap CMS Git-Based Content Management System for Static Sites

Decap CMS is an open source Git-based content management system built for static site generators and repository-driven publishing workflows. Formerly known as Netlify CMS, the project gives teams a browser-based editorial interface that sits at the /admin route of a site and writes content back to a Git repository. That makes it useful when the job is not “run a traditional database-backed CMS,” but “let editors manage structured content in a repo-backed website without asking them to work directly in Markdown and YAML.”

The project supports common static-site ecosystems such as Jekyll, Hugo, Hexo, and Gatsby, and its documentation frames setup around four steps: install the admin app, choose a backend such as GitHub or GitLab, configure collections and content models, and then manage content through the web UI. Because the content remains in Git, teams keep their existing review, branching, and deployment workflows instead of introducing a separate content silo. That makes Decap CMS a solid fit for documentation sites, marketing sites, and content-heavy static properties.

From an integration standpoint, Decap CMS works best when a site already has a build pipeline and repository-hosted content. Developers define collections in configuration, connect authentication and backend access, and let editors create or update entries through the admin experience. For agent-assisted workflows, it is a good anchor for automations that generate drafts, validate frontmatter, review content diffs, or coordinate publishing to static-site platforms while preserving Git as the system of record.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/decap-cms-git-based-content-management-system-for-static-sites/)
