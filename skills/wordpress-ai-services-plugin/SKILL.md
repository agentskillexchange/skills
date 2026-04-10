---
name: "WordPress AI Services Plugin"
description: "AI Services is a WordPress plugin by Felix Arntz that exposes AI capabilities centrally across PHP, REST API, JavaScript, and WP-CLI. It is built as infrastructure for other plugins and site workflows, rather than as a single-purpose chatbot feature."
verification: security_reviewed
source: "https://github.com/felixarntz/ai-services"
category:
  - "WordPress &amp; CMS"
framework:
  - "Multi-Framework"
---

# WordPress AI Services Plugin

AI Services is an open-source WordPress plugin that makes generative AI capabilities available through a common interface inside WordPress. According to the upstream project, it exposes AI functionality through PHP APIs, the WordPress REST API, JavaScript, and WP-CLI, which means developers can build WordPress features on top of one shared service layer instead of hard-coding directly to a single model provider. The plugin is provider-agnostic by design and is intended to support providers such as Anthropic, Google, and OpenAI through a uniform abstraction.
That scope makes it a strong ASE fit for WordPress and CMS workflows. The plugin is useful when an agent or developer wants to add AI-backed editorial tools, admin-side assistants, custom plugin features, or reusable AI integrations to a WordPress stack while keeping credentials and provider settings centralized. The upstream README also highlights an AI Playground screen and settings UI for configuring provider credentials, which gives teams a concrete environment for experimentation before they wire the APIs into production features.
The project is real and source-backed: it has an active GitHub repository, a WordPress.org plugin page, public documentation, and a GPL license. The documented development install flow is to clone the repository into wp-content/plugins/ai-services, then run composer install, npm install, and npm run build. Once activated, the plugin exposes admin screens under Settings and Tools, making it a practical integration layer for AI-enabled WordPress development rather than a vague concept entry.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-ai-services-plugin/)
