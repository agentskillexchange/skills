---
name: "Maxun No-Code Web Data Extraction Platform"
description: "Maxun is an open-source no-code web data platform for turning any website into structured, reliable data. It supports extraction via recorder mode and LLM-powered natural language mode, plus crawling, scraping, and search capabilities. With 15,000+ GitHub stars and both SDK and CLI interfaces, it handles everything from simple page scrapes to complex automated workflows."
verification: security_reviewed
source: "https://github.com/getmaxun/maxun"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "getmaxun/maxun"
  github_stars: 15319
---

# Maxun No-Code Web Data Extraction Platform

Maxun is an open-source no-code platform for web scraping, crawling, search, and AI-powered data extraction. It lets users turn websites into structured APIs and datasets without writing code, using either a visual recorder that captures browser interactions or an LLM-powered extraction mode where you describe what you want in natural language.
How It Works
Maxun operates through four types of robots, each designed for a different data collection job. Extract robots emulate real user behavior to capture structured data from websites. In Recorder Mode, you browse a site while Maxun records your actions and turns them into a reusable extraction robot. In AI Mode, you describe the data you want in plain language and an LLM-powered engine handles the rest, identifying elements, navigating pagination, and structuring output. Scrape robots convert full webpages into clean Markdown or HTML and capture screenshots. Crawl robots traverse entire websites following links and extracting content from every relevant page with configurable scope controls.
SDK and CLI
Beyond the visual interface, Maxun provides a complete developer SDK (available as an npm package) for programmatic extraction, scheduling, and robot management. The CLI lets you create robots, trigger runs, and retrieve extracted data directly from the terminal, making it suitable for integration into agent workflows and automation pipelines. Agents can create extraction robots via the SDK, schedule recurring runs, and retrieve structured JSON results through the API.
Output and Integration
Maxun outputs structured JSON data, clean Markdown, HTML content, and screenshots depending on the robot type. It handles common web complexities including pagination, infinite scrolling, dynamic content loading, cookie consent dialogs, and anti-bot detection. The platform supports scheduling for recurring extraction jobs, webhook notifications for completed runs, and proxy configuration for geographic targeting. Data can be exported to Google Sheets, databases, or consumed via the REST API.
Deployment
Maxun runs locally via Docker Compose or without Docker, and also offers a hosted cloud version. The self-hosted option gives full control over data flow and privacy. Configuration is managed through environment variables for database connections, browser settings, LLM API keys, and proxy configuration.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/maxun-no-code-web-data-extraction/)
