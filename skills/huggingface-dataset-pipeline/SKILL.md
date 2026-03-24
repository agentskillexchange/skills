---
name: "Hugging Face Dataset Pipeline"
description: "Fetches and preprocesses datasets from Hugging Face Hub via the datasets library and Hub REST API. Applies tokenization using AutoTokenizer and pushes processed splits back to a private Hub repo with push_to_hub(). Tracks dataset versions using the Hub dataset viewer API."
category: "Data Extraction & Transformation"
framework: "ChatGPT Agents"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/huggingface-dataset-pipeline/"
---

# Hugging Face Dataset Pipeline

Fetches and preprocesses datasets from Hugging Face Hub via the datasets library and Hub REST API. Applies tokenization using AutoTokenizer and pushes processed splits back to a private Hub repo with push_to_hub(). Tracks dataset versions using the Hub dataset viewer API.

## Overview

Fetches and preprocesses datasets from Hugging Face Hub via the datasets library and Hub REST API. Applies tokenization using AutoTokenizer and pushes processed splits back to a private Hub repo with push_to_hub(). Tracks dataset versions using the Hub dataset viewer API.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill huggingface-dataset-pipeline
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill huggingface-dataset-pipeline -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill huggingface-dataset-pipeline -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill huggingface-dataset-pipeline -a codex
```

### OpenClaw

```bash
clawhub install huggingface-dataset-pipeline
```

## Source

- Marketplace: https://agentskillexchange.com/skills/huggingface-dataset-pipeline/
