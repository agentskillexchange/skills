---
name: "Sage WordPress Starter Theme with Laravel Blade and Tailwind CSS"
description: "Sage by Roots is an advanced WordPress starter theme that brings Laravel Blade templating, Vite-powered front-end builds, Tailwind CSS, and block editor support to WordPress theme development. It is the most-starred WordPress theme framework on GitHub."
category: "WordPress &amp; CMS"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/roots/sage"
tool_ecosystem:
  github_repo: "https://github.com/roots/sage"
  github_stars: 13199
  license: "MIT"
---
# Sage WordPress Starter Theme with Laravel Blade and Tailwind CSS

Sage by Roots is an advanced WordPress starter theme that brings Laravel Blade templating, Vite-powered front-end builds, Tailwind CSS, and block editor support to WordPress theme development. It is the most-starred WordPress theme framework on GitHub.

Sage is the flagship WordPress starter theme from Roots, providing a modern development experience built on Laravel Blade components, Vite for asset compilation, and Tailwind CSS for styling. With over 13,000 GitHub stars and active development since 2011, Sage is one of the most established and widely-used WordPress theme frameworks in the ecosystem.

Architecture

Sage uses Acorn to integrate Laravel’s service container, Blade templating engine, and other Laravel features directly into WordPress. Theme templates are written as Blade components with clean PHP syntax, replacing WordPress’s traditional template hierarchy with organized, component-based views. Sage 11 supports the block editor out of the box and includes Tailwind CSS configuration pre-wired into the Vite build pipeline.

Development Workflow

The front-end build system uses Vite for instant hot module replacement during development and optimized production builds. Tailwind CSS is configured by default with WordPress-specific utilities. The theme follows a structured directory layout separating views (Blade templates), assets (CSS/JS), and application logic (composers, providers). Sage also includes support for view composers — classes that pass data to specific Blade views.

Agent Integration

AI coding agents can scaffold new Sage themes using composer create-project roots/sage, then modify Blade templates, Tailwind configuration, and theme logic programmatically. Agents can generate new Blade components, edit view composers to inject data, customize the Tailwind config, and run npm run build to compile assets. The clean separation of concerns in Sage makes it straightforward for agents to locate and modify specific parts of a theme without side effects.

Installation

Create a new Sage project with Composer: composer create-project roots/sage your-theme-name. Install front-end dependencies with npm install, then run npm run dev for development or npm run build for production. Requires PHP 8.2+, Composer, and Node.js. Full documentation is at roots.io/sage/docs.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sage-wordpress-starter-theme-laravel-blade
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sage-wordpress-starter-theme-laravel-blade -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sage-wordpress-starter-theme-laravel-blade -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sage-wordpress-starter-theme-laravel-blade -a codex
```

### OpenClaw

```bash
clawhub install sage-wordpress-starter-theme-laravel-blade
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sage-wordpress-starter-theme-laravel-blade/)
