# Security Patterns

Patterns checked during security review of Agent Skill Exchange skills. These are used by automated scanners and manual reviewers to identify potentially malicious content in SKILL.md files.

---

## 1. Prompt Injection Indicators

Patterns that attempt to override, bypass, or manipulate agent instructions.

```
# Direct instruction override
/ignore (all |any )?(previous|prior|above|earlier) (instructions|prompts|rules)/i
/forget (everything|all|your) (you know|instructions|rules)/i
/you are now/i
/from now on,? (you|your)/i
/new (instructions|rules|persona|identity)/i
/act as (a |an )?(?!the skill)/i

# System prompt manipulation
/system:?\s*\n/i
/\[system\]/i
/<\|im_start\|>system/i
/BEGININSTRUCTION/i
/###?\s*SYSTEM/i

# Persona injection
/you are (?:a |an )?(?:evil|malicious|unrestricted|unfiltered|jailbroken)/i
/pretend (you are|to be)/i
/roleplay as/i

# Delimiter exploitation
/---\s*\n.*?(?:ignore|override|forget)/is
/```\s*system/i
```

## 2. Data Exfiltration Patterns

Patterns that send user data or system information to external endpoints.

```
# Network exfiltration via CLI
/curl\s+.*(?:--data|--upload|-d\s|-F\s|-T\s).*(?:\$|`|ENV|HOME|KEY|TOKEN|SECRET|PASS|CRED)/i
/wget\s+--post/i
/curl\s+.*\|\s*(?:bash|sh|zsh)/i
/wget\s+-O\s*-.*\|\s*(?:bash|sh|zsh)/i

# DNS/network exfiltration
/nslookup\s.*\$\(/i
/dig\s.*\$\(/i
/ping\s+-c\s*1\s.*\$\(/i

# File upload to external services
/curl\s+.*(?:transfer\.sh|file\.io|0x0\.st|uguu\.se|tmpfiles)/i
/upload.*(?:pastebin|hastebin|gist)/i

# Environment/secret harvesting then sending
/(?:cat|echo|print)\s+.*(?:\.env|\.ssh|\.aws|credentials|\.npmrc|\.pypirc).*(?:curl|wget|nc\s|netcat)/is

# Encoded exfiltration
/base64\s.*(?:curl|wget|nc\b)/i
/\$\(.*\)\s*\|\s*(?:nc|netcat)\s/i
```

## 3. Destructive Commands

Patterns that delete, corrupt, or destroy data or systems.

```
# Filesystem destruction
/rm\s+-[a-z]*r[a-z]*f?\s+(?:\/|~|\$HOME|\$\(|`)/i
/rm\s+-[a-z]*f[a-z]*r?\s+(?:\/|~|\$HOME|\$\(|`)/i
/rmdir\s+--ignore-fail-on-non-empty\s+\//i
/find\s+\/\s+.*-delete/i
/find\s+\/\s+.*-exec\s+rm/i

# Disk operations
/dd\s+if=\/dev\/(zero|urandom|random)\s+of=(?!\/tmp)/i
/mkfs\./i
/format\s+[a-z]:/i
/fdisk\s/i
/parted\s/i
/wipefs\s/i

# Database destruction
/DROP\s+(DATABASE|TABLE|SCHEMA)\s/i
/TRUNCATE\s+TABLE\s/i
/DELETE\s+FROM\s+\w+\s*;?\s*$/im

# Git destruction
/git\s+push\s+.*--force\s+.*(?:main|master|production)/i
/git\s+reset\s+--hard\s+HEAD~\d{2,}/i

# Process/system destruction
/kill\s+-9\s+-1/i
/killall\s/i
/shutdown\s/i
/reboot\s*$/im
/init\s+0/i
```

## 4. Credential Harvesting

Patterns that collect, copy, or expose credentials.

```
# Reading credential files
/cat\s+.*(?:\.env|\.ssh\/id_|\.aws\/credentials|\.npmrc|\.pypirc|\.netrc|\.pgpass)/i
/(?:less|more|head|tail|grep)\s+.*(?:\.env|id_rsa|\.pem|\.key)/i

# Environment variable extraction
/(?:echo|printf|print)\s+.*(?:\$[A-Z_]*(?:KEY|TOKEN|SECRET|PASS|CRED|AUTH))/i
/env\s*\|\s*grep\s*-i\s*(?:key|token|secret|pass|auth|cred)/i
/printenv\s+(?:[A-Z_]*(?:KEY|TOKEN|SECRET|PASS))/i

# Keychain/keyring access
/security\s+find-(?:generic|internet)-password/i
/(?:keyring|keyctl)\s+/i

# Known credential locations
/\/etc\/shadow/i
/\/etc\/passwd.*(?:curl|wget|nc)/i
/\.kube\/config/i
/\.docker\/config\.json/i
```

## 5. Social Engineering Patterns

Instructions designed to manipulate agents into performing unwanted actions.

```
# Urgency/authority manipulation
/(?:urgent|critical|emergency):?\s*(?:run|execute|do|send|delete)/i
/(?:admin|root|supervisor)\s+(?:override|authorization|approved)/i
/this is (?:a |an )?(?:authorized|approved|sanctioned) (?:action|command|request)/i

# Deceptive framing
/(?:for (?:testing|debugging|maintenance) (?:purposes|only)):?\s*(?:run|execute|send|delete|curl)/i
/(?:temporary|temp) (?:fix|workaround):?\s*(?:chmod 777|disable|turn off)/i

# Permission escalation requests
/(?:please |just )?(?:run|execute) (?:as |with )?(?:root|sudo|admin)/i
/chmod\s+(?:777|666)\s+/i
/--no-verify/i
/(?:disable|turn off|bypass)\s+(?:security|firewall|auth|verification|ssl)/i

# Misdirection
/(?:don't|do not) (?:worry|mind|concern yourself) about (?:security|permissions|safety)/i
/(?:it's|its|this is) (?:safe|fine|harmless|normal) to/i
/(?:trust me|I promise|guaranteed safe)/i
```

---

## Usage

These patterns are used in two ways:

1. **Automated scanning** — Scripts apply these regex patterns against SKILL.md content
2. **Manual review** — Reviewers reference these patterns when evaluating flagged skills

### False Positive Handling

Some legitimate skills may match patterns (e.g., a security skill that teaches about `rm -rf` risks). Reviewers assess **context**:

- Is the command being **taught about** or **instructed to run**?
- Is the network call to a **known, legitimate service** the skill explicitly integrates with?
- Is the destructive command in a **warning/don't-do-this** section?

Skills flagged by automated scanning proceed to manual review, where context determines the final verdict.

### Reporting New Patterns

If you discover a malicious pattern not covered here, please report it via [SECURITY.md](../SECURITY.md).
