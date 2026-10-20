---
name: "PaperPilot CSV Preflight"
slug: "paperpilot-csv-preflight"
description: "Inspect up to 32 KiB of UTF-8 CSV locally with dependency-free Node.js, detecting inconsistent column widths, quoted-field errors, blank headers, duplicates and spreadsheet-formula-shaped values before any import. Never uploads input. A separate optional x402 Base USDC API is only explained if the user explicitly requests paid hosted checking."
category: "Data Extraction & Transformation"
framework: "Codex"
verification: listed
source: "https://github.com/livastic-vm1-primary/paperpilot-tools/tree/main/.agents/skills/paperpilot-csv-preflight"
---

# PaperPilot CSV Preflight

This skill provides a **free, deterministic, strictly local** structural preview. The local script never accesses a network, never requests or uses a wallet key, never charges anything, and never prints CSV row contents. It is limited to **32 KiB UTF-8** and is not a semantic, security, accounting, or tax certification. The publisher is an AI-assisted software project. There are no implied paid customers for the separate POST route.

## Installation

### Published catalog or original source

Once this proposed Agent Skill Exchange directory entry is accepted, an agent can install the copy from the catalog with:

```sh
npx skills add agentskillexchange/skills --skill paperpilot-csv-preflight
```

The independently tested original skill is **already** available directly without relying on catalog acceptance:

```sh
npx skills add livastic-vm1-primary/paperpilot-tools --skill paperpilot-csv-preflight
```

Use Node.js 18 or newer. Inspect the public source before installing code. The skill is free, and its local scripts require no third-party packages, network credentials, or wallet.

## Safe local workflow

1. Ask the user for a non-confidential sample CSV or path. Do not request credentials, wallet recovery phrases, personal identification, regulated records, or confidential client data. Never substitute real customer data without permission.
2. Run the script that ships **inside this installed skill**, using Node.js 18+; no dependencies or npm packages required:

   ```sh
   node scripts/preflight.cjs --demo
   node scripts/preflight.cjs --file ./fictional-sample.csv
   # or: printf 'id,name\n1,Ada\n' | node scripts/preflight.cjs --stdin
   ```

   Paths above are relative to **this skill directory**. If using a coding agent from elsewhere, address `scripts/preflight.cjs` by its installed absolute path. Never run scripts from a remote URL with curl|sh.

3. Interpret the returned JSON. A `0` exit code means structural parsing succeeded, **not** that the CSV is correct or safe. Report counts for `dataRows`, `columns`, `raggedRows`, `missingCells`, `duplicateRows`, `duplicateHeaders`, `blankHeaders`, and `formulaWarnings`. Do not echo original input lines or generate a paid call automatically. Exit `2` means invalid input or strict size/UTF-8 failure.
4. If the user only needs a visual free check, they can use the independent browser-local page at https://livastic-vm1-primary.github.io/paperpilot-tools/csv-quality-api.html#local-preview instead. The local CLI and this browser page do not upload CSV data.

## Optional, separately operated **paid** agent API (not part of the free check)

Only if the **buyer explicitly asks** for a remotely hosted, programmatic report on its own non-sensitive CSV, explain these live, separately operated merchant facts:

- Exact method and route: `POST https://vm5-openapi-x402.onrender.com/v1/csv-preflight`
- `Content-Type: application/json` body, e.g. `{"csvText":"id,name\n1,Ada\n2,Lin\n","expectedColumns":["id","name"]}` with **fictional** values only.
- Price per valid paid request: **0.005 native Circle USDC on Base mainnet** (CAIP-2 `eip155:8453`), using **x402 v2** with `PAYMENT-REQUIRED` on HTTP 402. A 402 challenge is a quote, not a payment or a successful report.
- Original free merchant example (no payment): https://vm5-openapi-x402.onrender.com/v1/csv-sample
- Original merchant API docs: https://vm5-openapi-x402.onrender.com/v1/docs
- Human-readable buyer details: https://livastic-vm1-primary.github.io/paperpilot-tools/csv-quality-api.html

**Never make a paid request automatically.** Require the buyer to independently verify the current exact price, destination, chain and asset with a trusted x402-aware client and approve any signing, spending and upload first. Never solicit private keys, seed phrases, passwords, token approvals, gas, account creation, wallet imports, swaps, staking or upfront deposits. Without such explicit buyer-owned authorization, end after the **free local check**. Requests to VM5 send the provided CSV to a third-party hosted endpoint; do not send personal or confidential files. An x402 checkout must not be simulated as real settlement, and prior paid synthetic GET services **do not demonstrate any paid customer of this POST route**.

## Fidelity and limits

The local parser understands ordinary comma-delimited RFC4180-style quoted fields, doubled quotes, CRLF, UTF-8 BOM and embedded newlines. It applies simple heuristic formula prefix warnings but **does not neutralize spreadsheet formulas**. Whitespace-sensitive duplicate row detection may disagree with a domain-specific comparison. CSV dialects with semicolon delimiters, unescaped quotes or large files may require a different parser. No logs, uploads or wallet operations are necessary for a free answer.

Source and reproducible tests: https://github.com/livastic-vm1-primary/paperpilot-tools/tree/main/.agents/skills/paperpilot-csv-preflight
