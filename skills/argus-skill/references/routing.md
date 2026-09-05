# Routing durable context

Route by the record's owner and future reader, not by whichever noun appeared in the chat.

| Durable delta | Canonical surface | Secondary link |
|---|---|---|
| Promise, deadline, waiting on a person, changed current priority | Configured commitment system | Link the owning project anchor when one exists |
| Token/GPU budget, rate limit, account allocation, autonomous-run session record | Configured budget authority | Log canonical archive or repository artefacts, not duplicated prose |
| Personal or cross-domain project, relationship context, stable preference | Home archive | Commitment system only when action or custody changed |
| Hypothesis, experiment, result, literature, research mechanism | Research Archivum | Link the home project or programme anchor |
| Company governance, contracts, finance, legal, people operations | Admin Archivum | Link the home company/project anchor |
| Job role, application answer, evidence packet, pipeline state | Career/application archive | Link the home career anchor and commitment system if submission is actionable |
| Public article, website, release, or repository | Output record in its owning archive | Private home index may link outward; public material must not expose a private backlink |

## Split records without duplicating truth

A single event may create several different records. For example, an experiment result belongs in the research archive, the decision it triggered may belong in a programme record, the promised follow-up belongs in the commitment system, and GPU/session spend belongs in the budget ledger. Link them; do not paste the same narrative into all four.

## Resolve the archive's layout

After choosing an owner, read that archive's `config.yaml`. In version-2 Archivums, use the configured `directories.*` and `canonical_files.*` values rather than conventional numbered paths. Read `AGENTS.md` before mutation and keep the context load bounded to the configured profile, state, schema, and target record.

## Threshold for a new Archivum

Recommend a new archive only when at least one boundary is durable:

- a different audience or owner;
- materially different privacy or access rules;
- an independent lifecycle or release cadence;
- enough canonical records that continued routing into an existing archive would obscure ownership.

A new topic, project, or large folder is not by itself a new Archivum. Ask before creating or cloning one.

## Ambiguity rule

Prefer the archive already owning the project. If ownership remains genuinely ambiguous after reading the home registry and searching candidates, present the two plausible destinations and recommend one. Do not spray copies across archives to avoid choosing.
