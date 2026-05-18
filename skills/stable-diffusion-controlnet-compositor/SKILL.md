---
name: "Stable Diffusion ControlNet Compositor"
slug: "stable-diffusion-controlnet-compositor"
description: "Orchestrates Stable Diffusion XL with ControlNet preprocessors (Canny, Depth, OpenPose) for guided image generation. Manages ComfyUI workflow JSON exports and A1111 API batch processing."
github_stars: 33867
verification: "security_reviewed"
source: "https://github.com/lllyasviel/ControlNet"
category: "Image & Creative Automation"
framework: "Gemini"
tool_ecosystem:
  github_repo: "lllyasviel/ControlNet"
  github_stars: 33867
---

# Stable Diffusion ControlNet Compositor

Orchestrates Stable Diffusion XL with ControlNet preprocessors (Canny, Depth, OpenPose) for guided image generation. Manages ComfyUI workflow JSON exports and A1111 API batch processing.

## Installation

Use the upstream install or setup path that matches your environment:
- conda env create -f environment.yaml
- conda activate control

Requirements and caveats from upstream:
- python gradio_canny2image.py
- python gradio_hough2image.py
- python gradio_hed2image.py

Basic usage or getting-started notes:
- Note that the UI is based on Gradio, and Gradio is somewhat difficult to customize. Right now you need to draw scribbles outside the UI (using your favorite drawing software, for example, MS Paint) and then import the...
- Note that the below example is 768×768. No prompts. No "positive" prompts. No "negative" prompts.
- Below is another challenging example:

- Source: https://github.com/lllyasviel/ControlNet
- Extracted from upstream docs: https://raw.githubusercontent.com/lllyasviel/ControlNet/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-controlnet-compositor/)
