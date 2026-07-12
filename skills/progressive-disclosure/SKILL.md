---
name: "Progressive Disclosure for Documentation"
slug: "progressive-disclosure"
description: "Restructure large documentation files (500+ lines, 5k+ tokens) into slim indexes with on-demand detail directories. Reduces always-included context by 40-60% while preserving full accessibility. Ideal for documentation auto-included in every agent context window."
github_stars: 14
verification: "listed"
source: "https://github.com/gptme/gptme-contrib"
author: "gptme"
category: "Templates & Workflows"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "gptme/gptme-contrib"
  github_stars: 14
---

# Progressive Disclosure for Documentation

A pattern for restructuring large documentation files into slim indexes with on-demand
subdirectories, reducing always-included context by 40-60%.

## Problem

Large documentation files (500+ lines, 5k+ tokens) that are always included in context:
- Waste context budget on rarely-needed content
- Slow down response times
- Crowd out more relevant information
- Create cognitive overload

## Solution

Split monolithic docs into:
1. **Slim index** (~20% of original) - Always included, provides overview + navigation
2. **Detail directories** - On-demand loading when specific topics needed

## Structure

```txt
Before:
  TOOLS.md (~11k tokens always included)
  ├── Section 1 (rarely needed)
  ├── Section 2 (rarely needed)
  ├── ... (15+ sections)
  └── Section N (rarely needed)

After:
  tools/
  ├── README.md (~4k tokens always included)  # Slim index
  ├── topic1/README.md   # Detailed docs (~1k tokens each)
  ├── topic2/README.md   # Loaded on-demand
  └── .../README.md      # etc.
```

## When to Use

**Good candidates for progressive disclosure:**
- Files > 500 lines or 5k tokens
- Files always included in context (via config or auto-load)
- Files with distinct sections that are rarely needed together
- Documentation with both overview and detailed reference content

**Keep as single file when:**
- File is < 200 lines
- Content is frequently needed together
- Structure is already lean
- Users commonly need the complete view

## Implementation Guide

### Step 1: Analyze Current Structure

Count tokens and identify sections:

```bash
# Count lines and estimate tokens
wc -l LARGE_FILE.md
# Rough: 1 line ≈ 8 tokens

# Identify sections (look for ## headers)
grep "^## " LARGE_FILE.md | head -20
```

### Step 2: Create Directory Structure

```bash
# Create the new directory
mkdir -p docs/topic-name

# Create the slim index (keep: overview, quick-reference, navigation links)
# Move detailed content to subdirectories
```

### Step 3: Write the Slim Index

The slim index should:
- Be 15-25% of the original file size
- Include: purpose, quick reference, and links to detail dirs
- Answer "what is this?" and "where do I find X?"
- NOT include: step-by-step guides, full examples, edge cases

```markdown
# Tool Name

Brief description (2-3 sentences).

## Quick Reference

| Command | Purpose |
|---------|---------|
| cmd1    | does X  |
| cmd2    | does Y  |

## Guides

- [Installation](./installation/README.md)
- [Advanced Config](./advanced/README.md)
- [Troubleshooting](./troubleshooting/README.md)
```

### Step 4: Move Detail Content

For each major section:
1. Create `./section-name/README.md`
2. Move the full content there
3. Replace original section with a one-line pointer

### Step 5: Update Config

Update any auto-include configuration to point to the new slim index:

```toml
# Example: update gptme.toml or equivalent config
[prompt]
files = [
    "docs/tools/README.md",    # slim index — was tools.md
    # ... other files
]
```

## Measured Results

Applied to a real agent documentation file:
- Before: `TOOLS.md` = ~11,000 tokens (always included)
- After: `tools/README.md` = ~4,000 tokens (always included)
- Detail files: ~1,000 tokens each (loaded on demand)
- **Context savings: ~64% reduction in always-included tokens**

## Anti-Patterns

| Anti-Pattern | Fix |
|---|---|
| Making the index too detailed | Index = navigation; details = subdirs |
| Too many detail files (>10) | Group related sections into one subdir |
| Inconsistent depth (some sections slim, others still huge) | Apply pattern uniformly |
| Forgetting to update config/imports | Always audit auto-include lists after restructuring |
| Splitting files that are always read together | Only split genuinely independent sections |

## Installation

### Claude Code

Copy this skill directory:

```bash
cp -R skills/progressive-disclosure ~/.claude/skills/progressive-disclosure
```

Then invoke with `/progressive-disclosure` before restructuring a large documentation file.

### Manual

The pattern is pure documentation design — no tools required. Read the Implementation
Guide above and apply the structure to any large file in your project.

## Related

- `autonomous-session-workflow` (in this catalog) — auto-include optimization helps agents stay within context budget
- `five-element-spec` (in this catalog) — scope documentation before restructuring
