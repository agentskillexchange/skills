---
name: "Chat with private document collections through Kotaemon"
slug: "chat-with-private-document-collections-through-kotaemon"
description: "Run a self-hosted Kotaemon document QA workflow so agents can index private files, ask grounded questions, and return cited answers."
github_stars: 25448
verification: "security_reviewed"
source: "https://github.com/Cinnamon/kotaemon"
author: "Cinnamon"
publisher_type: "organization"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "Cinnamon/kotaemon"
  github_stars: 25448
---

# Chat with private document collections through Kotaemon

Run a self-hosted Kotaemon document QA workflow so agents can index private files, ask grounded questions, and return cited answers.

## Prerequisites

Docker or Python environment, Kotaemon, document collection to index, configured LLM provider or local model such as Ollama

## Installation

Use the upstream install or setup path that matches your environment:
- [Docker](https://www.docker.com/): optional, if you [install with Docker](#with-docker-recommended)
- docker run \
- docker run <...> ghcr.io/cinnamon/kotaemon:main-ollama
- docker run <...> ghcr.io/cinnamon/kotaemon:main-lite

Requirements and caveats from upstream:
- [![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-31013/)
- <img src="https://img.shields.io/badge/docker_pull-kotaemon:latest-brightgreen" alt="docker pull ghcr.io/cinnamon/kotaemon:latest"></a>
- **Support for Various LLMs**: Compatible with LLM API providers (OpenAI, AzureOpenAI, Cohere, etc.) and local LLMs (via ollama and llama-cpp-python).

Basic usage or getting-started notes:
- **Extensible**: Being built on Gradio, you are free to customize or add any UI elements as you like. Also, we aim to support multiple strategies for document indexing & retrieval. GraphRAG indexing pipeline is provide...
- If you are not a developer and just want to use the app, please check out our easy-to-follow [User Guide](https://cinnamon.github.io/kotaemon/). Download the .zip file from the [latest release](https://github.com/Cinn...
- [Unstructured](https://docs.unstructured.io/open-source/installation/full-installation#full-installation) if you want to process files other than .pdf, .html, .mhtml, and .xlsx documents. Installation steps differ dep...

- Source: https://github.com/Cinnamon/kotaemon
- Extracted from upstream docs: https://raw.githubusercontent.com/Cinnamon/kotaemon/HEAD/README.md

## Documentation

- https://cinnamon.github.io/kotaemon/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/chat-with-private-document-collections-through-kotaemon/)
