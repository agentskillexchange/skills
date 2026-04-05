---
name: "eSpeak NG Multilingual Speech Synthesizer"
description: "An agent skill built on eSpeak NG, the open-source formant-based speech synthesizer supporting over 100 languages and accents. Provides fast, lightweight text-to-speech synthesis via CLI and library API, with phoneme output, SSML support, and MBROLA voice integration for improved naturalness."
category: "Media &amp; Transcription"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/espeak-ng/espeak-ng"
tool_ecosystem:
  github_repo: "espeak-ng/espeak-ng"
  github_stars: 6311
---
# eSpeak NG Multilingual Speech Synthesizer

An agent skill built on eSpeak NG, the open-source formant-based speech synthesizer supporting over 100 languages and accents. Provides fast, lightweight text-to-speech synthesis via CLI and library API, with phoneme output, SSML support, and MBROLA voice integration for improved naturalness.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill espeak-ng-multilingual-speech-synthesizer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill espeak-ng-multilingual-speech-synthesizer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill espeak-ng-multilingual-speech-synthesizer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill espeak-ng-multilingual-speech-synthesizer -a codex
```

### OpenClaw

```bash
clawhub install espeak-ng-multilingual-speech-synthesizer
```

## Details

eSpeak NG (Next Generation) is an open-source compact speech synthesizer that supports over 100 languages and accents. Forked from the original eSpeak project, it is actively maintained with over 6,200 GitHub stars and serves as the pronunciation engine behind many accessibility tools, language learning applications, and other TTS systems including Piper.

Formant Synthesis Approach
Unlike neural TTS models that require GPU acceleration and large model files, eSpeak NG uses formant synthesis — a rule-based approach that generates speech by combining fundamental frequency patterns, formant transitions, and noise components. This makes it extremely fast and lightweight: the entire engine runs on minimal hardware including Raspberry Pi, embedded systems, and low-power devices without any GPU requirement.

Language Coverage
eSpeak NG provides pronunciation rules for over 100 languages, making it one of the most linguistically diverse TTS engines available. Languages span European (English, German, French, Spanish, Italian, Portuguese, Dutch, Swedish, Norwegian, Polish, Czech, Romanian, and more), Asian (Hindi, Tamil, Mandarin, Cantonese, Korean, Vietnamese, Thai), Middle Eastern (Arabic, Persian, Hebrew, Turkish), African (Swahili, Amharic), and constructed languages (Esperanto, Lojban).

CLI Usage
The espeak-ng command synthesizes text directly: espeak-ng "Hello world" plays audio, espeak-ng -w output.wav "Hello world" writes to file, and espeak-ng -v de "Hallo Welt" selects German. Flags control speed (-s), pitch (-p), amplitude (-a), and word gap (-g). SSML input is supported with -m for fine-grained prosody control.

Phoneme Output and IPA
A unique capability is phoneme transcription: espeak-ng --ipa "hello" outputs the International Phonetic Alphabet representation of any text in any supported language. This makes eSpeak NG valuable beyond speech synthesis — it serves as a pronunciation dictionary and phoneme converter for language processing pipelines.

MBROLA Voice Integration
For improved naturalness, eSpeak NG can drive MBROLA diphone voices. MBROLA provides smoother, more natural-sounding output using recorded diphone segments while eSpeak NG handles text analysis, phoneme conversion, and prosody generation. Over 70 MBROLA voices are available across multiple languages.

Installation and Integration
Available via system package managers (apt install espeak-ng, brew install espeak-ng), as a C library (libespeak-ng), and with Python bindings. The SAPI5 interface on Windows enables use with screen readers. Licensed under GPL-3.0 with active development and regular releases on GitHub.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/espeak-ng-multilingual-speech-synthesizer/)
