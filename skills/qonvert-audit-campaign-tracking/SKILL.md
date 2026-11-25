---
name: "Qonvert Audit Campaign Tracking"
slug: "qonvert-audit-campaign-tracking"
description: "Inspect supplied campaign URLs for missing UTM fields and visible Google Ads or Yandex Direct click IDs, then identify the next attribution test."
category: "Data Extraction & Transformation"
framework: "Claude Code"
verification: listed
source: "https://github.com/Qonvert-Marketing-AI/qonvert-marketing-skills/tree/main/skills/audit-campaign-tracking"
---

# Qonvert Audit Campaign Tracking

Use this workflow when an ad report contains clicks but a web analytics report cannot reliably assign visits or confirmed conversions to a campaign. Start from example URLs with any sensitive values removed, the originating channel, and the system that should record the destination event. The first check runs on the supplied string and needs no advertising account, scripts, or keys.

1. Inspect whether `utm_source`, `utm_medium`, and `utm_campaign` are present, nonempty, unique, and consistent with the naming convention. Record optional `utm_content` and `utm_term` when the report uses them.
2. Record which click ID parameter names are visible. Google Ads and Yandex Direct can add an ID at click time. A sample with no ID cannot establish whether real clicks are tracked.
3. Return the sample label, observation, implication, and the next check. For the fictional link below, the first missing field is `utm_campaign`.
4. Verify an approved visit separately through redirects, the final URL, the analytics event, and the recorded business outcome. Use the earliest unverified stage as the next test.

```text
https://example.com/rooms?utm_source=google&utm_medium=cpc
```

The same example can be tried in the [optional Qonvert Connect guest guide](https://qonvert.ai/connect/google-ads?utm_source=agent_skill_exchange&utm_medium=directory&utm_campaign=google_ads_mcp). The underlying [Qonvert Marketing AI skill](https://github.com/Qonvert-Marketing-AI/qonvert-marketing-skills/tree/main/skills/audit-campaign-tracking) is public under the MIT license.

## Installation

### Claude Code project skill

From the project root, fetch the original skill and place its canonical `SKILL.md` in a project skill folder.

```bash
git clone --depth 1 https://github.com/Qonvert-Marketing-AI/qonvert-marketing-skills.git
mkdir -p .claude/skills/audit-campaign-tracking
cp qonvert-marketing-skills/skills/audit-campaign-tracking/SKILL.md .claude/skills/audit-campaign-tracking/SKILL.md
```

Ask Claude Code to use Audit Campaign Tracking on the synthetic URL above. The expected finding is a missing campaign tag. The workflow can also be read and used directly from the upstream source.
