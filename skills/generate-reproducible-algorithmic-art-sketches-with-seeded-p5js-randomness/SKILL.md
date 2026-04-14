---
title: "Generate reproducible algorithmic art sketches with seeded p5.js randomness"
description: "Use the Anthropic algorithmic-art skill when an agent should turn a creative brief into executable generative art, not into a static image prompt or a generic design suggestion. It directs the agent toward a repeatable p5.js workflow with seeded randomness, parameter controls, and an explicit creative philosophy."
verification: security_reviewed
source: "https://github.com/anthropics/skills/tree/main/skills/algorithmic-art"
category:
  - "Image &amp; Creative Automation"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-reproducible-algorithmic-art-sketches-with-seeded-p5js-randomness/)
