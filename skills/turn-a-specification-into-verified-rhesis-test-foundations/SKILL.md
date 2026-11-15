---
name: "Turn a specification into verified Rhesis test foundations"
slug: "turn-a-specification-into-verified-rhesis-test-foundations"
description: "Map source acceptance criteria to requirements, scoped metrics and typed test sets, with plan approval and generated-test verification."
github_stars: 404
verification: "security_reviewed"
source: "https://github.com/rhesis-ai/rhesis"
author: "Rhesis AI"
publisher_type: "Organization"
category: "Code Quality & Review"
framework: "MCP"
tool_ecosystem:
  github_repo: "rhesis-ai/rhesis"
  github_stars: 404
---

# Turn a specification into verified Rhesis test foundations

Map source acceptance criteria to requirements, scoped metrics and typed test sets, with plan approval and generated-test verification.

## Prerequisites

Git for pinned source; skill-capable MCP runtime; Rhesis account/backend and API token; supplied PRD/specification

## Installation

Install or set up from the source-backed instructions:

Obtain the reviewed source with git clone https://github.com/rhesis-ai/rhesis.git, then inside that checkout run git checkout 46bede325e77e3721a1698193e380988c6b0a500. Install the skills/rhesis directory into the chosen runtime's documented local skill directory, preserving its references. The upstream skills/rhesis/README.md describes the managed plugin and skills-CLI alternatives; choose one installation method. Separately configure the runtime's remote HTTP MCP connection to https://api.rhesis.ai/mcp/ with Authorization: Bearer , or the authorized self-hosted MCP endpoint. Keep the token in the runtime's secret configuration. Confirm the Rhesis MCP tools are available for the account role, then invoke the spec-to-test path with the PRD. No platform or endpoint execution is part of installation.

- Source: https://github.com/rhesis-ai/rhesis

## Documentation

- https://github.com/rhesis-ai/rhesis/blob/46bede325e77e3721a1698193e380988c6b0a500/skills/rhesis/references/spec-workflow.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/turn-a-specification-into-verified-rhesis-test-foundations/)
