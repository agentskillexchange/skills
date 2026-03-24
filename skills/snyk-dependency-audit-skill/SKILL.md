---
name: "Snyk Dependency Audit Skill"
description: "Uses the Snyk CLI and REST API v1 to scan package manifests for known CVEs. Cross-references findings with the GitHub Advisory Database and produces SBOM documents in CycloneDX format."
category: "Security & Verification"
framework: "Claude Code"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/snyk-dependency-audit-skill/"
tool_ecosystem:
  tool: "snyk"
  github_stars: 5457
  npm_weekly_downloads: 601684
  github_repo: "snyk/cli"
  license: "NOASSERTION"
  maintained: true
---

# Snyk Dependency Audit Skill

Uses the Snyk CLI and REST API v1 to scan package manifests for known CVEs. Cross-references findings with the GitHub Advisory Database and produces SBOM documents in CycloneDX format.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill snyk-dependency-audit-skill
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill snyk-dependency-audit-skill -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill snyk-dependency-audit-skill -a cursor
```

### OpenClaw
```bash
clawhub install snyk-dependency-audit-skill
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill snyk-dependency-audit-skill -a codex
```

## Details

| | |
|---|---|
| **Category** | Security & Verification |
| **Framework** | Claude Code |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [snyk](https://github.com/snyk/cli) — ⭐ 5.5k · NOASSERTION |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/snyk-dependency-audit-skill/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
