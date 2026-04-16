---
title: "OpenAI Agents SDK JavaScript Workflow Toolkit"
description: "A source-backed guide to the OpenAI Agents SDK for JavaScript and TypeScript. It covers agent orchestration, tools, handoffs, tracing, and the practical install path."
verification: "security_reviewed"
source: "https://github.com/openai/openai-agents-js"
category:
  - "Library &amp; API Reference"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "openai/openai-agents-js"
  github_stars: 2635
---

# OpenAI Agents SDK JavaScript Workflow Toolkit

The OpenAI Agents SDK for JavaScript, published as @openai/agents, is a lightweight framework for building multi-agent workflows and voice agents. The upstream repository documents core concepts such as agents, tools, guardrails, handoffs, sessions, tracing, and human-in-the-loop control.

This skill is useful when you need to wire OpenAI agents into a Node.js, Deno, Bun, or Cloudflare Workers project. The upstream README shows the primary install command, npm install @openai/agents zod, plus a minimal example using Agent and run. The repository also calls out Node.js 22+, OpenAI API access, and built-in tracing for debugging workflows.

Use this skill when you want to build agentic apps with explicit tool calls, chained handoffs, and a clear runtime path from local development to production. Source: https://github.com/openai/openai-agents-js

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openai-agents-sdk-javascript-workflow-toolkit/)
