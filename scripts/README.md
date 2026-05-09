# Scripts

Automation tooling for the Agent Skill Exchange repository.

## Available Scripts

### `validate-skill.sh`

Validates a `SKILL.md` file against the skill spec.

```bash
./scripts/validate-skill.sh path/to/SKILL.md
```

**Checks performed:**
- File exists and is non-empty
- YAML frontmatter is present (delimited by `---`)
- Required fields exist: `title`, `slug`, `description`, `category`, `framework`, `verification`
- `slug` matches the containing directory name
- Deprecated `name` frontmatter is not present
- Verification is a public value (`listed` or `security_reviewed`); internal `verified_metadata` must export as `listed`
- Body contains an H1 heading (`# `)

**Exit codes:** `0` on pass, `1` on fail with descriptive error messages.

### `generate-catalog.sh`

Regenerates `CATALOG.md` from the live Agent Skill Exchange WordPress REST API.

```bash
./scripts/generate-catalog.sh [repo_directory]
```

**What it does:**
- Fetches all skills and categories from the WP REST API (paginated)
- Generates `CATALOG.md` with summary stats and per-category skill tables
- Updates badge counts in `README.md`
- Handles HTML entity decoding in category and skill names

**Requirements:** `curl`, `jq`

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
