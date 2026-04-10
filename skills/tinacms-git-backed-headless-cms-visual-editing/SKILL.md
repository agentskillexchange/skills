---
name: "TinaCMS Git-Backed Headless CMS with Visual Editing"
description: "TinaCMS is a fully open-source headless CMS backed by Git that supports Markdown, MDX, JSON, and YAML content. It provides a GraphQL API for querying content, real-time visual editing for non-technical users, and seamless integration with static site generators and Next.js."
verification: security_reviewed
source: "https://github.com/tinacms/tinacms"
category:
  - "WordPress &amp; CMS"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "tinacms/tinacms"
  github_stars: 13245
  ase_npm_package: "tinacms"
  npm_weekly_downloads: 94278
---

# TinaCMS Git-Backed Headless CMS with Visual Editing

TinaCMS is an open-source headless content management system with over 13,000 GitHub stars, licensed under Apache-2.0, and actively maintained with daily commits. Unlike traditional headless CMSs that store content in a proprietary database, TinaCMS stores all content directly in your Git repository as Markdown, MDX, JSON, or YAML files, giving developers full version control and ownership of their content.
GraphQL Content API
TinaCMS automatically generates a GraphQL API from your content schema definition. This allows agents and frontend applications to query structured content using type-safe queries like post.author.firstName, with full support for references between documents, filtering, sorting, and pagination. The schema is defined in a tina/config.ts file using a TypeScript-based configuration DSL.
Visual Editing
One of TinaCMS's standout features is its optional real-time visual editing interface. Content editors can modify pages directly on the rendered site with a contextual sidebar editor that shows field inputs alongside the live preview. Changes are committed back to Git, maintaining a complete audit trail. This bridges the gap between developer-controlled infrastructure and editor-friendly workflows.
Content Modeling
TinaCMS supports rich content modeling through collections, which define content types with typed fields including strings, numbers, booleans, dates, images, rich text (MDX), references to other documents, and nested object groups. Collections map directly to directories of Markdown or JSON files in the repository, so the content structure is always transparent and portable.
Framework Integration
The CMS integrates natively with Next.js for both static generation (SSG) and server-side rendering (SSR), and works with any static site generator that consumes Markdown or JSON. The create-tina-app CLI scaffolds a new project with TinaCMS pre-configured, and the TinaCloud hosting service provides a managed GraphQL backend with GitHub integration for teams that want a hosted editorial workflow.
Agent Integration Points
AI agents can interact with TinaCMS through multiple surfaces: querying the GraphQL API to read content, committing Markdown files directly to the Git repository to create or update content, or using the TinaCMS client SDK to programmatically manage documents. This makes TinaCMS suitable for agent-driven content publishing, documentation generation, and CMS migration workflows where content needs to be both human-editable and machine-writable.
npm Package and CLI
TinaCMS is distributed as an npm package (tinacms) and can be installed into existing projects. The CLI provides commands for local development, content indexing, schema generation, and deployment. The package ecosystem includes the core CMS, the GraphQL client, and framework-specific integrations.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tinacms-git-backed-headless-cms-visual-editing/)
