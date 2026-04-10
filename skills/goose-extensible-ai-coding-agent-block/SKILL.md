---
name: Goose Extensible AI Coding Agent by Block
description: An open-source, extensible AI agent from Block (formerly Square) that
  goes beyond code suggestions to install packages, execute commands, edit files,
  and run tests. Supports any LLM and extends via MCP servers for tool integration.
verification: security_reviewed
source: https://github.com/block/goose
category:
- Developer Tools
framework:
- Custom Agents
tool_ecosystem:
  github_repo: block/goose
  github_stars: 33898
---
# Goose Extensible AI Coding Agent by Block

Goose is an open-source AI coding agent developed by Block (the company behind Square, Cash App, and Bitkey). With over 33,000 GitHub stars, it has become one of the most popular terminal-based coding agents. Unlike simpler code completion tools, Goose can take autonomous actions: installing dependencies, running commands, editing multiple files, and executing test suites.
How It Works
Goose operates as both a CLI tool and a desktop application. You describe a task in natural language, and the agent plans and executes a series of steps to accomplish it. It can read and understand your entire codebase, make coordinated edits across multiple files, run shell commands to verify changes, and iterate based on test results or error output.
The agent supports any LLM as its reasoning backend, including Claude, GPT-4, Gemini, and local models. You configure your preferred provider and model, and Goose handles the tool-calling protocol to translate natural language into concrete actions.
Extension System
Goose extends through MCP (Model Context Protocol) servers, which are plugins that expose additional tools and data sources. This means you can connect Goose to your GitHub repositories, Jira boards, Slack channels, databases, or any other service with an MCP server. The extension system makes Goose customizable for specific team workflows and technology stacks.
Key Capabilities
File operations include reading, writing, searching, and patching across your project. Shell command execution runs builds, tests, linters, and any other CLI tools. Built-in web search and browsing let Goose look up documentation or API references. Structured planning breaks complex tasks into manageable steps before execution. Session memory maintains context across long interactions.
Integration Points
Goose installs via Homebrew, pip, or direct download. It reads API keys from environment variables and stores configuration in ~/.config/goose. The MCP extension system connects to any service with an MCP server implementation. The tool works with any Git repository and any programming language. Both terminal and desktop interfaces are available for different workflow preferences.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/goose-extensible-ai-coding-agent-block/)
