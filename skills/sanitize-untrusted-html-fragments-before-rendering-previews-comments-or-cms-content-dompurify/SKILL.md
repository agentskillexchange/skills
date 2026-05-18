---
name: "Sanitize untrusted HTML fragments before rendering previews, comments, or CMS content with DOMPurify"
slug: "sanitize-untrusted-html-fragments-before-rendering-previews-comments-or-cms-content-dompurify"
description: "Use DOMPurify when an agent must accept HTML from users, rich text editors, imports, or model output but cannot safely render it as-is. The skill strips dangerous markup and unsafe attributes before the content is shown in previews, stored in CMS fields, or embedded in downstream pages."
github_stars: 16854
verification: "security_reviewed"
source: "https://github.com/cure53/DOMPurify"
author: "Cure53"
publisher_type: "user"
category: "Security & Verification"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "cure53/DOMPurify"
  github_stars: 16854
---

# Sanitize untrusted HTML fragments before rendering previews, comments, or CMS content with DOMPurify

Use DOMPurify when an agent must accept HTML from users, rich text editors, imports, or model output but cannot safely render it as-is. The skill strips dangerous markup and unsafe attributes before the content is shown in previews, stored in CMS fields, or embedded in downstream pages.

## Prerequisites

Node.js or a JavaScript runtime with DOM support

## Installation

Use the upstream install or setup path that matches your environment:
- npm install dompurify
- npm install jsdom
- npm install isomorphic-dompurify

Requirements and caveats from upstream:
- Our automated tests cover 9 browser/OS combinations (Chromium, Firefox, and WebKit across Ubuntu, macOS, and Windows) on every push, plus Node.js v20, v22, v24, v25 and v26 running DOMPurify on [jsdom](https://github....
- DOMPurify technically also works server-side with Node.js. Our support strives to follow the [Node.js release cycle](https://nodejs.org/en/about/previous-releases).
- Running DOMPurify on the server requires a DOM to be present, which is probably no surprise. Usually, [jsdom](https://github.com/jsdom/jsdom) is the tool of choice and we **strongly recommend** to use the latest versi...

Basic usage or getting-started notes:
- If you have problems making it work in your specific setup, consider looking at the amazing [isomorphic-dompurify](https://github.com/kkomelin/isomorphic-dompurify) project which solves lots of problems people might r...
- Note that in order to create a policy in trustedTypes using DOMPurify, RETURN_TRUSTED_TYPE: false is required, as createHTML expects a normal string, not TrustedHTML. The example below shows this.
- // be careful please, this mode is not recommended for production usage.

- Source: https://github.com/cure53/DOMPurify
- Extracted from upstream docs: https://raw.githubusercontent.com/cure53/DOMPurify/HEAD/README.md

## Documentation

- https://github.com/cure53/DOMPurify#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sanitize-untrusted-html-fragments-before-rendering-previews-comments-or-cms-content-dompurify/)
