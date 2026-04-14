---
title: "Inline CSS into HTML emails before delivery across mail clients with Juice"
description: "Use Juice when an agent already has finished HTML and needs it transformed into email-safe output before sending, archiving, or handing off to another system. The skill inlines stylesheet rules into element style attributes so downstream mail clients and embedded contexts keep the intended presentation without manual cleanup."
verification: security_reviewed
source: "https://github.com/Automattic/juice"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "Automattic/juice"
  github_stars: 3245
---

# Inline CSS into HTML emails before delivery across mail clients with Juice

Tool: Juice is an open source Node.js package from Automattic that inlines CSS stylesheets into HTML. This skill turns that capability into a narrow agent workflow: take an existing HTML email or embeddable fragment, resolve the stylesheet rules that matter, and emit a version that is much safer to send through mail clients or third-party renderers that ignore head-level CSS.

What the agent does: it receives HTML plus CSS, runs Juice, and returns transformed HTML with the important styling moved into inline style attributes. That is useful when an agent is preparing campaign emails, transactional notifications, generated reports, or archived email copies for systems that strip or inconsistently apply normal stylesheets.

When to use it: invoke this instead of using the tool as a generic package listing when the agent’s job is specifically to harden already-authored HTML for email delivery or constrained embedding. The trigger is not “I need an email framework.” The trigger is “I already have HTML and need the CSS inlined before I ship it.”

Scope boundary: this is not an email design system, template authoring framework, or sending platform. It does not write the copy, choose recipients, or manage campaigns. It only converts stylesheet-driven HTML into inline-styled output.

Integration points: Node.js pipelines, CMS export flows, notification workers, email preview checks, and post-processing steps after template rendering. Upstream evidence is strong: official GitHub repo, npm package, MIT license, tagged releases, and active maintenance.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inline-css-into-html-emails-before-delivery-across-mail-clients-juice/)
