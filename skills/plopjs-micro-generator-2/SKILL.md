---
name: "Plop.js Micro-Generator"
description: "Runs Plop.js micro-generators using Handlebars templates and the Plop Node API for component, hook, and module scaffolding. Supports custom Inquirer.js prompts and built-in addMany/modify/append actions."
category: "Templates & Workflows"
framework: "Cursor"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/plopjs-micro-generator-2/"
---

# Plop.js Micro-Generator

Runs Plop.js micro-generators using Handlebars templates and the Plop Node API for component, hook, and module scaffolding. Supports custom Inquirer.js prompts and built-in addMany/modify/append actions.

## Overview

The Plop.js Micro-Generator skill automates repetitive code generation tasks using the Plop framework. It executes Handlebars-based templates through the Plop Node API, generating consistent components, hooks, utilities, and modules from predefined patterns.

The skill supports the full Plop action palette including addMany for batch file creation, modify for existing file updates using regex patterns, and append for adding imports or exports to index files. Custom Inquirer.js prompts enable interactive or programmatic input for template variables.

Advanced features include dynamic generator registration, custom Handlebars helpers for case transformation and pluralization, and plopfile composition from multiple generator packages. The skill integrates with project-level plopfiles to ensure generated code follows established conventions for naming, directory structure, and import patterns across the codebase.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill plopjs-micro-generator-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill plopjs-micro-generator-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill plopjs-micro-generator-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill plopjs-micro-generator-2 -a codex
```

### OpenClaw

```bash
clawhub install plopjs-micro-generator-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/plopjs-micro-generator-2/
