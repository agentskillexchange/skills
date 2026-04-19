---
title: "Webhook Lightweight HTTP Endpoint Server for Shell Command Execution"
description: "Webhook by adnanh is a lightweight incoming webhook server written in Go that allows you to create HTTP endpoints (hooks) on your server. Each hook maps to a configured shell command that executes when the endpoint receives a request. The tool parses incoming HTTP headers, query parameters, and request payloads, then passes extracted data to your scripts through command-line arguments or environment variables. Core Capabilities Webhook supports both JSON and YAML configuration files for defining hooks. Each hook definition specifies an ID (which becomes the URL endpoint), the command to execute, a working directory, and optional trigger rules. Trigger rules let you validate incoming requests against headers, payload values, IP whitelists, or HMAC signatures before allowing execution. This makes it suitable for securing deployment triggers from services like GitHub, GitLab, Bitbucket, Docker Hub, Slack, and other platforms that send webhook notifications. Deployment Automation The most common use case is CI/CD deployment automation. When a Git hosting service sends a push notification to your webhook endpoint, the server validates the request signature and runs your deployment script. This eliminates the need for heavyweight CI/CD platforms when all you need is to trigger a script on push. The tool supports passing the entire payload as JSON, extracting specific fields, and conditional execution based on branch names or event types. Integration and Configuration Webhook runs as a standalone HTTP server on a configurable port and supports HTTPS with custom certificates. It can serve multiple hooks simultaneously from a single configuration file. Each hook can have its own pass-arguments-to-command definitions, pass-environment-to-command definitions, and independent trigger-rule chains. The server logs all incoming requests and their processing status, making it straightforward to debug integration issues. Installation Webhook is available through multiple package managers: apt on Debian and Ubuntu, pkg on FreeBSD, snap on Linux, and Homebrew. Pre-built binaries are provided for Linux, macOS, and Windows on the GitHub releases page. You can also build from source with Go 1.21 or newer using go build github.com/adnanh/webhook ."
source: "https://github.com/adnanh/webhook"
verification: "security_reviewed"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "adnanh/webhook"
  github_stars: 11718
---

# Webhook Lightweight HTTP Endpoint Server for Shell Command Execution

Webhook by adnanh is a lightweight incoming webhook server written in Go that allows you to create HTTP endpoints (hooks) on your server. Each hook maps to a configured shell command that executes when the endpoint receives a request. The tool parses incoming HTTP headers, query parameters, and request payloads, then passes extracted data to your scripts through command-line arguments or environment variables. Core Capabilities Webhook supports both JSON and YAML configuration files for defining hooks. Each hook definition specifies an ID (which becomes the URL endpoint), the command to execute, a working directory, and optional trigger rules. Trigger rules let you validate incoming requests against headers, payload values, IP whitelists, or HMAC signatures before allowing execution. This makes it suitable for securing deployment triggers from services like GitHub, GitLab, Bitbucket, Docker Hub, Slack, and other platforms that send webhook notifications. Deployment Automation The most common use case is CI/CD deployment automation. When a Git hosting service sends a push notification to your webhook endpoint, the server validates the request signature and runs your deployment script. This eliminates the need for heavyweight CI/CD platforms when all you need is to trigger a script on push. The tool supports passing the entire payload as JSON, extracting specific fields, and conditional execution based on branch names or event types. Integration and Configuration Webhook runs as a standalone HTTP server on a configurable port and supports HTTPS with custom certificates. It can serve multiple hooks simultaneously from a single configuration file. Each hook can have its own pass-arguments-to-command definitions, pass-environment-to-command definitions, and independent trigger-rule chains. The server logs all incoming requests and their processing status, making it straightforward to debug integration issues. Installation Webhook is available through multiple package managers: apt on Debian and Ubuntu, pkg on FreeBSD, snap on Linux, and Homebrew. Pre-built binaries are provided for Linux, macOS, and Windows on the GitHub releases page. You can also build from source with Go 1.21 or newer using go build github.com/adnanh/webhook .

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/webhook-http-endpoint-server-shell-commands/)
