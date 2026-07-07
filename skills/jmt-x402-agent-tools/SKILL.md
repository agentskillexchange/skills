---
name: "JMT x402 Agent Tools"
slug: "jmt-x402-agent-tools"
description: "Paid x402 HTTP-402 endpoints on Base mainnet that let agents pay-per-call in USDC for web search, AI analysis, crypto and stock market data, SEC filings, company intelligence, news, sentiment scoring, and a macro dashboard. 25 endpoints priced $0.001-$0.15/call, returning JSON. The proxy fronts local LLM inference and public data APIs so an agent can fetch grounded market, filings, and news data without API keys, charging micropayments via the x402 facilitator protocol."
verification: "listed"
source: "https://jmt-x402-proxy.jmthomasofficial.workers.dev"
category: "Integrations & Connectors"
framework: "Custom Agents"
---

# JMT x402 Agent Tools

JMT x402 Agent Tools exposes 25 paid HTTP endpoints on Base mainnet that use the
x402 payment protocol (HTTP 402) to bill agents per call in USDC. Prices range
from $0.001 to $0.15 per request, settled on-chain through the x402 facilitator.
Each endpoint returns structured JSON, so an agent can ground its answers in
real data without managing its own API keys or subscriptions.

The service fronts local LLM inference plus public data providers, packaging
them into a single paid interface:

- **Web search** — query the open web and receive ranked JSON results.
- **AI analysis** — summarization, extraction, and reasoning over supplied text
  or fetched content, powered by a local LLM.
- **Crypto and stock data** — current quotes, historical series, and market
  statistics for tickers and on-chain assets.
- **SEC filings** — retrieve and search EDGAR filings (10-K, 10-Q, 8-K) by
  company and form type.
- **Company intelligence** — fundamentals, sector, and business profile data.
- **News and sentiment** — news search plus sentiment scoring per article or
  query.
- **Macro dashboard** — a consolidated cross-market snapshot of rates, FX,
  indices, and commodity data.

Because payment is handled per request via the x402 facilitator, agents only
need a funded wallet on Base mainnet; there is no signup, billing account, or
shared API key to manage. The endpoint responds `402 Payment Required` with a
payment challenge, the agent pays, and the proxy returns the result JSON.

## Installation

### Direct endpoint usage

Point your agent at the proxy root and call any endpoint. A typical request
flow:

```bash
# 1. Request the endpoint — receive a 402 payment challenge
curl -i https://jmt-x402-proxy.jmthomasofficial.workers.dev/search?q=base+chain+tvl

# 2. Pay the quoted USDC amount on Base mainnet via the x402 facilitator
#    (use your x402 client library, e.g. x402-fetch)

# 3. Re-request with the payment header — receive JSON results
curl -H "X-PAYMENT: <payment-header>" \
     https://jmt-x402-proxy.jmthomasofficial.workers.dev/search?q=base+chain+tvl
```

### x402 client libraries

Use any x402-compatible client to handle the payment handshake automatically:

```bash
npm install x402-fetch      # browser/Node fetch wrapper
pip install x402-requests   # Python requests wrapper
```

Then make paid calls as if they were ordinary HTTP requests; the library
intercepts the `402` response, pays via the facilitator, and retries.

## Source

- Proxy endpoint: https://jmt-x402-proxy.jmthomasofficial.workers.dev
- x402 protocol: https://x402.org