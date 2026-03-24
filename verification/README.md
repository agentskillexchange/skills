# Verification Framework

The Agent Skill Exchange uses a **3-tier verification system** to ensure skills are safe, accurate, and production-ready.

## Verification Tiers

```
📝 Listed                  Base marketplace listing
     ↓
✅ Verified Metadata       Frontmatter and metadata reviewed
     ↓
🛡️ Security Reviewed      Content scanned for malicious patterns
```

### 📝 Tier 1: Listed

The skill has been published to the marketplace with a valid `SKILL.md` file.

- Valid YAML frontmatter with required fields
- Non-empty content body
- Assigned to a valid category and framework
- Has a creator attribution

### ✅ Tier 2: Verified Metadata

A reviewer has confirmed the skill's metadata is accurate and complete.

- Category and framework assignments match the skill's actual purpose
- Source links are valid and point to real pages
- Install commands work for the specified frameworks
- Naming is consistent with marketplace conventions
- Description accurately reflects the skill's functionality

### 🛡️ Tier 3: Security Reviewed

The skill's content has been scanned for potentially malicious patterns.

- No prompt injection attempts
- No data exfiltration patterns (unauthorized network calls)
- No destructive commands (`rm -rf`, disk formatting, etc.)
- No credential harvesting
- No obfuscated or encoded payloads

## Current Distribution

| Tier | Skills | Percentage |
|------|-------:|-----------:|
| 🛡️ Security Reviewed | **810** | 51% |
| ✅ Verified Metadata | **379** | 24% |
| 📝 Listed | **391** | 25% |

## Checking a Skill's Verification Status

Each skill's `SKILL.md` frontmatter includes a `verification` field:

```yaml
---
name: "Example Skill"
verification: security_reviewed
---
```

Valid values:

| Value | Tier | Meaning |
|-------|------|---------|
| `listed` | 📝 Tier 1 | Published and indexed — basic format validation |
| `verified_metadata` | ✅ Tier 2 | Frontmatter, links, and installs confirmed accurate |
| `security_reviewed` | 🛡️ Tier 3 | Content scanned for malicious patterns — production safe |

## More Information

- [Verification Criteria](CRITERIA.md) — detailed requirements for each tier
- [Security Patterns](SECURITY_PATTERNS.md) — patterns checked during security review
- [Live Verified Skills](https://agentskillexchange.com/verified-skills/) — browse verified skills on the marketplace
