---
name: "AShareHub Chinese Market Data"
slug: "asharehub"
description: "Query Chinese A-share, ETF, index, financial statement, valuation, capital-flow, and technical-indicator data through the AShareHub Python SDK and hosted API. Use this skill when an agent needs structured China market data as pandas DataFrames."
verification: "listed"
source: "https://github.com/ChuYiCui1/AshareHub-skills/tree/main/skills/en"
category: "Library & API Reference"
framework: "Custom Agents"
---

# AShareHub Chinese Market Data

AShareHub gives AI coding agents a documented interface to Chinese A-share and ETF market data. Use it when a workflow needs daily or real-time prices, valuations, company financial statements, dividends, analyst data, Stock Connect holdings, money flow, index constituents, ETF holdings, news, or technical indicators. The official skill maps natural-language requests to 47 API and Python SDK interfaces and documents each method's inputs and response fields. Public security identifiers use `symbol`, such as `000001.SZ`, `600519.SH`, or `000300.SH`, and SDK calls return pandas DataFrames for analysis, charting, or export. Access uses the hosted AShareHub API, so users must create an API key; a free tier provides 100 requests per day. See the [skill website](https://asharehub.com/en/skill), [API documentation](https://asharehub.com/en/docs), and [MCP setup](https://asharehub.com/en/docs/mcp-setup).

## Installation

Install the Python SDK and set the API key issued by AShareHub:

```bash
pip install asharehub
export ASHAREHUB_API_KEY="ash_your_key_here"
```

### Codex

```bash
git clone --depth 1 https://github.com/ChuYiCui1/AshareHub-skills.git
mkdir -p ~/.codex/skills/asharehub
cp -R AshareHub-skills/skills/en/. ~/.codex/skills/asharehub/
```

### Claude Code

```bash
git clone --depth 1 https://github.com/ChuYiCui1/AshareHub-skills.git
mkdir -p .claude/skills/asharehub
cp -R AshareHub-skills/skills/en/. .claude/skills/asharehub/
```

## Example

Ask the agent: "Use AShareHub to fetch CSI 300 daily prices since 2024-01-01 and summarize the monthly returns."

The underlying SDK call is:

```python
from asharehub import AShareHub
import os

client = AShareHub(api_key=os.environ["ASHAREHUB_API_KEY"], version="v2")
prices = client.index_daily(symbol="000300.SH", start_date="20240101")
print(prices[["trade_date", "close", "pct_chg"]])
client.close()
```
