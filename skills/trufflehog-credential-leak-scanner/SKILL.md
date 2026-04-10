---
name: "TruffleHog Credential Leak Scanner"
description: "Find, verify, and analyze leaked credentials across Git repositories, Slack, Jira, Docker images, and more using TruffleHog. Classifies 800+ secret types and validates whether discovered credentials are live."
verification: security_reviewed
source: "https://github.com/trufflesecurity/trufflehog"
category:
  - "Security &amp; Verification"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "trufflesecurity/trufflehog"
  github_stars: 25299
---

# TruffleHog Credential Leak Scanner

The TruffleHog Credential Leak Scanner skill uses TruffleHog by Truffle Security to scan for leaked secrets across a wide range of sources. Unlike simple regex-based scanners, TruffleHog combines pattern matching with active verification—it logs in with discovered credentials to confirm whether they are still live, providing a clear signal of present danger versus historical exposure.
TruffleHog classifies over 800 distinct secret types, including AWS access keys, Stripe API keys, database passwords, SSH private keys, OAuth tokens, and cloud provider credentials. For approximately 20 of the most commonly leaked credential types, TruffleHog goes beyond simple verification to perform full analysis: determining who created the secret, what resources it can access, and what permissions it holds. This transforms a raw finding into an actionable remediation ticket.
The scanner operates on Git repositories (scanning the full commit history, not just the current tree), GitHub and GitLab organizations, Docker images, S3 buckets, GCS buckets, Slack workspaces, Jira instances, Confluence spaces, local filesystems, and stdin. This breadth means the agent can audit not just source code but also the collaboration and infrastructure surfaces where secrets commonly leak.
TruffleHog outputs findings in JSON format with structured fields including the secret type, verification status (verified/unverified), source location, commit metadata, and for analyzed secrets, the full permission and resource inventory. In CI/CD pipelines, the official GitHub Action integrates with pull request checks. The tool supports baseline files to track known issues and avoid alert fatigue on accepted risks.
TruffleHog is written in Go, distributed via Homebrew, Docker, and direct binary download, and licensed under AGPL-3.0. It has over 18,000 GitHub stars, active weekly releases, and an engaged community on Slack and Discord. For teams managing any cloud infrastructure, this skill provides the detection layer that catches credential leaks before attackers do.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/trufflehog-credential-leak-scanner/)
