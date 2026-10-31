---
name: "Rent GPUs with the Ukiyo CLI"
slug: "rent-gpus-with-ukiyo-cli"
description: "Use when an agent must rent an on-demand GPU (RTX 4090, RTX 6000 Ada, A100), run a workload on it over SSH with the Ukiyo CLI, and terminate it within a spending limit."
verification: listed
source: "https://github.com/ukiyocompute/ukiyo-skill"
author: "ukiyocompute"
publisher_type: "company"
category: "Integrations & Connectors"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "ukiyocompute/ukiyo-cli"
---

# Rent GPUs with the Ukiyo CLI

This skill teaches an agent to run GPU workloads on Ukiyo, an on-demand GPU rental service, through the official Ukiyo CLI (`ukiyo`). Use it when a task needs a dedicated NVIDIA GPU for a bounded amount of time, for example a fine-tuning run, a batch inference job, a benchmark or a rendering task, and the user has authorized a budget.

The workflow is: sign up with explicit agreement to the current Terms (`ukiyo signup --accept-terms <version> --json`), have a person fund the account once with a hosted top-up link (`ukiyo topup link --amount 5 --json`), list live offers and prices (`ukiyo offers --json`), rent with an idempotency key so retries never create a second rental (`ukiyo rent --gpu RTX4090 --count 1 --wait --json`), run commands over SSH (`ukiyo exec <deployment-id> -- nvidia-smi`), and terminate (`ukiyo terminate <deployment-id> --json`), confirming the final state and charges. Rentals draw on the prepaid account balance and stop automatically when it runs low. The agent should stay within the user's task and budget, read the account's scoped key limits first, and never leave a GPU running after the work is done.

The canonical skill file, its SHA-256 and the CLI checksums are published by Ukiyo; see the source repository.

## Installation

### Ukiyo CLI (macOS, Linux, WSL; Node.js 22+)

```bash
curl -fsSLO https://u-kiyo.ai/releases/cli/0.2.5/install.sh
echo "53df716a4bf30db75f8d7cfa930b2dc6ec8005bf5c2b29fb69df1a5257a5e06e  install.sh" | shasum -a 256 -c -
sh install.sh
ukiyo --version
```

The installer then verifies the CLI release's SHA-256 and stops on a mismatch. Windows PowerShell steps are in https://github.com/ukiyocompute/ukiyo-cli.

### Skill file (manual install)

```bash
mkdir -p ~/.claude/skills/ukiyo-compute
curl -fsSL https://u-kiyo.ai/releases/skill/1.0.1/ukiyo-compute/SKILL.md -o ~/.claude/skills/ukiyo-compute/SKILL.md
echo "719fca36ec699aecd30f391c307703a9935aa56f510f8cc8803546f06c37fddf  $HOME/.claude/skills/ukiyo-compute/SKILL.md" | shasum -a 256 -c -
```

### Direct repo/manual install

```bash
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/skills/rent-gpus-with-ukiyo-cli ~/.agent-skills/rent-gpus-with-ukiyo-cli
```

Docs: https://docs.u-kiyo.ai/connect/skill · Contact: contact@u-kiyo.ai
