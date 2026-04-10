---
name: Gmail API Thread Label Triage
description: Triage inbox backlog with the Gmail API’s `users.threads`, `users.messages`,
  and `users.labels` methods so agents can classify and prioritize whole conversations
  instead of isolated emails. Useful for support, recruiting, or founder inboxes where
  thread context matters more than single-message scanning.
verification: security_reviewed
source: https://developers.google.com/gmail/api
category:
- Calendar, Email &amp; Productivity
framework:
- Gemini
---
# Gmail API Thread Label Triage

Gmail API Thread Label Triage is meant for workflows where an agent needs to sort conversation-heavy inboxes without losing thread context. It uses Gmail API resources such as users.threads, users.messages, and users.labels to inspect multi-message conversations, apply consistent labels, and separate urgent threads from background noise. That matters when a single reply chain contains the real state of a request and looking only at the most recent message would misclassify it.
The skill can review sender patterns, recent replies, unread state, and label history before suggesting or applying a triage outcome. It is especially effective in shared inboxes, recruiting pipelines, founder correspondence, or support queues where agents need to identify follow-up debt quickly. Because the workflow stays grounded in thread-level Gmail objects, it also makes downstream summaries and handoffs more coherent.
Use this skill when email triage should reflect the full conversation, when inbox labels drive workflow decisions, and when agents need something more structured than search operators alone.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gmail-api-thread-label-triage/)
