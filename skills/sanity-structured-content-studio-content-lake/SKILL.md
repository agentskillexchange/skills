---
title: "Sanity Structured Content Studio and Content Lake"
description: "Sanity is a structured content platform centered on Sanity Studio and the Content Lake, with APIs and tooling for modeling, editing, querying, and publishing content. This skill is for agents that need to operate inside a Sanity-based CMS environment instead of treating the site like an opaque webpage. It helps the agent work with schemas, document types, datasets, GROQ queries, asset references, slugs, and publishing workflows in a way that matches how Sanity projects are actually built. A common use case is content operations: create a new document, update fields, validate required properties, query related entries, or prepare structured content for publishing pipelines. Another is developer support: inspect schema definitions, explain why a field is not appearing in Studio, troubleshoot dataset mismatches, or suggest changes to document structure. Because Sanity has both a CLI and a mature JavaScript package, the skill can support local repo workflows and remote API-oriented workflows. The outputs are usually structured rather than purely narrative. An agent can return GROQ query snippets, schema recommendations, document mutation plans, content migration steps, or a normalized summary of documents and references pulled from a dataset. Integration points include JAMstack frontends, Next.js or Astro sites, content migration scripts, editorial QA, and automation pipelines that consume Sanity APIs. Technical terms that matter include GROQ, datasets, Studio configuration, schema types, references, portable text, mutations, and webhooks. By grounding the workflow in Sanity’s actual platform model, the skill helps agents perform reliable CMS work instead of producing generic content-management advice."
source: "https://github.com/sanity-io/sanity"
verification: "security_reviewed"
category:
  - "WordPress &amp; CMS"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "sanity-io/sanity"
  github_stars: 6041
  npm_package: "sanity"
  npm_weekly_downloads: 413166
---

# Sanity Structured Content Studio and Content Lake

Sanity is a structured content platform centered on Sanity Studio and the Content Lake, with APIs and tooling for modeling, editing, querying, and publishing content. This skill is for agents that need to operate inside a Sanity-based CMS environment instead of treating the site like an opaque webpage. It helps the agent work with schemas, document types, datasets, GROQ queries, asset references, slugs, and publishing workflows in a way that matches how Sanity projects are actually built. A common use case is content operations: create a new document, update fields, validate required properties, query related entries, or prepare structured content for publishing pipelines. Another is developer support: inspect schema definitions, explain why a field is not appearing in Studio, troubleshoot dataset mismatches, or suggest changes to document structure. Because Sanity has both a CLI and a mature JavaScript package, the skill can support local repo workflows and remote API-oriented workflows. The outputs are usually structured rather than purely narrative. An agent can return GROQ query snippets, schema recommendations, document mutation plans, content migration steps, or a normalized summary of documents and references pulled from a dataset. Integration points include JAMstack frontends, Next.js or Astro sites, content migration scripts, editorial QA, and automation pipelines that consume Sanity APIs. Technical terms that matter include GROQ, datasets, Studio configuration, schema types, references, portable text, mutations, and webhooks. By grounding the workflow in Sanity’s actual platform model, the skill helps agents perform reliable CMS work instead of producing generic content-management advice.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sanity-structured-content-studio-content-lake/)
