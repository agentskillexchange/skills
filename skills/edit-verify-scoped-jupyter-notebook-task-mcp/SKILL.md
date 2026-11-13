---
name: "Edit and verify a scoped Jupyter notebook task through MCP"
slug: "edit-verify-scoped-jupyter-notebook-task-mcp"
description: "Connect an external MCP agent to a selected Jupyter notebook, make bounded cell edits, execute the affected analysis and return saved results with execution evidence."
github_stars: 1324
verification: "security_reviewed"
source: "https://github.com/datalayer/jupyter-mcp-server"
author: "Datalayer"
publisher_type: "Community"
category: "Developer Tools"
framework: "MCP"
tool_ecosystem:
  github_repo: "datalayer/jupyter-mcp-server"
  github_stars: 1324
---

# Edit and verify a scoped Jupyter notebook task through MCP

Connect an external MCP agent to a selected Jupyter notebook, make bounded cell edits, execute the affected analysis and return saved results with execution evidence.

## Prerequisites

Python >=3.10; uv/uvx; JupyterLab; jupyter-collaboration; jupyter-mcp-tools; ipykernel; MCP client

## Installation

Install or set up from the source-backed instructions:

In the notebook environment install jupyterlab jupyter-collaboration jupyter-mcp-tools ipykernel. Start JupyterLab with token authentication on loopback port 8888 and confirm collaboration autosave works. Configure the MCP client command uvx with args ["jupyter-mcp-server==2.2.5"], env JUPYTER_URL=http://127.0.0.1:8888, JUPYTER_TOKEN set privately to the server token, and DOCUMENT_ID set to the authorized relative notebook path. Use a compatible Python environment; v2 requires MCP SDK >=2,=1.1.1. Keep credentials out of version control.

- Source: https://github.com/datalayer/jupyter-mcp-server

## Documentation

- https://github.com/datalayer/jupyter-mcp-server/blob/b85e6c588bcd1fc8c2c25e242c7f99d06bad9b2a/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/edit-verify-scoped-jupyter-notebook-task-mcp/)
