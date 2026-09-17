# Context pack template

Use the sections needed for a standalone, task-shaped handoff; mark unavailable evidence instead of inventing it.

```markdown
# Context Pack: <task>

## Task frame
- Outcome:
- Constraints:
- Non-goals:

## Repository snapshot
- Root:
- Revision (or not Git):
- Worktree state and observation time:
- Map artifact and exclusions:

## Big-picture architecture
Task-relevant overview; label inferences.

## Investigation questions
1. Question, answer status, and evidence.

## Selected zoom areas
### Area
- Why selected:
- Files and symbols:
- Relationship to other areas:
- Evidence (path:lines):

## Execution or data flow
1. Entry → next component → effect (path:lines).

## Contracts and constraints
- API/model/schema/configuration/policy/invariant (path:lines).

## Verification surface
- Existing tests/checks and citations:
- Commands supported by repository evidence:
- Checks actually run, outcomes, and limitations:
- Missing coverage:

## Likely change surface
- Primary files:
- Possible secondary files:
- Risks and coupling:

## Excluded areas
- Area and reason:

## Evidence states
### Observed facts
- Claim (path:lines).
### Reasoned inferences
- Inference and supporting evidence.
### Open questions
- Unresolved item and what would answer it.

## Recommended next action
One concrete step, with any required authorization.

## Evidence manifest
1. Repository-relative path and role in the pack.
```
