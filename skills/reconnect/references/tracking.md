# Private tracking and commands

Pass an explicit private database path to every command. The helper creates that
database with restrictive permissions; it never imports contact sources implicitly.
Resolve `SKILL_ROOT` to the installed reconnect directory before running commands.

```sh
python3 "$SKILL_ROOT/scripts/reconnect.py" --db /private/project/reconnect.sqlite3 import --input /private/project/candidates.json
python3 "$SKILL_ROOT/scripts/reconnect.py" --db /private/project/reconnect.sqlite3 prepare --batch review-001 --size 25
python3 "$SKILL_ROOT/scripts/reconnect.py" --db /private/project/reconnect.sqlite3 batch --batch review-001
python3 "$SKILL_ROOT/scripts/reconnect.py" --db /private/project/reconnect.sqlite3 authorize --batch review-001 --reference 'User message approving this exact batch'
python3 "$SKILL_ROOT/scripts/reconnect.py" --db /private/project/reconnect.sqlite3 observe --batch review-001 --url https://www.linkedin.com/in/example --kind relationship --value requested --evidence 'Profile-specific Pending readback'
python3 "$SKILL_ROOT/scripts/reconnect.py" --db /private/project/reconnect.sqlite3 status
```

Commands print JSON. `prepare` returns the same frozen batch on repeated invocation,
reserves destinations across batches, and rejects a changed size for an existing ID.
It reports when fewer candidates are available. Preparation includes unresolved
`review` candidates but clearly exposes eligibility and evidence; live review must
settle those before outreach. Active reservations exclude destinations from new
batches. Pending, contacted, held, blocked and ineligible destinations are excluded.

To preserve an existing prepared list, import its candidate records first, then use
`reserve --batch existing-001 --input /private/project/existing-urls.json`, where the
input is a JSON array of exact profile URLs. This preserves their order and refuses
overlap with another active batch. It can reserve already-contacted or excluded
records for historical reconciliation; reservation does not make them actionable.

An explicit `release --batch ID --url URL --reason TEXT` releases an unattempted or
resolved reservation. It refuses unresolved attempts. Release does not erase history
or undo a connection request. `observe` can also record `eligibility` (eligible,
review, excluded), `group` (invited, joined, unknown), or relationship states
(not_contacted, requested, pending, connected, uncertain, withheld, do_not_contact).
Observations attest to external evidence; they never perform external actions.

## Generic import JSON

An array of candidates; fields shown below are required except priority, which
defaults to zero. Evidence must contain at least one source reference.

```json
[
  {
    "url": "https://www.linkedin.com/in/example",
    "name": "Example Person",
    "source_ids": ["public:event-speaker-123"],
    "eligibility": "review",
    "relationship": "not_contacted",
    "priority": 30,
    "evidence": [{"source": "https://example.org/team", "claim": "Direct LinkedIn cross-link", "observed_at": "2026-09-05"}]
  }
]
```

Import merges duplicate destinations conservatively: blocked or contacted states
win over not_contacted, eligibility exclusions win, all source IDs and evidence are
retained. Source refreshes cannot silently clear local holds, exclusions, or observed
relationships. Use a new evidenced observation for a reviewed correction.
Group membership is recorded separately and never inferred from a connection.

## Project adapters and reconciliation

An optional project-local adapter translates authorised sources to the same JSON
format. Keep the adapter outside the installed skill, read its source without
mutation when possible, preserve source IDs and blocking states, and minimise the
personal data exported. The core has no built-in dependency on a particular CRM,
institution, community database, account, or machine path.

Include relevance and relationship context in evidence records when useful, for
example a sourced claim about the person's work or a pointer to the user's own
meeting note. A source ID may be a public profile/page identifier; no roster is needed.

The helper does not automatically update an upstream tracker. After live actions,
use the project's supported mutation API and append-only review events, then refresh
the imported view. Preserve the local outcome until that reconciliation is verified.
