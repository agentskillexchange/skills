# Verification Criteria

Detailed criteria for each trust tier in the Agent Skill Exchange.

---

## 📋 Tier 1: Published

A skill receives **Published** status when it meets the requirements for publication.

### Requirements

- [ ] **Valid SKILL.md** — File exists and is non-empty
- [ ] **YAML frontmatter** — Properly delimited with `---` markers
- [ ] **Required fields present:**
  - `name` — Skill name
  - `description` — What the skill does
  - `category` — Valid marketplace category
  - `framework` — Target framework
  - `verification` — Trust tier (`listed` or `security_reviewed`)
- [ ] **Non-empty content** — Body content after frontmatter (100+ words)
- [ ] **H1 heading** — At least one `# Heading` in the body
- [ ] **Real provenance** — Backed by a real tool, repo, or package

### Automated Check

```bash
./scripts/validate-skill.sh path/to/SKILL.md
```

---

## 🛡️ Tier 2: Security Reviewed

A skill receives **Security Reviewed** status after content scanning for malicious patterns.

### Requirements

All Tier 1 requirements, plus:

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

### What Triggers Re-Review

- Any edit to the skill's content
- Reports from users
- Updated security pattern definitions
- Periodic re-scanning
