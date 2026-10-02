---
name: "Pangolinfo AI SERP"
slug: "pangolinfo-ai-serp"
description: "Retrieve structured Google SERP and AI Overviews, run AI Mode follow-up queries, and optionally capture screenshots through Pangolinfo APIs."
category: "Research & Scraping"
framework: "OpenClaw"
verification: listed
source: "https://github.com/Pangolin-spg/openclaw-skills/tree/main/pangolinfo-ai-serp"
---

# Pangolinfo AI SERP

This OpenClaw skill retrieves structured Google search data through Pangolinfo APIs. Use it for search research, evidence collection, or workflows that need organic results and AI Overviews as JSON rather than a manually copied page. The upstream package includes a SKILL.md, Python helper, and reference files. The helper requires Python 3.6 or later and uses the standard library.

Use serp mode for standard search results and AI Overview extraction. Use ai-mode for AI Mode requests and add follow-up queries when a user needs a multi-turn exploration. Screenshots are optional and may be requested with the screenshot flag. The helper writes structured JSON to stdout, including organic_results, ai_overview when returned, screenshot when requested and available, task_id, and success. An absent AI Overview is not evidence that a query has no useful search results; distinguish missing data from an empty result set and preserve source links in reports.

The source is MIT licensed and designed for OpenClaw. Compatibility with other clients has not been independently tested here. Pangolinfo is an independent provider, not an official Google service. Its API requires an account and authentication; limited trial credits are followed by paid usage. No security-review claim is made by this submission.

## Installation

Obtain the complete canonical package and install its skill directory using your OpenClaw skill workflow:

```bash
git clone https://github.com/Pangolin-spg/openclaw-skills.git
cd openclaw-skills/pangolinfo-ai-serp
```

Keep scripts/ and references/ with SKILL.md. This catalog summary alone does not include the runtime helper. Configure PANGOLIN_TOKEN in the local environment, or PANGOLIN_EMAIL and PANGOLIN_PASSWORD as described upstream. Never expose actual credentials in prompts or public files. Review the upstream code before execution.

Run a standard search from the installed skill directory:

```bash
python3 scripts/pangolinfo.py --q "openclaw" --mode serp --screenshot
```

For AI Mode, use --mode ai-mode and optional --follow-up arguments. Keep requests within the user-approved scope and budget.

## Documentation

- [Skill product page](https://www.pangolinfo.com/ai-serp-skill/)
- [AI Overview SERP API](https://www.pangolinfo.com/ai-overview-serp-api/)
- [AI Mode API reference](https://docs.pangolinfo.com/en-api-reference/aiModeSerpApi/aiModeSerpAPI)
- [Canonical source and complete skill](https://github.com/Pangolin-spg/openclaw-skills/tree/main/pangolinfo-ai-serp)
