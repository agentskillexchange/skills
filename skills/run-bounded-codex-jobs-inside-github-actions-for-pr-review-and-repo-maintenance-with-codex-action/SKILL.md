---
name: "Run bounded Codex jobs inside GitHub Actions for PR review and repo maintenance with codex-action"
slug: "run-bounded-codex-jobs-inside-github-actions-for-pr-review-and-repo-maintenance-with-codex-action"
description: "Use codex-action when an agent operator wants Codex to run inside GitHub Actions for PR review or scheduled repo work with explicit workflow permissions, prompts, and CI boundaries."
github_stars: 927
verification: "listed"
source: "https://github.com/openai/codex-action"
author: "OpenAI"
publisher_type: "company"
category: "CI/CD Integrations"
framework: "Codex"
tool_ecosystem:
  github_repo: "openai/codex-action"
  github_stars: 927
---

# Run bounded Codex jobs inside GitHub Actions for PR review and repo maintenance with codex-action

Use codex-action when an agent operator wants Codex to run inside GitHub Actions for PR review or scheduled repo work with explicit workflow permissions, prompts, and CI boundaries.

## Prerequisites

GitHub Actions, a repository workflow file, Codex Action, and the required provider API secret configured in GitHub.

## Installation

Requirements and caveats from upstream:
- Users must provide an API key for their chosen provider (for example, [OPENAI_API_KEY](https://platform.openai.com/api-keys) or AZURE_OPENAI_API_KEY [if using Azure for OpenAI models](#azure)) as a [GitHub Actions sec...
- **Linux/macOS**: All options for safety-strategy are supported. Again, if you pick drop-sudo, remember that later steps in your job that rely on sudo will fail. If you do need to run code that requires sudo after open...
- The responses-api-endpoint must be set to the full URL (including any required query parameters) that Codex will POST to for a Responses API request. For Azure, this might look like https://YOUR_PROJECT_NAME.openai.az...

Basic usage or getting-started notes:
- Run [Codex](https://github.com/openai/codex#codex-exec) from a GitHub Actions workflow while keeping tight control over the privileges available to Codex. This action handles installing the Codex CLI and configuring i...
- ## Example: Create Your Own Pull Request Bot
- While Codex cloud offers a [powerful code review tool](https://developers.openai.com/codex/cloud/code-review) that you can use today, here is an example of how you can build your own code review workflow with openai/c...

- Source: https://github.com/openai/codex-action
- Extracted from upstream docs: https://raw.githubusercontent.com/openai/codex-action/HEAD/README.md

## Documentation

- https://github.com/openai/codex-action#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-bounded-codex-jobs-inside-github-actions-for-pr-review-and-repo-maintenance-with-codex-action/)
