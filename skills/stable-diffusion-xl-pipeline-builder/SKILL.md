---
name: "Stable Diffusion XL Pipeline Builder"
slug: "stable-diffusion-xl-pipeline-builder"
description: "Constructs and executes SDXL image generation pipelines using diffusers library and ComfyUI API. Supports LoRA loading, ControlNet conditioning, and batch prompt scheduling."
github_stars: 27135
verification: "listed"
source: "https://github.com/Stability-AI/generative-models"
category: "Image & Creative Automation"
framework: "Cursor"
tool_ecosystem:
  github_repo: "Stability-AI/generative-models"
  github_stars: 27135
---

# Stable Diffusion XL Pipeline Builder

Constructs and executes SDXL image generation pipelines using diffusers library and ComfyUI API. Supports LoRA loading, ControlNet conditioning, and batch prompt scheduling.

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/Stability-AI/generative-models.git
- pip install hatch
- pip install "numpy>=1.17" "PyWavelets>=1.1.1" "opencv-python>=4.1.0.25"
- pip install --no-deps invisible-watermark

Requirements and caveats from upstream:
- python scripts/sampling/simple_video_sample_4d2.py --input_path assets/sv4d_videos/camel.gif --output_folder outputs (after downloading [sv4d2.safetensors](https://huggingface.co/stabilityai/sv4d2.0) from HuggingFace...
- Run inference: python scripts/sampling/simple_video_sample_4d2.py --input_path <path/to/video>
- Run inference: python scripts/sampling/simple_video_sample_4d2.py --model_path checkpoints/sv4d2_8views.safetensors --input_path assets/sv4d_videos/chest.gif --output_folder outputs

Basic usage or getting-started notes:
- To run **SV4D 2.0** on a single input video of 21 frames:
- **Low VRAM environment** : To run on GPUs with low VRAM, try setting --encoding_t=1 (of frames encoded at a time) and --decoding_t=1 (of frames decoded at a time) or lower video resolution like --img_size=512.
- The 5x8 model takes 5 frames of input at a time. But the inference scripts for both model take 21-frame video as input by default (same as SV3D and SV4D), we run the model autoregressively until we generate 21 frames.

- Source: https://github.com/Stability-AI/generative-models
- Extracted from upstream docs: https://raw.githubusercontent.com/Stability-AI/generative-models/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-xl-pipeline-builder/)
