# Contributing

Contributions are welcome when they keep the package small, auditable, and
stdlib-only.

Before opening a pull request:

```bash
python3 scripts/self_test.py
python3 scripts/validate_package.py
python3 -m compileall -q scripts
```

Include a regression test for behavioral changes. Never use a real vault,
master password, session, item identifier, organization name, or retrieved
secret in tests or bug reports. Security-model changes should begin as a
private vulnerability report or a design discussion without exploit details.
