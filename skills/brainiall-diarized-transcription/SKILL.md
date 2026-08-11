---
name: "BRAINIALL Diarized Transcription"
slug: "brainiall-diarized-transcription"
description: "Transcribes one explicitly authorized Brazilian Portuguese or Spanish audio or video file through the metered BRAINIALL API, then creates speaker-labelled JSON, SRT, and WebVTT with word timestamps and no automatic retry."
category: "Media & Transcription"
framework: "Multi-Framework"
verification: "listed"
source: "https://github.com/fasuizu-br/brainiall-transcription-skill"
---

# BRAINIALL Diarized Transcription

Use this skill when an agent must turn one explicitly authorized Brazilian
Portuguese or Spanish recording into a reviewable transcript and caption
artifacts. The upstream repository provides a dependency-free Node.js 22
client, mocked tests, a public OpenAPI contract, and JSON, SRT, and WebVTT
outputs with word timestamps and anonymous speaker-turn labels.

The BRAINIALL endpoint is an external metered API. Before selecting media, the
workflow requires confirmation of recording rights and any applicable speaker
notice or consent. It accepts one local regular `.mp3`, `.wav`, `.m4a`, `.mp4`,
`.mpeg`, `.mpga`, `.webm`, or `.ogg` file up to 25 MB. It rejects directories,
globs, symbolic links, remote URLs, unsupported languages, existing output
directories, and missing confirmation. A dedicated revocable key stays in the
`BRAINIALL_API_KEY` environment variable; keys, media, transcripts, filenames,
and upstream response bodies are excluded from logs.

The client sends exactly one request with `diarize=true`. It never retries an
ambiguous upload automatically because another request can create another
charge. Human review remains required: speaker labels indicate turns, not
biometric identities, and generated words and times can be wrong.

## Installation

Clone and inspect the upstream source before installing it. This avoids
executing an unpinned third-party package as part of the install path:

```bash
git clone https://github.com/fasuizu-br/brainiall-transcription-skill.git
cd brainiall-transcription-skill
git rev-parse HEAD
npm test
```

After reviewing the checked-out source and test result, copy
`skills/brainiall-diarized-transcription` into the local skills directory using
the agent host's documented installation process. The clone directory is not
itself the host's skills directory.

Review the [public source and tests](https://github.com/fasuizu-br/brainiall-transcription-skill)
before use. Create or manage the required account through the skill-specific
setup link in the installed upstream `SKILL.md`, and check the current price
and balance before any live request.

## Invocation

After the skill is installed and the rights, cost, input, language, and output
path are confirmed, its bundled client runs relative to the upstream
`SKILL.md`:

```bash
node scripts/transcribe.mjs \
  --input /absolute/path/to/authorized-recording.wav \
  --language pt \
  --output-dir /absolute/path/to/new-output-directory \
  --rights-and-consent
```

Report only output paths and speaker/word counts unless the user explicitly
asks to display sensitive transcript content.
