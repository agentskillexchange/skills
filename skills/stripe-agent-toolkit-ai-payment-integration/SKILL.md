---
name: "Stripe Agent Toolkit for AI Payment Integration"
description: "The official Stripe Agent Toolkit provides Python and TypeScript libraries plus a hosted MCP server for integrating Stripe payment APIs with AI agent frameworks. Supports OpenAI, LangChain, CrewAI, and Vercel AI SDK through function calling with granular API key permissions."
category: "Integrations &amp; Connectors"
framework: "MCP"
verification: security_reviewed
source: "https://github.com/stripe/ai"
tool_ecosystem:
  github_repo: "stripe/ai"
  github_stars: 1422
---
# Stripe Agent Toolkit for AI Payment Integration

The official Stripe Agent Toolkit provides Python and TypeScript libraries plus a hosted MCP server for integrating Stripe payment APIs with AI agent frameworks. Supports OpenAI, LangChain, CrewAI, and Vercel AI SDK through function calling with granular API key permissions.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill stripe-agent-toolkit-ai-payment-integration
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill stripe-agent-toolkit-ai-payment-integration -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill stripe-agent-toolkit-ai-payment-integration -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill stripe-agent-toolkit-ai-payment-integration -a codex
```

### OpenClaw

```bash
clawhub install stripe-agent-toolkit-ai-payment-integration
```

## Details

What is the Stripe Agent Toolkit?
The Stripe Agent Toolkit is Stripe’s official SDK for connecting AI agents to payment infrastructure. Hosted at github.com/stripe/ai with over 1,400 GitHub stars, it includes @stripe/agent-toolkit for function calling integration, @stripe/ai-sdk for Vercel AI billing, and @stripe/token-meter for usage metering across OpenAI, Anthropic, and Google Gemini. Stripe also operates a hosted MCP server at mcp.stripe.com with OAuth-based remote access.

How the Skill Works
An agent skill built on the Stripe Agent Toolkit exposes payment operations as callable functions within an AI agent’s tool repertoire. The toolkit wraps Stripe’s Python and Node SDKs, providing 25 tools across 13 categories including creating payment links, managing subscriptions, issuing refunds, querying transaction data, and creating customer records. Permissions are enforced through Stripe’s Restricted API Keys, giving fine-grained control over which operations an agent can perform.

The MCP server implementation follows the Model Context Protocol standard, allowing any MCP-compatible client to connect to Stripe’s payment APIs. The local server runs via npx, while the remote server at mcp.stripe.com supports OAuth authentication for secure cloud-based access. Tool availability automatically adapts based on the permissions configured on the restricted API key.

Integration Points
The toolkit integrates with OpenAI’s Agent SDK, LangChain, CrewAI, and Vercel’s AI SDK natively. The MCP server works with Claude Desktop, Cursor, and any MCP-compatible client. Both Python (pip install stripe-agent-toolkit) and TypeScript (npm install @stripe/agent-toolkit) packages are available. The toolkit requires Python 3.11+ or Node.js and a Stripe API key.

What It Outputs
The skill produces structured payment operation results including payment link URLs, subscription IDs, refund confirmations, customer records, and transaction query results. Error responses include Stripe error codes and human-readable messages for agent interpretation.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-agent-toolkit-ai-payment-integration/)
