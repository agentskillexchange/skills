---
name: "Give MCP agents disposable code execution sandboxes with OpenSandbox MCP"
slug: "give-mcp-agents-disposable-code-execution-sandboxes-with-opensandbox-mcp"
description: "Expose sandbox creation, command execution, and file operations to MCP-capable agents so they can run untrusted code inside disposable Docker or Kubernetes-backed runtimes."
github_stars: 10207
verification: "security_reviewed"
source: "https://github.com/alibaba/OpenSandbox"
author: "Alibaba"
publisher_type: "organization"
category: "Security & Verification"
framework: "MCP"
tool_ecosystem:
  github_repo: "alibaba/OpenSandbox"
  github_stars: 10207
---

# Give MCP agents disposable code execution sandboxes with OpenSandbox MCP

Expose sandbox creation, command execution, and file operations to MCP-capable agents so they can run untrusted code inside disposable Docker or Kubernetes-backed runtimes.

## Prerequisites

Docker for local runtime or Kubernetes for cluster runtime, plus an MCP-capable client such as Claude Code or Cursor.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Run the OpenSandbox server, then install the MCP bridge with pip install opensandbox-mcp and point your MCP client at opensandbox-mcp with the documented domain and protocol settings.
```

## Documentation

- https://open-sandbox.ai

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/give-mcp-agents-disposable-code-execution-sandboxes-with-opensandbox-mcp/)
