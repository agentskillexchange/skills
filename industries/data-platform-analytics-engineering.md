# 🗄️ Data Platform & Analytics Engineering

Data engineering and analytics operations workflows for SQL, dbt, Airflow, warehouses, Postgres, CSV cleanup, schema quality, backups, lineage, dashboards, and query tuning.

- Live page: https://agentskillexchange.com/industry-skills/#data-platform-analytics-engineering
- Homepage access: Curated Collections on https://agentskillexchange.com/

## Who this is for

- Data engineers, analytics engineers, data platform teams, BI operators, and database reliability owners.
- Teams managing dbt projects, SQL quality, warehouse performance, CSV cleanup, pipeline orchestration, schema review, dashboards, and database operations.

## Jobs covered

- Operate Airflow and dbt context for pipeline orchestration, lineage, and transformation review.
- Lint, format, and validate SQL, dbt, CSV, and schema changes before they break downstream consumers.
- Profile local files and query structured exports before loading them into warehouses or dashboards.
- Tune PostgreSQL and Snowflake performance while preserving backup and restore readiness.

## Workflow Stacks

- **dbt change review:** Inspect lineage → compare warehouse relations → format SQL/Jinja → run dbt checks → publish review notes
- **CSV to trusted dataset:** Profile raw files → validate schema → clean rows → query locally with SQL → promote to pipeline
- **Warehouse reliability loop:** Detect slow queries → lint migrations → inventory schemas → optimize warehouse queries → verify backup path

## Recommended Picks

