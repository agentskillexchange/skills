# 💼 Finance & Filings

Filings research, invoice intake, billing operations, reconciliation, and finance-adjacent reporting.

- Live page: https://agentskillexchange.com/industry-skills/#finance-filings
- Homepage access: Curated Collections on https://agentskillexchange.com/

## Who this is for

- Finance operators, founders, RevOps teams, and analysts who need evidence-backed filings, invoice, billing, and reconciliation workflows.
- Teams that receive messy PDFs, CSV exports, payment processor data, or portfolio records and need repeatable extraction before analysis.

## Jobs covered

- Pull SEC filing data and source documents for review packets.
- Extract invoice fields and PDF tables into structured records.
- Reconcile payments, invoices, subscriptions, and usage-metered revenue.
- Profile CSV exports before loading them into spreadsheets, warehouses, or dashboards.
- Build finance-facing reports without inventing a full data platform first.

## Workflow Stacks

- **Invoice intake to review:** OCR or parse vendor PDFs → extract invoice fields → diff recurring exports → send exceptions to accounting
- **Usage billing operations:** Meter product usage → map usage to customers → reconcile Stripe revenue → publish finance dashboard
- **Filing research packet:** Collect EDGAR filings → extract tables → query local CSV/JSON/PDF outputs → summarize with source links

## Recommended Picks

| Skill | What it does here | Persona | Install | Stars |
|---|---|---|---|---:|
| [SEC EDGAR Financial Filing Parser](../skills/sec-edgar-financial-filing-parser/) | Anchors filing research with EDGAR search, company filing APIs, and XBRL-oriented extraction. | Analyst / finance researcher | Medium | — |
| [Extract invoice fields from vendor PDFs into structured records](../skills/extract-invoice-fields-from-vendor-pdfs-into-structured-records/) | Turns recurring vendor invoices into structured records before approval, coding, or reconciliation. | AP ops / finance analyst | Medium | 2.1k |
| [QuickBooks Online Invoice Reconciliation Agent](../skills/quickbooks-invoice-reconciliation/) | Connects invoice state to accounting-system reconciliation instead of stopping at document extraction. | Bookkeeper / finance ops | High | — |
| [OpenMeter Usage Metering and Billing Platform](../skills/openmeter-usage-metering-and-billing-platform/) | Covers usage metering and entitlement data needed before usage-based billing can be trusted. | RevOps / billing engineer | High | 1.9k |
| [Stripe Reporting Agent](../skills/stripe-reporting-agent/) | Keeps Stripe coverage focused on operational reporting rather than generic payment API access. | RevOps / finance analyst | Medium | 4.4k |
| [Stripe Revenue Reconciliation Agent](../skills/stripe-revenue-reconciliation-agent/) | Pulls charges, refunds, disputes, and payouts into a reconciliation workflow with finance-facing evidence. | Revenue accountant / RevOps | Medium | 4.4k |
| [Ghostfolio Open Source Wealth Management and Portfolio Tracking Platform](../skills/ghostfolio-wealth-management-portfolio-tracking/) | Adds portfolio tracking for investment and asset reporting workflows beyond payments and invoices. | Portfolio operator / finance analyst | High | 8.1k |
| [pdfplumber Python PDF Text and Table Extraction Library](../skills/pdfplumber-python-pdf-text-table-extraction/) | Extracts tables and layout-aware text from financial PDFs that are not invoice-shaped. | Analyst / data wrangler | Medium | 10.1k |
| [Tabula PDF Table Extractor](../skills/tabula-pdf-table-extractor/) | Gives teams a focused table-extraction path for statements, filings, and PDF schedules. | Analyst / reporting ops | Medium | 2k |
| [Turn messy document collections into structured rows with DocETL](../skills/turn-messy-document-collections-into-structured-rows-with-docetl/) | Moves document-heavy finance work from one-off prompts into repeatable extraction pipelines. | Data analyst / ops engineer | High | 3.7k |
| [DuckDB SQL Analytics Agent](../skills/duckdb-sql-analytics-agent/) | Lets analysts query local CSV, Parquet, and JSON exports quickly without standing up a warehouse. | Finance analyst / analytics engineer | Low | 37.1k |
| [trdsql SQL Query Engine for CSV JSON and YAML Files](../skills/trdsql-sql-query-engine-csv-json-yaml-files/) | Supports quick SQL checks over exported files when reconciliation questions start as CSV or JSON. | Ops analyst / data wrangler | Low | 2.2k |
| [Profile and clean large CSV datasets from the terminal with qsv](../skills/profile-and-clean-large-csv-datasets-from-the-terminal-with-qsv/) | Profiles and cleans large exports before spreadsheet review or warehouse load. | Finance analyst / data ops | Low | 3.6k |
| [Compare recurring CSV, TSV, or JSON exports and emit row-level change sets before syncs](../skills/compare-recurring-csv-tsv-or-json-exports-and-emit-row-level-change-sets-before-syncs/) | Explains row-level differences between recurring exports, which is core to reconciliation review. | Finance ops / QA analyst | Low | 330 |
| [Run persistent finance research workspaces with LangAlpha](../skills/run-persistent-finance-research-workspaces-with-langalpha/) | Creates persistent finance research workspaces where filings, market data, models, charts, and thesis notes stay organized across analysis passes. | Investment analyst / finance researcher | High | 1.2k |
| [Apache Superset Dashboard and SQL Exploration Skill](../skills/apache-superset-dashboard-sql-exploration-skill/) | Turns cleaned finance datasets into shareable dashboards and SQL-backed reporting views. | Analytics engineer / finance lead | High | 72.3k |
| [Create, repair, and recalculate spreadsheet workbooks without breaking formulas](../skills/create-repair-and-recalculate-spreadsheet-workbooks-without-breaking-formulas/) | Creates and repairs workbook models while preserving formulas, which is central to finance reporting and reconciliation handoffs. | Finance analyst / spreadsheet ops | Medium | 116.9k |
| [Metabase Dashboard Snapshot & Alerting](../skills/metabase-dashboard-snapshot-alerting-2/) | Captures dashboard snapshots and alerts so finance teams can monitor recurring metrics without manually checking reports. | Finance analytics engineer / ops lead | Medium | — |

## Editorial Notes

- The collection is intentionally not a Stripe shelf: Stripe appears only where it represents a differentiated reporting or reconciliation workflow.
- Listed-but-domain-specific picks remain when there is no stronger security-reviewed substitute for the finance job, especially EDGAR and QuickBooks workflows.
- Prefer tools that leave auditable intermediate files over black-box financial advice or autonomous money movement.
- Frame Stripe-based entries as revenue-ops and billing workflows, not generic payment tooling.

## Adjacent Collections

- [Legal Ops & Compliance](legal-ops-compliance.md)
- [Product Analytics & Growth Ops](product-analytics-growth-ops.md)
- [Ecommerce & Retail Operations](ecommerce-retail-operations.md)

---

[← Back to industry collections](README.md)
