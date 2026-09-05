# Contributing

Issues and focused pull requests are welcome. Before submitting a change:

```bash
npm ci
npm test
npm run build
```

New actions or oracles should include schema validation, execution tests, and reporting
tests. Preserve Heimdall's central invariant: an unexecuted case must never be reported as
passed.
