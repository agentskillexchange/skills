---
title: "Stagehand AI Browser Automation Framework"
description: "What is Stagehand?\nStagehand is an AI browser automation framework created by Browserbase that bridges the gap between low-level browser automation code (Selenium, Playwright, Puppeteer) and high-level AI agents that can be unpredictable. It uses natural language to control browsers while maintaining the precision and reliability needed for production workflows.\nThe framework provides three core primitives: act() for executing individual browser actions described in natural language, extract() for pulling structured data from pages using Zod schemas, and agent() for multi-step tasks where the AI plans and executes a sequence of actions autonomously. This gives developers fine-grained control over when to use AI reasoning versus deterministic code.\nHow It Works\nStagehand runs on top of Playwright’s CDP (Chrome DevTools Protocol) engine and connects to LLM providers like OpenAI, Anthropic, or Google for the AI-driven portions. When you call act(\"click the submit button\"), Stagehand analyzes the current page DOM, identifies the target element, and performs the action. The extract() function parses visible page content and returns typed data matching your schema definition.\nA key differentiator is Stagehand’s auto-caching and self-healing capabilities. Once an action is performed, Stagehand remembers the DOM selectors and can replay them without LLM inference on subsequent runs. If the website changes and the cached selectors break, Stagehand automatically falls back to AI to find the new element location, then updates its cache.\nIntegration and Output\nInstall via npm with npm install @browserbasehq/stagehand or bootstrap a new project with npx create-browser-app. Stagehand supports both local browser instances and Browserbase’s cloud infrastructure. It outputs structured data via extract() using Zod schema validation, produces screenshots and DOM snapshots for debugging, and integrates into CI/CD pipelines for automated testing and data collection workflows. The MIT-licensed framework has over 21,000 GitHub stars and active development with daily commits."
verification: security_reviewed
source: "https://github.com/browserbase/stagehand"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "browserbase/stagehand"
  github_stars: 21782
---

# Stagehand AI Browser Automation Framework

What is Stagehand?
Stagehand is an AI browser automation framework created by Browserbase that bridges the gap between low-level browser automation code (Selenium, Playwright, Puppeteer) and high-level AI agents that can be unpredictable. It uses natural language to control browsers while maintaining the precision and reliability needed for production workflows.
The framework provides three core primitives: act() for executing individual browser actions described in natural language, extract() for pulling structured data from pages using Zod schemas, and agent() for multi-step tasks where the AI plans and executes a sequence of actions autonomously. This gives developers fine-grained control over when to use AI reasoning versus deterministic code.
How It Works
Stagehand runs on top of Playwright’s CDP (Chrome DevTools Protocol) engine and connects to LLM providers like OpenAI, Anthropic, or Google for the AI-driven portions. When you call act("click the submit button"), Stagehand analyzes the current page DOM, identifies the target element, and performs the action. The extract() function parses visible page content and returns typed data matching your schema definition.
A key differentiator is Stagehand’s auto-caching and self-healing capabilities. Once an action is performed, Stagehand remembers the DOM selectors and can replay them without LLM inference on subsequent runs. If the website changes and the cached selectors break, Stagehand automatically falls back to AI to find the new element location, then updates its cache.
Integration and Output
Install via npm with npm install @browserbasehq/stagehand or bootstrap a new project with npx create-browser-app. Stagehand supports both local browser instances and Browserbase’s cloud infrastructure. It outputs structured data via extract() using Zod schema validation, produces screenshots and DOM snapshots for debugging, and integrates into CI/CD pipelines for automated testing and data collection workflows. The MIT-licensed framework has over 21,000 GitHub stars and active development with daily commits.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/stagehand-ai-browser-automation-framework
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/stagehand-ai-browser-automation-framework` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stagehand-ai-browser-automation-framework/)
