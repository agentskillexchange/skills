---
name: "Scan LLM systems for jailbreaks, prompt injections, and unsafe behaviors with garak"
slug: "scan-llm-systems-for-jailbreaks-prompt-injections-and-unsafe-behaviors-with-garak"
description: "Probe a model or agent stack with adversarial test suites so safety failures show up before deployment or review."
github_stars: 7549
verification: "listed"
source: "https://github.com/NVIDIA/garak"
author: "NVIDIA"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "NVIDIA/garak"
  github_stars: 7549
---

# Scan LLM systems for jailbreaks, prompt injections, and unsafe behaviors with garak

Probe a model or agent stack with adversarial test suites so safety failures show up before deployment or review.

## Prerequisites

Python 3.10+, target LLM or API credentials, command line access

## Installation

Use the upstream install or setup path that matches your environment:
- ### Standard install with pip
- python -m pip install -U garak
- python -m pip install -U git+https://github.com/NVIDIA/garak.git@main
- conda create --name garak "python>=3.10,<=3.12"

Requirements and caveats from upstream:
- [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/garak)](https://pypi.org/project/garak)
- For testing. This always generates the empty string, using the test.Blank generator. Will be marked as failing for any tests that *require* an output, e.g. those that make contentious claims and expect the model to re...

Basic usage or getting-started notes:
- garak is a command-line tool. It's developed in Linux and OSX.
- Just grab it from PyPI and you should be good to go:
- The standard pip version of garak is updated periodically. To get a fresher version from GitHub, try:

- Source: https://github.com/NVIDIA/garak
- Extracted from upstream docs: https://raw.githubusercontent.com/NVIDIA/garak/HEAD/README.md

## Documentation

- https://garak.ai

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-llm-systems-for-jailbreaks-prompt-injections-and-unsafe-behaviors-with-garak/)
