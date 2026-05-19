---
name: "Realign drifting subtitles against finished video audio"
slug: "realign-drifting-subtitles-against-finished-video-audio"
description: "Uses Subaligner to retime an existing subtitle file against the final audio track, then outputs a corrected subtitle asset. This is for subtitle drift, forced alignment, or batch retiming, not for full video editing or general media management."
github_stars: 504
verification: "security_reviewed"
source: "https://github.com/baxtree/subaligner"
publisher_type: "open_source_project"
category: "Media & Transcription"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "baxtree/subaligner"
  github_stars: 504
---

# Realign drifting subtitles against finished video audio

Uses Subaligner to retime an existing subtitle file against the final audio track, then outputs a corrected subtitle asset. This is for subtitle drift, forced alignment, or batch retiming, not for full video editing or general media management.

## Prerequisites

FFmpeg

## Installation

Requirements and caveats from upstream:
- [![python](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/)
- [![Docker Pulls](https://img.shields.io/docker/pulls/baxtree/subaligner)](https://hub.docker.com/r/baxtree/subaligner)
- Note that subaligner[stretch], subaligner[dev] and subaligner[harmony] require [eSpeak](https://espeak.sourceforge.net/) to be pre-installed:

Basic usage or getting-started notes:
- <details>
- <summary>Install dependencies for enabling translation and transcription</summary>
- <pre><code>pip install 'subaligner[llm]'</code></pre>

- Source: https://github.com/baxtree/subaligner
- Extracted from upstream docs: https://raw.githubusercontent.com/baxtree/subaligner/HEAD/README.md

## Documentation

- https://subaligner.readthedocs.io/en/latest/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/realign-drifting-subtitles-against-finished-video-audio/)
