# Verification Criteria

Detailed criteria for the public trust tiers in Agent Skill Exchange.

---

## 📋 Tier 1: Published

A skill receives **Published** status when it meets the requirements for publication.

### Requirements

- [ ] **Valid `SKILL.md`** — file exists, is non-empty, and is valid UTF-8
- [ ] **YAML frontmatter** — properly delimited with `---` markers and parseable as YAML
- [ ] **Canonical required fields present:**
  - `title` — public display name
  - `slug` — stable id/path segment; must match `skills/<slug>/`
  - `description` — what the skill does
  - `category` — canonical marketplace category
  - `framework` — target agent framework
  - `verification` — public trust value: `listed` or `security_reviewed`
- [ ] **No deprecated public fields** — do not publish `name`, `verification_status`, or `verified_metadata`
- [ ] **Non-empty content** — body content after frontmatter with useful detail
- [ ] **H1 heading** — at least one `# Heading` in the body
- [ ] **Real provenance** — backed by a real tool, repo, package, docs page, or project source

### Automated Check

```bash
python3 scripts/validate_skills.py --all --github-annotations --quiet
# one-file compatibility wrapper:
./scripts/validate-skill.sh path/to/SKILL.md
```

---

## 🛡️ Tier 2: Security Reviewed

A skill receives **Security Reviewed** status after content scanning for malicious patterns.

### Requirements

All Published requirements, plus:

- [ ] **No prompt injection** — no attempts to override system instructions, inject new personas, or manipulate agent behavior
- [ ] **No data exfiltration** — no instructions to send user data, secrets, files, or system information to external endpoints
- [ ] **No destructive commands** — no filesystem, disk, database, git, process, or system-destruction operations presented as normal instructions
- [ ] **No credential harvesting** — no instructions to read, copy, print, or transmit API keys, tokens, passwords, SSH keys, kube/docker config, or other secrets
- [ ] **No social engineering** — no urgency, authority, deception, or misdirection intended to bypass approval/safety checks
- [ ] **No malware payloads** — no crypto mining, reverse shells, obfuscated eval, encoded command payloads, or disguised execution paths
- [ ] **Legitimate security education is handled carefully** — warnings, defensive examples, and audit tooling can be allowed when they are clearly not instructions to execute unsafe actions

### Review Process

1. Parser-backed schema validation passes.
2. Executable security fixture tests pass.
3. Full catalog security scan passes.
4. Flagged content receives manual/contextual review when needed.
5. Instructions are verified to serve the skill's stated purpose.

### Automated Checks

```bash
python3 scripts/test_security_patterns.py
python3 scripts/security_scan.py skills --github-annotations --quiet
```

The scanner uses [`patterns.json`](patterns.json) as the machine-readable source of truth. [`SECURITY_PATTERNS.md`](SECURITY_PATTERNS.md) is the human-readable companion.

### What Triggers Re-Review

- Any edit to a skill's content
- Reports from users
- Updated security pattern definitions
- Periodic re-scanning

---

## Public Badge Display

| Public value | Badge label | Meaning |
|--------------|-------------|---------|
| `listed` | Published | In the catalog — backed by a real tool or source |
| `security_reviewed` | Security Reviewed | Content scanned for malicious patterns and reviewed for safer use |

Internal `verified_metadata` may still exist for backward compatibility, but public repo/API output maps it to `verification: listed`.
