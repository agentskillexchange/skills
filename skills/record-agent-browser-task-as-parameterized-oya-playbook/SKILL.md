---
name: "Record an agent-completed browser task as a parameterized Oya playbook"
slug: "record-agent-browser-task-as-parameterized-oya-playbook"
description: "Complete a test browser task once, save its learned steps as an Oya playbook, and verify a replay with new inputs while retaining repair evidence."
github_stars: 349
verification: "security_reviewed"
source: "https://github.com/OyadotAI/oya-browser"
author: "OyadotAI"
publisher_type: "community"
category: "Browser Automation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "OyadotAI/oya-browser"
  github_stars: 349
  npm_package: "@oya-ai/browser"
  npm_weekly_downloads: 4464
---

# Record an agent-completed browser task as a parameterized Oya playbook

Complete a test browser task once, save its learned steps as an Oya playbook, and verify a replay with new inputs while retaining repair evidence.

## Prerequisites

Node.js 20+, @oya-ai/browser, configured Oya control plane or cloud API key, model API route; Docker/Compose for self-hosting

## Installation

Install or set up from the source-backed instructions:

Run npm install @oya-ai/browser@1.0.233 in a Node.js 20+ project. For an existing self-hosted deployment set OYA_BASE_URL and OYA_API_KEY; for Oya Cloud follow upstream account setup and set OYA_API_KEY. Configure the model route for learning, then adapt the pinned examples/sdk/05-playbooks.ts sample using a test form and clean up the browser after each run.

- Source: https://github.com/OyadotAI/oya-browser

## Documentation

- https://github.com/OyadotAI/oya-browser/blob/7125d696291bdf8b2a4879e68b6a33186dbe8791/examples/sdk/05-playbooks.ts

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/record-agent-browser-task-as-parameterized-oya-playbook/)
