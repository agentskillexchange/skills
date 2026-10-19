# Home-anchor and backlink contract

The home Archivum is the continuity layer across specialist archives. Cross-archive links use stable logical URIs:

```text
archivum://<archive-name>/<repository-relative-path>#optional-fragment
```

The private `00_meta/archivum_registry.toml` maps `<archive-name>` to a local root. Absolute machine paths belong in that private registry, not in portable or public records. Logical paths are repository-relative and must not contain traversal that escapes the registered archive root.

## Bidirectional rule

For every private record written outside the home Archivum:

1. Select or create the smallest home anchor that owns the relationship.
2. Add the satellite record's `archivum://` URI to that home anchor or the central cross-archive index.
3. Add the home anchor's `archivum://` URI to the satellite record.
4. Prefer project-level anchors over a flat index row for every low-level note, while ensuring every record remains reachable through its project anchor.

Example:

```markdown
Home anchor: [Embodied memory programme](archivum://my/01_projects/embodied-memory/README.md)
Research record: [Structure study](archivum://research/01_active_research/structure/README.md)
```

## Public privacy exception

Never place a private home URI in a public repository or published output. In that case, preserve the outward link only in the private home anchor and use the public URL in the private index. This is an intentional one-way link, not a failed backlink.

## Registry shape

```toml
version = 1
home = "my"
index = "00_meta/cross_archive_index.md"

[archives.my]
kind = "home"
root = "/srv/archives/home"

[archives.research]
kind = "research"
root = "/srv/archives/research"
home_anchor = "00_meta/home_anchor.md"
```

An archive with `home_anchor` must contain that file, and the file must link to `archivum://<home>/<index>`. Archives without `home_anchor` may still be indexed, especially public or non-Archivum stores.
