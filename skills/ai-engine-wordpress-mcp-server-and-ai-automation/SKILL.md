---
name: AI Engine WordPress MCP Server and AI Automation
description: AI Engine is a WordPress plugin by Meow Apps that connects sites to OpenAI,
  Claude, Gemini, and other models while exposing WordPress actions through MCP and
  REST interfaces. This skill helps agents configure providers, enable the plugin&#8217;s
  MCP capabilities, and automate content, chatbots, media, and site-management workflows
  from WordPress.
verification: security_reviewed
source: https://github.com/jordymeow/ai-engine
category:
- WordPress &amp; CMS
framework:
- MCP
tool_ecosystem:
  github_repo: jordymeow/ai-engine
  github_stars: 37
---
# AI Engine WordPress MCP Server and AI Automation

AI Engine is a WordPress plugin from Meow Apps that turns a normal WordPress installation into an AI-enabled workspace. It supports multiple providers including OpenAI, Anthropic, Google, OpenRouter, and others, and it exposes WordPress capabilities through internal APIs, REST endpoints, function-calling features, and MCP support. That makes it a strong fit for ASE because the job-to-be-done is specific: connect a site to AI providers, enable AI-powered features inside WordPress, and let agents interact with posts, media, comments, SEO, and broader site operations through documented plugin interfaces.
A useful skill built around AI Engine can guide an agent through the documented install path, configure an API environment, create chatbots, use the Copilot and content tools, and enable MCP so tools like Claude, Claude Code, ChatGPT, or OpenClaw can work against a live WordPress site. The upstream docs and plugin page also describe embeddings, vector-database integrations, AI forms, and plugin-to-plugin extensions such as SEO Engine and Social Engine. Those are practical integration points, not vague marketing claims.
From an intake perspective, AI Engine passes because it has a real WordPress.org plugin listing, official documentation from Meow Apps, an active GitHub repository, and recent updates. The skill would output provider setup steps, MCP configuration guidance, shortcode and chatbot patterns, and troubleshooting notes for REST, nonce, caching, or provider quota issues. That gives ASE a source-backed WordPress-and-MCP entry rather than a generic AI for WordPress placeholder.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ai-engine-wordpress-mcp-server-and-ai-automation/)
