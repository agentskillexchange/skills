---
name: "Amazon Listing Checker"
slug: "amazon-listing-checker"
description: "Audit pasted Amazon listing text for length, structure, risky claims, repeated terms, and keyword coverage. Use when asked to review or improve a product title, bullets, description, or backend search terms."
category: "Content Writing & SEO"
framework: "Claude Code"
verification: listed
source: "https://github.com/MelMayssonOwen/agent-skills/tree/main/skills/amazon-listing-checker"
---

# Amazon Listing Checker

This skill audits listing text supplied directly by the user. A bundled Python script accepts a title, bullets, description, backend search terms, and main keyword, then returns severity-scored findings with practical rewrite suggestions. Checks include a 200-character title ceiling, whether five bullets were supplied, backend terms under 249 UTF-8 bytes, repeated words, a small set of potentially risky claims, and whether the main keyword appears naturally in key fields.

The script is deterministic and runs locally. It does not scrape Amazon, inspect a seller account, or verify current marketplace policy. Risk flags are prompts for a human to check the claim against evidence and current rules. Suggestions should preserve the product's true attributes; users should not add unsupported certifications, guarantees, or comparisons.

The skill is a fast first pass for sellers and copywriters who want clear text-level feedback before editing a listing. For a fuller manual audit and rewrite, Listingtonic offers a free preview; current paid pricing should be checked on its site. Neither the skill nor any service can guarantee ranking outcomes.

Creator: Opsibyte. License: MIT. Product: https://listingtonic.com/?utm_source=ase&utm_medium=skill&utm_campaign=agent-skills&utm_content=amazon-listing-checker

## Installation

### Direct repo/manual install

```bash
git clone https://github.com/MelMayssonOwen/agent-skills.git
cp -R agent-skills/skills/amazon-listing-checker ~/.agent-skills/amazon-listing-checker
```

### Optional Third-Party Installer

```bash
npx skills add MelMayssonOwen/agent-skills --skill amazon-listing-checker
```
