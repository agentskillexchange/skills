---
name: "Pronounce Developer Jargon"
slug: "pronounce-developer-jargon"
description: "Answers short pronunciation questions about developer tools, AI models, acronyms, and project names by using the say-it CLI to play local audio and return IPA, a plain-English respelling, source evidence, and contested alternatives."
verification: "listed"
source: "https://github.com/anzy-renlab-ai/pronounce"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "anzy-renlab-ai/pronounce"
---

# Pronounce Developer Jargon

Use this skill when a user asks how to pronounce one developer term, project,
product, AI model, acronym, or researcher name—for example `kubectl`, `nginx`,
`Qwen`, `JEPA`, `GIF`, or `PostgreSQL`. It wraps the open-source `say-it` CLI and
its 1,900+ entry TSV dictionary. The tool plays the intended local pronunciation
through macOS `say`, Linux `espeak-ng`/`espeak`, or Windows PowerShell
`System.Speech`, rather than asking a generic speech engine to guess from the raw
spelling. Dictionary records include General American IPA, an English-like TTS
respelling, alternate readings, confidence labels, editorial notes, and a source
URL when an official FAQ, creator statement, or other useful citation exists.

Do not use this skill to narrate sentences or paragraphs. It is deliberately
scoped to one short technical name. Quote the target when invoking the CLI so
punctuation in names such as `C++` is passed literally.

## Instructions

1. Run `say-it --json "<word>"` to inspect the canonical dictionary record
   without playing audio. Never invent a source when `source_url` is empty.
2. Run `say-it "<word>"` to play the primary reading three times. The default
   also speaks recorded alternatives after an audible “or”.
3. Reply with the IPA, a readable stressed respelling, the source URL when
   present, and a brief note when the confidence is `contested`.
4. If the user asks for the rival reading, run `say-it --alt "<word>"`. Use
   `--solo` when the user wants only the primary and `--why` for a text record.
5. When `in_dict` is false, say that the local dictionary has no curated record;
   do not present the speech engine guess as creator-verified.

## Installation

No source-backed install or usage instructions could be extracted automatically. Review the upstream project before running this skill in a sensitive workflow.

- Source: https://github.com/anzy-renlab-ai/pronounce

