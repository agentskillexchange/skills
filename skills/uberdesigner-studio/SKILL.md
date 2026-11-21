---
name: "uberdesigner studio: edit a site one part at a time"
slug: "uberdesigner-studio"
description: "Maps a website into parts and installs a localhost editor where each part can be inspected, tweaked live, or changed by Claude on its own, with history and restore. Works on Vite + React projects and plain HTML sites."
category: "Developer Tools"
framework: "Claude Code"
verification: listed
source: "https://github.com/bogdan239/uberdesigner-studio"
---

# uberdesigner studio: edit a site one part at a time

uberdesigner studio is a Claude Code skill that reads a website, from its build prompt, its code or both, and maps it into parts: headlines, buttons, photos and sections, each listed as a layer like in a design file. It then installs an editor that runs on localhost, next to the site. Click a part to select it, adjust sizes, colours, fonts, spacing, timing and easing with sliders and pickers, or type over text directly on the page. Saving writes the values back into your own source files.

When a change needs judgement, ask Claude to change that one part. The request carries only that part's code rather than the whole project, which the authors report uses 3 to 5 times fewer tokens. Each result arrives as a card you can keep, undo or ask again, and every change is stored as a version in History so you can restore an earlier state.

It supports Vite + React projects, uberdesigner templates, and sites with no build step such as a single HTML file with inline CSS and JS. It needs Claude Code and Node.js. The skill is AGPL-3.0 licensed and maintained by uberdesigner.

## Installation

### Claude Code

```bash
git clone https://github.com/bogdan239/uberdesigner-studio ~/.claude/skills/uberdesigner-studio
```

Then open the site's folder in Claude Code and say "set up uberdesigner studio".

### Direct repo/manual install

Copy this listing's directory only if you want the catalog entry; the skill itself lives in the upstream repository linked in `source`.
