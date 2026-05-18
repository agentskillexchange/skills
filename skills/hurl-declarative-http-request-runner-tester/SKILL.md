---
name: "Hurl Declarative HTTP Request Runner and Tester"
slug: "hurl-declarative-http-request-runner-tester"
description: "Hurl is a command-line tool for running and testing HTTP requests defined in plain text files. Built on libcurl, it supports chaining multiple requests, capturing values, asserting responses with JSONPath and XPath, and integrating into CI/CD pipelines — making it ideal for API testing, integration testing, and endpoint validation."
github_stars: 18696
verification: "listed"
source: "https://github.com/Orange-OpenSource/hurl"
category: "Developer Tools"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "Orange-OpenSource/hurl"
  github_stars: 18696
---

# Hurl Declarative HTTP Request Runner and Tester

Hurl is a command-line tool for running and testing HTTP requests defined in plain text files. Built on libcurl, it supports chaining multiple requests, capturing values, asserting responses with JSONPath and XPath, and integrating into CI/CD pipelines — making it ideal for API testing, integration testing, and endpoint validation.

## Installation

Use the upstream install or setup path that matches your environment:
- $ brew install hurl
- $ cargo install --locked hurl
- $ conda install -c conda-forge hurl
- $ docker pull ghcr.io/orange-opensource/hurl:latest

Requirements and caveats from upstream:
- [Docker](#docker)
- Asserting JSON body response (node values, collection count etc...) with [JSONPath]:
- By default, Hurl doesn't follow redirection so each step of a redirect must be run manually and can be analysed:

Basic usage or getting-started notes:
- GET https://example.org
- POST https://example.org/login
- GET https://example.org/api/health

- Source: https://github.com/Orange-OpenSource/hurl
- Extracted from upstream docs: https://raw.githubusercontent.com/Orange-OpenSource/hurl/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hurl-declarative-http-request-runner-tester/)
