# Security Policy

## Reporting a Security Issue

**Do not open a public GitHub issue for security vulnerabilities.**

If you find a skill that contains malicious content, prompt injection, or any security concern:

1. **Open a [GitHub Security Advisory](https://github.com/agentskillexchange/skills/security/advisories/new)** (private by default)
2. Or email: **skills@agentskillexchange.com** with subject line: `[SECURITY] <brief description>`

We will acknowledge receipt within 24 hours and aim to resolve confirmed issues within 72 hours.

## What Counts as a Security Issue

Agent skills are instructions that AI agents follow. A malicious skill could instruct an agent to:

- **Exfiltrate data** — send files, environment variables, or credentials to external endpoints
- **Prompt injection** — override the user's instructions or the agent's safety guidelines
- **Credential harvesting** — trick users into providing API keys, passwords, or tokens
- **Malicious URLs** — link to phishing sites, malware downloads, or tracking endpoints
- **Destructive commands** — delete files, drop databases, or modify system configurations without user consent
- **Privilege escalation** — instruct the agent to bypass permission checks or access restricted resources

If a skill does any of these things — whether intentionally or accidentally — report it.

## Trust Model

| Tier | Description |
|------|-------------|
| **Listed** | Published — backed by a real tool, repo, or package. Basic format validation. |
| **Security Reviewed** | Content scanned for prompt injection, data exfiltration, credential harvesting, and malicious patterns. Cleared for production use. |

Skills that fail security review are either fixed or removed from the marketplace and this repo.

## Security Review Criteria

For a skill to reach **Security Reviewed** status, it must pass:

1. **No external data transmission** — the skill must not instruct the agent to send data to endpoints the user hasn't explicitly configured
2. **No credential requests** — the skill must not ask for or handle credentials beyond what its stated APIs require
3. **No instruction overrides** — the skill must not contain prompts that attempt to override the agent's system instructions or safety guidelines
4. **No destructive defaults** — any commands that modify or delete data must require explicit user confirmation
5. **URL safety** — all URLs in the skill must resolve to legitimate, non-malicious destinations
6. **Transparent behavior** — the skill must do what its description says and nothing more

## Responsible Disclosure

- We credit reporters in the security advisory (unless you prefer anonymity)
- We do not pursue legal action against good-faith security researchers
- We ask that you give us reasonable time to address the issue before public disclosure

## Scope

This policy covers:
- All skills in the `skills/` directory of this repository
- Content synced from [agentskillexchange.com](https://agentskillexchange.com)

For security issues with the website itself (XSS, CSRF, authentication bypasses), email **skills@agentskillexchange.com** with `[WEB SECURITY]` in the subject.
