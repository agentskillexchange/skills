---
name: "agent-swarm-build: replay a site's build as a 60 fps video"
slug: "agent-swarm-build"
description: "After an agent builds a site, a swarm of agents rebuilds the finished site on screen, element by element, as a live replay or an exact 60 fps MP4 with sound."
category: "Image & Creative Automation"
framework: "Claude Code"
verification: listed
source: "https://github.com/seanaiux/uberdesigner-skills/tree/main/skills/agent-swarm-build"
---

# agent-swarm-build: replay a site's build as a 60 fps video

agent-swarm-build is an agent skill from uberdesigner for showing how a website was made. After your agent has built a site, a swarm of agents rebuilds the finished site on screen, element by element, as a live replay in the browser or as a frame-exact 60 fps MP4 with a sound track. It is meant for build-in-public posts, demos and walkthroughs where you want the construction itself to be the content.

Use it after a build by asking "show me how it was built" or for a build video. Rendering the video needs Node.js and ffmpeg on your computer. The skill is a `SKILL.md` with bundled scripts and sound assets, follows the open agent-skills format, and is licensed Apache-2.0. It ships in the uberdesigner-skills repository together with a Claude Code plugin marketplace entry and a Gemini CLI extension.

## Installation

### Claude Code plugin

```bash
/plugin marketplace add seanaiux/uberdesigner-skills
/plugin install uberdesigner@uberdesigner
```

### Any agent, with the skills CLI

```bash
npx skills add seanaiux/uberdesigner-skills
```

### Direct repo/manual install

Copy `skills/agent-swarm-build` from https://github.com/seanaiux/uberdesigner-skills into your agent's skills folder (Claude Code: `~/.claude/skills/`).
