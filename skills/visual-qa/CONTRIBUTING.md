# Contributing

Contributions are welcome when they keep the skill generic, evidence-driven, and runtime-neutral.

Before opening a pull request:

```bash
python3 -m unittest discover -s tests -v
python3 -m compileall -q scripts tests
git diff --check
```

Do not commit project-specific adapters, real screenshots, private paths, credentials, or personal data. New roster seats must add a genuinely distinct lens and an explicit negative constraint; near-duplicates should be merged.
