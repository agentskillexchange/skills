# Scripts

Automation tooling for the Agent Skill Exchange repository.

## Available Scripts

### `validate_skills.py`

Parser-backed validator for one skill, a directory of skills, or the full catalog.

```bash
python3 scripts/validate_skills.py skills/playwright-mcp-browser-automation/SKILL.md
python3 scripts/validate_skills.py --all --github-annotations --quiet
```

`validate-skill.sh` remains as a compatibility wrapper around this script:

```bash
./scripts/validate-skill.sh path/to/SKILL.md
```

**Checks performed:**
- File exists, is non-empty, and is valid UTF-8
- YAML frontmatter is present and parsed with PyYAML
- Duplicate YAML keys are rejected
- Required fields exist and have the expected scalar types: `name`, `slug`, `description`, `category`, `framework`, `verification`
- `slug` is lowercase kebab-case and matches the containing directory name
- Deprecated `title` is allowed only as a temporary alias equal to `name`; internal fields are rejected: `verification_status`, `verified_metadata`
- `verification` is a public value (`listed` or `security_reviewed`); internal `verified_metadata` must export as `listed`
- Category and framework labels are validated against the known public taxonomy/framework sets
- `source` is URL-like when present
- Numeric signal fields are real numbers, not quoted strings
- `tool_ecosystem` is an object with typed optional fields
- Body contains an H1 heading and enough useful content
- GitHub Actions annotations are emitted with `--github-annotations`

**Requirement:** Python 3 + `PyYAML`.

**Exit codes:** `0` on pass, `1` on validation failure, `2` when PyYAML is unavailable.

### `security_scan.py` and `test_security_patterns.py`

Executable security pattern scanner and fixture test suite for the trust layer.

```bash
python3 scripts/test_security_patterns.py
python3 scripts/security_scan.py skills --github-annotations --quiet
```

`security_scan.py` loads machine-readable patterns from `verification/patterns.json` and scans Markdown files/directories. `test_security_patterns.py` verifies pattern compilation, required security classes, positive malicious fixtures, and a benign negative fixture under `verification/fixtures/security/`.

CI runs both the fixture suite and a full `skills/` catalog scan.

### `sync-from-api.sh` / `generate-all.sh`

Reproduces all generated public repo artifacts from the public ASE API, without OpenClaw or Hostinger paths.

```bash
ASE_API_BASE=https://agentskillexchange.com ./scripts/sync-from-api.sh
# or directly:
ASE_API_BASE=https://agentskillexchange.com ./scripts/generate-all.sh [repo_directory]
```

Generated artifacts include `README.md`, `CATALOG.md`, `categories/`, `industries/`, `TOP-STARS.md`, `TOP-DOWNLOADS.md`, `skills.json`, public agent endpoint files (`openclaw.json`, `codex.json`, `llms.txt`), agent manifest files, and `sync-metadata.json`.

`sync-metadata.json` records:
- `generated_at`
- `source_api_base`
- `source_total`
- `source_etag_or_hash` (SHA-256 of generated `skills.json`)
- `generator_version`
- `schema_version`

### Public agent endpoints

`generate-agent-endpoints.py` uses the canonical generated `skills.json` to write static, cacheable agent discovery files:

```bash
python3 scripts/generate-agent-endpoints.py [repo_directory]
python3 scripts/smoke-agent-endpoints.py --base https://agentskillexchange.com
```

Live endpoint contract:
- `/skills.json` — full canonical public catalog (`application/json`)
- `/openclaw.json` — OpenClaw-oriented manifest (`application/json`)
- `/codex.json` — Codex-oriented manifest (`application/json`)
- `/llms.txt` — concise agent/human discovery document (`text/plain`)
- cache header: `Cache-Control: public, max-age=300, stale-while-revalidate=86400`

### `generate-catalog.sh`

Regenerates `CATALOG.md` from the public Agent Skill Exchange WordPress REST API.

```bash
ASE_API_BASE=https://agentskillexchange.com ./scripts/generate-catalog.sh [repo_directory]
```

**What it does:**
- Fetches all skills and categories from the WP REST API (paginated)
- Generates `CATALOG.md` with summary stats and per-category skill tables
- Handles HTML entity decoding in category and skill names

**Requirements:** Python 3

### `generate-categories.sh`

Regenerates per-category `README.md` files in the `categories/` directory.

```bash
./scripts/generate-categories.sh [repo_directory]
```

**What it does:**
- Fetches all skills and the category taxonomy from the WP REST API
- Creates/updates `categories/README.md` (index of all categories)
- Creates/updates `categories/<slug>/README.md` for each category
- Handles HTML entity decoding

**Requirements:** `curl`, `jq`
