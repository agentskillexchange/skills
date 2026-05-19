---
name: "Extract translation keys from code and maintain locale catalogs with i18next-parser"
slug: "extract-translation-keys-from-code-and-maintain-locale-catalogs-i18next-parser"
description: "Use i18next-parser when an agent needs to scan a codebase, find translation calls, and update locale resource files as part of localization maintenance. This is a bounded catalog-maintenance workflow, not a generic i18n platform listing."
github_stars: 556
verification: "security_reviewed"
source: "https://github.com/i18next/i18next-parser"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "i18next/i18next-parser"
  github_stars: 556
---

# Extract translation keys from code and maintain locale catalogs with i18next-parser

Use i18next-parser when an agent needs to scan a codebase, find translation calls, and update locale resource files as part of localization maintenance. This is a bounded catalog-maintenance workflow, not a generic i18n platform listing.

## Prerequisites

Node.js, source code using i18next translation patterns

## Installation

Use the upstream install or setup path that matches your environment:
- This project is no more maintained as of September 2025. Please use [i18next/i18next-cli](https://github.com/i18next/i18next-cli) instead that does everything you might need and more. Just run npx i18next-cli migrate-...
- yarn global add i18next-parser
- npm install -g i18next-parser
- yarn add -D i18next-parser

Requirements and caveats from upstream:
- 9.x is tested on Node 18, 20 and 22.
- 8.x is tested on Node 16, 18 and 20.
- 7.x is tested on Node 14, 16 and 18.

Basic usage or getting-started notes:
- ### CLI
- You can use the CLI with the package installed locally but if you want to use it from anywhere, you better install it globally:
- i18next 'app/**/*.{js,hbs}' 'lib/**/*.{js,hbs}' [-oc]

- Source: https://github.com/i18next/i18next-parser
- Extracted from upstream docs: https://raw.githubusercontent.com/i18next/i18next-parser/HEAD/README.md

## Documentation

- https://www.i18next.com/how-to/extracting-translations

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/extract-translation-keys-from-code-and-maintain-locale-catalogs-i18next-parser/)
