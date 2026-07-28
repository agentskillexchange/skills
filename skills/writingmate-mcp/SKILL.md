---
name: "Writingmate MCP Video and Image Generation"
slug: "writingmate-mcp"
description: "Connects Claude Code, Codex, Cursor, and other MCP hosts to Writingmate for model discovery, text comparison, image generation, and video generation with Seedance, Sora, Veo, Kling, PixVerse, and other available models."
category: "Image & Creative Automation"
framework: "Multi-Framework"
verification: listed
source: "https://github.com/writingmate/skills"
tool_ecosystem:
  tool: "Writingmate MCP"
  github_repo: "writingmate/skills"
  license: "MIT"
  maintained: true
---

# Writingmate MCP Video and Image Generation

Use Writingmate as a remote Model Context Protocol server from Claude Code, Codex, Cursor, or another MCP-compatible agent. The server exposes tools for discovering the models available to the authenticated account, creating text responses, comparing models, generating images, starting video generations, and checking video jobs until they finish.

The model catalog can change, so the skill instructs agents to call `list_models` before choosing a model and to use the exact returned model ID. Writingmate currently provides access to creative model families that include Seedance, Sora, Veo, Kling, PixVerse, and image-generation models. Account access and generation allowances depend on the user's Writingmate plan.

The official remote endpoint is:

```text
https://writingmate.ai/api/mcp
```

OAuth is preferred when the MCP host supports it. A Writingmate Developer Key can be stored in the host's secure bearer-token configuration when OAuth is unavailable. Never place a Developer Key, OAuth token, or Authorization header in source control, screenshots, issues, or prompts.

## Installation

### OpenClaw

```bash
clawhub install writingmate-mcp
```

### Direct repo/manual install

Clone Agent Skill Exchange and copy this skill into the skill directory used by your agent:

```bash
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/skills/writingmate-mcp ~/.agent-skills/writingmate-mcp
```

The canonical Writingmate skill can also be installed directly:

```bash
npx skills add writingmate/skills --skill writingmate-mcp
```

For Claude Code, connect the remote server:

```bash
claude mcp add --transport http writingmate https://writingmate.ai/api/mcp
claude mcp list
```

For Codex hosts that require a fixed bearer token, configure the endpoint and reference an environment variable containing the Developer Key:

```toml
[mcp_servers.writingmate]
url = "https://writingmate.ai/api/mcp"
bearer_token_env_var = "WRITINGMATE_DEVELOPER_KEY"
```

## Agent workflow

1. Call `list_models` before selecting a text, image, or video model.
2. Use an exact model ID returned by Writingmate; do not invent or silently substitute IDs.
3. Ask before starting a large batch of paid or allowance-consuming generations.
4. For video, save the generation ID returned by `generate_video` and poll `get_video` at reasonable intervals instead of starting duplicate jobs.
5. Return the generated asset only after the tool reports success. Surface errors and unavailable models directly.
6. Tell the user which model IDs were used, especially for comparisons.

The canonical skill, MCP safety rules, current setup documentation, and portable installer are maintained in the public MIT-licensed [writingmate/skills](https://github.com/writingmate/skills) repository.
