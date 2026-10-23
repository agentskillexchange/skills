---
name: "Publish Files to a Permanent URL with deed.page"
slug: "deed-page"
description: "Publishes a generated HTML file or a static folder to a permanent https://<slug>.deed.page/ URL with one curl PUT or the deed.page MCP server, with no account, API key, email code or claim link. Use when the user asks to publish, host, share or put online a report, dashboard, slide deck, prototype, game or docs folder the agent built."
verification: "listed"
source: "https://github.com/f-o-x11/deed-page-skill"
publisher_type: "vendor"
category: "Developer Tools"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "f-o-x11/deed-page-skill"
---

# Publish Files to a Permanent URL with deed.page

deed.page is a static host built for agents. The agent picks a slug, sends one HTTP request with the files, and gets back JSON whose `url` field is the live site at `https://<slug>.deed.page/`. Nobody signs up, reads an email code or clicks a claim link, so the skill also works in unattended runs. Sites stay up until they are deleted; an expiry is opt-in with an `X-Ttl` header.

The REST API takes a raw HTML body (stored as `index.html`), a gzipped tarball of a folder (paths kept exactly), multipart uploads, or a JSON map of file paths to contents. The same operations are exposed by a remote MCP server at `https://deed.page/mcp` (Streamable HTTP, no auth) with tools such as `publish_site`, `update_site`, `list_versions`, `restore_version` and `delete_site`. The full API is described at https://deed.page/docs and https://deed.page/openapi.json.

The first publish returns a `token` once. It is the only key that can update or delete that site. Keep it in the `DEEDPAGE_TOKEN` environment variable for the session and send it as `Authorization: Bearer` on later publishes so all slugs share one owner. Only a SHA-256 of the token is stored server-side, so a token without the optional recovery email cannot be recovered.

Limits on the free plan: 25 sites, 25 MB per site, 60 publishes per hour, and a 4 MB cap per request body (larger sites use the manifest upload flow in the docs). Free sites are public. Static files only: no server-side code or databases.

## Installation

### Any agent (skills CLI)

```bash
npx skills add f-o-x11/deed-page-skill
```

### Claude Code (plugin)

```bash
claude plugin marketplace add f-o-x11/deed-page-skill
claude plugin install deed-page@deed-page
```

### Gemini CLI (skill plus MCP server)

```bash
gemini extensions install https://github.com/f-o-x11/deed-page-skill
```

### Any MCP client

Point the client at `https://deed.page/mcp` (Streamable HTTP). For Claude Code without the plugin:

```bash
claude mcp add --transport http deed-page https://deed.page/mcp
```

### Direct repo/manual install

```bash
git clone --depth 1 https://github.com/f-o-x11/deed-page-skill /tmp/deed-page-skill
mkdir -p ~/.claude/skills && cp -R /tmp/deed-page-skill/skills/deed-page ~/.claude/skills/
```

- Source: https://github.com/f-o-x11/deed-page-skill

## Usage

1. Confirm with the user that the content may be public. Never publish secrets, credentials or private data to a free site.
2. Pick a slug of lowercase letters, digits and hyphens (1 to 63 characters, no leading or trailing hyphen) with a random suffix, for example `report-7f3a2c`. Invalid slugs return 400 `slug_invalid` and are not rewritten.
3. Publish a single HTML file:

   ```bash
   curl -sS -T index.html "https://deed.page/v1/sites?slug=report-7f3a2c" -H "X-Client: <agent name>"
   ```

   Or a folder, with its contents at the site root:

   ```bash
   tar -C ./site -czf /tmp/site.tar.gz .
   curl -sS -T /tmp/site.tar.gz "https://deed.page/v1/sites?slug=report-7f3a2c" -H "X-Client: <agent name>"
   ```

4. Answer with the `url` field from the JSON. On the first publish, tell the user the returned `token` is the key to update or delete the site and keep it in `DEEDPAGE_TOKEN`.
5. To update, repeat the publish with `-H "Authorization: Bearer $DEEDPAGE_TOKEN"`. Send `-H 'If-Match: "v3"'` with the last version to get 409 `version_conflict` instead of overwriting a newer version.
6. On 409 `slug_taken`, use the `suggestion` field. On 429, wait `retry_after` seconds.
7. Delete a site only when the user asks: `curl -X DELETE https://deed.page/v1/sites/<slug> -H "Authorization: Bearer $DEEDPAGE_TOKEN"`.

## Licensing

The skill, the Claude Code plugin and the Gemini CLI extension in `f-o-x11/deed-page-skill` are MIT licensed. The hosting service at deed.page is a closed-source commercial service operated by Avatar 8 LLC. It has a free plan; paid plans (Hobby $3/month, Pro $15/month) raise limits and add site passwords. See https://deed.page/pricing.

## Documentation

- Docs: https://deed.page/docs
- OpenAPI: https://deed.page/openapi.json
- llms.txt: https://deed.page/llms.txt
- Abuse reports: https://deed.page/abuse
