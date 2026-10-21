# AgentSkillExchange PR — ready to file

Prepared 2026-10-21. Nothing submitted yet; opening the PR needs the owner's GitHub
account (yasuo22). Best done in the GEO/SEO side chat's browser window, which already
holds his GitHub login, after the skills.pub / MCP Market submissions return.

## What this is

A PR-ready skill wrapping the AI Services Market MCP server — the one route from the
directory-submission-pack that accepts our *store's own asset* (a documented API),
since every skills directory only lists individual skills, not stores.
AgentSkillExchange's hard rule: every skill must wrap a real tool/API — our live MCP
server at https://aiservicesmarket.lol/mcp qualifies.

Target: https://github.com/agentskillexchange/skills (public, MIT, 3,168 published
skills, verified live 2026-10-21).

## The prepared file

`SKILL.md` in this folder — commit it as `skills/ai-services-market-mcp/SKILL.md`
in the fork. It follows their template/SKILL.md and CONTRIBUTING.md exactly:

- Frontmatter: name, slug, description, category `Integrations & Connectors`
  (exact string from their 17 valid categories), framework `MCP` (from their valid
  list), verification `listed`, source `https://aiservicesmarket.lol/mcp`.
- Body: H1 matching name; 100+ words of real technical detail (endpoint, OAuth 2.1
  DCR/PKCE flow, all six real tool names and semantics, pricing, paywall behavior);
  Installation section with working commands.
- Every claim grounded in `~/workspace/skillshop/mcp/MCP.md` (v0.3.0): tool names,
  the `agent` parameter values, prices ($4.99 / $9.99 / $79 / $169), no refunds,
  605-skill catalog. The use-case count is stated conservatively as "1,300+" to
  stay under the three figures seen across sources (1,392 / 1,443 / 1,471) — the
  server computes counts live, so the skill text does not hard-code drift-prone
  numbers beyond the verified 605.

## Suggested PR

**Title:** `Add ai-services-market-mcp`

**Body:**
> Adds a skill wrapping the AI Services Market MCP server — a documented, live API
> (https://aiservicesmarket.lol/mcp) that lets AI agents search a 605-skill catalog
> of installable agent skills, read full details and pricing, and generate Stripe
> checkout links.
>
> - Category: Integrations & Connectors; framework: MCP
> - Backed by a real, existing tool: six MCP tools
>   (search_skills, get_skill, search_use_cases, get_use_case, get_entitlement,
>   create_checkout) over Streamable HTTP + OAuth 2.1
> - No new code; the skill teaches agents to connect, search, compare, and hand
>   off purchases

## Filing steps (browser, his account)

1. Fork `agentskillexchange/skills` as yasuo22.
2. In the fork, create `skills/ai-services-market-mcp/SKILL.md` with the prepared
   file. (First: search the repo/CATALOG.md for "ai-services-market" to confirm
   no duplicate slug — not done yet, one-line check.)
3. Open the PR with the title/body above.
4. Their process: automated format + security scan checks, then human review for
   quality/accuracy; merge to main on approval (marketplace publication handled
   separately by maintainers). No CLA text was found in CONTRIBUTING.md.

## Related checks already done

- Free-samples repo format for skills.sh / SkillsMP: all 5 SKILL.md files in
  `~/workspace/skillshop/github-free-samples/skills/` carry `name` + `description`
  frontmatter — meets skills.sh's stated requirement. No fix needed.
