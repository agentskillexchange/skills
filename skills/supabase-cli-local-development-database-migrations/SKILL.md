---
title: "Supabase CLI for Local Development and Database Migrations"
description: "Supabase CLI manages local Supabase projects, database migrations, types, and edge functions. It is the upstream command-line tool for developers who need to work against Supabase from the terminal and CI."
slug: "supabase-cli-local-development-database-migrations"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/supabase/cli"
---

# Supabase CLI for Local Development and Database Migrations

Supabase CLI manages local Supabase projects, database migrations, types, and edge functions. It is the upstream command-line tool for developers who need to work against Supabase from the terminal and CI.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install supabase-cli-local-development-database-migrations
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Supabase CLI is the official command-line tool in the supabase/cli repository. It manages local Supabase development, database migrations, edge function deployment, database-backed type generation, and authenticated requests to the Supabase Management API. That makes it a good fit for developers who want a terminal-first workflow around Supabase projects.
The upstream README documents installation paths for npm, Homebrew, Scoop, Linux packages, go install, pkgx, Nix, and npx bootstrap flows. It also links directly to the CLI reference and release artifacts, which gives this skill a real operational foundation rather than a generic description. Agents can use it to initialize projects, manage schema changes, and automate deploy steps in CI.
This skill is especially useful when the job is not just “use Supabase” but “do the repetitive project and database operations safely and consistently.” It belongs in a general tooling category because it connects local development, database workflows, and deployment automation under one CLI surface.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/supabase-cli-local-development-database-migrations/)
