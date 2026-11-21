---
name: "deploy-stack: put a site live on Cloudflare Workers, Supabase and R2"
slug: "deploy-stack"
description: "Deploys a website on Cloudflare Workers with Supabase for data and sign-in and R2 for media, including a Cloudflare Registrar domain, image resizing and cache settings, with a check before launch."
category: "CI/CD Integrations"
framework: "Claude Code"
verification: listed
source: "https://github.com/seanaiux/uberdesigner-skills/tree/main/skills/deploy-stack"
---

# deploy-stack: put a site live on Cloudflare Workers, Supabase and R2

deploy-stack is an agent skill from uberdesigner that takes a finished site live on the same stack uberdesigner runs on. It covers a domain bought through Cloudflare Registrar, hosting on Cloudflare Workers, Supabase for the database and sign-in, and Cloudflare R2 for media uploads. It also sets up image resizing and cache settings, and runs a check before launch so problems with routes, environment variables or storage are found before visitors see them.

Use it when you ask your agent to put a site live, connect a domain, or add a database, accounts or file uploads to a project. The skill is plain Markdown instructions in a `SKILL.md` that Claude Code, Codex, Cursor and other agents that read skills can follow. It is licensed Apache-2.0 and ships in the uberdesigner-skills repository together with a Claude Code plugin marketplace entry and a Gemini CLI extension.

## Installation

### Claude Code plugin

```bash
/plugin marketplace add seanaiux/uberdesigner-skills
/plugin install uberdesigner@uberdesigner
```

### Any agent, with the skills CLI

```bash
npx skills add seanaiux/uberdesigner-skills
```

### Direct repo/manual install

Copy `skills/deploy-stack` from https://github.com/seanaiux/uberdesigner-skills into your agent's skills folder (Claude Code: `~/.claude/skills/`).
