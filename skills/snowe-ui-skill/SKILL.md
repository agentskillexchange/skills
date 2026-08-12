---
name: "Snowe UI Skill"
slug: "snowe-ui-skill"
description: "Architecture-first UI/UX design skill for Codex that helps agents reason from product truth, user journeys, causal design decisions, art direction, interaction, responsive behavior, imagery, iconography, and motion before implementation, then validate the result through rendered browser critique."
category: "Developer Tools"
framework: "Codex"
verification: "listed"
source: "https://github.com/What0ff/snowe-ui-skill"
---

# Snowe UI Skill

Snowe is an architecture-first UI/UX design skill for Codex and compatible SKILL.md runtimes.

Use it when a coding agent needs to design, redesign, or critically review a web, mobile, or desktop product without jumping directly from a brief into a familiar layout or visual recipe.

Snowe works from product truth and the actual user journey, keeps high-leverage decisions open until evidence closes them, compares materially different experience directions, and records important choices causally:

`driver → design move → expected consequence → evidence → risk → revisit trigger`

The skill covers experience architecture, navigation, art direction, typography, color and materials, imagery, iconography, custom graphics, motion, interaction, accessibility, responsive transformation, and rendered browser evaluation.

It explicitly allows outcomes such as no imagery, no custom asset, or no animation when those choices better serve the product.

Snowe is not a category-to-style generator or landing-page recipe system.

## Installation

### Codex — Windows

```powershell
git clone https://github.com/What0ff/snowe-ui-skill.git

Copy-Item -Recurse -Force `
  .\snowe-ui-skill\skill\snowe-ui-skill `
  "$env:USERPROFILE\.codex\skills\snowe-ui-skill"
