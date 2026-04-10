---
name: "Himalaya CLI Email Client for IMAP SMTP and Notmuch"
description: "Himalaya is a CLI email client written in Rust that supports IMAP, Maildir, and Notmuch backends for reading mail, and SMTP and Sendmail for sending. It features multi-account configuration, PGP encryption, OAuth 2.0, system keyring integration, and JSON output for scripting and agent automation."
verification: security_reviewed
source: "https://github.com/pimalaya/himalaya"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "pimalaya/himalaya"
  github_stars: 5825
---

# Himalaya CLI Email Client for IMAP SMTP and Notmuch

Himalaya is a command-line interface for managing email, written in Rust as part of the Pimalaya project. It provides a scriptable, terminal-native email experience with support for multiple backends and advanced features like PGP encryption and OAuth 2.0 authentication flows.
Backend Support
For reading email, Himalaya supports three backends: IMAP for connecting to standard email servers, Maildir for local mail storage, and Notmuch for indexed search across local mail. For sending email, it supports SMTP direct connections and Sendmail for piping through a local MTA. Each backend is a Cargo feature that can be enabled or disabled at compile time, allowing minimal builds for specific use cases.
Multi-Account Configuration
Himalaya supports multiple email accounts configured via a TOML-based configuration file. An interactive wizard guides initial setup for common providers including Gmail, Outlook, iCloud Mail, and Proton Mail. Each account can use different backends, authentication methods, and sending configurations. Account switching is handled via the -account flag on any command.
Security Features
The client integrates with the system keyring for secure secret storage, avoiding plaintext passwords in configuration files. OAuth 2.0 authorization flows are supported for providers that require them. PGP encryption is available through three methods: shell commands (calling external GPG), native GPG bindings, or a pure Rust native PGP implementation. This allows encrypted email composition and decryption directly from the terminal.
Message Composition and Output
Email composition uses the $EDITOR environment variable, opening the configured text editor for writing messages. The client supports listing envelopes, reading messages, creating drafts, and managing folders. All commands support -output json for structured output, making it suitable for scripting and integration with agent frameworks that parse JSON responses.
Agent Integration
The JSON output mode makes Himalaya directly usable as an agent tool. An AI agent can list inbox messages, read specific emails, compose replies, and manage folders entirely through CLI invocations with JSON parsing. The multi-account support allows agents to manage multiple mailboxes. Himalaya is available via Homebrew, Scoop, Arch Linux packages, Nix, Cargo, and pre-built binaries. It has over 5,700 GitHub stars and is licensed under MIT.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/himalaya-cli-email-client-imap-smtp-notmuch/)
