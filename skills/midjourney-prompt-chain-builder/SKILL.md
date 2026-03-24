---
name: "Midjourney Prompt Chain Builder"
description: "Constructs and manages Midjourney prompt chains for iterative image refinement. Automates parameter tuning for –ar, –v, –style, and –chaos flags across generation sequences."
category: "42"
framework: "25"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/midjourney-prompt-chain-builder/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "midjourney"  # from ase_tool_match
---

# Midjourney Prompt Chain Builder

Constructs and manages Midjourney prompt chains for iterative image refinement. Automates parameter tuning for –ar, –v, –style, and –chaos flags across generation sequences.

## Overview

The Midjourney Prompt Chain Builder automates iterative image generation workflows by constructing sophisticated prompt chains with systematic parameter variations. It manages prompt composition by combining subject descriptions, style modifiers, lighting directives, and Midjourney-specific parameters including –ar for aspect ratio, –v for model version, –style for aesthetic presets, –chaos for variation randomness, and –stylize for artistic intensity. The skill builds generation sequences where each step refines the previous output, using –seed values from successful generations to maintain consistency while varying specific prompt elements. It supports multi-prompt syntax with :: weight separators for precise concept blending and negative prompting with –no flags. The skill generates parameter sweep matrices that systematically explore combinations of –stylize (0-1000), –chaos (0-100), and –weird (0-3000) values to discover optimal aesthetic configurations for a given concept. Prompt templates are stored with variable placeholders that can be batch-populated from CSV data for mass generation campaigns. The skill tracks prompt-to-output quality scores for iterative refinement of prompt engineering strategies.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill midjourney-prompt-chain-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill midjourney-prompt-chain-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill midjourney-prompt-chain-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill midjourney-prompt-chain-builder -a codex
```

### OpenClaw

```bash
clawhub install midjourney-prompt-chain-builder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/midjourney-prompt-chain-builder/
