---
name: "Run context → spec → implement coding loops in Claude Code with Conductor"
slug: "run-context-spec-and-implement-coding-loops-in-claude-code-with-conductor"
description: "Turn Claude Code into a structured project workflow that captures context, plans work, and executes implementation in reviewable tracks."
verification: "security_reviewed"
source: "https://github.com/wshobson/agents/tree/main/plugins/conductor"
author: "wshobson"
publisher_type: "individual"
category: "Templates & Workflows"
framework: "Claude Code"
---

# Run context → spec → implement coding loops in Claude Code with Conductor

Turn Claude Code into a structured project workflow that captures context, plans work, and executes implementation in reviewable tracks.

## Prerequisites

Claude Code with plugin support, access to the wshobson/agents marketplace, a Git repository to manage

## Installation

Use the upstream install or setup path that matches your environment:
- uv run plugin-eval score path/to/skill --depth quick
- uv run plugin-eval score path/to/skill --depth standard
- uv run plugin-eval certify path/to/skill

Requirements and caveats from upstream:
- **Example**: Installing python-development loads 3 Python agents, 1 scaffolding tool, and makes 16 skills available (~1000 tokens), not the entire marketplace.
- /plugin install python-development # Python with 16 specialized skills
- | python-development | python-pro, django-pro, fastapi-pro |

Basic usage or getting-started notes:
- [![Run in Smithery](https://smithery.ai/badge/skills/wshobson)](https://smithery.ai/skills?ns=wshobson&utm_source=github&utm_medium=badge) [![Gemini CLI](https://img.shields.io/badge/Gemini%20CLI-supported-blue)](GEMI...
- **80 Focused Plugins** - Granular, single-purpose plugins optimized for minimal token usage and composability
- **Granular Plugin Architecture**: 80 focused plugins optimized for minimal token usage

- Source: https://github.com/wshobson/agents/tree/main/plugins/conductor
- Extracted from upstream docs: https://raw.githubusercontent.com/wshobson/agents/HEAD/README.md

## Documentation

- https://raw.githubusercontent.com/wshobson/agents/main/plugins/conductor/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-context-spec-and-implement-coding-loops-in-claude-code-with-conductor/)
