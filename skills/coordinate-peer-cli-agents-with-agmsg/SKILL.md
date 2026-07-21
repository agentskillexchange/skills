---
name: "Coordinate peer CLI agents with agmsg"
slug: "coordinate-peer-cli-agents-with-agmsg"
description: "Let Claude Code, Codex, Gemini CLI, Copilot CLI, and other terminal agents exchange messages through a shared local SQLite channel."
github_stars: 1291
verification: "security_reviewed"
source: "https://github.com/fujibee/agmsg"
author: "fujibee"
publisher_type: "individual"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "fujibee/agmsg"
  github_stars: 1291
  npm_package: "agmsg"
  npm_weekly_downloads: 3984
---

# Coordinate peer CLI agents with agmsg

Let Claude Code, Codex, Gemini CLI, Copilot CLI, and other terminal agents exchange messages through a shared local SQLite channel.

## Prerequisites

bash, sqlite3, agmsg scripts, Claude Code/Codex/Gemini CLI/Copilot CLI/Antigravity/OpenCode as applicable

## Installation

Use the upstream install or setup path that matches your environment:
- npx agmsg
- npx agmsg # one-shot, no global install
- npm i -g agmsg && agmsg install
- git clone https://github.com/fujibee/agmsg.git

Requirements and caveats from upstream:
- **Requires:** bash and sqlite3. macOS ships both. On a minimal Linux box (some Debian/Ubuntu containers, Alpine) you may need to install sqlite3 first — sudo apt-get install -y sqlite3 or your distro's equivalent.
- Monitor tool. The sandbox allowlist is still required for writes performed by
- single run. In that case, the run-specific writable roots must also include the

Basic usage or getting-started notes:
- That's it. The slash command prompts you for a team name and an agent name on first use, then asks you to pick a [delivery mode](#delivery-modes) (default on Claude Code: monitor — real-time push; Codex offers a beta...
- Prefer to inspect the code first, track the latest main, or pick a custom command name? See [Install](#install) below for the setup.sh one-liner, git clone, and the Claude Code plugin marketplace paths.
- agmsg is a thin transport. Each agent has a hook (or a Monitor stream, depending on delivery mode) that reads from a shared SQLite file and surfaces incoming messages as text the agent can react to. Sending is a send....

- Source: https://github.com/fujibee/agmsg
- Extracted from upstream docs: https://raw.githubusercontent.com/fujibee/agmsg/HEAD/README.md

## Documentation

- https://github.com/fujibee/agmsg

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/coordinate-peer-cli-agents-with-agmsg/)
