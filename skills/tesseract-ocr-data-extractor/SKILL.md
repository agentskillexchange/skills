---
title: "Tesseract OCR Data Extractor"
description: "Extracts structured data from scanned documents using Tesseract OCR engine with LSTM models. Supports table detection via OpenCV contour analysis and outputs to CSV, JSON, or Pandas DataFrames."
verification: "security_reviewed"
source: "https://github.com/tesseract-ocr/tesseract"
author: "Tesseract OCR"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "tesseract-ocr/tesseract"
  github_stars: 73629
---

# Tesseract OCR Data Extractor

Extracts structured data from scanned documents using Tesseract OCR engine with LSTM models. Supports table detection via OpenCV contour analysis and outputs to CSV, JSON, or Pandas DataFrames.

## Prerequisites

Tesseract OCR, OpenCV

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
sudo apt install tesseract-ocr
```

## Documentation

- https://tesseract-ocr.github.io/tessdoc/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tesseract-ocr-data-extractor/)
