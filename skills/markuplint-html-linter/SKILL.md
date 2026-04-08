---
title: markuplint HTML Linter for All Markup Developers
description: 'markuplint is an open-source HTML linter built to help markup developers
  maintain high-quality, accessible, and standards-compliant HTML across modern web
  projects. Unlike generic linters that only check raw HTML, markuplint understands
  the output of template engines and component frameworks, making it uniquely suited
  for real-world codebases. How It Works markuplint operates as a Node.js CLI tool
  and can be integrated into CI/CD pipelines, editor workflows (via its official VS
  Code extension), or run standalone. It parses markup using framework-specific parser
  plugins — including @markuplint/jsx-parser, @markuplint/vue-parser, @markuplint/svelte-parser,
  @markuplint/astro-parser, @markuplint/php-parser, @markuplint/pug-parser, and more
  — then evaluates the parsed output against its rule set. Key Features Multi-framework
  support: JSX, Vue, Svelte, Astro, Alpine.js, HTMX, Pug, PHP, Nunjucks, Mustache,
  Liquid, and EJS templates are all supported through dedicated parser plugins. Accessibility
  enforcement: Rules check for proper ARIA attributes, landmark roles, heading hierarchy,
  and semantic HTML usage to ensure WCAG compliance. HTML spec validation: Validates
  elements and attributes against the living HTML specification, catching deprecated
  patterns and invalid nesting. Custom rule configuration: Rules are fully configurable
  via .markuplintrc JSON or YAML config files, supporting per-file overrides and shared
  presets. VS Code integration: The official vscode-markuplint extension provides
  real-time linting feedback directly in the editor. Integration Points Install via
  npm with npm install -D markuplint or use npx for one-off runs. Configure rules
  in a .markuplintrc file at your project root. The CLI outputs standard lint results
  compatible with CI formatters. For monorepos, markuplint supports workspace-level
  configuration with per-package overrides. Agent Integration AI coding agents can
  use markuplint as a code quality gate — run it after generating or modifying HTML
  templates to catch accessibility violations, deprecated elements, or invalid attribute
  usage before committing. The structured JSON output format makes it easy to parse
  results programmatically and feed them back into the agent loop for auto-correction.'
verification: security_reviewed
source: https://github.com/markuplint/markuplint
category:
- Code Quality &amp; Review
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: markuplint/markuplint
  github_stars: 601
---

# markuplint HTML Linter for All Markup Developers

markuplint is an open-source HTML linter built to help markup developers maintain high-quality, accessible, and standards-compliant HTML across modern web projects. Unlike generic linters that only check raw HTML, markuplint understands the output of template engines and component frameworks, making it uniquely suited for real-world codebases. How It Works markuplint operates as a Node.js CLI tool and can be integrated into CI/CD pipelines, editor workflows (via its official VS Code extension), or run standalone. It parses markup using framework-specific parser plugins — including @markuplint/jsx-parser, @markuplint/vue-parser, @markuplint/svelte-parser, @markuplint/astro-parser, @markuplint/php-parser, @markuplint/pug-parser, and more — then evaluates the parsed output against its rule set. Key Features Multi-framework support: JSX, Vue, Svelte, Astro, Alpine.js, HTMX, Pug, PHP, Nunjucks, Mustache, Liquid, and EJS templates are all supported through dedicated parser plugins. Accessibility enforcement: Rules check for proper ARIA attributes, landmark roles, heading hierarchy, and semantic HTML usage to ensure WCAG compliance. HTML spec validation: Validates elements and attributes against the living HTML specification, catching deprecated patterns and invalid nesting. Custom rule configuration: Rules are fully configurable via .markuplintrc JSON or YAML config files, supporting per-file overrides and shared presets. VS Code integration: The official vscode-markuplint extension provides real-time linting feedback directly in the editor. Integration Points Install via npm with npm install -D markuplint or use npx for one-off runs. Configure rules in a .markuplintrc file at your project root. The CLI outputs standard lint results compatible with CI formatters. For monorepos, markuplint supports workspace-level configuration with per-package overrides. Agent Integration AI coding agents can use markuplint as a code quality gate — run it after generating or modifying HTML templates to catch accessibility violations, deprecated elements, or invalid attribute usage before committing. The structured JSON output format makes it easy to parse results programmatically and feed them back into the agent loop for auto-correction.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/markuplint-html-linter/)
