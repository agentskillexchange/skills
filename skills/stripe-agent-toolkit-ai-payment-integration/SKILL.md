---
title: "Stripe Agent Toolkit for AI Payment Integration"
description: "What is the Stripe Agent Toolkit? The Stripe Agent Toolkit is Stripe&#8217;s official SDK for connecting AI agents to payment infrastructure. Hosted at github.com/stripe/ai with over 1,400 GitHub stars, it includes @stripe/agent-toolkit for function calling integration, @stripe/ai-sdk for Vercel AI billing, and @stripe/token-meter for usage metering across OpenAI, Anthropic, and Google Gemini. Stripe also operates a hosted MCP server at mcp.stripe.com with OAuth-based remote access. How the Skill Works An agent skill built on the Stripe Agent Toolkit exposes payment operations as callable functions within an AI agent&#8217;s tool repertoire. The toolkit wraps Stripe&#8217;s Python and Node SDKs, providing 25 tools across 13 categories including creating payment links, managing subscriptions, issuing refunds, querying transaction data, and creating customer records. Permissions are enforced through Stripe&#8217;s Restricted API Keys, giving fine-grained control over which operations an agent can perform. The MCP server implementation follows the Model Context Protocol standard, allowing any MCP-compatible client to connect to Stripe&#8217;s payment APIs. The local server runs via npx, while the remote server at mcp.stripe.com supports OAuth authentication for secure cloud-based access. Tool availability automatically adapts based on the permissions configured on the restricted API key. Integration Points The toolkit integrates with OpenAI&#8217;s Agent SDK, LangChain, CrewAI, and Vercel&#8217;s AI SDK natively. The MCP server works with Claude Desktop, Cursor, and any MCP-compatible client. Both Python (pip install stripe-agent-toolkit) and TypeScript (npm install @stripe/agent-toolkit) packages are available. The toolkit requires Python 3.11+ or Node.js and a Stripe API key. What It Outputs The skill produces structured payment operation results including payment link URLs, subscription IDs, refund confirmations, customer records, and transaction query results. Error responses include Stripe error codes and human-readable messages for agent interpretation."
source: "https://github.com/stripe/ai"
verification: "security_reviewed"
category:
  - "Integrations &amp; Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "stripe/ai"
  github_stars: 1422
---

# Stripe Agent Toolkit for AI Payment Integration

What is the Stripe Agent Toolkit? The Stripe Agent Toolkit is Stripe&#8217;s official SDK for connecting AI agents to payment infrastructure. Hosted at github.com/stripe/ai with over 1,400 GitHub stars, it includes @stripe/agent-toolkit for function calling integration, @stripe/ai-sdk for Vercel AI billing, and @stripe/token-meter for usage metering across OpenAI, Anthropic, and Google Gemini. Stripe also operates a hosted MCP server at mcp.stripe.com with OAuth-based remote access. How the Skill Works An agent skill built on the Stripe Agent Toolkit exposes payment operations as callable functions within an AI agent&#8217;s tool repertoire. The toolkit wraps Stripe&#8217;s Python and Node SDKs, providing 25 tools across 13 categories including creating payment links, managing subscriptions, issuing refunds, querying transaction data, and creating customer records. Permissions are enforced through Stripe&#8217;s Restricted API Keys, giving fine-grained control over which operations an agent can perform. The MCP server implementation follows the Model Context Protocol standard, allowing any MCP-compatible client to connect to Stripe&#8217;s payment APIs. The local server runs via npx, while the remote server at mcp.stripe.com supports OAuth authentication for secure cloud-based access. Tool availability automatically adapts based on the permissions configured on the restricted API key. Integration Points The toolkit integrates with OpenAI&#8217;s Agent SDK, LangChain, CrewAI, and Vercel&#8217;s AI SDK natively. The MCP server works with Claude Desktop, Cursor, and any MCP-compatible client. Both Python (pip install stripe-agent-toolkit) and TypeScript (npm install @stripe/agent-toolkit) packages are available. The toolkit requires Python 3.11+ or Node.js and a Stripe API key. What It Outputs The skill produces structured payment operation results including payment link URLs, subscription IDs, refund confirmations, customer records, and transaction query results. Error responses include Stripe error codes and human-readable messages for agent interpretation.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-agent-toolkit-ai-payment-integration/)
