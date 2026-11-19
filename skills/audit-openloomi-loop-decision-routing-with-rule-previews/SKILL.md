---
name: "Audit OpenLoomi Loop decision routing with deterministic rule previews"
slug: "audit-openloomi-loop-decision-routing-with-rule-previews"
description: "Inspect OpenLoomi Loop classifier rules, dry-run sample work signals and return an ordered routing diagnosis before changing live decisions."
verification: "security_reviewed"
source: "https://github.com/melandlabs/openloomi/tree/main/skills/openloomi-loop"
author: "melandlabs"
publisher_type: "Organization"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
---

# Audit OpenLoomi Loop decision routing with deterministic rule previews

Inspect OpenLoomi Loop classifier rules, dry-run sample work signals and return an ordered routing diagnosis before changing live decisions.

## Prerequisites

OpenLoomi Desktop with local session; skill-capable agent runtime; Node.js for setup helper; curl; jq

## Installation

Install or set up from the source-backed instructions:

Install and open OpenLoomi Desktop from https://github.com/melandlabs/openloomi/releases and complete sign-in or guest setup inside the app. With Node.js/npm available, install the upstream skill subset: npx skills add https://github.com/melandlabs/openloomi/tree/main/skills --skill openloomi openloomi-setup openloomi-loop . Select the intended runtime in the installer. Invoke openloomi-setup and run its bundled status helper; proceed only when ready is true. Invoke openloomi-loop for the bounded routing diagnosis. No plugin marketplace or MCP server is required.

- Source: https://github.com/melandlabs/openloomi/tree/main/skills/openloomi-loop

## Documentation

- https://github.com/melandlabs/openloomi/blob/main/skills/openloomi-loop/SKILL.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-openloomi-loop-decision-routing-with-rule-previews/)
