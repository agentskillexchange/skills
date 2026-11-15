---
name: "Recover Playwright selectors after UI refactors with QA Skills"
slug: "recover-playwright-selectors-after-ui-refactors-with-qa-skills"
description: "Compare old and new UI evidence, repair confirmed locator drift in existing Playwright tests, and return a validated diff with per-change evidence."
verification: "security_reviewed"
source: "https://github.com/petrkindlmann/qa-skills/tree/62434253c2592f27b494609c27f224939c86346d/skills/selector-drift-recovery"
author: "kindlmann (petrkindlmann)"
publisher_type: "individual"
category: "Code Quality & Review"
framework: "Multi-Framework"
---

# Recover Playwright selectors after UI refactors with QA Skills

Compare old and new UI evidence, repair confirmed locator drift in existing Playwright tests, and return a validated diff with per-change evidence.

## Prerequisites

Agent Skills-compatible host; existing Playwright >=1.50 suite and browser dependencies; project Node/TypeScript tooling; old and new UI evidence; optional tsx and GitHub CLI for authorized PR work

## Installation

Install or set up from the source-backed instructions:

Clone https://github.com/petrkindlmann/qa-skills.git into a new checkout and check out reviewed revision 62434253c2592f27b494609c27f224939c86346d. Copy the entire skills/selector-drift-recovery directory, including references, into the agent host’s configured skills directory (upstream documents project .skills/). Preserve any existing skill directory rather than overwriting it. Reload skills as the host requires and invoke selector-drift-recovery explicitly. Use the existing project Playwright toolchain and review the prerequisite gates before running recovery; individual skill installation does not install the repository QA runner.

- Source: https://github.com/petrkindlmann/qa-skills/tree/62434253c2592f27b494609c27f224939c86346d/skills/selector-drift-recovery

## Documentation

- https://github.com/petrkindlmann/qa-skills/tree/62434253c2592f27b494609c27f224939c86346d/skills/selector-drift-recovery/SKILL.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/recover-playwright-selectors-after-ui-refactors-with-qa-skills/)
