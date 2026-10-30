---
name: "Ground React UI edits in project components and tokens with the Onsystem skill"
slug: "ground-react-ui-edits-in-project-components-and-tokens-with-onsystem-skill"
description: "Discover project-specific React components and tokens, implement a bounded UI change, and repair new design-system violations with Onsystem checks."
verification: "security_reviewed"
source: "https://github.com/dgesteves/onsystem/blob/b589c7aff82d90440eb941bc464200e0ca7e1df4/plugins/onsystem-agent/skills/onsystem/SKILL.md"
author: "Diogo Esteves"
publisher_type: "individual"
category: "Code Quality & Review"
framework: "Multi-Framework"
---

# Ground React UI edits in project components and tokens with the Onsystem skill

Discover project-specific React components and tokens, implement a bounded UI change, and repair new design-system violations with Onsystem checks.

## Prerequisites

Node.js >=20.19, npm/npx, coding agent supporting Agent Skills; optional stdio MCP client; React project with discoverable design-system components and tokens

## Installation

Install or set up from the source-backed instructions:

From the target project run npx skills add dgesteves/onsystem. Confirm discovery with npx -y onsystem inspect. Optional MCP stdio server: command npx, args ["-y", "onsystem", "--root", "/absolute/path/to/project"]. Without MCP, use the documented inspect, export --format design-md, and check --format json commands.

- Source: https://github.com/dgesteves/onsystem/blob/b589c7aff82d90440eb941bc464200e0ca7e1df4/plugins/onsystem-agent/skills/onsystem/SKILL.md

## Documentation

- https://onsystem.vercel.app/docs

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ground-react-ui-edits-in-project-components-and-tokens-with-onsystem-skill/)
