---
title: "WhisperX Speech Recognition with Word-Level Timestamps and Diarization"
description: "WhisperX extends OpenAI Whisper with batched inference for 70x realtime transcription, phoneme-based word-level timestamp alignment via wav2vec2, voice activity detection, and speaker diarization. It produces accurate per-word timestamps and speaker labels from audio files."
slug: "whisperx-speech-recognition-timestamps-diarization"
category:
  - "Media &amp; Transcription"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/m-bain/whisperX"
tool_ecosystem:
  github_repo: "m-bain/whisperX"
  github_stars: 21036
listed: true
---

# WhisperX Speech Recognition with Word-Level Timestamps and Diarization

WhisperX extends OpenAI Whisper with batched inference for 70x realtime transcription, phoneme-based word-level timestamp alignment via wav2vec2, voice activity detection, and speaker diarization. It produces accurate per-word timestamps and speaker labels from audio files.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install whisperx-speech-recognition-timestamps-diarization
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

WhisperX is an automatic speech recognition system that builds on OpenAI Whisper to deliver word-level timestamps and speaker diarization capabilities. While standard Whisper produces utterance-level timestamps that can be off by several seconds, WhisperX refines these using forced alignment with phoneme-based ASR models like wav2vec 2.0, producing accurate per-word timing.
Batched Inference
WhisperX implements batched inference using the faster-whisper backend (CTranslate2), achieving up to 70x realtime transcription speed with the large-v2 model. This makes it practical for processing long audio files, podcast archives, meeting recordings, and video libraries. The batch processing operates within individual files, maximizing GPU utilization without the overhead of sequential decoding.
Forced Alignment and Timestamps
The forced alignment pipeline takes the text output from Whisper and aligns it to the audio using a phoneme recognition model. This produces word-level timestamps with significantly higher accuracy than Whisper native timestamps. The alignment supports multiple languages through language-specific wav2vec2 models, and users can specify custom alignment models for specialized domains.
Speaker Diarization
WhisperX integrates speaker diarization via pyannote-audio, partitioning the transcript by speaker identity. Users can specify minimum and maximum speaker counts when the number of speakers is known. The diarization pipeline segments the audio by speaker and maps segments back to the word-level transcript, producing labeled output showing which speaker said what, with precise timing.
Voice Activity Detection
A VAD preprocessing step detects speech segments before transcription, filtering out silence and non-speech audio. This improves both transcription speed and accuracy by focusing compute on actual speech content. The VAD filter is especially useful for long recordings with significant silence or background noise.
Integration and Usage
WhisperX is installed via pip and runs from the command line: whisperx audio.wav –model large-v2 –diarize –highlight_words True. It outputs SRT, VTT, TSV, and JSON formats with word-level timing. The project has over 20,900 GitHub stars, is licensed under BSD-2-Clause, and has an associated academic paper. It is used in production for podcast transcription, meeting notes, subtitle generation, and content indexing pipelines.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/whisperx-speech-recognition-timestamps-diarization/)
