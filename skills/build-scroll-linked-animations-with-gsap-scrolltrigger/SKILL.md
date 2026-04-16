---
title: "Build scroll-linked animations with GSAP ScrollTrigger"
description: "Use Greensock’s official gsap-scrolltrigger skill to plan, implement, and debug scroll-linked animations, pinned sections, and scrubbed storytelling without guessing at plugin setup. The agent should reach for this when a user needs a bounded scroll-animation workflow, not when they just need the GSAP product page."
verification: "security_reviewed"
source: "https://github.com/greensock/gsap-skills/tree/main/skills/gsap-scrolltrigger"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
---

# Build scroll-linked animations with GSAP ScrollTrigger

Tool name: GSAP ScrollTrigger, from Greensock’s official gsap-skills repository.

This entry is skill-shaped because it describes a concrete operator task: building and debugging scroll-linked animation behavior. The agent is not acting as a generic GSAP explainer or catalog card. It is being invoked to wire up ScrollTrigger correctly, choose start and end points, register the plugin once, decide when to pin, scrub, batch, or proxy custom scrollers, and resolve the usual breakages that show up in real projects.

Use this when a user says they need parallax, pinned storytelling sections, scroll-synced timelines, ScrollTrigger markers, smooth-scroll integration, or a page section that animates as the viewport moves. This is the right skill when the user wants an agent to implement or repair a scroll-animation workflow. It is not the right entry for learning GSAP in general, buying a license, browsing the docs, or listing animation libraries.

The scope boundary matters. ScrollTrigger is only the scroll-linked animation playbook inside the broader GSAP ecosystem. The agent should stay focused on scroll triggers, start and end calculations, scrub behavior, pin spacing, container animation, scrollerProxy integrations, and cleanup. If the task is general tween authoring, timeline architecture, React hook cleanup, or plugin licensing, that belongs elsewhere.

Integration points include frontend JavaScript projects that already use GSAP, sites that need ScrollTrigger registered and configured, React or other framework builds that need lifecycle-safe setup, and custom smooth-scroll stacks that need scrollerProxy() coordination. Source-backed evidence is strong: official repo, official docs references inside the skill, a license file, and active recent commits.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-scroll-linked-animations-with-gsap-scrolltrigger/)
