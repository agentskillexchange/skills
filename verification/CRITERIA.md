# Verification Criteria

Detailed criteria for each verification tier in the Agent Skill Exchange.

---

## 📝 Tier 1: Listed

A skill receives **Listed** status when it meets the minimum requirements for publication.

### Requirements

- [ ] **Valid SKILL.md** — File exists and is non-empty
- [ ] **YAML frontmatter** — Properly delimited with `---` markers
- [ ] **Required fields present:**
  - `name` — Skill name
  - `description` — Brief description of what the skill does
  - `category` — Valid marketplace category
  - `framework` — Target framework(s)
  - `verification.verified_metadata` — Boolean
  - `verification.security_reviewed` — Boolean
  - `rating` — Numeric rating (1.0–5.0)
  - `reviews` — Review count
  - `creator.name` — Creator attribution
- [ ] **Non-empty content** — Body content after frontmatter
- [ ] **H1 heading** — At least one `# Heading` in the body
- [ ] **Valid rating** — Between 1.0 and 5.0

### Automated Check

```bash
./scripts/validate-skill.sh path/to/SKILL.md
```

---

## ✅ Tier 2: Verified Metadata

A skill receives **Verified Metadata** status when a reviewer confirms accuracy.

### Requirements

All Tier 1 requirements, plus:

- [ ] **Accurate category** — The assigned category correctly reflects the skill's primary function
- [ ] **Accurate framework** — The framework assignment matches the skill's actual compatibility
- [ ] **Working source links** — Any URLs in the skill (source repo, documentation) resolve to valid pages
- [ ] **Correct install commands** — Install snippets actually work when executed
- [ ] **Consistent naming** — Skill name matches the directory name (slug), and the title in the frontmatter matches the H1 heading
- [ ] **Description quality** — Description is clear, accurate, and not misleading
- [ ] **No placeholder content** — No Lorem Ipsum, TODO markers, or stub content

### Review Process

1. Automated validation passes (Tier 1)
2. Reviewer checks category/framework accuracy
3. Reviewer spot-checks source links
4. Reviewer verifies install commands
5. `verified_metadata` set to `true`

---

## 🛡️ Tier 3: Security Reviewed

A skill receives **Security Reviewed** status after content scanning for malicious patterns.

### Requirements

All Tier 2 requirements, plus:

- [ ] **No prompt injection** — No attempts to override system instructions, inject new personas, or manipulate agent behavior
- [ ] **No data exfiltration** — No instructions to send user data to external URLs via `curl`, `wget`, API calls, or other network methods
- [ ] **No destructive commands** — No `rm -rf /`, `format`, `dd if=/dev/zero`, `mkfs`, or other destructive operations presented as normal instructions
- [ ] **No credential harvesting** — No instructions to read, copy, or transmit API keys, tokens, passwords, SSH keys, or other secrets to external services
- [ ] **No obfuscated code** — No base64-encoded payloads, hex-encoded commands, or other encoding used to disguise malicious intent
- [ ] **No social engineering** — No instructions that trick agents into performing actions the user didn't request
- [ ] **No privilege escalation** — No instructions to run as root/admin when unnecessary, or to disable security features

### Review Process

1. Automated pattern scanning (see [SECURITY_PATTERNS.md](SECURITY_PATTERNS.md))
2. Manual review of flagged content
3. Verification that all instructions serve the skill's stated purpose
4. `security_reviewed` set to `true`

### What Triggers Re-Review

- Any edit to the skill's content
- Reports from users
- Updated security pattern definitions
- Periodic re-scanning (quarterly)

---

## Verification Badge Display

On the marketplace website, verification status is shown as:

| Status | Badge | Meaning |
|--------|-------|---------|
| Listed only | 📝 | Published but not yet reviewed |
| Verified Metadata | ✅ | Metadata confirmed accurate |
| Security Reviewed | 🛡️ | Safe for production use |

Skills in this GitHub repository have all reached at minimum **Verified Metadata** status.
