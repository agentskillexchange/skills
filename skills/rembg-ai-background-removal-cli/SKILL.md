---
name: "rembg AI Background Removal CLI and Python Library"
slug: "rembg-ai-background-removal-cli"
description: "rembg is a Python tool for automatic image background removal powered by AI models like U2-Net and SAM. It works as a CLI, Python library, HTTP server, or Docker container, supporting CPU and GPU acceleration for batch processing of images and video frames."
github_stars: 22400
verification: "security_reviewed"
source: "https://github.com/danielgatis/rembg"
category: "Image & Creative Automation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "danielgatis/rembg"
  github_stars: 22400
---

# rembg AI Background Removal CLI and Python Library

rembg is a Python tool for automatic image background removal powered by AI models like U2-Net and SAM. It works as a CLI, Python library, HTTP server, or Docker container, supporting CPU and GPU acceleration for batch processing of images and video frames.

## Installation

Use the upstream install or setup path that matches your environment:
- pip install "rembg[cpu]" # for library
- pip install "rembg[cpu,cli]" # for library + cli
- pip install "rembg[gpu]" # for library
- pip install "rembg[gpu,cli]" # for library + cli

Requirements and caveats from upstream:
- <p align="center">Rembg is a tool to remove image backgrounds. It can be used as a CLI, Python library, HTTP server, or Docker container.</p>
- python: >=3.11, <3.14
- **Note:** NVIDIA GPUs may require onnxruntime-gpu, CUDA, and cudnn-devel. See [#668](https://github.com/danielgatis/rembg/issues/668#issuecomment-2689830314) for details. If rembg[gpu] doesn't work and you can't insta...

Basic usage or getting-started notes:
- text
- Choose **one** of the following backends based on your hardware:
- ### CPU support

- Source: https://github.com/danielgatis/rembg
- Extracted from upstream docs: https://raw.githubusercontent.com/danielgatis/rembg/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rembg-ai-background-removal-cli/)
