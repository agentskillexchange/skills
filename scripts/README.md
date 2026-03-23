# Scripts

Automation tooling for the Agent Skill Exchange repository.

## Available Scripts

### `validate-skill.sh`

Validates a `SKILL.md` file against the Agent Skill Exchange format specification.

```bash
./scripts/validate-skill.sh path/to/SKILL.md
```

**Checks performed:**
- File exists and is non-empty
- YAML frontmatter is present (delimited by `---`)
- Required fields exist: `name`, `description`, `category`, `framework`, `verification.verified_metadata`, `verification.security_reviewed`, `rating`, `reviews`, `creator.name`
- Rating is a valid number between 1.0 and 5.0
- Body contains an H1 heading (`# `)

**Exit codes:** `0` on pass, `1` on fail with descriptive error messages.

### `generate-catalog.sh`

Regenerates `CATALOG.md` from the live Agent Skill Exchange WordPress REST API.

```bash
./scripts/generate-catalog.sh [repo_directory]
```

**What it does:**
- Fetches all skills and categories from the WP REST API (paginated)
- Generates `CATALOG.md` with summary stats and per-category skill tables sorted by rating
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
- Creates/updates `categories/<slug>/README.md` for each category with:
  - Skill listings sorted by rating
  - Install snippets for all supported agents
  - Links to related categories
- Handles HTML entity decoding

**Requirements:** `curl`, `jq`

## Usage in CI/Cron

These scripts are designed to be called from the GitHub sync cron job:

```bash
# After syncing new SKILL.md files:
./scripts/generate-catalog.sh /path/to/repo
./scripts/generate-categories.sh /path/to/repo
# Then commit and push the changes
```
