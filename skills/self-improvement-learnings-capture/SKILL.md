---
name: "Self-Improvement / Learnings Capture"
description: "Capture failures, corrections, and repeatable lessons so important operational knowledge persists across sessions."
category: "Templates & Workflows"
framework: "OpenClaw"
verification: security_reviewed
source: "https://github.com/pskoett/pskoett-ai-skills/tree/main/skills/self-improvement"
---

# Self-Improvement / Learnings Capture

Capture failures, corrections, and repeatable lessons so important operational knowledge persists across sessions.

## Overview

Self-Improvement / Learnings Capture is a workflow skill for turning one-off errors and corrections into durable operating knowledge. Instead of losing lessons between sessions, it helps store them in structured markdown files and promote recurring patterns into workspace guidance.

Best for

logging errors, corrections, and feature gaps into durable files

turning recurring mistakes into documented process improvements

maintaining operational memory inside OpenClaw workspaces

Install notes

Install the skill into an OpenClaw workspace with write access to memory and learning files. Optional hooks can be added later for deeper automation, but the core value is already there without them.

**Source:** self-improving-agent skill for OpenClaw workflows.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill self-improvement-learnings-capture
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill self-improvement-learnings-capture -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill self-improvement-learnings-capture -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill self-improvement-learnings-capture -a codex
```

### OpenClaw

```bash
clawhub install self-improvement-learnings-capture
```

## Source

- Marketplace: https://agentskillexchange.com/skills/self-improvement-learnings-capture/
