---
name: "Use OmniParser for vision-based GUI parsing"
slug: "use-omniparser-for-vision-based-gui-parsing"
description: "Parse screenshots into structured UI elements so computer-use agents can reason about controls before acting."
github_stars: 24836
verification: "security_reviewed"
source: "https://github.com/microsoft/OmniParser"
author: "Microsoft"
publisher_type: "open_source"
category: "Browser Automation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "microsoft/OmniParser"
  github_stars: 24836
---

# Use OmniParser for vision-based GUI parsing

Parse screenshots into structured UI elements so computer-use agents can reason about controls before acting.

## Prerequisites

Python 3.12; conda; Hugging Face model weights; optional Gradio demo

## Installation

Use the upstream install or setup path that matches your environment:
- conda create -n "omni" python==3.12
- conda activate omni
- pip install -r requirements.txt

Requirements and caveats from upstream:
- python
- python weights/convert_safetensor_to_pt.py
- python gradio_demo.py

Basic usage or getting-started notes:
- First clone the repo, and then install environment:
- cd OmniParser
- Ensure you have the V2 weights downloaded in weights folder (ensure caption weights folder is called icon_caption_florence). If not download them with:

- Source: https://github.com/microsoft/OmniParser
- Extracted from upstream docs: https://raw.githubusercontent.com/microsoft/OmniParser/HEAD/README.md

## Documentation

- https://microsoft.github.io/OmniParser/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/use-omniparser-for-vision-based-gui-parsing/)
