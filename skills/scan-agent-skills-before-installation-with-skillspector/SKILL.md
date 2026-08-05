---
name: "Scan agent skills before installation with SkillSpector"
slug: "scan-agent-skills-before-installation-with-skillspector"
description: "Use SkillSpector to scan Claude Code, Codex, Gemini, MCP, and other agent skills for vulnerabilities, malicious patterns, prompt injection, data exfiltration, and supply-chain risk before installation."
github_stars: 14191
verification: "security_reviewed"
source: "https://github.com/NVIDIA/SkillSpector"
author: "NVIDIA"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "NVIDIA/SkillSpector"
  github_stars: 14191
---

# Scan agent skills before installation with SkillSpector

Use SkillSpector to scan Claude Code, Codex, Gemini, MCP, and other agent skills for vulnerabilities, malicious patterns, prompt injection, data exfiltration, and supply-chain risk before installation.

## Prerequisites

SkillSpector, uv or Docker, optional MCP extra, optional LLM provider credentials for semantic analysis

## Installation

Install or set up from the source-backed instructions:

uv tool install git+https://github.com/NVIDIA/skillspector.git; optional MCP mode: uv tool install 'skillspector[mcp] @ git+https://github.com/NVIDIA/skillspector.git'; then run skillspector scan

- Source: https://github.com/NVIDIA/SkillSpector

## Documentation

- https://docs.nvidia.com/skills/scanning-agent-skills

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-agent-skills-before-installation-with-skillspector/)
