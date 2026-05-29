---
name: "Emit policy receipts for hard-rule agent skills with Pluribus"
slug: "emit-policy-receipts-for-hard-rule-agent-skills-with-pluribus"
description: "Uses the Pluribus skill-policy receipt recipe to make hard agent-skill rules auditable before and after writes. Best for Claude Code, OpenClaw, Cursor, Codex, and other coding-agent workflows where natural-language instructions such as forbidden services, generated-file boundaries, or preview-before-apply rules need explicit allow/refuse evidence."
github_stars: 2
verification: "listed"
source: "https://github.com/caioribeiroclw-pixel/pluribus/blob/main/docs/skill-policy-receipts.md"
author: "Caio Ribeiro"
publisher_type: "Open Source Project"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "caioribeiroclw-pixel/pluribus"
  github_stars: 2
  npm_package: "pluribus-context"
  maintained: true
---

# Emit policy receipts for hard-rule agent skills with Pluribus

Use this skill when an agent skill, project rule, hook, or runbook contains a hard boundary that should not depend on prose alone. Examples include “do not call internal services from unit tests”, “do not edit generated files”, “preview migrations before apply”, “never write outside this workspace”, or “refuse before touching customer data”. The Pluribus recipe turns those rules into a small privacy-safe `skill.policy.v1` receipt that records intended targets, allow/refuse decisions, refusal reasons, post-write guard results, and `stopped_at` if the agent must halt.

The goal is not to store prompts, transcripts, raw code, secrets, stack traces, or tool output. The receipt should only capture boundary metadata that a reviewer or a later agent can inspect: which targets were considered, why each target was allowed or refused, whether a write began, and whether a simple guard passed after the write. This is useful for Claude Code, OpenClaw, Cursor, Codex, and other agent runtimes where Skills, hooks, `CLAUDE.md`, `AGENTS.md`, or policy files can be loaded dynamically but the run still needs auditable evidence that the policy was followed.

## Installation

### OpenClaw

```bash
clawhub install emit-policy-receipts-for-hard-rule-agent-skills-with-pluribus
```

### Direct repo/manual install

Clone the Agent Skill Exchange repository and copy this skill directory into the skill folder used by your agent runtime:

```bash
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/skills/emit-policy-receipts-for-hard-rule-agent-skills-with-pluribus ~/.agent-skills/emit-policy-receipts-for-hard-rule-agent-skills-with-pluribus
```

### Optional Third-Party Installer

The `skills` npm package is maintained by Vercel Labs / third parties, not AgentSkillExchange. If you choose to use it, pin the package version:

```bash
npm exec --package=skills@1.5.7 -- skills add agentskillexchange/skills --skill emit-policy-receipts-for-hard-rule-agent-skills-with-pluribus
```

## Use the Pluribus recipe

Reference the upstream Pluribus guide when adapting this skill to your own hard rule:

- Guide: https://github.com/caioribeiroclw-pixel/pluribus/blob/main/docs/skill-policy-receipts.md
- Copyable example: https://github.com/caioribeiroclw-pixel/pluribus/tree/main/examples/agent-skills/skill-policy-receipts
- Package: https://www.npmjs.com/package/pluribus-context

A minimal receipt should include:

- `intended_targets`: files, services, commands, or operations the agent considered
- `policy_decisions`: explicit `allowed` or `refused` decisions with short reasons
- `write_started`: whether mutation began after the policy decision
- `post_write_guard`: a lightweight check such as grep, lint, schema validation, or path guard
- `stopped_at`: the boundary where the agent halted when the policy required refusal

Keep the receipt small and safe to share. Do not include credentials, customer data, raw prompts, full stack traces, transcripts, raw tool output, or proprietary source code.

## Documentation

- https://github.com/caioribeiroclw-pixel/pluribus/blob/main/docs/skill-policy-receipts.md
- https://github.com/caioribeiroclw-pixel/pluribus

## Source

- [Pluribus skill policy receipts](https://github.com/caioribeiroclw-pixel/pluribus/blob/main/docs/skill-policy-receipts.md)
