---
title: "Stress-test JavaScript and TypeScript test suites with mutation testing before risky changes ship with StrykerJS"
description: "Run mutation testing against JS or TS projects to find tests that still pass when real defects are introduced."
verification: listed
source: "https://github.com/stryker-mutator/stryker-js"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "stryker-mutator/stryker-js"
  github_stars: 2828
  npm_package: "@stryker-mutator/core"
  npm_weekly_downloads: 1537001
---

# Stress-test JavaScript and TypeScript test suites with mutation testing before risky changes ship with StrykerJS

Use StrykerJS when an agent needs to measure whether a JavaScript or TypeScript test suite actually catches meaningful code changes, especially before merges, refactors, or releases. This is distinct from using the project normally because the job is specifically mutation-testing and reporting weak assertions, surviving mutants, and test effectiveness gaps. The scope boundary is clear: it is a mutation-testing quality gate, not a general test runner, framework, or CI platform listing.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stress-test-javascript-and-typescript-test-suites-with-mutation-testing-before-risky-changes-ship-with-strykerjs/)
