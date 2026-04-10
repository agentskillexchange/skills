---
name: "EmDash Full-Stack TypeScript CMS by Cloudflare"
description: "EmDash is an open-source, full-stack TypeScript CMS built on Astro and Cloudflare, designed as a spiritual successor to WordPress. It features sandboxed plugins, structured content via Portable Text, a built-in MCP server for AI agents, and runs on Cloudflare Workers, D1, and R2 or any Node.js server with SQLite."
verification: security_reviewed
source: "https://github.com/emdash-cms/emdash"
category:
  - "WordPress &amp; CMS"
framework:
  - "Multi-Framework"
---

# EmDash Full-Stack TypeScript CMS by Cloudflare

EmDash is a next-generation content management system built by Cloudflare as a spiritual successor to WordPress. Unlike WordPress, EmDash is written entirely in TypeScript, built on the Astro web framework, and designed from the ground up for modern serverless infrastructure.
Core Architecture
EmDash runs natively on Cloudflare infrastructure (D1 for database, R2 for storage, Workers for compute) but also supports any Node.js server with SQLite, Turso/libSQL, PostgreSQL, AWS S3, or local filesystem storage. The CMS is distributed as an Astro integration — add it to your astro.config.mjs and you get a complete CMS with admin panel, REST API, authentication, media library, and plugin system.
Sandboxed Plugin Architecture
The defining feature of EmDash is its sandboxed plugin system. WordPress plugins have unrestricted access to the database, filesystem, and user data — Patchstack reports that 96% of WordPress security vulnerabilities originate in plugins. EmDash plugins run in isolated Worker sandboxes via Dynamic Worker Loaders, each with a declared capability manifest. A plugin that requests read:content and email:send can do exactly that and nothing else. The definePlugin() API supports lifecycle hooks, KV storage, settings, admin pages, dashboard widgets, custom block types, and API routes.
Structured Content with Portable Text
WordPress stores rich text as serialized HTML with metadata embedded in comments. EmDash uses Portable Text, a structured JSON format that decouples content from presentation. Content can render as a web page, mobile app, email, or API response without parsing HTML. The TipTap-based rich text editor provides a familiar editing experience while storing content in this portable format.
Agent-Ready Design
EmDash ships with agent skills for building plugins and themes, a CLI for programmatic content and schema management, and a built-in MCP (Model Context Protocol) server so AI tools like Claude and ChatGPT can interact with your site directly. Content types are defined in the database and modifiable through the admin UI, with TypeScript type generation via npx emdash types.
Authentication and Access Control
EmDash uses passkey-first (WebAuthn) authentication with OAuth and magic link fallbacks. Role-based access control supports Administrator, Editor, Author, and Contributor roles.
WordPress Migration
EmDash can import posts, pages, media, and taxonomies from WXR exports, the WordPress REST API, or WordPress.com. Agent skills help port plugins and themes from WordPress to EmDash.
Installation
Install via npm create emdash@latest or deploy directly to Cloudflare. Three starter templates ship out of the box: a blog, a marketing landing page, and a portfolio. The project is MIT-licensed and available on GitHub at github.com/emdash-cms/emdash.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/emdash-full-stack-typescript-cms-cloudflare/)
