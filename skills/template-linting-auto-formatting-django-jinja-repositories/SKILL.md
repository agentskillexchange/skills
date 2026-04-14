---
title: "Template Linting and Auto-Formatting for Django and Jinja Repositories"
description: "Uses djLint to scan Django, Jinja, Nunjucks, Twig, and HTML templates for indentation problems, malformed tags, and style drift, then optionally rewrites them into a consistent format. This is for agents that need to clean and validate template-heavy repos before review or release, not for general web framework setup."
verification: security_reviewed
source: "https://github.com/djlint/djLint"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
---

# Template Linting and Auto-Formatting for Django and Jinja Repositories

This ASE entry turns djLint into a bounded repository hygiene skill rather than a generic package card. The agent behavior is simple and useful: inspect template files, run djLint against the relevant directories, surface concrete formatting and lint failures, and, when allowed, apply the formatter so the repository comes back into a stable and reviewable state. djLint supports Django templates, Jinja, Nunjucks, Twig, Handlebars, Go templates, and plain HTML, which makes it practical for mixed frontend and server-rendered projects where markup conventions drift over time.

The right time to invoke this skill is when a user needs an agent to clean up template files, catch broken tag structure, normalize indentation, or enforce template style before a pull request, release, migration, or large refactor. It is especially useful after AI-assisted code generation or multi-author edits, when templates often accumulate inconsistent spacing, duplicate constructs, or hard-to-read blocks. The agent returns a lint report, a list of touched files, and optionally the formatted output that can be committed or reviewed.

The scope boundary matters. This skill is not a listing for djLint as a product, and it is not a generic web framework entry. Its job-to-be-done is narrowly about template linting and auto-formatting inside an existing repo. It does not create applications, serve pages, or replace the framework’s own runtime features. Integration points are straightforward: pre-commit hooks, CI pipelines, local developer scripts, Python virtualenvs, and review bots that comment on changed templates. Upstream evidence is strong, with an active official repository, a published PyPI package, a live docs site, tags, and recent maintenance.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/template-linting-auto-formatting-django-jinja-repositories/)
