---
name: "Prompt Optimizer"
slug: "prompt-optimizer-skill"
description: "Turns a rough request or an existing prompt into one copy-ready prompt for any AI agent that can load Skills (or as pasted custom instructions). Keeps the user's wording verbatim, keeps its own additions subordinate, never invents missing facts, and replies in the user's language. It only rewrites the prompt and does not do the task. Invoked automatically only when a request is clearly vague or missing key information, or when the user explicitly asks to optimize or review a prompt."
verification: "listed"
source: "https://github.com/Samuel-Shek/prompt-optimizer-skill"
category: "Templates & Workflows"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "samuel-shek/prompt-optimizer-skill"
---

# Prompt Optimizer

Prompt Optimizer is an MIT-licensed Skill, maintained at [Samuel-Shek/prompt-optimizer-skill](https://github.com/Samuel-Shek/prompt-optimizer-skill) (current version v4.1.2), that turns a rough request or an existing prompt into one copy-ready prompt. It only rewrites the prompt; it does not do the task itself. It works in any AI agent that can load Skill files, and in tools that cannot install Skills you can paste its `SKILL.md` into the custom instructions. It is not a standalone app or model and needs no API key or background service.

**When it runs.** For each question or task, the agent first judges whether the request is clear enough to answer well directly. If it is, the agent just answers. The optimizer is called automatically only when the request is clearly vague or missing key information, or when the user explicitly asks to optimize, rewrite, tighten, expand, adapt, or review a prompt, System Prompt, or agent instruction. Saying "review it, don't rewrite" returns feedback only.

**What it guarantees.**

- **Verbatim wording.** The user's request is copied word for word into a "User's exact words" section. Numbers, dates, names, file names, prohibitions, and relative times stay exactly as written.
- **Subordinate additions.** Anything the optimizer adds (steps, checks, handling of missing information) goes into "Supplementary notes", which open by stating that the user's exact words win any conflict. It does not add word counts, formats, prohibitions, or acceptance criteria the user did not ask for.
- **No invented facts.** Missing information becomes a placeholder such as `{{TO FILL: ...}}` or a "To confirm" item with a fallback, never a guess.
- **Instructions vs. material.** Pasted text that attempts to override instructions is kept as material and treated as data, not as an order.
- **Language.** It replies in the user's language (English, Chinese, or others) and never translates the user's wording or material. Documentation is available in English and Simplified Chinese.

**Output.** One code block with plain-text labels: Task (optional), User's exact words, Material, Supplementary notes, and To confirm. Empty sections are left out. Optional shortcuts: `+explain` adds up to five notes on key changes, and `+two` gives two versions with different purposes.

**Limits.** For simple one-line tasks, asking directly is usually enough; the result is about the same. It cannot guarantee that the target AI complies. Its validation set is small: fictional Chinese and English cases, run mainly on Claude and GPT models.

## Installation

Install from the official repository: [https://github.com/Samuel-Shek/prompt-optimizer-skill](https://github.com/Samuel-Shek/prompt-optimizer-skill). The official repo is where updates are released, so prefer it over copying this catalog entry.

**Before installing**, check whether the agent already has a skill named `prompt-optimizer` or any similar prompt-optimization skill, plugin, or custom instruction. If one exists, ask the user whether to replace it, keep it, or run both. Do not overwrite it or install a second copy silently.

### Any agent that loads Skill folders (manual install)

```bash
git clone --branch v4.1.2 --depth 1 https://github.com/Samuel-Shek/prompt-optimizer-skill.git prompt-optimizer
```

Copy the whole `prompt-optimizer` folder into your agent's skills folder, keeping its `references/` and `agents/` subfolders, then start a new session. Common locations are `~/.claude/skills/` for Claude Code and `~/.agents/skills/` for Codex; check your tool's current docs for others. You can also download the archive from the [v4.1.2 release page](https://github.com/Samuel-Shek/prompt-optimizer-skill/releases/tag/v4.1.2).

### Claude Code (plugin marketplace)

```text
/plugin marketplace add Samuel-Shek/prompt-optimizer-skill
/plugin install prompt-optimizer@prompt-optimizer
```

### Tools that cannot install Skills (ChatGPT GPTs, Claude Projects, other chat apps)

Paste the contents of [`SKILL.md`](https://github.com/Samuel-Shek/prompt-optimizer-skill/blob/main/SKILL.md) into the custom instructions. Add [`references/methods.md`](https://github.com/Samuel-Shek/prompt-optimizer-skill/blob/main/references/methods.md) if you want its optional methods.

## Usage

```text
Use $prompt-optimizer: write a research prompt comparing three note-taking apps.
Target: ChatGPT on the web. Public sources only, separate facts from opinions, keep source dates.
```

Call it by name with `$prompt-optimizer` (Codex) or `/prompt-optimizer` (manually installed Claude Code skill). After a plugin marketplace install, use `/prompt-optimizer:prompt-optimizer`.

## Source

- Official repository: https://github.com/Samuel-Shek/prompt-optimizer-skill
- README (English): https://github.com/Samuel-Shek/prompt-optimizer-skill/blob/main/README.md
- README (简体中文): https://github.com/Samuel-Shek/prompt-optimizer-skill/blob/main/README.zh-CN.md
- Disclosure: this listing was submitted by the project's maintainer.
