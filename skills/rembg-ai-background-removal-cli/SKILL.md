---
name: "rembg AI Background Removal CLI and Python Library"
description: "rembg is a Python tool for automatic image background removal powered by AI models like U2-Net and SAM. It works as a CLI, Python library, HTTP server, or Docker container, supporting CPU and GPU acceleration for batch processing of images and video frames."
category: "Image &amp; Creative Automation"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/danielgatis/rembg"
tool_ecosystem:
  github_repo: "danielgatis/rembg"
  github_stars: 22400
  license: "MIT"
---
# rembg AI Background Removal CLI and Python Library

rembg is a Python tool for automatic image background removal powered by AI models like U2-Net and SAM. It works as a CLI, Python library, HTTP server, or Docker container, supporting CPU and GPU acceleration for batch processing of images and video frames.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill rembg-ai-background-removal-cli
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill rembg-ai-background-removal-cli -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill rembg-ai-background-removal-cli -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill rembg-ai-background-removal-cli -a codex
```

### OpenClaw

```bash
clawhub install rembg-ai-background-removal-cli
```

## Details

rembg is a specialized image processing tool built by Daniel Gatis that removes backgrounds from images using deep learning models. The tool leverages ONNX Runtime to run pre-trained neural networks including U2-Net, U2-Net-P, and Segment Anything Model (SAM) for precise foreground-background segmentation.

How It Works
rembg accepts images through multiple interfaces: a command-line tool for single files and batch folders, a Python API for programmatic integration, an HTTP server with REST endpoints, and a binary stream mode compatible with FFmpeg pipelines. The tool processes each image through a selected neural network model that generates a segmentation mask, which is then applied to produce a transparent-background PNG output.

Core Features and CLI Usage
The CLI supports four subcommands: rembg i for single files, rembg p for batch folder processing with watch mode, rembg s to start an HTTP server with optional Gradio UI, and rembg b for binary stream input from tools like FFmpeg. Users can select specific models, apply alpha matting for refined edges, output just the mask, or pass custom ONNX models.

Model Selection
rembg ships with multiple models suited to different tasks: u2net (general purpose, 176MB), u2netp (lightweight, 4MB), isnet-general-use (high accuracy), sam (interactive point-based segmentation), and birefnet variants for high-resolution images. Custom ONNX models can be loaded by path.

Integration Points
As a Python library, rembg integrates with PIL/Pillow and NumPy workflows. The HTTP server mode exposes a REST API at /api/remove accepting both URL parameters and file uploads. The FFmpeg binary stream mode enables frame-by-frame video background removal. rembg supports CPU, NVIDIA CUDA, and AMD ROCm backends for hardware acceleration.

Installation
Install via pip: pip install "rembg[cpu,cli]" for CPU support, or pip install "rembg[gpu,cli]" for NVIDIA GPU acceleration. Requires Python 3.11 or later. Docker images are also available for containerized deployments.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rembg-ai-background-removal-cli/)
