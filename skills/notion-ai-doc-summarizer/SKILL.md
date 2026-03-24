---
name: "Notion AI Document Summarizer & Action Item Extractor"
description: "Uses the Notion SDK and Notion AI’s /v1/pages and /v1/blocks/children endpoints to retrieve page content and invoke AI-powered summarization. Extracted action items are appended as a structured database entry via databases.query and pages.create."
category: "Calendar, Email & Productivity"
framework: "Claude Code"
verification: security_reviewed
rating: 4.6
reviews: 19
creator: "Chris Lee"
creator_handle: "@chrislee"
creator_verified: false
source: "https://agentskillexchange.com/skills/notion-ai-doc-summarizer/"
---
# Notion AI Document Summarizer & Action Item Extractor

Uses the Notion SDK and Notion AI’s /v1/pages and /v1/blocks/children endpoints to retrieve page content and invoke AI-powered summarization. Extracted action items are appended as a structured database entry via databases.query and pages.create.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill notion-ai-doc-summarizer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill notion-ai-doc-summarizer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill notion-ai-doc-summarizer -a cursor
```

### OpenClaw

```bash
clawhub install notion-ai-doc-summarizer
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill notion-ai-doc-summarizer -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Calendar, Email & Productivity |
| Framework | Claude Code |
| Verification | Security Reviewed |
| Rating | 4.6/5 (19 reviews) |

## Creator

**Chris Lee**
- Profile: [@chrislee](https://agentskillexchange.com/browse-skills/?creator=chrislee)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/notion-ai-doc-summarizer/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
