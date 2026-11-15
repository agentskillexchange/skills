---
name: "Extract SEC filings and XBRL financials with edgartools"
slug: "extract-sec-filings-and-xbrl-financials-with-edgartools"
description: "Use edgartools to fetch SEC EDGAR filings, parse 10-K/10-Q/8-K documents, and extract XBRL financial data for repeatable agent research workflows."
github_stars: 2754
verification: "security_reviewed"
source: "https://github.com/dgunning/edgartools"
author: "dgunning"
publisher_type: "individual"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "dgunning/edgartools"
  github_stars: 2754
---

# Extract SEC filings and XBRL financials with edgartools

Use edgartools to fetch SEC EDGAR filings, parse 10-K/10-Q/8-K documents, and extract XBRL financial data for repeatable agent research workflows.

## Prerequisites

Python, edgartools package, SEC-compliant identity email, network access to SEC EDGAR

## Installation

Install or set up from the source-backed instructions:

Install with pip install edgartools or uv pip install edgartools, set an SEC identity with set_identity("your.name@email.com"), then use the documented Python API such as Company("TSLA").get_filings(form="10-K").latest() to retrieve and parse filings.

- Source: https://github.com/dgunning/edgartools

## Documentation

- https://dgunning.github.io/edgartools/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/extract-sec-filings-and-xbrl-financials-with-edgartools/)
