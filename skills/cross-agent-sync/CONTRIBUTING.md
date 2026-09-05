# Contributing

Contributions are welcome, especially small parser fixtures for documented harness-format changes.

## Before opening a pull request

```bash
python3 -m unittest discover -s tests -v
python3 -m compileall -q scripts tests
git diff --check
```

Keep tests synthetic. Never commit real transcripts, home-directory paths, credentials, `.agent-sync/imports/`, or generated progress from a private project.

Parser changes should state:

- which documented record shape changed;
- which content is considered visible user/assistant text;
- which content is deliberately excluded;
- whether malformed input is skipped or fails closed.
