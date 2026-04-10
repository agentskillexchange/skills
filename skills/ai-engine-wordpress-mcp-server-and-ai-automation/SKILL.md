---
title: "AI Engine WordPress MCP Server and AI Automation"
description: "AI Engine is a WordPress plugin by Meow Apps that connects sites to OpenAI, Claude, Gemini, and other models while exposing WordPress actions through MCP and REST interfaces. This skill helps agents configure providers, enable the plugin’s MCP capabilities, and automate content, chatbots, media, and site-management workflows from WordPress."
slug: "ai-engine-wordpress-mcp-server-and-ai-automation"
category:
  - "WordPress &amp; CMS"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://github.com/jordymeow/ai-engine"
tool_ecosystem:
  github_repo: "jordymeow/ai-engine"
  github_stars: 37
---

# AI Engine WordPress MCP Server and AI Automation

AI Engine is a WordPress plugin by Meow Apps that connects sites to OpenAI, Claude, Gemini, and other models while exposing WordPress actions through MCP and REST interfaces. This skill helps agents configure providers, enable the plugin’s MCP capabilities, and automate content, chatbots, media, and site-management workflows from WordPress.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install ai-engine-wordpress-mcp-server-and-ai-automation
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

AI Engine is a WordPress plugin from Meow Apps that turns a normal WordPress installation into an AI-enabled workspace. It supports multiple providers including OpenAI, Anthropic, Google, OpenRouter, and others, and it exposes WordPress capabilities through internal APIs, REST endpoints, function-calling features, and MCP support. That makes it a strong fit for ASE because the job-to-be-done is specific: connect a site to AI providers, enable AI-powered features inside WordPress, and let agents interact with posts, media, comments, SEO, and broader site operations through documented plugin interfaces.
A useful skill built around AI Engine can guide an agent through the documented install path, configure an API environment, create chatbots, use the Copilot and content tools, and enable MCP so tools like Claude, Claude Code, ChatGPT, or OpenClaw can work against a live WordPress site. The upstream docs and plugin page also describe embeddings, vector-database integrations, AI forms, and plugin-to-plugin extensions such as SEO Engine and Social Engine. Those are practical integration points, not vague marketing claims.
From an intake perspective, AI Engine passes because it has a real WordPress.org plugin listing, official documentation from Meow Apps, an active GitHub repository, and recent updates. The skill would output provider setup steps, MCP configuration guidance, shortcode and chatbot patterns, and troubleshooting notes for REST, nonce, caching, or provider quota issues. That gives ASE a source-backed WordPress-and-MCP entry rather than a generic AI for WordPress placeholder.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ai-engine-wordpress-mcp-server-and-ai-automation/)
