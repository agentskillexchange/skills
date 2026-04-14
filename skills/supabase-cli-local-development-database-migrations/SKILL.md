---
title: "Supabase CLI for Local Development and Database Migrations"
description: "Supabase CLI manages local Supabase projects, database migrations, types, and edge functions. It is the upstream command-line tool for developers who need to work against Supabase from the terminal and CI."
verification: security_reviewed
source: "https://github.com/supabase/cli"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "supabase/cli"
  github_stars: 2112
---

# Supabase CLI for Local Development and Database Migrations

Supabase CLI is the official command-line tool in the supabase/cli repository. It manages local Supabase development, database migrations, edge function deployment, database-backed type generation, and authenticated requests to the Supabase Management API. That makes it a good fit for developers who want a terminal-first workflow around Supabase projects.

The upstream README documents installation paths for npm, Homebrew, Scoop, Linux packages, go install, pkgx, Nix, and npx bootstrap flows. It also links directly to the CLI reference and release artifacts, which gives this skill a real operational foundation rather than a generic description. Agents can use it to initialize projects, manage schema changes, and automate deploy steps in CI.

This skill is especially useful when the job is not just “use Supabase” but “do the repetitive project and database operations safely and consistently.” It belongs in a general tooling category because it connects local development, database workflows, and deployment automation under one CLI surface.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/supabase-cli-local-development-database-migrations/)
