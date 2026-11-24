---
name: "Mailtrap Sending Emails"
slug: "mailtrap-sending-emails"
description: "Official Mailtrap skill for wiring outbound email into an app through Mailtrap Email Live Sending: pick the transactional or bulk stream, then send with an official SDK, the email API (send.api.mailtrap.io or bulk.api.mailtrap.io) or SMTP (live.smtp.mailtrap.io or bulk.smtp.mailtrap.io)."
verification: "listed"
source: "https://github.com/mailtrap/mailtrap-skills/tree/main/skills/sending-emails"
category: "Calendar, Email & Productivity"
framework: "Multi-Framework"
---

# Mailtrap Sending Emails

This skill helps a coding agent integrate, configure or troubleshoot live email sending with Mailtrap Email Live Sending. It explains the two sending streams: the transactional stream for email an app generates, such as password resets, receipts and notifications, and the bulk stream for promotional email sent at volume. It then steers the agent through integration options in order of preference: an existing platform integration, an official SDK, the HTTP email API, and SMTP only when the stack requires it.

For the email API, transactional mail goes to `POST https://send.api.mailtrap.io/api/send` and bulk mail to `POST https://bulk.api.mailtrap.io/api/send`, authenticated with an API token in an `Authorization: Bearer` header. For SMTP, the hosts are `live.smtp.mailtrap.io` (transactional) and `bulk.smtp.mailtrap.io` (bulk) on port 587, with the username `api` and the API token as the password. The skill points the agent to the official SDKs (Node.js, Python, PHP, Ruby, .NET, Java, Go and Elixir) and tells it to read the SDK README instead of guessing method names.

It also lists common mistakes, such as sending promotional mail on the transactional host, using an email address as the SMTP username, or sending before the domain is verified. Use it when adding Mailtrap sending to a new or existing application, or when debugging why messages are not going out.

## Installation

### Upstream (official Mailtrap skills)

```bash
npx skills add mailtrap/mailtrap-skills
```

The upstream repository also ships related skills for API tokens, templates, sending domains, contacts and inbound email.

### Direct repo/manual install

Clone the Agent Skill Exchange repository and copy this skill directory into the skill folder used by your agent runtime:

```bash
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/skills/mailtrap-sending-emails ~/.agent-skills/mailtrap-sending-emails
```

## Documentation

- https://docs.mailtrap.io/email-live-sending/setup/api-integration
- https://docs.mailtrap.io/email-live-sending/setup/smtp-integration
- https://docs.mailtrap.io/email-live-sending/setup/bulk-stream
- https://docs.mailtrap.io/for-ai-agents/tools/skills
