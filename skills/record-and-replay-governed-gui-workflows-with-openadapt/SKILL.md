---
name: "Record and replay governed GUI workflows with OpenAdapt"
slug: "record-and-replay-governed-gui-workflows-with-openadapt"
description: "Use OpenAdapt to demonstrate a repeated browser or GUI workflow once, compile it into a deterministic replay bundle, and certify or halt runs with reviewable reports when interfaces drift."
github_stars: 1645
verification: "security_reviewed"
source: "https://github.com/OpenAdaptAI/OpenAdapt"
author: "OpenAdapt contributors"
publisher_type: "open_source"
category: "Browser Automation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "OpenAdaptAI/OpenAdapt"
  github_stars: 1645
---

# Record and replay governed GUI workflows with OpenAdapt

Use OpenAdapt to demonstrate a repeated browser or GUI workflow once, compile it into a deterministic replay bundle, and certify or halt runs with reviewable reports when interfaces drift.

## Prerequisites

OpenAdapt Python package, Python 3.10+, openadapt flow CLI, browser target or supported GUI environment, optional capture extras, certification policies, and sanitized workflow artifacts for hosted use

## Installation

Use the upstream install or setup path that matches your environment:
- pip install openadapt installs the launcher and the compiler, exposed as
- pip install openadapt # CLI + demonstration compiler (openadapt flow …)
- pip install openadapt[capture] # + native GUI capture/recording
- pip install openadapt[privacy] # + Presidio-backed PII/PHI scrubbing

Requirements and caveats from upstream:
- [![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
- available on headless systems. This launcher requires openadapt-flow>=1.7.0,<2

Basic usage or getting-started notes:
- The flagship compiler ships in the base install, so openadapt flow … works
- right after pip install openadapt. Install openadapt-flow[hosted] when you
- want OS-keychain token storage; environment-based token configuration remains

- Source: https://github.com/OpenAdaptAI/OpenAdapt
- Extracted from upstream docs: https://raw.githubusercontent.com/OpenAdaptAI/OpenAdapt/HEAD/README.md

## Documentation

- https://docs.openadapt.ai

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/record-and-replay-governed-gui-workflows-with-openadapt/)
