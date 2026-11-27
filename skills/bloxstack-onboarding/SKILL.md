---
name: "BloxStack Onboarding"
slug: "bloxstack-onboarding"
description: "Help Roblox teams start using BloxStack Studio to organize their own games, tasks, and files. Use when a creator wants to set up a team workspace, connect Claude Code, Codex, Cursor or another MCP client, plan their first task, or ask about work their team has added."
verification: "listed"
source: "https://github.com/BloxStack/skills/tree/main/skills/bloxstack-onboarding"
category: "Integrations & Connectors"
framework: "MCP"
---

# BloxStack Onboarding

Explain that BloxStack Studio provides the team’s tools and that the team adds its own games, tasks, and files. Connect the creator’s assistant through the official remote HTTP MCP endpoint at `https://bloxstack.app/mcp`.

## Start where the creator is

- If BloxStack tools are already available, go straight to the first studio read. If a configured connection needs to sign in again, reuse it.
- If the creator is new, open [BloxStack Studio](https://bloxstack.app/studio). Let them sign in with Roblox and select an existing studio or create one. Use an existing team's studio when joining teammates. If an expected studio is missing, check the Roblox identity and membership with the creator.
- If you can configure the current client, do that for the creator. If you need their input, give just the next step for their app. Ask which app they use only if you cannot tell.

## Connect the current app

| Client | Setup |
| --- | --- |
| Claude Code | Run `claude mcp add --transport http bloxstack https://bloxstack.app/mcp`. In Claude Code, open `/mcp` and select `bloxstack` to sign in. |
| Codex CLI | Run `codex mcp add bloxstack --url https://bloxstack.app/mcp`, then `codex mcp login bloxstack`. |
| Gemini CLI | Run `gemini mcp add --transport http bloxstack https://bloxstack.app/mcp`, then enter `/mcp auth bloxstack` in Gemini. |
| Cursor or VS Code | Open the studio's **Agent → Connect**, select the editor, and use its install button. Then connect or start the server in the editor. |
| Claude or ChatGPT | Open **Agent → Connect** and select the app for its current connector settings. Use the remote address above and OAuth when prompted. |
| Other MCP clients | Add a remote Streamable HTTP server named `bloxstack` at the official address and start the client's OAuth flow. |

Let the creator finish the browser handoff. They check the app, choose one studio, and turn off **Allow changes** for a read-only introduction before selecting **Allow**. Leave sign-in details and tokens in the client and browser. If the client needs to reload its tools, resume from the first read in the refreshed session.

## Deliver the first result

1. Call the connected server's `get_studio` with `{}` first. Use the client-qualified tool name when shown. Verify the studio name matches the creator's intended team. If it differs, pause before reading further and have them reconnect to the intended studio.
2. Use the connected tools to check the part of the workspace the creator asked about. For tasks, use `list_tasks` if available. An empty task list tells you about that board only. If a tool or permission is missing, tell the creator what you could verify.
3. For a new workspace or an empty board, tell the creator what they can add. Ask what their team is building and offer to draft a first task in chat from their answer. For an existing workspace, answer using only the games, tasks, or files the tools actually returned.
4. Keep drafts in chat until the creator asks to save them. Respect read-only access. Opening a hosted Roblox Studio session uses Studio hours and is a separate workflow.

A configured endpoint alone is insufficient to verify access. If the studio read is unavailable, describe the last successful step and the single action that will unblock it. If an access or connection-limit notice appears, use its instructions. The creator can review or end a connection from the studio's **Agent** page.

[Set up a studio](https://bloxstack.app/learn/studio) · [Connect an AI app](https://bloxstack.app/learn/studio/agents)

## Installation

Install the upstream skill in a client that supports Agent Skills and remote MCP connections:

```sh
npx skills add BloxStack/skills --skill bloxstack-onboarding
```

## License

MIT License

Copyright (c) 2026 BloxStack

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
