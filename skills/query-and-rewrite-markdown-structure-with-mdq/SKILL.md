---
name: "Query and rewrite Markdown structure with mdq"
slug: "query-and-rewrite-markdown-structure-with-mdq"
description: "Use mdq when an agent needs to target headings, lists, links, or other Markdown structure without falling back to brittle regex edits."
github_stars: 1708
verification: "listed"
source: "https://github.com/yshavit/mdq"
author: "yshavit"
publisher_type: "individual"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "yshavit/mdq"
  github_stars: 1708
---

# Query and rewrite Markdown structure with mdq

Use mdq when an agent needs to target headings, lists, links, or other Markdown structure without falling back to brittle regex edits.

## Prerequisites

mdq and Markdown files to inspect or rewrite.

## Installation

Use the upstream install or setup path that matches your environment:
- brew install mdq
- docker pull yshavit/mdq
- cargo install --git https://github.com/yshavit/mdq
- cargo build

Requirements and caveats from upstream:
- reviewers to complete. Enforcing these often requires ugly regexes that are a pain to write and worse to debug. Instead,
- echo 'My [example](https://github.com/yshavit/mdq) markdown' | docker run --rm -i yshavit/mdq '[]()'
- To use a specific release version, use yshavit/mdq:<version>. See [Docker Hub] for available version tags.

Basic usage or getting-started notes:
- For example, GitHub PRs are Markdown documents, and some organizations have specific templates with checklists for all
- you can (for example) ask mdq for all uncompleted tasks:
- [!tip]

- Source: https://github.com/yshavit/mdq
- Extracted from upstream docs: https://raw.githubusercontent.com/yshavit/mdq/HEAD/README.md

## Documentation

- https://github.com/yshavit/mdq

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/query-and-rewrite-markdown-structure-with-mdq/)
