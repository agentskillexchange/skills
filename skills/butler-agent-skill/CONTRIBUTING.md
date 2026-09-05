# Contributing

Use Python 3.10 or newer on macOS/Linux. Keep runtime code portable and state outside this repository. Tests must create isolated temporary state and ephemeral loopback ports, never connect to an existing operator service. Fixtures must be clearly synthetic.

Run `python3 -m unittest discover -s tests -v`. Questlog's escaper checks also require Node.js. Keep provenance and public-release privacy boundaries intact; do not add personal logs, accounts, fleet configuration, or example task records to shipped initial state. Document behavior changes and test failures, and update CHANGELOG.md. Pull requests must not silently add external actions or scheduling.
