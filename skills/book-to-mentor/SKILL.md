---
name: "Book to Mentor"
slug: "book-to-mentor"
description: "Convert a book or long document into a reusable AI mentor with source-grounded lessons, guided practice, citations, and persistent learning records."
category: "Templates & Workflows"
framework: "Codex"
verification: listed
source: "https://github.com/gengwenhao/book-to-mentor"
---

# Book to Mentor

Book to Mentor turns a book or long-form document into a dedicated learning mentor instead of producing a one-off summary. The upstream project provides a tested Agent Skill, Python utilities, reusable templates, and installation metadata for Codex, Claude Code, OpenClaw, and other Agent Skills-compatible runtimes. It extracts and indexes source material, creates a scoped mentor skill, and supports short lessons, source-grounded explanations, guided exercises, review sessions, and persistent progress records. Use it when a learner wants to study from a specific PDF, EPUB, Markdown document, or text collection over time. The workflow keeps explanations tied to the supplied source and clearly labels interpretation, which makes it useful for technical books, professional training material, and structured self-study. Full scripts, documentation, privacy notes, and issue-based feedback are maintained in the upstream repository.

## Installation

### OpenClaw

```bash
clawhub install book-to-mentor
```

### Codex, Claude Code, Cursor, and compatible agents

```bash
npx skills add gengwenhao/book-to-mentor
```

### Claude Code marketplace

```bash
claude plugin marketplace add gengwenhao/book-to-mentor
claude plugin install book-to-mentor@gengwenhao-skills
```

## Example

Attach a book file and ask: “Turn this book into a mentor skill, then start with a 15-minute lesson and one practical exercise.”

## Links

- Source and documentation: https://github.com/gengwenhao/book-to-mentor
- Feedback: https://github.com/gengwenhao/book-to-mentor/issues
- Author on RedNote: 宇宙机吴彦祖, ID 292844431
