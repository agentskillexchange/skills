---
name: "FreeFM"
slug: "freefm"
description: "Safely synchronize free-playable NetEase Private FM tracks into an append-only playlist using a native Rust CLI/TUI. Use when an operator needs QR login, read-only preview, strict playability checks, explicit cross-platform review, append-only sync, or zero-LLM scheduled execution."
verification: "listed"
source: "https://github.com/Yuxin-Qiao/FreeFM"
category: "Media & Transcription"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "yuxin-qiao/freefm"
---

# FreeFM

FreeFM is a native Rust CLI/TUI for reading NetEase Cloud Music Private FM and
appending only original tracks with consistent evidence of free full playback
to an operator-owned playlist. It keeps credentials local, never unlocks VIP
audio, never downloads or replaces playback URLs, and fails closed when
playability or playlist ownership is ambiguous.

Use this skill for interactive QR authentication, `preview`, `status`, `doctor`,
`audit`, explicit `review` of cross-platform candidates, or a user-confirmed
`sync`. Scheduled operation must call the deterministic binary directly as
`freefm sync --quiet`; do not turn routine synchronization into an Agent or
model request.

## Installation

### OpenClaw

```bash
openclaw skills install @yuxin-qiao/freefm
```

### Direct repo/manual install

```bash
git clone https://github.com/Yuxin-Qiao/FreeFM.git
cp -R FreeFM/skills/freefm ~/.agent-skills/freefm
```

### Rust CLI

```bash
cargo install --git https://github.com/Yuxin-Qiao/FreeFM --locked
```

Run `freefm preview` before the first write. Only `freefm sync` may append
tracks remotely; it must preserve existing tracks and order. Confirm the
account is authenticated and ordinary (`vipType == 0`) before synchronization.
