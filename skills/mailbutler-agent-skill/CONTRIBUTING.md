# Contributing

Contributions are welcome when they preserve the safety contract.

Before opening a pull request:

1. Use only synthetic `.invalid` addresses and invented message content in tests and documentation.
2. Do not add real mailbox data, credentials, private narratives, or provider logs.
3. Keep triage read-only and preserve separate draft and send approvals.
4. Keep recipients and thread metadata adapter-derived, never model-derived.
5. Run `python3 -m unittest discover -s tests` and the skill-package validator.

Security changes should include a regression test. Provider-specific integrations should live behind a documented adapter boundary.
