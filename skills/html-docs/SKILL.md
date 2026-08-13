---
name: "HTML Docs"
slug: "html-docs"
description: "Turns folders, codebases, websites, PDFs, documents, and research topics into source-grounded HTML documents, deterministic narrated videos, or complete learning courses; also publishes and revises collaborative HTML pages through the HTML Docs CLI, REST API, and MCP server."
category: "Content Writing & SEO"
framework: "Multi-Framework"
verification: listed
source: "https://github.com/raunaqbn/html-docs-skill"
tool_ecosystem:
  github_repo: "raunaqbn/html-docs-skill"
  npm_package: "@html-docs/cli"
  license: "MIT"
  maintained: true
---

# HTML Docs

HTML Docs is an installable agent skill and open production toolkit for turning
a folder, codebase, website, PDF, document, pasted material, or research topic
into a polished HTML document, deterministic narrated explainer video, combined
document-and-video explanation, or source-grounded learning course. Use it when
an answer needs durable presentation, citations, visual explanation, narration,
or a reviewable artifact instead of chat alone. The skill guides Codex and
Claude Code through source capture, evidence records, responsive HTML design,
accessibility checks, deterministic scene timing, captions, rendering, and
private preview publication. The companion `@html-docs/cli` publishes static
HTML, installs an MCP server, and exposes API workflows for reading and updating
document regions, leaving inline comments, managing versions, and reacting to
collaborator feedback. Public publication remains an explicit user decision;
provider credentials and authored source projects stay local.

## Installation

Install the canonical upstream skill in Codex or Claude Code with the pinned
third-party `skills` installer:

```bash
npm exec --package=skills@1.5.7 -- skills add raunaqbn/html-docs-skill --skill html-docs -g
```

Or clone the MIT-licensed source and copy the skill directory into the skill
folder used by your agent runtime:

```bash
git clone https://github.com/raunaqbn/html-docs-skill.git
cp -R html-docs-skill/html-docs ~/.agent-skills/html-docs
```

Publish a standalone HTML page without installing the skill:

```bash
npx @html-docs/cli publish page.html
```

The public agent guide documents Codex, Claude Code, MCP, CLI, and REST API
workflows: https://www.html-docs.com/agents
