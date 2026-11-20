# Evidence policy

Use this policy whenever converting conversation into decisions, actions, recommendations, or durable memory.

## Source boundary

Treat only the supplied conversation and explicitly supplied attachments as source evidence. General reasoning may organize or challenge that evidence, but must not masquerade as something participants said.

If external research is requested:

1. separate `Source-derived analysis` from `External context`;
2. cite the external sources;
3. explain whether the external information changes any recommendation;
4. never backfill missing participant intent with outside facts.

## Evidence ledger

Build this structure internally before writing the final document. Render it only when useful or requested.

| Field | Meaning |
|---|---|
| ID | Stable local identifier such as `E01` |
| Type | fact, proposal, decision, commitment, concern, hypothesis, disagreement, unknown |
| Claim | Faithful paraphrase of the smallest meaningful claim |
| Speaker | Named speaker, role, group, or `Unknown` |
| Locator | Line range, timestamp, message ID, page, or source name |
| Status | explicit, strong inference, tentative inference, contested, unknown |
| Conditions | Dependencies, qualifications, or expiry conditions |
| Sensitivity | private, internal, shareable, or unknown |

Keep excerpts short. Prefer locators plus faithful paraphrase over copying large passages.

## Classification rules

### Decision

Record a decision only when the source shows a selection, authorization, or settled direction. Distinguish:

- proposed;
- tentatively agreed;
- decided;
- superseded;
- reversed;
- rejected.

Statements such as “we could,” “maybe,” and “I like that” are not decisions by themselves.

### Commitment

Require an accountable actor plus an intended action. Capture stated deadlines and conditions. If the actor is missing, classify the item as an unassigned action rather than a commitment.

Do not treat silence, enthusiasm, reactions, or meeting attendance as acceptance.

### Fact and hypothesis

Preserve the source's level of certainty. A confident participant assertion is still a participant claim unless independently established within the supplied material.

### Disagreement

Record both positions fairly. Do not flatten productive tension into artificial consensus. If the apparent conflict could be caused by different definitions or time horizons, say so as an inference.

## Epistemic labels

- `[Explicit]`: directly present in the source.
- `[Strong inference]`: supported by several compatible signals with no major contradiction.
- `[Tentative inference]`: plausible but another interpretation remains credible.
- `[Recommendation]`: introduced by the analyst.
- `[Unknown]`: evidence needed for the claim is missing.
- `[Contested]`: conflicting statements or unclear agreement.

Use labels on consequential claims, decisions, commitments, risks, and recommendations. Avoid cluttering obvious descriptive prose.

## Temporal reconciliation

Conversation is stateful. Before synthesis:

1. order claims by source position or timestamp;
2. link replies to the proposal they address;
3. detect corrections, retractions, conditions, and changes of mind;
4. prefer the latest explicit settled state;
5. retain the earlier state only when it explains the tradeoff or decision history;
6. flag unresolved contradictions rather than selecting the most convenient version.

For multiple meetings, preserve meeting dates and distinguish current state from historical context.

## Source locators

Use the strongest locator available:

1. timestamp plus speaker;
2. line range plus speaker;
3. message or paragraph identifier;
4. filename and section;
5. short excerpt when no stable locator exists.

Never invent timestamps, line numbers, speaker names, or quote boundaries. If segmentation generated line ranges, cite the original source ranges rather than chunk-relative positions.

## Privacy and audience

Sensitivity is separate from truth. A claim can be well supported and still unsuitable for sharing.

- **Private:** personal, confidential, legally sensitive, raw personnel judgment, or explicitly off-record.
- **Internal:** appropriate within the intended team but not outside it.
- **Shareable:** safe for the named audience based on supplied constraints.
- **Unknown:** sharing permission cannot be established.

When producing a shareable report, omit or generalize sensitive details without changing the operational meaning. Never claim the shareable report is safe for publication unless the source and audience constraints establish that.

## Failure patterns to prevent

- Converting brainstorming into commitments.
- Assigning the most relevant person as owner without evidence.
- Preserving a proposal after a later rejection.
- Treating repeated statements as independent corroboration when they come from one speaker.
- Manufacturing a moonshot because a section exists.
- Hiding disagreement behind a polished executive summary.
- Mixing analyst recommendations into a participant decision register.
- Reporting precise confidence scores unsupported by a calibration method.
