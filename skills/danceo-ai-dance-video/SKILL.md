---
name: "AI Dance Video with Danceo"
slug: "danceo-ai-dance-video"
description: "Use Danceo Video MCP to select a dance template, check credits, create a portrait-based dance video, and poll the render status."
verification: "listed"
source: "https://github.com/jasonliu119/danceo-ai-dance-mcp-skills"
category: "Image & Creative Automation"
framework: "MCP"
tool_ecosystem:
  github_repo: "jasonliu119/danceo-ai-dance-mcp-skills"
---

# AI Dance Video with Danceo

Use this skill when someone wants to animate a portrait using a Danceo dance template. The Danceo Video MCP server connects an assistant to the Danceo API: list available reference templates, check the account's credit balance, create a render and retrieve its status. The server runs locally over stdio and calls the remote Danceo service.

A Danceo account, API key and purchased credits are required. There are no free credits. A render spends credits from the account attached to the configured key. Check the current price and balance before creating a job; confirm the cost unless the user has already clearly authorized the paid render. Never include API keys in output or logs.

## Installation

Install the original skill in a compatible agent with the third-party skills CLI:

```bash
npx skills add jasonliu119/danceo-ai-dance-mcp-skills --skill ai-dance-video
```

Configure the MCP server in a compatible client using Node.js:

```json
{
  "mcpServers": {
    "danceo": {
      "command": "npx",
      "args": ["-y", "danceo-video-mcp"],
      "env": { "DANCEO_API_KEY": "<your-api-key>" }
    }
  }
}
```

Create an API key in Danceo account settings. See the [MCP guide](https://danceo.ai/mcp?ref=agentskillexchange) and [Danceo homepage](https://danceo.ai/?ref=agentskillexchange) for setup and product information.

## Workflow

1. Ask for a publicly reachable HTTPS portrait image URL and confirm permission to transform the person's likeness.
2. Call `get_credits` and `list_dance_templates`. Select an appropriate template and use its returned ID. The API uses Danceo showcase references; arbitrary reference video URLs are not supported.
3. Confirm the duration is an integer from 5 to 30 seconds and no longer than the selected reference. Supply the number of portraits requested by the template.
4. Check the current render cost and available balance. Obtain authorization for the paid render, then call `create_dance_video` and retain the returned job ID.
5. Poll `get_video_status` at reasonable intervals. Return the result URL when the job succeeds, or explain the reported error if it fails. Do not create duplicate jobs while waiting.

For invalid credentials, visit [API key settings](https://danceo.ai/settings/apikeys). For insufficient credits, review [pricing](https://danceo.ai/pricing). The original source and detailed usage notes are in the [Danceo repository](https://github.com/jasonliu119/danceo-ai-dance-mcp-skills).
