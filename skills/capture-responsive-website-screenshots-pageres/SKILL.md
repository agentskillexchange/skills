---
title: "Capture responsive website screenshots for visual QA with Pageres"
description: "Tool used: Pageres ( sindresorhus/pageres ). This skill turns Pageres into a narrow operator workflow: an agent takes the same URL, captures it at multiple viewport sizes, and returns a clean set of screenshots for visual QA. The useful behavior is not “use a screenshot tool” in the abstract. The useful behavior is: given a page or a short list of pages, capture desktop and mobile views consistently so a human can inspect layout drift, hero changes, broken sections, or release regressions without opening a browser and resizing windows by hand. Invoke this when the job is specifically about visual verification. Good fits include checking landing page changes before publish, building before-and-after artifacts for a design review, generating proof screenshots for client approval, or creating a lightweight visual baseline after a deploy. Do not invoke it when the user needs general site browsing, interaction testing, scraping, or accessibility audits. Pageres is the boundary here: it captures pages, it does not replace Playwright, Selenium, or a full QA suite. The scope boundary matters because it keeps this entry skill-shaped instead of turning it into a generic product listing. An agent using this skill should accept URLs, viewport presets, and output naming rules, then produce organized screenshot artifacts. It should not pretend to do end-to-end browser automation. Integration points are straightforward: URL lists from a CMS or deployment pipeline, file output to local folders or cloud storage, and handoff into review docs, release notes, or issue threads."
source: "https://github.com/sindresorhus/pageres"
verification: "security_reviewed"
category:
  - "Browser Automation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "sindresorhus/pageres"
  github_stars: 9741
---

# Capture responsive website screenshots for visual QA with Pageres

Tool used: Pageres ( sindresorhus/pageres ). This skill turns Pageres into a narrow operator workflow: an agent takes the same URL, captures it at multiple viewport sizes, and returns a clean set of screenshots for visual QA. The useful behavior is not “use a screenshot tool” in the abstract. The useful behavior is: given a page or a short list of pages, capture desktop and mobile views consistently so a human can inspect layout drift, hero changes, broken sections, or release regressions without opening a browser and resizing windows by hand. Invoke this when the job is specifically about visual verification. Good fits include checking landing page changes before publish, building before-and-after artifacts for a design review, generating proof screenshots for client approval, or creating a lightweight visual baseline after a deploy. Do not invoke it when the user needs general site browsing, interaction testing, scraping, or accessibility audits. Pageres is the boundary here: it captures pages, it does not replace Playwright, Selenium, or a full QA suite. The scope boundary matters because it keeps this entry skill-shaped instead of turning it into a generic product listing. An agent using this skill should accept URLs, viewport presets, and output naming rules, then produce organized screenshot artifacts. It should not pretend to do end-to-end browser automation. Integration points are straightforward: URL lists from a CMS or deployment pipeline, file output to local folders or cloud storage, and handoff into review docs, release notes, or issue threads.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/capture-responsive-website-screenshots-pageres/)