| Skill | What it does here | Persona | Install | Stars |
|---|---|---|---|---:|
| [Apache Airflow MCP](../skills/apache-airflow-mcp/) | Connects agents to Airflow DAG context and orchestration workflows for platform-owned pipelines. | Data platform engineer | High | 45k |
| [dbt Cloud MCP](../skills/dbt-cloud-mcp/) | Lets agents inspect and operate dbt Cloud context without treating the warehouse as a black box. | Analytics engineer | Medium | 12.6k |
| [dbt Data Transform Orchestrator](../skills/dbt-data-transform-orchestrator/) | Frames dbt model runs and transformation orchestration as a repeatable analytics engineering workflow. | Analytics engineer | Medium | 12.6k |
| [Compare dbt models and warehouse relations before trusting migration parity with dbt-audit-helper](../skills/compare-dbt-models-and-warehouse-relations-before-trusting-migration-parity-with-dbt-audit-helper/) | Checks dbt model and warehouse parity before migrations or refactors are trusted. | Data quality lead | Medium | 402 |
| [dbt Model Lineage Extractor](../skills/dbt-model-lineage-extractor-2/) | Extracts model lineage so teams can reason about downstream impact before changing data assets. | Analytics platform owner | Medium | 12.6k |
| [Gate dbt projects with pre-commit checks from dbt-checkpoint](../skills/gate-dbt-projects-with-pre-commit-checks-from-dbt-checkpoint/) | Adds pre-commit gates for dbt projects before style, tests, or docs drift. | Analytics engineering reviewer | Low | 738 |
| [Normalize dbt SQL and Jinja templates into consistent review-ready style with sqlfmt](../skills/normalize-dbt-sql-and-jinja-templates-into-consistent-review-ready-style-with-sqlfmt/) | Normalizes dbt SQL and Jinja into review-ready form before warehouse changes merge. | Analytics engineer | Low | 530 |
| [SQLFluff SQL Linter and Auto-Formatter](../skills/sqlfluff-sql-linter-auto-formatter/) | Lints and formats SQL so warehouse changes are reviewable and consistent. | Data engineer | Low | 9.6k |
| [sqruff High-Performance SQL Linter and Formatter](../skills/sqruff-sql-linter-formatter/) | Provides a fast SQL lint/format path for teams that need lightweight query quality checks. | Analytics engineer | Low | 1.3k |
| [DuckDB SQL Analytics Agent](../skills/duckdb-sql-analytics-agent/) | Runs local analytics over structured files for fast investigation without provisioning a warehouse. | Data analyst / analytics engineer | Low | 37.1k |
| [trdsql SQL Query Engine for CSV JSON and YAML Files](../skills/trdsql-sql-query-engine-csv-json-yaml-files/) | Queries CSV, JSON, and YAML exports with SQL before loading them into a larger system. | Data operations analyst | Low | 2.2k |
| [Anyquery Universal SQL Engine with MCP Integration](../skills/anyquery-universal-sql-engine-mcp-integration/) | Turns many APIs and files into SQL-queryable surfaces for agents and data operators. | Data platform engineer | Medium | 1.7k |
| [Profile and clean large CSV datasets from the terminal with qsv](../skills/profile-and-clean-large-csv-datasets-from-the-terminal-with-qsv/) | Profiles and cleans large CSV files before ingestion, reconciliation, or dashboarding. | Data operations engineer | Low | 3.6k |
| [CSV Schema Validator & Auto-Fixer](../skills/csv-schema-validator-auto-fixer/) | Validates and fixes CSV schema issues before messy files pollute pipelines. | Data quality analyst | Low | 14.7k |
| [csvkit Python CSV Utility Suite](../skills/csvkit-python-csv-utility-suite/) | Adds a standard command-line CSV toolbox for inspection, conversion, and quick joins. | Data analyst | Low | 6.4k |
| [Great Expectations Data Validation Pipeline](../skills/great-expectations-data-validation-pipeline/) | Creates explicit data quality expectations and validation artifacts for pipelines. | Data quality engineer | Medium | 11.3k |
| [Lint PostgreSQL migrations and SQL changes before irreversible schema mistakes land with Squawk](../skills/lint-postgresql-migrations-and-sql-changes-before-irreversible-schema-mistakes-land-with-squawk/) | Catches risky PostgreSQL migration patterns before irreversible schema mistakes land. | Database operator | Low | 1.1k |
| [Inventory live database schemas and generate reviewable docs before risky SQL changes with SchemaCrawler](../skills/inventory-live-database-schemas-and-generate-reviewable-docs-before-risky-sql-changes-with-schemacrawler/) | Inventories live schemas and produces reviewable docs before risky SQL or database changes. | Database platform engineer | Medium | 1.8k |
| [PostgreSQL Slow Query Analyzer](../skills/postgresql-slow-query-analyzer/) | Finds slow PostgreSQL queries and suggests tuning targets from live database evidence. | Database operator / SRE | Medium | 13.1k |
| [Orchestrate database backup, restore, retention, and failure-notification runbooks through Databasement](../skills/orchestrate-database-backup-restore-retention-and-failure-notification-runbooks-through-databasement/) | Covers database backup, restore, retention, and failure notification as part of data platform operations. | Database reliability owner | Medium | 315 |
| [Schedule and retain cross-database backups from one self-hosted control plane with Databasus](../skills/schedule-and-retain-cross-database-backups-from-one-self-hosted-control-plane-with-databasus/) | Schedules and retains database backups across systems from one control plane. | Data platform operator | Medium | 6.6k |
| [Metabase Dashboard Snapshot & Alerting](../skills/metabase-dashboard-snapshot-alerting-2/) | Turns dashboards into scheduled snapshots and alerts for analytics operations. | Analytics operations lead | Medium | — |
| [Apache Superset Dashboard and SQL Exploration Skill](../skills/apache-superset-dashboard-sql-exploration-skill/) | Supports SQL exploration and dashboard workflows for BI and analytics teams. | Analytics engineer / BI operator | Medium | 72.3k |
| [Snowflake Query Optimizer Agent](../skills/snowflake-query-optimizer-agent/) | Optimizes Snowflake queries so warehouse cost and performance issues are visible before they grow. | Warehouse performance engineer | Medium | 724 |

## Editorial Notes

- This collection spans Data Extraction, Code Quality, Runbooks, and dashboarding because data platform work is both engineering and operations.
- Several dbt picks are included, but each covers a different job: orchestration, parity, lineage, pre-commit gates, and formatting.
- Listed SchemaCrawler is included because live schema inventory is a distinct database-operations gap not covered by the security-reviewed data picks.
- Keep this centered on data platform and analytics engineering workflows; do not turn it into a generic Data Extraction category page.

## Adjacent Collections

- [Finance & Filings](finance-filings.md)
- [Product Analytics & Growth Ops](product-analytics-growth-ops.md)
- [Infrastructure, SRE & Incident Operations](infrastructure-sre-incident-operations.md)
- [Education & Research Workflows](education-research-workflows.md)

---

[← Back to industry collections](README.md)
