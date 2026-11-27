---
name: "Find Hiring Manager and Referral Contacts"
slug: "find-hiring-manager-and-referral-contacts-for-a-job-posting"
description: "Find the likely hiring manager, the recruiter and the best referral contacts for one job posting through Apify LinkedIn Actors (johnvc/linkedin-jobs-api, johnvc/linkedin-company-api, johnvc/linkedin-people-search-api), with evidence for each person, a current-employer check, and outreach drafts. Use when someone has a LinkedIn job URL or a company plus title and asks who is hiring for this role, who can refer me, or how to reach out about this posting."
verification: "listed"
source: "https://github.com/johnisanerd/claude-skill-find-hiring-manager"
category: "Research & Scraping"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "johnisanerd/claude-skill-find-hiring-manager"
---

# Find Hiring Manager and Referral Contacts

This skill takes one job posting, as a LinkedIn job URL or a company plus a title, and finds the people tied to it: the likely hiring manager, the recruiter and a talent lead, plus up to eight people at the company who could refer you because they share your school, a past employer, your city or the team. It chains hosted Apify Actors. `johnvc/linkedin-jobs-api` resolves the posting, `johnvc/linkedin-company-api` resolves the employer by its LinkedIn company slug, `johnvc/linkedin-people-search-api` finds the people, and `johnvc/linkedin-profile-api` is a second check on the current employer. Optional context steps use `johnvc/crunchbase-company-api` for funding and key people, `johnvc/GoogleNewsAPI` for recent news filtered to the company, and `johnvc/linkedin-posts-api` for company posts that name the role.

Each person comes back as a card with name, title (or "title hidden" when LinkedIn masks it), profile URL, evidence links and a label: Named, Likely or Inferred for the people who own the req, and shared school, shared employer, same city or team, or recruiter for referral contacts. A person is kept as current only when the headline or an enriched row ties them to the employer; otherwise the card says the employer is unconfirmed. Connection degree stays "unknown" unless you supply it, because the Actor rows never carry it. The skill then drafts a connection note, a LinkedIn message, an email and a text for each person.

It does not send messages or connection requests, and LinkedIn data includes no email addresses. A verified work email is an opt-in step through a third-party finder, `clearpath/email-finder-api`, and is shown only when the finder marks it safe to send. It turns down lead lists, recruiter directories across many companies, hiring-signal monitoring and bulk email discovery.

Requirements: an Apify account, authenticated with `apify login` or an `APIFY_TOKEN` environment variable. Runs are billed to that account per event, mostly per person returned by the people search. The skill gives a cost estimate first and asks for confirmation above $0.50 or for more than one posting.

## Example

This people search looks for engineering managers at Notion and returns at most 10 people without profile enrichment. Replace the company and title with the ones from your posting.

```bash
apify actors call "johnvc/linkedin-people-search-api" \
  -i '{"company":"Notion","jobTitle":"Engineering Manager","maxResults":10,"enrichProfiles":false}' \
  --output-dataset --silent
```

`--output-dataset` prints the run's dataset items, one row per person with name, headline and profile URL, rather than the run details. The `company` filter matches current or past employers, so the skill keeps a row as current only when the headline says "at" or "@" the company or the current company field matches it, and confirms its shortlist with `enrichProfiles: true`.

Agents can also call the core chain over MCP with the hosted server `https://mcp.apify.com/?tools=actors,docs,johnvc/linkedin-jobs-api,johnvc/linkedin-company-api,johnvc/linkedin-people-search-api`.

## Installation

### Claude Code, Cursor and other skills-compatible agents

```bash
npx skills add johnisanerd/claude-skill-find-hiring-manager
```

### Direct repo/manual install

```bash
git clone https://github.com/johnisanerd/claude-skill-find-hiring-manager.git
mkdir -p ~/.claude/skills
cp -R claude-skill-find-hiring-manager/apify-find-hiring-manager ~/.claude/skills/apify-find-hiring-manager
```

## Source

- Skill repo: https://github.com/johnisanerd/claude-skill-find-hiring-manager
- Actors: https://apify.com/johnvc/linkedin-jobs-api, https://apify.com/johnvc/linkedin-company-api, https://apify.com/johnvc/linkedin-people-search-api
