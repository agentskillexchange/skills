---
name: "Telegram Bot UI"
slug: "telegram-bot-ui"
description: "UI/UX skill that makes Telegram bots look and feel like real products: messages, keyboards, buttons, navigation, streaming AI replies with Stop, HTML widgets and premium emoji. Use it when building a new bot interface or auditing an existing one. Updated with every new Bot API release."
category: "Developer Tools"
framework: "Claude Code"
verification: listed
source: "https://github.com/hlibsuslov/telegram-bot-ui"
---

# Telegram Bot UI

Telegram Bot UI is an MIT-licensed Agent Skill, maintained at [hlibsuslov/telegram-bot-ui](https://github.com/hlibsuslov/telegram-bot-ui), that helps a coding agent design, build and audit the interface of Telegram bots so they look and feel like real products. Its entry point is `SKILL.md`, with reference files, recipes and an offline Bot API catalog next to it. It is not a bot framework or a hosted service and needs no API key of its own.

**What it covers.**

- Message texts, microcopy, titles and captions, and formatting with HTML, MarkdownV2 or entities, including Rich Messages and tables.
- Inline and reply keyboards, button labels and grouping, colored buttons (`style`), custom emoji on buttons (`icon_custom_emoji_id`), the menu button and bot commands.
- Navigation: back, pagination, confirmations, empty and error states, and consistency between screens.
- Streaming AI replies with a Stop control (`sendMessageDraft`), typing and progress feedback.
- HTML widgets, premium custom emoji, channel publishing, agent-operated bots and Telegram Stars payments.
- Auditing an existing bot's interface and proposing concrete fixes.
- An offline catalog of Bot API methods and fields, updated with every new Bot API release.

**When to use it.** Ask the agent things like "improve the UX of this Telegram bot", "rewrite this menu", "add colored buttons" or "the bot feels frozen while the model answers". The skill activates on its own; no API names are needed.

**Hosts.** It works in Claude Code (as a plugin with five subagents, or as a plain skill folder), Codex, Cursor, Gemini CLI, GitHub Copilot and any agent that reads `AGENTS.md`, through adapters in the repository's `adapters/` folder.

## Installation

Install from the official repository: [https://github.com/hlibsuslov/telegram-bot-ui](https://github.com/hlibsuslov/telegram-bot-ui). Updates are released there, so prefer it over copying this catalog entry.

### Claude Code (plugin marketplace)

```text
/plugin install telegram-bot-ui --marketplace hlibsuslov/telegram-bot-ui
```

### Claude Code (plain skill folder)

```bash
git clone https://github.com/hlibsuslov/telegram-bot-ui.git ~/.claude/skills/telegram-bot-ui
```

### Codex, Cursor, Gemini CLI, Copilot and other hosts

Clone the repository and run its installer (standard library Python; it prints its plan first with `--dry-run`):

```bash
git clone https://github.com/hlibsuslov/telegram-bot-ui.git
cd telegram-bot-ui
python scripts/install.py --host all --scope user --dry-run
```

## Usage

Open your bot's repository in the agent and ask, for example: "Improve the UX of this Telegram bot" or "Audit the keyboards and messages in this bot".

## Source

- [hlibsuslov/telegram-bot-ui](https://github.com/hlibsuslov/telegram-bot-ui)
