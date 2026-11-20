# Contributing

Contributions that make the graph grammar more portable, testable, or falsifiable are welcome.

1. Open an issue describing the failure mode or orchestration pattern.
2. Keep `SKILL.md` runtime-neutral. Put host-specific code in an example or adapter.
3. Preserve isolation, adversarial review, escalation, and filesystem-safety invariants.
4. Add or update validation for structural changes.
5. Run `python3 tests/validate_repo.py` and, when Node.js is available,
   `node --check examples/saturating-review-engine.workflow.js`.

Examples must use fictional paths and identities and must not contain credentials or private
operational claims. By submitting a contribution, you agree that it is licensed under MIT.
