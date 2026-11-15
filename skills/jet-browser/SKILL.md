---
name: "Jet Browser"
slug: "jet-browser"
description: "Install, verify, integrate, or troubleshoot the Jet Browser WPE WebKit runtime for isolated agent browser sessions with ordered JSONL automation, native input, screenshots, and reproducible container checks."
github_stars: 2
verification: "listed"
source: "https://github.com/masakaai/jet-browser"
author: "masakaai"
category: "Browser Automation"
framework: "Codex"
tool_ecosystem:
  github_repo: "masakaai/jet-browser"
  github_stars: 2
---

# Jet Browser

Jet Browser is an open-source, local or self-hosted WPE WebKit runtime for AI-agent browser work. Use this skill when a repository needs an isolated browser process with ordered JSONL commands, native pointer and keyboard input, screenshots, explicit profile or download mounts, and a reproducible container acceptance check. It keeps model choice, reasoning, credentials, and orchestration in the calling project. The runtime is WebKit rather than Chromium: do not assume Chrome DevTools Protocol, Chrome extensions, or Chromium-only behavior. It is also not an anti-bot service, hosted proxy network, or replacement for a user's already-running personal Chrome profile.

## Installation

Install or set up from the source-backed instructions:

codex plugin marketplace add masakaai/jet-browser --ref main && codex plugin add jet-browser@masaka

- Source: https://github.com/masakaai/jet-browser

## Integration guidance

- Read `docs/demo.md` for the container lifecycle and `docs/agent-tools.md` for the model-facing declarations.
- Reuse the versioned tool definitions exported by `sdk/tools.mjs`; do not invent command names or response fields.
- Send one JSON command per line, consume one JSON response per line, preserve ordering, and close the session in guaranteed cleanup.
- Keep one isolated browser session per container. Mount profile and download paths explicitly, and do not pass unrelated host credentials into the container.
- Use semantic evidence for target selection and screenshots for visual verification when both are available.

Benchmark claims must retain their published scope. The repository's benchmark and technical report describe a pinned offline fixture; they do not establish public-site success, stealth, CAPTCHA handling, model accuracy, or long-running stability.
