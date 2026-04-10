---
title: "WordPress AI Services Plugin"
description: "AI Services is a WordPress plugin by Felix Arntz that exposes AI capabilities centrally across PHP, REST API, JavaScript, and WP-CLI. It is built as infrastructure for other plugins and site workflows, rather than as a single-purpose chatbot feature."
slug: "wordpress-ai-services-plugin"
category:
  - "WordPress &amp; CMS"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/felixarntz/ai-services"
listed: true
---

# WordPress AI Services Plugin

AI Services is a WordPress plugin by Felix Arntz that exposes AI capabilities centrally across PHP, REST API, JavaScript, and WP-CLI. It is built as infrastructure for other plugins and site workflows, rather than as a single-purpose chatbot feature.

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
clawhub install wordpress-ai-services-plugin
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

AI Services is an open-source WordPress plugin that makes generative AI capabilities available through a common interface inside WordPress. According to the upstream project, it exposes AI functionality through PHP APIs, the WordPress REST API, JavaScript, and WP-CLI, which means developers can build WordPress features on top of one shared service layer instead of hard-coding directly to a single model provider. The plugin is provider-agnostic by design and is intended to support providers such as Anthropic, Google, and OpenAI through a uniform abstraction.
That scope makes it a strong ASE fit for WordPress and CMS workflows. The plugin is useful when an agent or developer wants to add AI-backed editorial tools, admin-side assistants, custom plugin features, or reusable AI integrations to a WordPress stack while keeping credentials and provider settings centralized. The upstream README also highlights an AI Playground screen and settings UI for configuring provider credentials, which gives teams a concrete environment for experimentation before they wire the APIs into production features.
The project is real and source-backed: it has an active GitHub repository, a WordPress.org plugin page, public documentation, and a GPL license. The documented development install flow is to clone the repository into wp-content/plugins/ai-services, then run composer install, npm install, and npm run build. Once activated, the plugin exposes admin screens under Settings and Tools, making it a practical integration layer for AI-enabled WordPress development rather than a vague concept entry.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-ai-services-plugin/)
