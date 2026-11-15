---
name: "Annotate Classical Chinese corpora with HanLP"
slug: "annotate-classical-chinese-corpora-with-hanlp"
description: "Produce reviewable token, lemma, POS and dependency annotations for Classical Chinese passages with HanLP’s dedicated Ancient Chinese model."
github_stars: 36524
verification: "security_reviewed"
source: "https://github.com/hankcs/HanLP"
author: "hankcs / HanLP contributors"
publisher_type: "community"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "hankcs/HanLP"
  github_stars: 36524
---

# Annotate Classical Chinese corpora with HanLP

Produce reviewable token, lemma, POS and dependency annotations for Classical Chinese passages with HanLP’s dedicated Ancient Chinese model.

## Prerequisites

Python, pip, HanLP 2.1.1, compatible PyTorch environment, upstream Ancient Chinese model resources; optional GPU

## Installation

Install or set up from the source-backed instructions:

Create an isolated Python environment; run python -m pip install hanlp==2.1.1 with a compatible PyTorch stack. Load hanlp.pretrained.mtl.KYOTO_EVAHAN_TOK_LEM_POS_UDEP_LZH; first load downloads model resources. Check model licensing before use and run the upstream two-sentence demo before processing operator data. No MCP server or hosted API is required.

- Source: https://github.com/hankcs/HanLP

## Documentation

- https://hanlp.hankcs.com/docs/api/hanlp/pretrained/mtl.html#hanlp.pretrained.mtl.KYOTO_EVAHAN_TOK_LEM_POS_UDEP_LZH

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/annotate-classical-chinese-corpora-with-hanlp/)
