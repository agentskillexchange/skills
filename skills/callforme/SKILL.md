---
name: "CallForMe"
slug: "callforme"
description: "Phone a business for the user through the CallForMe remote MCP server (https://callforme.tel/mcp) or its REST API: get quotes, book a table, check stock, cancel a membership or wait on hold, then report the answers and transcript."
github_stars: 1
verification: "listed"
source: "https://github.com/callforme-tel/callforme"
author: "Great Work LLC"
category: "Integrations & Connectors"
framework: "MCP"
tool_ecosystem:
  github_repo: "callforme-tel/callforme"
  github_stars: 1
---

# CallForMe

CallForMe is a remote MCP server that gives an agent a phone. The agent supplies a business phone number (or uses find_business to look one up), a goal and the questions to ask. A voice assistant places the call to businesses in the US and Canada, works the phone menu, waits on hold, and opens with "an assistant calling for <name>, on a recorded line"; it says it is an AI whenever asked. If the business asks something the agent did not cover, the question comes back to the agent mid-call through answer_question, and the answer goes into the live call. When the call ends the agent receives answers in order, any open questions, a full transcript and a recording link.

The server exposes 15 tools: find_business, plan_call, place_call, call_around (phone several businesses in parallel and compare), get_call, answer_question, hang_up, redial, wait_for_setup, share_call, list_calls, get_batch, stop_batch, account and pricing. A REST API with an OpenAPI description at https://callforme.tel/openapi.json covers the same operations for agents without MCP. Connecting asks for nothing: OAuth 2.1 with dynamic client registration creates a guest account, and the first real call returns a one-time link where the user adds prepaid credit. Pricing is pay per call: $1 per answered call including the first 2 minutes, then $0.40 per minute. Unanswered and busy calls are free, but connected phone-menu and hold time can be billed even if no person is reached. See the [current pricing and voicemail exceptions](https://callforme.tel/docs/pricing).

Use it when the answer needs a phone call: three brake quotes, a dinner reservation, a cancellation that only works by phone, or a long hold queue. Do not use it for texting or emailing a business.

## Installation

Install or set up from the source-backed instructions:

claude mcp add --transport http callforme https://callforme.tel/mcp

- Source: https://github.com/callforme-tel/callforme

