# Local metadata contract (version 1)

The validator accepts one JSON object with the following required keys. Extra keys are allowed for project-specific extensions. Every unknown required value must be `null` and listed exactly in `missing`; strings such as “unknown” are not substitutes. Empty descriptive strings are invalid. This is a validation contract, not evidence collection.

| Key | Type / meaning |
|---|---|
| `schema_version` | Integer `1` |
| `run_id` | Nonempty string; stable execution identity |
| `created_at` | ISO 8601 timezone-aware timestamp, or null if historical birth is unknown |
| `recorded_at` | ISO 8601 timezone-aware timestamp for this record |
| `metadata_origin` | `birth` or `backfill` |
| `phase`, `variant`, `modality`, `dataset`, `reason` | Nonempty string or null |
| `notes` | String; may be empty |
| `repo_url`, `branch`, `commit`, `commit_url` | Nonempty string or null; validator does not access or validate remote objects |
| `dirty` | Boolean or null |
| `code_snapshot` | Nonempty string identifying preserved patch/tree artifact, or null; especially relevant if dirty |
| `seed` | Integer (not Boolean) or null |
| `config` | Nonempty string identifying resolved configuration artifact/hash, or null |
| `data` | Nonempty string identifying dataset revision and preprocessing/tokenizer artifact, or null |
| `tags` | Array of distinct nonempty strings |
| `missing` | Array listing exactly the required keys whose value is null |

`schema_version`, `run_id`, `recorded_at`, `metadata_origin`, `notes`, `tags`, and `missing` cannot be null. `created_at` must not be later than `recorded_at`. A birth record requires known `created_at`; a backfill may leave it unknown. The timestamps are claims supplied by the caller, not independently measured evidence.

Normal validation accepts explicit gaps and emits warnings. Strict mode rejects missing `created_at`, `phase`, `variant`, `modality`, `dataset`, `reason`, `commit`, `dirty`, `seed`, `config`, or `data`; when `dirty` is true it also requires `code_snapshot`. It does not require a public URL, branch (detached HEAD is valid), or unnecessary clean-worktree snapshot.

Suggested tracker mapping: phase/variant/modality/dataset/reason under a project-owned config namespace; `phase:*`, `variant:*`, `modality:*`, `dataset:*`, `seed:*` tags; notes in the provider's notes field; code/config/data identities in immutable metadata where supported. These mappings are recommendations, not implemented adapters. Tag-value consistency and remote persistence are not checked by the local validator.

Resume attempts should be appended under a project-specific extension with attempt ID, checkpoint source, timestamp, code identity, config identity, and changes since birth. Never rewrite birth code to the resumed code. There is no runtime enforcement or resume-schema validator in this release.
