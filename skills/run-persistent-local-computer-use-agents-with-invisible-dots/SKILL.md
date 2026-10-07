---
name: "Run persistent local computer-use agents with invisible_dots"
slug: "run-persistent-local-computer-use-agents-with-invisible-dots"
description: "Give each agent its own local QEMU desktop, browser identity, files, memory, task queue, and approval rules for supervised long-running web and computer workflows."
github_stars: 31797
verification: "security_reviewed"
source: "https://github.com/feder-cr/invisible_dots"
author: "Federico Elia"
publisher_type: "individual"
category: "Browser Automation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "feder-cr/invisible_dots"
  github_stars: 31797
---

# Run persistent local computer-use agents with invisible_dots

Give each agent its own local QEMU desktop, browser identity, files, memory, task queue, and approval rules for supervised long-running web and computer workflows.

## Prerequisites

Node.js 24+, Go 1.25+, Git, QEMU or Windows Hypervisor Platform/KVM, hardware virtualization, and an OpenRouter API key

## Installation

Install or set up from the source-backed instructions:

Clone https://github.com/feder-cr/invisible_dots, run npm ci, build the CLI with npm run build --workspace @invisible-dots/cli, run node apps/cli/dist/invisible-dots.mjs setup --all, then start the server with node apps/cli/dist/invisible-dots.mjs server and create a Dot from the local web UI.

- Source: https://github.com/feder-cr/invisible_dots

## Documentation

- https://github.com/feder-cr/invisible_dots/blob/main/docs/guide.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-persistent-local-computer-use-agents-with-invisible-dots/)
