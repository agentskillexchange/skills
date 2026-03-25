# Trust & Safety

Every skill in the Agent Skill Exchange is backed by a real tool, repo, or package. New skills go through a discovery pipeline that requires real provenance before listing.

## How It Works

```
📋 Listed                  Published — real tool, real provenance
     ↓
🛡️ Security Reviewed      Scanned for safety — highest trust
```

### 📋 Listed

The skill is published in the catalog. To be listed, a skill must:

- Be backed by a real tool, repo, or package
- Have a valid `SKILL.md` with required frontmatter
- Be assigned to a valid category and framework
- Have substantive content (100+ words with technical references)
- Pass deduplication checks against existing skills

### 🛡️ Security Reviewed

The skill's content has been scanned for potentially malicious patterns:

- No prompt injection attempts
- No data exfiltration patterns (unauthorized network calls)
- No destructive commands (`rm -rf /`, disk formatting, etc.)
- No credential harvesting instructions
- No obfuscated or encoded payloads
- No reverse shells or crypto mining

## Checking a Skill's Status

Each skill's `SKILL.md` frontmatter includes a `verification` field:

```yaml
---
name: "Example Skill"
verification: security_reviewed
---
```

Valid values:

| Value | Meaning |
|-------|---------|
| `listed` | Published — backed by a real tool |
| `security_reviewed` | Content scanned for malicious patterns — safe to use |

## More Information

- [Verification Criteria](CRITERIA.md) — detailed requirements for each tier
- [Security Patterns](SECURITY_PATTERNS.md) — patterns checked during security review
- [Browse Skills](https://agentskillexchange.com/browse-skills/) — explore the full catalog
