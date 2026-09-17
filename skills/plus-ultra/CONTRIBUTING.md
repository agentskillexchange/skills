# Contributing

Please preserve the workflow's core invariants: blind read-only proposals, explicit arbitration,
one implementation pass, and a fresh plan-blind reality check.

For hook changes, add regression tests for both the blocked mutation and a neighboring read-only
command that must remain usable. Run `python3 -m unittest discover -s tests -v` before opening a
pull request. Avoid adding third-party runtime dependencies to the hook path.

By submitting a contribution, you agree that it is licensed under MIT.
