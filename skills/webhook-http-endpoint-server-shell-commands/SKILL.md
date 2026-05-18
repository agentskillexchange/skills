---
name: "Webhook Lightweight HTTP Endpoint Server for Shell Command Execution"
slug: "webhook-http-endpoint-server-shell-commands"
description: "Webhook is a lightweight, configurable tool written in Go that creates HTTP endpoints on your server to execute shell commands. It supports JSON and YAML hook definitions with rule-based triggering, request payload parsing, and data passthrough to scripts via command-line arguments or environment variables."
github_stars: 11718
verification: "listed"
source: "https://github.com/adnanh/webhook"
category: "Integrations & Connectors"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "adnanh/webhook"
  github_stars: 11718
---

# Webhook Lightweight HTTP Endpoint Server for Shell Command Execution

Webhook is a lightweight, configurable tool written in Go that creates HTTP endpoints on your server to execute shell commands. It supports JSON and YAML hook definitions with rule-based triggering, request payload parsing, and data passthrough to scripts via command-line arguments or environment variables.

## Installation

Requirements and caveats from upstream:
- ## Interested in running webhook inside of a Docker container?
- You can use one of the following Docker images, or create your own (please read [this discussion](https://github.com/adnanh/webhook/issues/63)):
- [almir/webhook](https://github.com/almir/docker-webhook)

Basic usage or getting-started notes:
- For example, if you're using Github or Bitbucket, you can use [webhook][w] to set up a hook that runs a redeploy script for your project on your staging server, whenever you push changes to the master branch of your p...
- If you use Mattermost or Slack, you can set up an "Outgoing webhook integration" or "Slash command" to run various commands on your server, which can then report back directly to you or your channels using the "Incomi...
- | Scriptable webhook gateway to safely run your custom builds, deploys, and proxy scripts on your servers. | An event gateway to reliably ingest, verify, queue, transform, filter, inspect, monitor, and replay webhooks. |

- Source: https://github.com/adnanh/webhook
- Extracted from upstream docs: https://raw.githubusercontent.com/adnanh/webhook/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/webhook-http-endpoint-server-shell-commands/)
