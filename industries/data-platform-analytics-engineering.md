# 🗄️ Data Platform & Analytics Engineering

Data engineering and analytics operations workflows for SQL, dbt, Airflow, warehouses, Postgres, CSV cleanup, schema quality, retrieval indexes, data catalogs, dashboards, and query tuning.

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
- Build and evaluate retrieval, vector, and catalog context before agents consume data assets.

## Workflow Stacks

- **Agent-safe data operations:** Inspect database or DAG context → Review permissions and query scope → Run controlled analysis → Record evidence for the operator
- **Analytics engineering change review:** Plan dbt or SQL model change → Lint and validate SQL → Compare model or relation parity → Preview rollout impact
- **Warehouse and database performance:** Inspect schema and execution plans → Tune query, index, or RLS behavior → Document risky migrations → Hand off a review packet
- **Tabular intake and cleanup:** Inspect large CSV or messy tables → Profile schema and anomalies → Normalize for downstream transforms → Validate quality before ingestion

## Recommended Picks

| Skill | What it does here | Persona | Install | Stars |
|---|---|---|---|---:|
| [Query and inspect Postgres databases through MCP with pgEdge Postgres MCP](../skills/query-and-inspect-postgres-databases-through-mcp-with-pgedge-postgres-mcp/) | Gives agents a controlled Postgres inspection path for schema, table, and query context without turning database access into ad hoc shell work. | Postgres operator / data platform engineer | Medium | 165 |
| [Query cross-connector business data for agents with Dinobase](../skills/query-cross-connector-business-data-for-agents-with-dinobase/) | Lets data teams query business context across connectors when analytics questions span tools rather than one warehouse table. | Analytics platform engineer | Medium | 252 |
| [Review SQL Server execution plans through an MCP-compatible analysis workflow with Performance Studio](../skills/review-sql-server-execution-plans-through-an-mcp-compatible-analysis-workflow-with-performance-studio/) | Adds SQL Server execution-plan review to the workflow for query tuning and database performance investigations. | Database performance engineer | Medium | 175 |
| [Run deterministic SQL and dbt analysis under coding agents with Altimate Code](../skills/run-deterministic-sql-and-dbt-analysis-under-coding-agents-with-altimate-code/) | Keeps SQL and dbt analysis deterministic under coding agents, which matters when agents review warehouse changes. | Analytics engineering lead | Medium | 552 |
| [Operate Airflow and warehouse workflows through agent-safe data engineering skills with Astronomer Agents](../skills/operate-airflow-and-warehouse-workflows-through-agent-safe-data-engineering-skills-with-astronomer-agents/) | Connects Airflow and warehouse operations through agent-safe data engineering workflows instead of unbounded DAG manipulation. | Data platform engineer | High | 337 |
| [Tune Supabase Postgres queries, indexing, and RLS with Supabase Postgres Best Practices](../skills/tune-supabase-postgres-queries-indexing-and-rls-with-supabase-postgres-best-practices/) | Covers Supabase/Postgres query, index, and RLS tuning where app data teams need database advice tied to production constraints. | Supabase/Postgres engineer | Medium | — |
| [Compare dbt models and warehouse relations before trusting migration parity with dbt-audit-helper](../skills/compare-dbt-models-and-warehouse-relations-before-trusting-migration-parity-with-dbt-audit-helper/) | Checks dbt model and warehouse parity before migrations or refactors are trusted. | Data quality lead | Medium | 402 |
| [Translate and validate SQL across dialects with SQLGlot](../skills/translate-and-validate-sql-across-dialects-with-sqlglot/) | Translates and validates SQL across dialects so warehouse migrations and multi-engine analytics work stay reviewable. | Data engineer / migration reviewer | Low | 9.1k |
| [Lint PostgreSQL migrations and SQL changes before irreversible schema mistakes land with Squawk](../skills/lint-postgresql-migrations-and-sql-changes-before-irreversible-schema-mistakes-land-with-squawk/) | Catches risky PostgreSQL migration patterns before irreversible schema mistakes land. | Database operator | Low | 1.1k |
| [Inspect large CSV files interactively before cleanup, mapping, or downstream transforms with csvlens](../skills/inspect-large-csv-files-interactively-before-cleanup-mapping-or-downstream-transforms-with-csvlens/) | Provides interactive inspection of large CSV files before teams map, clean, or ingest messy tabular data. | Data operations analyst | Low | 3.7k |
| [Profile and triage messy tabular files from the terminal with VisiData](../skills/profile-and-triage-messy-tabular-files-from-the-terminal-with-visidata/) | Helps analysts profile and triage messy tabular files quickly before building downstream transforms. | Data analyst / data wrangler | Low | 9k |
| [Plan and preview warehouse SQL model changes before rollout with SQLMesh](../skills/plan-and-preview-warehouse-sql-model-changes-before-rollout-with-sqlmesh/) | Adds plan-and-preview discipline for warehouse SQL model changes before rollout. | Analytics engineer / warehouse reviewer | Medium | 3k |
| [Apache Airflow MCP](../skills/apache-airflow-mcp/) | Connects agents to Airflow DAG context and orchestration workflows for platform-owned pipelines. | Data platform engineer | High | 45k |
| [dbt Cloud MCP](../skills/dbt-cloud-mcp/) | Lets agents inspect and operate dbt Cloud context without treating the warehouse as a black box. | Analytics engineer | Medium | 12.6k |
| [dbt Data Transform Orchestrator](../skills/dbt-data-transform-orchestrator/) | Frames dbt model runs and transformation orchestration as a repeatable analytics engineering workflow. | Analytics engineer | Medium | 12.6k |
| [dbt Model Lineage Extractor](../skills/dbt-model-lineage-extractor-2/) | Extracts model lineage so teams can reason about downstream impact before changing data assets. | Analytics platform owner | Medium | 12.6k |
| [Gate dbt projects with pre-commit checks from dbt-checkpoint](../skills/gate-dbt-projects-with-pre-commit-checks-from-dbt-checkpoint/) | Adds pre-commit gates for dbt projects before style, tests, or docs drift. | Analytics engineering reviewer | Low | 738 |
| [SQLFluff SQL Linter and Auto-Formatter](../skills/sqlfluff-sql-linter-auto-formatter/) | Lints and formats SQL so warehouse changes are reviewable and consistent. | Data engineer | Low | 9.6k |
| [sqruff High-Performance SQL Linter and Formatter](../skills/sqruff-sql-linter-formatter/) | Provides a fast SQL lint/format path for teams that need lightweight query quality checks. | Analytics engineer | Low | 1.3k |
| [DuckDB SQL Analytics Agent](../skills/duckdb-sql-analytics-agent/) | Runs local analytics over structured files for fast investigation without provisioning a warehouse. | Data analyst / analytics engineer | Low | 37.1k |
| [trdsql SQL Query Engine for CSV JSON and YAML Files](../skills/trdsql-sql-query-engine-csv-json-yaml-files/) | Queries CSV, JSON, and YAML exports with SQL before loading them into a larger system. | Data operations analyst | Low | 2.2k |
| [Anyquery Universal SQL Engine with MCP Integration](../skills/anyquery-universal-sql-engine-mcp-integration/) | Turns many APIs and files into SQL-queryable surfaces for agents and data operators. | Data platform engineer | Medium | 1.7k |
| [Great Expectations Data Validation Pipeline](../skills/great-expectations-data-validation-pipeline/) | Creates explicit data quality expectations and validation artifacts for pipelines. | Data quality engineer | Medium | 11.3k |
| [Inventory live database schemas and generate reviewable docs before risky SQL changes with SchemaCrawler](../skills/inventory-live-database-schemas-and-generate-reviewable-docs-before-risky-sql-changes-with-schemacrawler/) | Inventories live schemas and produces reviewable docs before risky SQL or database changes. | Database platform engineer | Medium | 1.8k |
| [Build local vector retrieval indexes with Faiss](../skills/build-local-vector-retrieval-indexes-with-faiss/) | Adds a local vector-indexing layer for retrieval and RAG experiments before teams adopt heavier managed vector infrastructure. | Data platform engineer / retrieval engineer | Medium | 40.2k |
| [Expose data catalog context to AI workflows with DataHub](../skills/expose-data-catalog-context-to-ai-workflows-with-datahub/) | Grounds agent-assisted data discovery in catalog metadata, ownership, schema, and lineage context. | Data governance lead / analytics platform engineer | High | 12.1k |
| [Query ClickHouse analytics safely from MCP clients](../skills/query-clickhouse-analytics-safely-from-mcp-clients/) | Gives agents bounded, schema-aware ClickHouse analytics access without handing them ad hoc database credentials. | Analytics platform engineer / ClickHouse operator | Medium | 801 |
| [Serve production agentic RAG through R2R](../skills/serve-production-agentic-rag-through-r2r/) | Provides production hybrid retrieval and agentic RAG APIs with citations and reviewable document operations. | Retrieval engineer / data platform lead | High | 7.9k |
| [Build document search layers for AI apps with Morphik](../skills/build-document-search-layers-for-ai-apps-with-morphik/) | Adds document ingestion and search quality tuning before AI apps or agents consume retrieval context. | Retrieval engineer / AI data platform builder | High | 3.6k |
| [Parse multi-format RAG inputs with OmniParse](../skills/parse-multi-format-rag-inputs-with-omniparse/) | Converts PDFs, tables, images, audio, video, and web pages into structured text/markdown so RAG pipelines receive reviewable multi-format inputs. | Retrieval engineer / data ingestion platform owner | High | 7.6k |
| [Add Postgres-native vector retrieval to agent and RAG workflows with pgvector](../skills/add-postgres-native-vector-retrieval-to-agent-and-rag-workflows-with-pgvector/) | Stores embeddings beside application data in Postgres for semantic search, RAG, recommendations, and agent memory retrieval. | Postgres data platform engineer / retrieval engineer | Medium | 21.7k |
| [Generate and evaluate retrieval embeddings with FlagEmbedding](../skills/generate-and-evaluate-retrieval-embeddings-with-flagembedding/) | Helps teams choose, evaluate, and rerank retrieval embeddings before feeding context into RAG workflows. | Retrieval engineer / ML platform engineer | Medium | 11.8k |
| [Scale agent retrieval workloads with Milvus](../skills/scale-agent-retrieval-workloads-with-milvus/) | Adds a scalable vector database path for filtered similarity search across RAG and agent retrieval workloads. | Vector database operator / data platform engineer | High | 44.7k |
| [Build enterprise RAG and agent workflows with Bisheng](../skills/build-enterprise-rag-and-agent-workflows-with-bisheng/) | Assembles and evaluates enterprise RAG workflows across internal data, models, and business users. | Enterprise AI platform lead / retrieval workflow owner | High | 11.4k |

## Editorial Notes

- This collection spans Data Extraction, Code Quality, Runbooks, and dashboarding because data platform work is both engineering and operations.
- Several dbt picks are included, but each covers a different job: orchestration, parity, lineage, pre-commit gates, and formatting.
- Listed SchemaCrawler is included because live schema inventory is a distinct database-operations gap not covered by the security-reviewed data picks.
- Recent RAG and vector-database picks are included when they serve data-platform ownership: retrieval quality, catalog grounding, and production data access.
- Keep this centered on data platform and analytics engineering workflows; do not turn it into a generic Data Extraction category page.

## Adjacent Collections

- [Finance & Filings](finance-filings.md)
- [Product Analytics & Growth Ops](product-analytics-growth-ops.md)
- [Infrastructure, SRE & Incident Operations](infrastructure-sre-incident-operations.md)
- [Education & Research Workflows](education-research-workflows.md)

---

[← Back to industry collections](README.md)
