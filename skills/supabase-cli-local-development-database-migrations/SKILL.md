---
name: Supabase CLI for Local Development and Database Migrations
description: Supabase CLI manages local Supabase projects, database migrations, types,
  and edge functions. It is the upstream command-line tool for developers who need
  to work against Supabase from the terminal and CI.
verification: security_reviewed
source: https://github.com/supabase/cli
category:
- Developer Tools
framework:
- Multi-Framework
---
# Supabase CLI for Local Development and Database Migrations

Supabase CLI is the official command-line tool in the supabase/cli repository. It manages local Supabase development, database migrations, edge function deployment, database-backed type generation, and authenticated requests to the Supabase Management API. That makes it a good fit for developers who want a terminal-first workflow around Supabase projects.
The upstream README documents installation paths for npm, Homebrew, Scoop, Linux packages, go install, pkgx, Nix, and npx bootstrap flows. It also links directly to the CLI reference and release artifacts, which gives this skill a real operational foundation rather than a generic description. Agents can use it to initialize projects, manage schema changes, and automate deploy steps in CI.
This skill is especially useful when the job is not just &#8220;use Supabase&#8221; but &#8220;do the repetitive project and database operations safely and consistently.&#8221; It belongs in a general tooling category because it connects local development, database workflows, and deployment automation under one CLI surface.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/supabase-cli-local-development-database-migrations/)
