---
name: "Verify Nix package and option choices through MCP-NixOS"
slug: "verify-nix-package-and-option-choices-through-mcp-nixos"
description: "Search NixOS packages and configuration options, inspect exact results and version metadata, then hand off an evidenced configuration plan through the MCP-NixOS query tools."
github_stars: 889
verification: "security_reviewed"
source: "https://github.com/utensils/mcp-nixos"
author: "James Brink"
publisher_type: "individual"
category: "Library & API Reference"
framework: "MCP"
tool_ecosystem:
  github_repo: "utensils/mcp-nixos"
  github_stars: 889
---

# Verify Nix package and option choices through MCP-NixOS

Search NixOS packages and configuration options, inspect exact results and version metadata, then hand off an evidenced configuration plan through the MCP-NixOS query tools.

## Prerequisites

MCP-capable client; Python >=3.11; uv/uvx; network access to the selected public Nix metadata sources

## Installation

Install or set up from the source-backed instructions:

Add mcpServers.nixos with command "uvx" and args ["mcp-nixos"] to the MCP client configuration. Launch through the client over stdio. The selected public-query workflow does not require Nix installation.

- Source: https://github.com/utensils/mcp-nixos

## Documentation

- https://github.com/utensils/mcp-nixos#the-tools

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/verify-nix-package-and-option-choices-through-mcp-nixos/)
