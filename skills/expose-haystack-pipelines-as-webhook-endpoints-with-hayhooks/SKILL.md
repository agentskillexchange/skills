---
name: "Expose Haystack pipelines as webhook endpoints with Hayhooks"
slug: "expose-haystack-pipelines-as-webhook-endpoints-with-hayhooks"
description: "Turn an existing Haystack pipeline into an HTTP or MCP endpoint without building and maintaining a custom wrapper service."
github_stars: 138
verification: "security_reviewed"
source: "https://github.com/deepset-ai/hayhooks"
author: "deepset"
publisher_type: "organization"
category: "Integrations & Connectors"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "deepset-ai/hayhooks"
  github_stars: 138
---

# Expose Haystack pipelines as webhook endpoints with Hayhooks

Turn an existing Haystack pipeline into an HTTP or MCP endpoint without building and maintaining a custom wrapper service.

## Prerequisites

Python environment, Haystack pipeline definitions, hayhooks package, network access for HTTP serving, optional MCP clients

## Installation

Use the upstream install or setup path that matches your environment:
- pip install hayhooks

Requirements and caveats from upstream:
- [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/hayhooks.svg)](https://pypi.org/project/hayhooks)
- [![Docker image release](https://github.com/deepset-ai/hayhooks/actions/workflows/docker.yml/badge.svg)](https://github.com/deepset-ai/hayhooks/actions/workflows/docker.yml)
- python

Basic usage or getting-started notes:
- 🖥️ **Embed a [Chainlit](https://chainlit.io/) chat UI** directly in Hayhooks with pip install "hayhooks[chainlit]" and hayhooks run --with-chainlit -- zero-configuration frontend with streaming, pipeline selection, an...
- 🕹️ **Control Hayhooks core API endpoints through chat** - deploy, undeploy, list, or run Haystack pipelines and agents by chatting with [Claude Desktop](https://claude.ai/download), [Cursor](https://cursor.com), or an...
- 📈 **Trace Hayhooks lifecycle actions with OpenTelemetry** (pip install "hayhooks[tracing]") for deploy/run/undeploy visibility across REST and MCP, with a /dashboard UI via hayhooks run --with-tracing-dashboard (backe...

- Source: https://github.com/deepset-ai/hayhooks
- Extracted from upstream docs: https://raw.githubusercontent.com/deepset-ai/hayhooks/HEAD/README.md

## Documentation

- https://docs.haystack.deepset.ai/docs/hayhooks

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/expose-haystack-pipelines-as-webhook-endpoints-with-hayhooks/)
