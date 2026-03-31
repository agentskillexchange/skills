---
name: "Bedrock Modern WordPress Project Boilerplate by Roots"
description: "Bedrock is a WordPress boilerplate with Composer-based dependency management, environment-specific configuration via .env files, and an improved folder structure. It separates WordPress core from application code for cleaner version control and deployment."
category: "WordPress &amp; CMS"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/roots/bedrock"
---
# Bedrock Modern WordPress Project Boilerplate by Roots

Bedrock is a WordPress boilerplate with Composer-based dependency management, environment-specific configuration via .env files, and an improved folder structure. It separates WordPress core from application code for cleaner version control and deployment.

## Overview

Bedrock is an open-source WordPress project boilerplate created by the Roots team that modernizes how WordPress sites are structured and managed. Instead of the traditional WordPress directory layout, Bedrock reorganizes the project into a Composer-managed structure where WordPress core, plugins, and themes are treated as dependencies rather than committed code.

The key architectural change is separating the web root from the project root. WordPress core lives in its own directory (wp/) while application code — custom plugins and themes — lives in app/. This means WordPress itself is a Composer dependency that can be updated with a single command, and the entire project can be tracked in Git without including WordPress core files.

Bedrock uses vlucas/phpdotenv for environment-specific configuration through .env files, replacing the traditional wp-config.php approach. Database credentials, salts, debug settings, and other environment variables are stored in .env files that never get committed to version control. Different environments (development, staging, production) each get their own configuration without code changes.

The project structure follows modern PHP conventions: an autoloader handles custom code, WordPress plugins are installed via Composer from wpackagist.org (a Composer mirror of the WordPress plugin directory), and mu-plugins provide must-use functionality that loads automatically. Bedrock also configures proper file permissions and security headers out of the box.

Bedrock integrates with other Roots tools like Trellis for server provisioning and Sage for theme development, forming a complete modern WordPress development stack. Install with composer create-project roots/bedrock. Licensed under MIT with over 6,400 GitHub stars and extensive documentation at roots.io/bedrock/docs.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill bedrock-wordpress-composer-boilerplate-roots
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill bedrock-wordpress-composer-boilerplate-roots -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill bedrock-wordpress-composer-boilerplate-roots -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill bedrock-wordpress-composer-boilerplate-roots -a codex
```

### OpenClaw

```bash
clawhub install bedrock-wordpress-composer-boilerplate-roots
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bedrock-wordpress-composer-boilerplate-roots/)
