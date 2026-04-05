---
name: "Tabby Self-Hosted AI Coding Assistant and Copilot Alternative"
description: "Tabby is an open-source, self-hosted AI coding assistant that serves as an on-premises alternative to GitHub Copilot. It provides code completion and chat capabilities using consumer-grade GPUs with no cloud dependency."
category: "Developer Tools"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/TabbyML/tabby"
tool_ecosystem:
  github_repo: "TabbyML/tabby"
  github_stars: 33294
---
# Tabby Self-Hosted AI Coding Assistant and Copilot Alternative

Tabby is an open-source, self-hosted AI coding assistant that serves as an on-premises alternative to GitHub Copilot. It provides code completion and chat capabilities using consumer-grade GPUs with no cloud dependency.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill tabby-self-hosted-ai-coding-assistant
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill tabby-self-hosted-ai-coding-assistant -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill tabby-self-hosted-ai-coding-assistant -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill tabby-self-hosted-ai-coding-assistant -a codex
```

### OpenClaw

```bash
clawhub install tabby-self-hosted-ai-coding-assistant
```

## Details

Tabby is a self-hosted AI coding assistant built in Rust that provides a fully open-source alternative to GitHub Copilot. It runs entirely on-premises, requiring no external DBMS or cloud services, making it suitable for organizations with strict data privacy requirements.

Core Features
Tabby provides intelligent code completion and an Answer Engine for internal engineering teams. It supports consumer-grade GPUs for inference and offers an OpenAPI interface for integration with existing development infrastructure including cloud IDEs. The system supports multiple models from its official registry including StarCoder, CodeLlama, CodeGemma, and Qwen series.

Integration Points
Tabby integrates with major code editors through dedicated extensions for VS Code, JetBrains IDEs, and Vim/Neovim. It supports repository-level context through RAG-based code completion, allowing it to understand your codebase for more relevant suggestions. The platform also supports indexing GitLab Merge Requests and GitHub issues as context.

Enterprise Capabilities
The platform includes team management features, LDAP authentication, SSO via GitHub and GitLab, usage analytics with team-wise reporting, and an admin UI for configuration. It can be deployed via Docker with GPU support or through SkyServe for cloud deployment. Recent versions introduced shareable Pages from Answer Engine conversations and enhanced notification systems.

Architecture
Tabby uses a self-contained architecture with no external database requirements. It exposes a well-documented OpenAPI interface and supports Llamafile deployment integration. The Rust-based backend ensures high performance, and Apple M1/M2 Metal inference is supported for macOS users.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tabby-self-hosted-ai-coding-assistant/)
