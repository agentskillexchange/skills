---
name: "Van Westendorp Analysis"
slug: "van-westendorp-analysis"
description: "Compute a Van Westendorp price sensitivity meter (PSM) from a CSV of pricing survey answers: OPP, IPP, PMC, PME and the acceptable price range, plus the optional Newton-Miller-Smith purchase-intent extension, with a standard-library Python script."
category: "Data Extraction & Transformation"
framework: "Claude Code"
verification: listed
source: "https://github.com/questionpunk/research-skills/tree/main/skills/van-westendorp-analysis"
tool_ecosystem:
  github_repo: "questionpunk/research-skills"
---

# Van Westendorp Analysis

This skill turns respondent-level answers to the four Van Westendorp pricing questions (too cheap, cheap, expensive, too expensive) into the price sensitivity meter: the optimal price point (OPP), the indifference price point (IPP), the point of marginal cheapness (PMC), the point of marginal expensiveness (PME) and the acceptable price range. It prints the range under both common definitions, because tools such as R, Conjointly and Sawtooth do not all use the same one, so a result can be reconciled with theirs.

The arithmetic runs in `scripts/van_westendorp_analysis.py`, a Python 3.9+ script that uses only the standard library and makes no network calls. It finds the price columns by name, excludes respondents whose four prices are out of order and reports how many, prints the minimum, median and maximum for each question, and can write an SVG chart. When the survey also asked purchase intent at the respondent's own cheap and expensive prices, it adds the Newton-Miller-Smith trial and revenue curves. Segment and weight columns are supported. The skill's `references/sources.md` cites each formula, and its tests check the script against fixtures with hand-worked and published results.

Use it when you have a CSV with one row per respondent and want the price points and range. If there is no data yet, the skill's instructions tell the agent to give you the four questions to field and stop, rather than invent or simulate responses. It measures price perception, not demand, so it gives a range to test rather than a price to ship. For yes/no answers to a price ladder (Gabor-Granger) or conjoint tasks, use a different method.

## Installation

### Optional Third-Party Installer

The `skills` npm package is maintained by Vercel Labs / third parties, not AgentSkillExchange. If you choose to use it, pin the package version:

```bash
npm exec --package=skills@1.5.7 -- skills add questionpunk/research-skills --skill van-westendorp-analysis
```

### Claude Code plugin marketplace (installs the pricing-research group)

```text
/plugin marketplace add questionpunk/research-skills
/plugin install pricing-research@research-skills
```

### Direct repo/manual install

```bash
git clone https://github.com/questionpunk/research-skills.git
mkdir -p ~/.claude/skills
cp -R research-skills/skills/van-westendorp-analysis ~/.claude/skills/
```

The script needs Python 3.9 or later and nothing else.
