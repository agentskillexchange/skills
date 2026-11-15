---
name: "Parse agent-ready PDFs and document images with MonkeyOCR"
slug: "parse-agent-ready-pdfs-and-document-images-with-monkeyocr"
description: "Run MonkeyOCR over PDFs, scanned pages, formulas, and tables to produce structured Markdown/text that downstream agents can ingest and reason over."
github_stars: 6595
verification: "security_reviewed"
source: "https://github.com/Yuliang-Liu/MonkeyOCR"
author: "Yuliang-Liu"
publisher_type: "individual"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "Yuliang-Liu/MonkeyOCR"
  github_stars: 6595
---

# Parse agent-ready PDFs and document images with MonkeyOCR

Run MonkeyOCR over PDFs, scanned pages, formulas, and tables to produce structured Markdown/text that downstream agents can ingest and reason over.

## Prerequisites

Python environment, CUDA-capable GPU or supported inference backend, Hugging Face Hub or ModelScope access for model weights, PDF or image documents to parse

## Installation

Use the upstream install or setup path that matches your environment:
- pip install huggingface_hub
- pip install modelscope
- docker compose build monkeyocr
- docker pull zenosai/monkeyocr:260304

Requirements and caveats from upstream:
- python
- python tools/download_model.py -n MonkeyOCR-pro-3B # or MonkeyOCR-pro-1.2B, MonkeyOCR
- python tools/download_model.py -t modelscope -n MonkeyOCR-pro-3B # or MonkeyOCR-pro-1.2B, MonkeyOCR

Basic usage or getting-started notes:
- [![Youtube](https://img.shields.io/badge/Run-dots.mocr-red)](https://www.youtube.com/watch?v=BxH5KD5lDSM)
- Due to the limited types of GPUs available to us, we may not be able to provide highly accurate hardware specifications. We've tested the model on GPUs such as the 3090, 4090, A6000, H800, A100, and even the 4060 with...
- See the [installation guide](https://github.com/Yuliang-Liu/MonkeyOCR/blob/main/docs/install_cuda_pp.md#install-with-cuda-support) to set up your environment.

- Source: https://github.com/Yuliang-Liu/MonkeyOCR
- Extracted from upstream docs: https://raw.githubusercontent.com/Yuliang-Liu/MonkeyOCR/HEAD/README.md

## Documentation

- https://github.com/Yuliang-Liu/MonkeyOCR

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parse-agent-ready-pdfs-and-document-images-with-monkeyocr/)
