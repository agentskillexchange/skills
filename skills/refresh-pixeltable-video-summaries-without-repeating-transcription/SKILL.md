---
name: "Refresh Pixeltable video summaries without repeating transcription"
slug: "refresh-pixeltable-video-summaries-without-repeating-transcription"
description: "Review a summary-prompt change, recompute only the summary and its search dependents, and verify that stored audio and transcripts stay unchanged."
github_stars: 1662
verification: "security_reviewed"
source: "https://github.com/pixeltable/pixeltable"
author: "Pixeltable"
publisher_type: "organization"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "pixeltable/pixeltable"
  github_stars: 1662
---

# Refresh Pixeltable video summaries without repeating transcription

Review a summary-prompt change, recompute only the summary and its search dependents, and verify that stored audio and transcripts stay unchanged.

## Prerequisites

Python 3.11+, Pixeltable CLI 0.7.24, existing app.py and local video table, configured model provider, shell and HTTP client

## Installation

Install or set up from the source-backed instructions:

Use Python 3.11+ and an isolated environment. Install pip install 'pixeltable[serve]==0.7.24' openai. Work in an existing local pxt project with the documented Videos model, summary computed column and embedding index. Supply the authorized provider credential through the environment; inspect pxt schema --help, pxt service --help and pxt recompute --help against this installed version. This workflow requires no Cloud trial or hosted account.

- Source: https://github.com/pixeltable/pixeltable

## Documentation

- https://github.com/pixeltable/pixeltable#change-the-summary-without-redoing-transcription

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/refresh-pixeltable-video-summaries-without-repeating-transcription/)
