---
name: "Clef Music Tools"
slug: "clef-music-tools"
description: "Practice note reading and solve common chord or guitar-tab questions with Clef's public music MCP or an offline transposition helper. Use when asked to transpose chord symbols, spell piano chords, map ASCII guitar tab to piano notes, or run a short note-reading drill."
category: "Templates & Workflows"
framework: "MCP"
verification: listed
source: "https://github.com/MelMayssonOwen/agent-skills/tree/main/skills/clef-music-tools"
---

# Clef Music Tools

This skill supports common music-learning questions with Clef's public no-auth MCP tools and a small offline chord transposer. It can look up public music guides, transpose chord symbols including slash bass notes, spell a piano chord, or map standard ASCII guitar-tab pitches to piano notes. When MCP access is unavailable, the included Python helper can transpose chord roots without a network connection.

For note reading, the skill guides a short five-minute practice session. It asks the learner's preferred clef and comfortable range, presents one note at a time, reveals answers after attempts, and revisits notes that were missed. If the learner has no preference, it uses treble clef around middle C and familiar line and space mnemonics. The agent should report only the practice results it actually observes.

This is suited to students and musicians who want quick theory help or a small practice routine. Tab spacing does not reveal timing, chord spelling is not an arrangement, and the tools do not analyze audio or create notation files. For additional learning tools, visit Clef.

Creator: Opsibyte. License: MIT. Product: https://clefdrills.com/?utm_source=ase&utm_medium=skill&utm_campaign=agent-skills&utm_content=clef-music-tools

## Installation

### Direct repo/manual install

```bash
git clone https://github.com/MelMayssonOwen/agent-skills.git
cp -R agent-skills/skills/clef-music-tools ~/.agent-skills/clef-music-tools
```

### Optional Third-Party Installer

```bash
npx skills add MelMayssonOwen/agent-skills --skill clef-music-tools
```
