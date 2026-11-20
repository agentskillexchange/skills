---
name: "Build a multi-tenant WhatsApp Business Cloud API gateway"
slug: "build-multitenant-whatsapp-cloud-api-gateway"
description: "Build a FastAPI + PostgreSQL gateway that receives WhatsApp Business Cloud API webhooks and sends compliant messages for many tenants, with row-level-security tenant isolation, 24-hour service window enforcement, opt-in tracking and pacing. Includes the asyncpg and RLS failure modes that crash-loop silently."

category: "Developer Tools"
framework: "Multi-Framework"
verification: listed
source: "https://github.com/nusabyte-my/agent-skills"
author: "nusabyte-my"
publisher_type: "individual"
---

# Build a multi-tenant WhatsApp Business Cloud API gateway

A server that is both a public webhook endpoint and a compliant send engine, for one
WhatsApp number or for many clients each holding their own WhatsApp Business account.

## Why Meta Cloud API and not an unofficial library

`whatsapp-web.js` and Baileys drive a personal WhatsApp account over the multi-device
protocol. Numbers are banned for it, quickly and permanently, and the ban lands on the
client's real business number. There is no careful version of this. Meta Cloud API is free
for the first 1,000 service conversations per month per WABA and cannot be banned for
automating. The one legitimate use of an unofficial client is as a fallback for a number
the business already owns, driven from a residential IP — datacenter IPs fail the QR
registration step outright.

## Compliance mechanisms baked into the send path

An opt-in store per tenant, with inbound messages treated as implied consent. The
24-hour service window enforced at send time: free-form text only within 24 hours of the
last inbound message, otherwise an approved template is mandatory. A per-tenant token
bucket for per-minute caps, a per-recipient cooldown and a daily counter, with randomised
jitter between sends. Automatic opt-in removal when Meta reports a `failed` status.
`X-Hub-Signature-256` verification against `sha256=HMAC_SHA256(app_secret, raw_body)`,
computed over the raw bytes before JSON parsing, with a per-tenant secret.

## Tenant isolation with PostgreSQL row-level security

Application-level scoping means one forgotten `WHERE` clause leaks one client's
conversations into another client's panel. RLS makes that leak structurally impossible:
every request opens a session, pins `app.current_tenant_id`, and policies filter every
`optins`, `events` and `daily_counter` row automatically. The application connects as a
non-superuser role, because superusers bypass RLS and silently defeat the design.

The pin must use `SELECT set_config('app.current_tenant_id', $1, false)` and not
`SET LOCAL`. `SET LOCAL` is transaction-scoped and resets on the first `commit()`, and the
store helpers commit mid-session — so later queries in that session lose the pin and RLS
returns zero rows without raising an error. Postgres also rejects a bound parameter as the
right-hand side of `SET`.

## Failure modes that look like something else

An async engine URL of `postgresql://` makes SQLAlchemy select psycopg2, which is not
installed, so the container crash-loops with empty health responses while the import error
only appears in `docker logs`. asyncpg rejects multi-statement `execute()`, so an
`init_schema()` that sends several `CREATE TABLE` statements in one call dies on first
boot. Containers on a bridge network cannot reach host services because Docker FORWARD
drops container-to-host-bridge traffic. A placeholder password copied from `.env.example`
connects to nothing and surfaces only as `password authentication failed`.

## Installation

### Direct repo/manual install

```bash
git clone https://github.com/nusabyte-my/agent-skills.git
cp -R agent-skills/skills/whatsapp-cloud-api-gateway ~/.agent-skills/whatsapp-cloud-api-gateway
```

### Optional Third-Party Installer

The `skills` npm package is maintained by Vercel Labs / third parties, not AgentSkillExchange. If you choose to use it, pin the package version:

```bash
npm exec --package=skills@1.5.7 -- skills add nusabyte-my/agent-skills --skill whatsapp-cloud-api-gateway
```

## Verification

Client-side token permission checks are not enough — the gateway is only correct when a
second tenant provably cannot read the first tenant's rows, an unsigned webhook is
rejected with 403, an out-of-window send without a template is refused, and a `failed`
status webhook removes the opt-in. `token_configured` reporting true means an environment
variable exists, not that the credential is valid.
