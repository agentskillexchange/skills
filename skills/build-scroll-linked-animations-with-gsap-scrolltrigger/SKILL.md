---
name: "Build scroll-linked animations with GSAP ScrollTrigger"
description: "Use Greensock's official gsap-scrolltrigger skill to plan, implement, and debug scroll-linked animations, pinned sections, and scrubbed storytelling without guessing at plugin setup. The agent should reach for this when a user needs a bounded scroll-animation workflow, not when they just need the GSAP product page."
verification: listed
source: "https://github.com/greensock/gsap-skills/tree/main/skills/gsap-scrolltrigger"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
---

# Build scroll-linked animations with GSAP ScrollTrigger

Tool name: GSAP ScrollTrigger, from Greensock's official gsap-skills repository.
This entry is skill-shaped because it describes a concrete operator task: building and debugging scroll-linked animation behavior. The agent is not acting as a generic GSAP explainer or catalog card. It is being invoked to wire up ScrollTrigger correctly, choose start and end points, register the plugin once, decide when to pin, scrub, batch, or proxy custom scrollers, and resolve the usual breakages that show up in real projects.
Use this when a user says they need parallax, pinned storytelling sections, scroll-synced timelines, ScrollTrigger markers, smooth-scroll integration, or a page section that animates as the viewport moves. This is the right skill when the user wants an agent to implement or repair a scroll-animation workflow. It is not the right entry for learning GSAP in general, buying a license, browsing the docs, or listing animation libraries.
The scope boundary matters. ScrollTrigger is only the scroll-linked animation playbook inside the broader GSAP ecosystem. The agent should stay focused on scroll triggers, start and end calculations, scrub behavior, pin spacing, container animation, scrollerProxy integrations, and cleanup. If the task is general tween authoring, timeline architecture, React hook cleanup, or plugin licensing, that belongs elsewhere.
Integration points include frontend JavaScript projects that already use GSAP, sites that need ScrollTrigger registered and configured, React or other framework builds that need lifecycle-safe setup, and custom smooth-scroll stacks that need scrollerProxy() coordination. Source-backed evidence is strong: official repo, official docs references inside the skill, a license file, and active recent commits.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-scroll-linked-animations-with-gsap-scrolltrigger/)
