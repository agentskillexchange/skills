---
title: "Generate right-to-left CSS variants from LTR stylesheets before multilingual launches with RTLCSS"
description: "Tool: RTLCSS is an open source framework and npm package for converting left-to-right CSS into right-to-left CSS. In ASE, the useful skill-shaped framing is narrow: an agent takes an existing stylesheet that was authored for LTR layouts, generates an RTL counterpart, and returns it for a multilingual build, preview, or deployment step.\nWhat the agent does: it runs RTLCSS against prepared CSS assets, flips directional declarations where appropriate, preserves non-directional rules, and emits an RTL-ready stylesheet for downstream packaging. That is valuable during website localization, white-label theming, email template localization, design-system exports, and release preparation for products that need Arabic or Hebrew support without manually rewriting every selector.\nWhen to use it: invoke this when the task is specifically “produce the RTL stylesheet from the existing LTR source.” Do not invoke it as a generic CSS framework listing or as a stand-in for translation work. The agent uses it after UI strings and layout requirements already exist and before the localized build is shipped.\nScope boundary: this skill does not translate copy, audit locale coverage, redesign components, or test the final UX. It strictly handles directional stylesheet transformation.\nIntegration points: frontend build scripts, localization pipelines, CMS theme exports, email template variants, and CI steps that generate release assets per locale. Upstream evidence is strong: official GitHub repo, npm package, MIT license, public documentation, tagged releases, and ongoing adoption."
verification: security_reviewed
source: "https://github.com/MohammadYounes/rtlcss"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "MohammadYounes/rtlcss"
  github_stars: 1708
---

# Generate right-to-left CSS variants from LTR stylesheets before multilingual launches with RTLCSS

Tool: RTLCSS is an open source framework and npm package for converting left-to-right CSS into right-to-left CSS. In ASE, the useful skill-shaped framing is narrow: an agent takes an existing stylesheet that was authored for LTR layouts, generates an RTL counterpart, and returns it for a multilingual build, preview, or deployment step.
What the agent does: it runs RTLCSS against prepared CSS assets, flips directional declarations where appropriate, preserves non-directional rules, and emits an RTL-ready stylesheet for downstream packaging. That is valuable during website localization, white-label theming, email template localization, design-system exports, and release preparation for products that need Arabic or Hebrew support without manually rewriting every selector.
When to use it: invoke this when the task is specifically “produce the RTL stylesheet from the existing LTR source.” Do not invoke it as a generic CSS framework listing or as a stand-in for translation work. The agent uses it after UI strings and layout requirements already exist and before the localized build is shipped.
Scope boundary: this skill does not translate copy, audit locale coverage, redesign components, or test the final UX. It strictly handles directional stylesheet transformation.
Integration points: frontend build scripts, localization pipelines, CMS theme exports, email template variants, and CI steps that generate release assets per locale. Upstream evidence is strong: official GitHub repo, npm package, MIT license, public documentation, tagged releases, and ongoing adoption.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/generate-right-to-left-css-variants-from-ltr-stylesheets-before-multilingual-launches-rtlcss
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/generate-right-to-left-css-variants-from-ltr-stylesheets-before-multilingual-launches-rtlcss` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-right-to-left-css-variants-from-ltr-stylesheets-before-multilingual-launches-rtlcss/)
