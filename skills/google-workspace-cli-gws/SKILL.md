---
name: "Google Workspace CLI (gws)"
slug: "google-workspace-cli-gws"
description: "Google Workspace CLI, branded as gws, is a command-line tool that gives humans and AI agents structured access to Drive, Gmail, Calendar, Sheets, Docs, Chat, and other Workspace APIs. It is designed to remove API boilerplate while keeping responses machine-friendly for agent workflows."
github_stars: 24348
verification: "security_reviewed"
source: "https://github.com/googleworkspace/cli"
author: "googleworkspace"
publisher_type: "Community"
category: "Calendar, Email & Productivity"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "googleworkspace/cli"
  github_stars: 24348
  npm_package: "@googleworkspace/cli"
  npm_weekly_downloads: 38925
---

# Google Workspace CLI (gws)

Google Workspace CLI, branded as gws, is a command-line tool that gives humans and AI agents structured access to Drive, Gmail, Calendar, Sheets, Docs, Chat, and other Workspace APIs. It is designed to remove API boilerplate while keeping responses machine-friendly for agent workflows.

## Prerequisites

Node.js or prebuilt gws binary, Google account, Google Cloud OAuth credentials

## Installation

Use the upstream install or setup path that matches your environment:
- For convenience, you can also use npm to automate downloading the appropriate binary from GitHub Releases:
- npm install -g @googleworkspace/cli
- cargo install --git https://github.com/googleworkspace/cli --locked
- brew install googleworkspace-cli

Requirements and caveats from upstream:
- [Prerequisites](#prerequisites)
- **Node.js 18+** — for npm install (or download a pre-built binary from [GitHub Releases](https://github.com/googleworkspace/cli/releases))
- gws auth setup requires the [gcloud CLI](https://cloud.google.com/sdk/docs/install). If you don't have gcloud, use the [manual setup](#manual-oauth-setup-google-cloud-console) below instead.

Basic usage or getting-started notes:
- [Quick Start](#quick-start)
- [Advanced Usage](#advanced-usage)
- **A Google Cloud project** — required for OAuth credentials. You can create one via the [Google Cloud Console](https://console.cloud.google.com/) or with the [gcloud CLI](https://cloud.google.com/sdk/docs/install) or...

- Source: https://github.com/googleworkspace/cli
- Extracted from upstream docs: https://raw.githubusercontent.com/googleworkspace/cli/HEAD/README.md

## Documentation

- https://developers.google.com/workspace

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/google-workspace-cli-gws/)
