---
title: Coqui TTS Deep Learning Text-to-Speech Toolkit
description: 'Coqui TTS is an open-source deep learning toolkit for text-to-speech
  synthesis, originally developed by Coqui AI and now maintained by the community.
  With over 44,000 GitHub stars, it is one of the most widely adopted TTS frameworks
  available and has been battle-tested in both research and production environments.
  Core Capabilities The toolkit provides a unified interface to multiple neural TTS
  model architectures. Supported models include VITS (Variational Inference with adversarial
  learning for end-to-end Text-to-Speech), Tacotron2 with DDC alignment, GlowTTS,
  FastSpeech2, and Bark. Each model can be trained from scratch or fine-tuned on custom
  datasets using the built-in training pipeline. Voice Cloning and Conversion Coqui
  TTS supports zero-shot multi-speaker TTS using the XTTS model, which can clone a
  voice from a short reference audio clip without any fine-tuning. The toolkit also
  includes on-the-fly voice conversion, allowing synthesized speech in one voice to
  be converted to another target voice in real time. CLI and API Usage The tts command-line
  tool enables quick synthesis from the terminal. For example, tts --text "Hello world"
  --model_name tts_models/en/ljspeech/vits generates audio directly. The Python API
  provides fine-grained control: load models, configure vocoders, set speaker embeddings,
  and stream output to files or audio devices. Multilingual Support Pre-trained models
  cover multiple languages including English, German, French, Spanish, Portuguese,
  Italian, Dutch, Turkish, and more. The XTTS v2 model supports cross-lingual voice
  cloning, synthesizing speech in one language using a voice sample from another language.
  Integration Points Install via PyPI with pip install TTS . The package integrates
  with PyTorch for GPU-accelerated inference, supports ONNX export for production
  deployment, and can serve models via a built-in HTTP server for REST API access.
  Models are automatically downloaded from Coqui’s model hub on first use.'
verification: security_reviewed
source: https://github.com/coqui-ai/TTS
category:
- Media &amp; Transcription
framework:
- Custom Agents
tool_ecosystem:
  github_repo: coqui-ai/TTS
  github_stars: 44959
---

# Coqui TTS Deep Learning Text-to-Speech Toolkit

Coqui TTS is an open-source deep learning toolkit for text-to-speech synthesis, originally developed by Coqui AI and now maintained by the community. With over 44,000 GitHub stars, it is one of the most widely adopted TTS frameworks available and has been battle-tested in both research and production environments. Core Capabilities The toolkit provides a unified interface to multiple neural TTS model architectures. Supported models include VITS (Variational Inference with adversarial learning for end-to-end Text-to-Speech), Tacotron2 with DDC alignment, GlowTTS, FastSpeech2, and Bark. Each model can be trained from scratch or fine-tuned on custom datasets using the built-in training pipeline. Voice Cloning and Conversion Coqui TTS supports zero-shot multi-speaker TTS using the XTTS model, which can clone a voice from a short reference audio clip without any fine-tuning. The toolkit also includes on-the-fly voice conversion, allowing synthesized speech in one voice to be converted to another target voice in real time. CLI and API Usage The tts command-line tool enables quick synthesis from the terminal. For example, tts --text "Hello world" --model_name tts_models/en/ljspeech/vits generates audio directly. The Python API provides fine-grained control: load models, configure vocoders, set speaker embeddings, and stream output to files or audio devices. Multilingual Support Pre-trained models cover multiple languages including English, German, French, Spanish, Portuguese, Italian, Dutch, Turkish, and more. The XTTS v2 model supports cross-lingual voice cloning, synthesizing speech in one language using a voice sample from another language. Integration Points Install via PyPI with pip install TTS . The package integrates with PyTorch for GPU-accelerated inference, supports ONNX export for production deployment, and can serve models via a built-in HTTP server for REST API access. Models are automatically downloaded from Coqui’s model hub on first use.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/coqui-tts-deep-learning-text-to-speech-toolkit/)
