---
name: "Retrieve upstream implementation evidence before coding with XERJ"
slug: "retrieve-upstream-implementation-evidence-before-coding-with-xerj"
description: "Build a focused reference corpus, retrieve implementation passages with file-and-line citations, and check license constraints before adapting unfamiliar code."
verification: "security_reviewed"
source: "https://github.com/xerj-org/xerj/blob/cb990c63de7eea1db084285c702c181ef57b7bc5/tools/xerj-code/SKILL.md"
author: "xerj-org"
publisher_type: "organization"
category: "Developer Tools"
framework: "Multi-Framework"
---

# Retrieve upstream implementation evidence before coding with XERJ

Build a focused reference corpus, retrieve implementation passages with file-and-line citations, and check license constraints before adapting unfamiliar code.

## Prerequisites

XERJ binary; Git; reachable XERJ node; shell-capable agent or configured MCP client

## Installation

Install or set up from the source-backed instructions:

Use the upstream v1.0.0-rc.100 release or official installation instructions to install the platform binary; the shell installer places it in ~/.local/bin. On a trusted single-user dev machine, start xerj --insecure --data-dir ~/xerj-data and wait for the loopback node at http://localhost:9200. This disables TLS/auth; use the documented authenticated configuration on shared hosts. Keep storage outside indexed directories. Add the binary directory to PATH if required. Then run xerj corpus add reference-task ..., xerj corpus index reference-task, and xerj code reference-task "". No npm dependency is asserted. For MCP, configure the absolute binary path with argument mcp and the appropriate XERJ_URL; this proxy requires an already running node.

- Source: https://github.com/xerj-org/xerj/blob/cb990c63de7eea1db084285c702c181ef57b7bc5/tools/xerj-code/SKILL.md

## Documentation

- https://github.com/xerj-org/xerj/blob/cb990c63de7eea1db084285c702c181ef57b7bc5/tools/xerj-code/SKILL.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/retrieve-upstream-implementation-evidence-before-coding-with-xerj/)
