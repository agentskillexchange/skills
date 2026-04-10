---
name: "Tolgee Open Source Localization and i18n Platform"
description: "Tolgee is an open-source localization platform that lets developers and translators manage translations through in-context editing, machine translation integration, and SDKs for React, Vue, Angular, Svelte, and more. It includes MCP server support for AI coding assistants."
verification: security_reviewed
source: "https://github.com/tolgee/tolgee-platform"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "tolgee/tolgee-platform"
  github_stars: 3875
---

# Tolgee Open Source Localization and i18n Platform

Tolgee is a developer-friendly, open-source localization platform that replaces the tedious process of managing .json, .po, and other translation files with an integrated, visual workflow. It supports in-context translation editing directly within your running application, machine translation via DeepL, Google Translate, and AWS Translate, and provides SDKs for all major JavaScript frameworks.
How It Works
Tolgee consists of a self-hostable backend platform (Java/Kotlin) and frontend SDKs that embed into your application. The SDKs intercept translation keys at runtime and enable in-context editing — developers and translators can ALT+click on any text element in the app to edit translations directly, with automatic screenshot capture for context. The platform exposes a REST API for programmatic access and a CLI tool (tolgee-cli) for syncing translations between your codebase and the Tolgee server.
Key Features

In-context translation: ALT+click any string in your app to edit translations directly. Works in development and production via the Tolgee Tools Chrome extension.
Machine translation: Integrated DeepL, Google Translate, and AWS Translate services for instant translation suggestions.
Translation memory: Automatically suggests translations based on previously used strings in your project, showing similarity percentages.
Auto-translation: New keys are automatically translated using translation memory or configured machine translation services.
Framework SDKs: Official SDKs for React, Vue, Angular, Svelte, Next.js, Gatsby, and vanilla JavaScript with i18next integration.
MCP server: Exposes a Model Context Protocol server enabling AI coding assistants to search keys, create/update translations, manage languages, and trigger machine translation directly from the editor.
Activity log: Track who modified, reviewed, or commented on every translation phrase.

Integration Points
Self-host with Docker (docker run -p 8085:8085 tolgee/tolgee) or use Tolgee Cloud. Install framework SDKs via npm (e.g., npm install @tolgee/react). Use the Tolgee CLI (npm install -g @tolgee/cli) to push/pull translations between your repo and the platform. The REST API supports webhooks for CI/CD integration.
Agent Integration
AI agents can leverage Tolgee's MCP server to manage translations without leaving the coding environment. The MCP interface supports searching translation keys, creating new keys with translations, updating existing translations across languages, managing project languages, and triggering batch machine translation — making it possible for coding agents to handle internationalization tasks end-to-end.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tolgee-localization-i18n-platform/)
