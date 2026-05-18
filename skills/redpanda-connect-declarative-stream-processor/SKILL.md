---
name: "Redpanda Connect Declarative Stream Processor"
slug: "redpanda-connect-declarative-stream-processor"
description: "Redpanda Connect (formerly Benthos) is a high-performance stream processor that connects data sources and sinks through declarative YAML pipelines. It supports hundreds of connectors and a built-in mapping language called Bloblang for data transformation."
github_stars: 8618
verification: "listed"
source: "https://github.com/redpanda-data/connect"
category: "Data Extraction & Transformation"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "redpanda-data/connect"
  github_stars: 8618
---

# Redpanda Connect Declarative Stream Processor

Redpanda Connect (formerly Benthos) is a high-performance stream processor that connects data sources and sinks through declarative YAML pipelines. It supports hundreds of connectors and a built-in mapping language called Bloblang for data transformation.

## Installation

Use the upstream install or setup path that matches your environment:
- brew install redpanda-data/tap/redpanda
- docker pull docker.redpanda.com/redpandadata/connect
- docker run --rm -v /path/to/your/config.yaml:/connect.yaml docker.redpanda.com/redpandadata/connect run
- docker run --rm -p 4195:4195 docker.redpanda.com/redpandadata/connect run \

Requirements and caveats from upstream:
- It comes with a [powerful mapping language][bloblang-about], is easy to deploy and monitor, and ready to drop into your pipeline either as a static binary or docker image, making it cloud native as heck.
- Or pull the docker image:
- Or, with docker:

Basic usage or getting-started notes:
- shell
- curl -LO https://github.com/redpanda-data/redpanda/releases/latest/download/rpk-linux-amd64.zip
- unzip rpk-linux-amd64.zip -d ~/.local/bin/

- Source: https://github.com/redpanda-data/connect
- Extracted from upstream docs: https://raw.githubusercontent.com/redpanda-data/connect/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/redpanda-connect-declarative-stream-processor/)
