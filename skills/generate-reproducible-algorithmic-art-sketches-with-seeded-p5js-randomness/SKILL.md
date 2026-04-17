---
title: "Generate reproducible algorithmic art sketches with seeded p5.js randomness"
description: "The upstream tool is Anthropic’s algorithmic-art skill from the anthropics/skills repository. The agent’s job is unusually specific: create original generative art systems in p5.js, grounded in a defined algorithmic philosophy, then implement them as reproducible sketches with seeds and interactive parameters. In practice that means the agent does more than brainstorm aesthetics. It frames a computational art direction, translates that into code, and produces a sketch where reruns are intentional rather than accidental.\nThis should be invoked when a user wants coded art, generative visuals, flow fields, particle systems, or other algorithmic compositions. It is the right tool when the user needs executable creative output that can be tuned, replayed, and iterated on, especially when a normal product workflow would stop at a static mockup or image prompt. The skill is useful for artists, demo builders, creative coders, and anyone who wants the agent to make a working sketch instead of just describing one.\nThe scope boundary keeps this from collapsing into a plain product listing. This is not a card for p5.js itself, not a gallery site, and not a generic image model. The value is the bounded workflow: establish the creative system, keep randomness seeded, expose parameters cleanly, and ship runnable code. Integration points include p5.js, HTML viewers, parameter controls, seeded random and noise functions, and iterative testing of generative behavior."
verification: security_reviewed
source: "https://github.com/anthropics/skills/tree/main/skills/algorithmic-art"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "anthropics/skills"
  github_stars: 116918
---

# Generate reproducible algorithmic art sketches with seeded p5.js randomness

The upstream tool is Anthropic’s algorithmic-art skill from the anthropics/skills repository. The agent’s job is unusually specific: create original generative art systems in p5.js, grounded in a defined algorithmic philosophy, then implement them as reproducible sketches with seeds and interactive parameters. In practice that means the agent does more than brainstorm aesthetics. It frames a computational art direction, translates that into code, and produces a sketch where reruns are intentional rather than accidental.
This should be invoked when a user wants coded art, generative visuals, flow fields, particle systems, or other algorithmic compositions. It is the right tool when the user needs executable creative output that can be tuned, replayed, and iterated on, especially when a normal product workflow would stop at a static mockup or image prompt. The skill is useful for artists, demo builders, creative coders, and anyone who wants the agent to make a working sketch instead of just describing one.
The scope boundary keeps this from collapsing into a plain product listing. This is not a card for p5.js itself, not a gallery site, and not a generic image model. The value is the bounded workflow: establish the creative system, keep randomness seeded, expose parameters cleanly, and ship runnable code. Integration points include p5.js, HTML viewers, parameter controls, seeded random and noise functions, and iterative testing of generative behavior.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/generate-reproducible-algorithmic-art-sketches-with-seeded-p5js-randomness
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/generate-reproducible-algorithmic-art-sketches-with-seeded-p5js-randomness` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-reproducible-algorithmic-art-sketches-with-seeded-p5js-randomness/)
