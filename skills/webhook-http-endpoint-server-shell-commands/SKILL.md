---
name: "Webhook Lightweight HTTP Endpoint Server for Shell Command Execution"
description: "Webhook is a lightweight, configurable tool written in Go that creates HTTP endpoints on your server to execute shell commands. It supports JSON and YAML hook definitions with rule-based triggering, request payload parsing, and data passthrough to scripts via command-line arguments or environment variables."
category: "Integrations & Connectors"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/adnanh/webhook"
tool_ecosystem:
  github_repo: "adnanh/webhook"
  github_stars: 11718
  license: "MIT"
---
# Webhook Lightweight HTTP Endpoint Server for Shell Command Execution

Webhook is a lightweight, configurable tool written in Go that creates HTTP endpoints on your server to execute shell commands. It supports JSON and YAML hook definitions with rule-based triggering, request payload parsing, and data passthrough to scripts via command-line arguments or environment variables.

Webhook by adnanh is a lightweight incoming webhook server written in Go that allows you to create HTTP endpoints (hooks) on your server. Each hook maps to a configured shell command that executes when the endpoint receives a request. The tool parses incoming HTTP headers, query parameters, and request payloads, then passes extracted data to your scripts through command-line arguments or environment variables.



Core Capabilities

Webhook supports both JSON and YAML configuration files for defining hooks. Each hook definition specifies an ID (which becomes the URL endpoint), the command to execute, a working directory, and optional trigger rules. Trigger rules let you validate incoming requests against headers, payload values, IP whitelists, or HMAC signatures before allowing execution. This makes it suitable for securing deployment triggers from services like GitHub, GitLab, Bitbucket, Docker Hub, Slack, and other platforms that send webhook notifications.



Deployment Automation

The most common use case is CI/CD deployment automation. When a Git hosting service sends a push notification to your webhook endpoint, the server validates the request signature and runs your deployment script. This eliminates the need for heavyweight CI/CD platforms when all you need is to trigger a script on push. The tool supports passing the entire payload as JSON, extracting specific fields, and conditional execution based on branch names or event types.



Integration and Configuration

Webhook runs as a standalone HTTP server on a configurable port and supports HTTPS with custom certificates. It can serve multiple hooks simultaneously from a single configuration file. Each hook can have its own pass-arguments-to-command definitions, pass-environment-to-command definitions, and independent trigger-rule chains. The server logs all incoming requests and their processing status, making it straightforward to debug integration issues.



Installation

Webhook is available through multiple package managers: apt on Debian and Ubuntu, pkg on FreeBSD, snap on Linux, and Homebrew. Pre-built binaries are provided for Linux, macOS, and Windows on the GitHub releases page. You can also build from source with Go 1.21 or newer using go build github.com/adnanh/webhook.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill webhook-http-endpoint-server-shell-commands
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill webhook-http-endpoint-server-shell-commands -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill webhook-http-endpoint-server-shell-commands -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill webhook-http-endpoint-server-shell-commands -a codex
```

### OpenClaw

```bash
clawhub install webhook-http-endpoint-server-shell-commands
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/webhook-http-endpoint-server-shell-commands/)
