---
name: Stagehand AI Browser Automation Framework
description: Stagehand is an open-source browser automation framework that combines
  natural language instructions with code for reliable web automation. Built on top
  of Playwright, it lets developers use AI when navigating unfamiliar pages and code
  when they know exactly what to do.
verification: security_reviewed
source: https://github.com/browserbase/stagehand
category:
- Browser Automation
framework:
- Custom Agents
tool_ecosystem:
  github_repo: browserbase/stagehand
  github_stars: 21782
---
# Stagehand AI Browser Automation Framework

What is Stagehand?
Stagehand is an AI browser automation framework created by Browserbase that bridges the gap between low-level browser automation code (Selenium, Playwright, Puppeteer) and high-level AI agents that can be unpredictable. It uses natural language to control browsers while maintaining the precision and reliability needed for production workflows.
The framework provides three core primitives: act() for executing individual browser actions described in natural language, extract() for pulling structured data from pages using Zod schemas, and agent() for multi-step tasks where the AI plans and executes a sequence of actions autonomously. This gives developers fine-grained control over when to use AI reasoning versus deterministic code.
How It Works
Stagehand runs on top of Playwright's CDP (Chrome DevTools Protocol) engine and connects to LLM providers like OpenAI, Anthropic, or Google for the AI-driven portions. When you call act("click the submit button"), Stagehand analyzes the current page DOM, identifies the target element, and performs the action. The extract() function parses visible page content and returns typed data matching your schema definition.
A key differentiator is Stagehand's auto-caching and self-healing capabilities. Once an action is performed, Stagehand remembers the DOM selectors and can replay them without LLM inference on subsequent runs. If the website changes and the cached selectors break, Stagehand automatically falls back to AI to find the new element location, then updates its cache.
Integration and Output
Install via npm with npm install @browserbasehq/stagehand or bootstrap a new project with npx create-browser-app. Stagehand supports both local browser instances and Browserbase's cloud infrastructure. It outputs structured data via extract() using Zod schema validation, produces screenshots and DOM snapshots for debugging, and integrates into CI/CD pipelines for automated testing and data collection workflows. The MIT-licensed framework has over 21,000 GitHub stars and active development with daily commits.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stagehand-ai-browser-automation-framework/)
