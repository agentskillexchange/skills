---
title: "Extract translation keys from code and maintain locale catalogs with i18next-parser"
description: "Use i18next-parser when an agent needs to scan a codebase, find translation calls, and update locale resource files as part of localization maintenance. This is a bounded catalog-maintenance workflow, not a generic i18n platform listing."
verification: security_reviewed
source: "https://github.com/i18next/i18next-parser"
category:
  - "Templates &amp; Workflows"
framework:
  - "Multi-Framework"
---

# Extract translation keys from code and maintain locale catalogs with i18next-parser

Tool used: i18next-parser (i18next/i18next-parser).

This skill is for an agent that maintains localization files by scanning an application codebase for translation keys and synchronizing those findings into locale catalogs. The agent uses i18next-parser to detect translation calls, extract keys and default values, and update the resource files that translators or release pipelines depend on. The job-to-be-done is concrete: keep translation catalogs aligned with the actual strings referenced in code.

Invoke this when a project already uses i18next-style translation patterns and the user wants automation around catalog upkeep, missing-key discovery, CI checks, or pre-release localization prep. It is useful when the agent should scan source files, regenerate or merge locale JSON, surface missing entries, and hand the result to translators or commit automation. It is not the right choice for general translation management, runtime language switching, or choosing an internationalization framework from scratch.

The scope boundary is what makes this a skill instead of a product card. The entry is not about i18next as a whole, and not even about the parser as a generic package. It is about a narrow operator workflow: inspect code, extract translation keys, update locale resources, and reduce drift between source and catalog files. Typical integration points include CI pipelines, monorepo maintenance scripts, release preparation, localization QA, and coding agents that need to update translation assets after feature work changes UI strings.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/extract-translation-keys-from-code-and-maintain-locale-catalogs-i18next-parser/)
