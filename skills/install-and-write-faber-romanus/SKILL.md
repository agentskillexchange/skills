---
name: "Install and write Faber Romanus"
slug: "install-and-write-faber-romanus"
description: "Download the Faber CLI and write Faber Romanus programs using the official agent skill guides (install, English reader spelling, packages, corpus)."
category: "Developer Tools"
framework: "Multi-Framework"
verification: listed
source: "https://github.com/faberlang/faber"
author: "faberlang"
publisher_type: "organization"
tool_ecosystem:
  github_repo: "faberlang/faber"
---

# Install and write Faber Romanus

Faber Romanus is an experimental statically typed language designed to be written by language models and read by people ([faberlang.dev](https://faberlang.dev)). It is type-first, its grammar is mechanical, and one source file uses one reader locale. The open-core compiler lives at [github.com/faberlang/faber](https://github.com/faberlang/faber) under MIT OR Apache-2.0. The language is experimental through 1.x: breaking changes ship in minor releases. Current release archives publish a `faber` binary for macOS arm64 and Linux x64 only.

This catalog entry wraps the official agent skills. Do not invent install URLs, spelling rules, or CLI flags from memory. The live skill catalog is https://faberlang.dev/.well-known/agent-skills/index.json; those four `SKILL.md` files are indexed from https://faberlang.dev/llms.txt. Fetch the official files when you need current archive names, checksums, or writing rules.

## How an agent should use the official skills

1. **install** — Fetch https://faberlang.dev/.well-known/agent-skills/install/SKILL.md first. It names the current CLI release, the two published archives (`aarch64-apple-darwin` and `x86_64-unknown-linux-gnu`), SHA-256 verification, and PATH placement of `bin/faber`. The archive ships one file; reader packs and the Norma standard library are built into the binary. Prove the install with `faber --version` and `faber explain SEM001`. On any other platform, stop and tell the human. Prefer prebuilts. `cargo build --release -p faber` from the open-source repo builds the compiler front end and MIR runner; release binaries also include the target code generators, which are not in that repository.

2. **language** — Fetch https://faberlang.dev/.well-known/agent-skills/language/SKILL.md for the English reader spelling. Start at the agent canon https://faberlang.dev/agents/index.md and follow only the links that page names. Meaning lives in HIR; a reader locale is a rendering of that core. English signals include type-first declarations (`string name`, `int n`), `fn name(int a) → int`, bind `←`, equality `≡`, `return`, nullable `int ∪ none` (the missing value is `null`), and comments as a `#` line by itself. Do not write `name: T`, `int?`, `//`, or a `#` after code on the same line.

3. **packages** — Fetch https://faberlang.dev/.well-known/agent-skills/packages/SKILL.md to scaffold and drive packages. `faber init` writes `faber.toml` and `src/main.fab`. Use `faber check` for the front-end type-check loop (lex, parse, type check without building a native binary), `faber run` to interpret, `faber build` to compile (for example `-t rust`), `faber test` for proba suites, `faber format` (add `--write` to apply), and `faber explain <CODE>` for stable diagnostic codes. `norma:*` resolves from the library embedded in the binary; other libraries resolve from the Cista package store recorded in `faber.lock`. Pass `--library-home` only for an intentional local override.

4. **corpus** — Fetch https://faberlang.dev/.well-known/agent-skills/corpus/SKILL.md after the writing guide, as a keyword lookup rather than a substitute for it. Read https://faberlang.dev/llms-full.txt, use the English reader spelling the catalog entry names, then open the term page URL (for example `fn` → https://faberlang.dev/en-US/corpus/fn.html).

## Installation

### OpenClaw

```bash
clawhub install install-and-write-faber-romanus
```

### Direct repo/manual install

Clone the Agent Skill Exchange repository and copy this skill directory into the skill folder used by your agent runtime:

```bash
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/skills/install-and-write-faber-romanus ~/.agent-skills/install-and-write-faber-romanus
```

### Optional Third-Party Installer

The `skills` npm package is maintained by Vercel Labs / third parties, not AgentSkillExchange. If you choose to use it, pin the package version:

```bash
npm exec --package=skills@1.5.7 -- skills add agentskillexchange/skills --skill install-and-write-faber-romanus
```

## Documentation

- https://faberlang.dev
- https://faberlang.dev/llms.txt
- https://faberlang.dev/.well-known/agent-skills/install/SKILL.md
- https://faberlang.dev/.well-known/agent-skills/language/SKILL.md
- https://faberlang.dev/.well-known/agent-skills/packages/SKILL.md
- https://faberlang.dev/.well-known/agent-skills/corpus/SKILL.md
