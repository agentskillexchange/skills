---
title: "Refresh Cookiecutter-based repositories from their upstream template without losing local answers"
description: "Use Cruft when an agent needs to pull new changes from a Cookiecutter template into an existing generated repository without redoing the project from scratch. The agent tracks the template origin, previews the diff, applies the update, and preserves the repository’s saved answers and local customizations as carefully as possible."
verification: security_reviewed
source: "https://github.com/cruft/cruft"
category:
  - "Templates &amp; Workflows"
framework:
  - "Multi-Framework"
---

# Refresh Cookiecutter-based repositories from their upstream template without losing local answers

This ASE entry is built around Cruft, the open source tool for keeping Cookiecutter-generated repositories in sync with the template they came from. The agent job-to-be-done is specific: identify the original template for a repository, compare the current project against the latest template revision, apply the upstream template changes, and help the maintainer review conflicts without blowing away the repo’s existing answers and hand-edited code.

You use this skill when normal product usage is the wrong abstraction. The task is not “scaffold a new project” or “list a templating engine.” The real task is to refresh many downstream repos after the platform template gains a new CI workflow, a security hardening tweak, a docs skeleton improvement, or a packaging fix. An agent can inspect the .cruft.json state file, fetch the newer template version, generate the update diff, call out conflicts in generated files versus local edits, and turn template maintenance into a repeatable review step instead of a risky manual copy-paste job.

The scope boundary is what makes this skill-shaped. This entry is not a generic Cookiecutter card, and it is not for creating templates in the abstract. It is specifically for updating already-generated repositories from their source template. Integration points include template-governed monorepos, internal starter kits, compliance-driven repo refresh programs, release engineering checklists, and maintenance bots that need a safe operator playbook for propagating template changes. Upstream evidence is strong: official GitHub repository, PyPI package, documentation site, tagged releases, MIT license, and an existing install/update workflow used in real templated repos.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/refresh-cookiecutter-based-repositories-from-upstream-template/)
