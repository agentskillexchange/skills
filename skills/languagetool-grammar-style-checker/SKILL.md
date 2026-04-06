---
name: LanguageTool Grammar and Style Checker
description: Check grammar, style, and spelling across 25+ languages with LanguageTool.
  This open-source proofreading engine can run as a local Java server or via its public
  API, providing detailed error reports with correction suggestions for any text content.
category: "Content Writing &amp; SEO"
framework: Multi-Framework
verification: security_reviewed
source: "https://github.com/languagetool-org/languagetool"
tool_ecosystem:
  github_repo: "https://github.com/languagetool-org/languagetool"
  github_stars: 14238
  license: LGPL-2.1
---
# LanguageTool Grammar and Style Checker

Check grammar, style, and spelling across 25+ languages with LanguageTool. This open-source proofreading engine can run as a local Java server or via its public API, providing detailed error reports with correction suggestions for any text content.

LanguageTool is an open-source grammar, style, and spell-checking engine that supports over 25 languages including English, German, French, Spanish, Portuguese, Dutch, Polish, and Russian. Written in Java, it can run as a standalone server, be embedded as a library, or accessed through its public REST API at api.languagetool.org.

The tool applies thousands of pattern-based and AI-powered rules to detect errors that simple spell checkers miss: subject-verb agreement, confused words (their/there/they’re), redundant phrases, passive voice overuse, punctuation errors, and style inconsistencies. Each detected issue includes the error position, a human-readable explanation, and one or more suggested corrections, making automated fixing straightforward.

For local deployment, LanguageTool runs as an HTTP server (java -jar languagetool-server.jar --port 8081) that accepts POST requests with text and returns JSON-formatted error reports. This self-hosted approach keeps content private and avoids API rate limits. The public API is available for lower-volume use with a free tier.

AI agents can integrate LanguageTool as a proofreading step in content generation pipelines. After an LLM drafts a blog post, email, or documentation page, LanguageTool scans the output for grammatical errors, style issues, and typographical mistakes that language models frequently produce. The structured JSON response allows agents to programmatically apply corrections or flag issues for human review.

Client libraries exist for Python (language_tool_python), Node.js, and other languages, simplifying integration. The tool also provides browser extensions, LibreOffice integration, and editor plugins, but its REST API is the primary interface for agent-based automation workflows.

LanguageTool’s rule system is extensible through XML-based pattern definitions and Java rule classes, allowing teams to add organization-specific terminology checks or industry jargon validation. The project maintains active development with frequent releases addressing new language rules and accuracy improvements.

Source: github.com/languagetool-org/languagetool — LGPL-2.1 licensed, 14,000+ GitHub stars, 1,400+ forks, actively maintained.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill languagetool-grammar-style-checker
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill languagetool-grammar-style-checker -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill languagetool-grammar-style-checker -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill languagetool-grammar-style-checker -a codex
```

### OpenClaw

```bash
clawhub install languagetool-grammar-style-checker
```


## Source

- [GitHub](https://github.com/languagetool-org/languagetool)
