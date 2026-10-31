---
name: "Measure installed Skill use-rate with Pluribus receipts"
slug: "skill-use-rate-receipts"
description: "Use Pluribus context receipts to distinguish skills that are only discovered, installed, or bound from skills that were actually invoked and acted on. Best for Claude Code, Cursor, Codex, OpenClaw, and multi-agent teams debugging skill sprawl, context pollution, or unused installed resources."
github_stars: 3
verification: "listed"
source: "https://github.com/caioribeiroclw-pixel/pluribus/blob/main/docs/skill-use-rate-receipts.md"
author: "Caio Ribeiro"
publisher_type: "User"
category: "Monitoring & Alerts"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "caioribeiroclw-pixel/pluribus"
  github_stars: 3
  npm_package: "pluribus-context"
---

# Measure installed Skill use-rate with Pluribus receipts

Use this skill when a project has installed Agent Skills, MCP-backed skills, prompt bundles, or shared context resources, but nobody can tell which ones actually influenced work. Installation alone is a weak signal: a skill can be present in Claude Code, Cursor, Codex, OpenClaw, or another agent runtime while never being discovered, invoked, or used in a tool call. This skill teaches the agent to emit a small Pluribus-style receipt that separates lifecycle states instead of treating installed resources as active context.

The receipt records the skill source, target agent, scope, install method, bind/attach status, whether invocation was observed, whether the skill appears to have affected an action, and the measurement window. It should use `null` or `unknown` when the host cannot observe invocation rather than pretending absence of evidence is evidence of no use. The goal is to help reviewers remove dead context, find skills that are installed but never invoked, and debug cases where a user expected a skill to activate but the agent never loaded it.

Do not include prompts, transcripts, secrets, full tool inputs, customer data, or raw model outputs in the receipt. Keep only privacy-safe lifecycle evidence: names, source refs, agent/runtime, timestamps or windows, coarse action categories, counts, and warning status.

## Installation

### OpenClaw

```bash
clawhub install skill-use-rate-receipts
```

### Manual install

```bash
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/skills/skill-use-rate-receipts ~/.agent-skills/skill-use-rate-receipts
```

### Optional third-party installer

The `skills` npm package is maintained by Vercel Labs / third parties, not AgentSkillExchange. If you choose to use it, pin the package version:

```bash
npm exec --package=skills@1.5.7 -- skills add agentskillexchange/skills --skill skill-use-rate-receipts
```

## Usage

1. List the skills or prompt resources installed for the current project or agent.
2. For each item, classify lifecycle state: discovered, installed, bound/attached, invocation observed, acted-on observed.
3. Emit `unknown` for host states that cannot be measured directly.
4. Warn when a skill is installed or bound but has zero observed invocations in the measurement window.
5. Keep values privacy-safe and store the receipt beside other project evidence.

Minimal receipt example:

```json
{
  "receipt_type": "pluribus.skill_use_rate.v1",
  "measurement_window": "last_7_days",
  "skills": [
    {
      "slug": "api-review-skill",
      "source_ref": "github:org/agent-skills/api-review@abc123",
      "target_agent": "Claude Code",
      "scope": "project",
      "install_method": "copy",
      "installed": true,
      "bound": true,
      "invocation_observed": false,
      "acted_on_observed": null,
      "warning": "installed_but_unused"
    }
  ]
}
```

## Documentation

- Pluribus skill use-rate receipts: https://github.com/caioribeiroclw-pixel/pluribus/blob/main/docs/skill-use-rate-receipts.md
- Example receipt and checker: https://github.com/caioribeiroclw-pixel/pluribus/tree/main/examples/skill-use-rate-receipts
- npm package: https://www.npmjs.com/package/pluribus-context

## Source

- https://github.com/caioribeiroclw-pixel/pluribus
