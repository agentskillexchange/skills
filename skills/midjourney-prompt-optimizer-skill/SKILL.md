---
name: "Midjourney Prompt Optimizer"
description: "Analyze and optimize Midjourney prompts using parameter tuning for -ar, -stylize, -chaos, and -weird flags. Generates prompt variations with style references (-sref) and character references (-cref) for consistent image output."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/midjourney-prompt-optimizer-skill/"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Gemini"
---

# Midjourney Prompt Optimizer

Midjourney Prompt Optimizer is built around Midjourney prompt engineering workflow. It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like parameter tuning, style references, aspect ratio, chaos, stylize, version flags and preserving the operational context that matters for real tasks.
In practice, the skill gives an agent a stable interface to midjourney so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Analyze and optimize Midjourney prompts using parameter tuning for -ar, -stylize, -chaos, and -weird flags. Generates prompt variations with style references (-sref) and character references (-cref) for consistent image output. The implementation typically relies on parameter tuning, style references, aspect ratio, chaos, stylize, version flags, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses parameter tuning, style references, aspect ratio, chaos, stylize, version flags instead of scraping a UI, which makes runs easier to audit and retry.
Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
Fits into broader integration points such as iterative image generation, style consistency, and creative prompt chains.

 Key integration points include iterative image generation, style consistency, and creative prompt chains. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/midjourney-prompt-optimizer-skill/)
