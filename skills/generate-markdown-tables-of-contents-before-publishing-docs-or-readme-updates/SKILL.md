---
title: "Generate Markdown tables of contents before publishing docs or README updates"
description: "This skill uses DocToc , the Markdown table-of-contents generator from the thlorenz/doctoc project, to insert or refresh TOC blocks inside README files and longer documentation pages. An agent invokes it after headings already exist and the content structure is mostly settled, but before publishing or opening a pull request. That is the sweet spot where a generated table of contents adds value without forcing the agent to hand-maintain anchor links or reorder entire documents manually. The agent behavior here is intentionally bounded. It is not writing the documentation from scratch, acting as a documentation portal, or replacing a full docs generator. It is performing one narrow operator task: detect Markdown headings and generate or update a stable, compatible TOC block that matches the document’s current structure. That scope boundary is what keeps this entry from being a plain CLI listing. A user should invoke this skill when the docs already exist and navigability is the problem. If the user needs API docs generation, site theming, or static-site rendering, this skill is the wrong tool. DocToc fits naturally into README maintenance workflows, repository documentation sweeps, release-prep passes, and git-hook or CI jobs that keep TOCs from drifting out of date. The upstream evidence is solid: the official GitHub repository exists, the npm package exists, the project is licensed, and recent commits are present. The upstream install path is npm install -g doctoc , and the project supports dry runs, stdout output, and repeated updates to existing doctoc markers."
source: "https://github.com/thlorenz/doctoc"
verification: "security_reviewed"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "thlorenz/doctoc"
  github_stars: 4432
---

# Generate Markdown tables of contents before publishing docs or README updates

This skill uses DocToc , the Markdown table-of-contents generator from the thlorenz/doctoc project, to insert or refresh TOC blocks inside README files and longer documentation pages. An agent invokes it after headings already exist and the content structure is mostly settled, but before publishing or opening a pull request. That is the sweet spot where a generated table of contents adds value without forcing the agent to hand-maintain anchor links or reorder entire documents manually. The agent behavior here is intentionally bounded. It is not writing the documentation from scratch, acting as a documentation portal, or replacing a full docs generator. It is performing one narrow operator task: detect Markdown headings and generate or update a stable, compatible TOC block that matches the document’s current structure. That scope boundary is what keeps this entry from being a plain CLI listing. A user should invoke this skill when the docs already exist and navigability is the problem. If the user needs API docs generation, site theming, or static-site rendering, this skill is the wrong tool. DocToc fits naturally into README maintenance workflows, repository documentation sweeps, release-prep passes, and git-hook or CI jobs that keep TOCs from drifting out of date. The upstream evidence is solid: the official GitHub repository exists, the npm package exists, the project is licensed, and recent commits are present. The upstream install path is npm install -g doctoc , and the project supports dry runs, stdout output, and repeated updates to existing doctoc markers.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-markdown-tables-of-contents-before-publishing-docs-or-readme-updates/)
