---
name: "Stancl Tenancy v3 — Multi-Tenant Laravel"
slug: "tenancy-development"
description: "Builds multi-tenant Laravel SaaS applications with stancl/tenancy v3. Best when you need domain/subdomain/path-based tenant identification, multi-database or single-database isolation, tenant-aware queues/cache/filesystems/Redis, production bootstrappers, configuration per-tenant, and seamless integration with Horizon, Scout, Livewire, and Spatie packages. Covers the full package API surface including event system, JobPipeline, console commands, testing patterns, and critical production gotchas."
verification: "security_reviewed"
source: "https://tenancyforlaravel.com/docs/v3/"
category: "Developer Tools"
framework: "Claude Code"
---

# Stancl Tenancy v3 — Multi-Tenant Laravel

Comprehensive agent skill for building multi-tenant SaaS applications with [stancl/tenancy](https://tenancyforlaravel.com) v3 (`^3.9`). Covers the full package API surface, real-world production patterns, and critical gotchas.

## What this skill covers

- **Package architecture** — central vs tenant contexts, automatic/manual tenancy modes, tenant model patterns
- **Tenant identification** — `InitializeTenancyByDomain`, `InitializeTenancyBySubdomain`, `InitializeTenancyByPath`, `InitializeTenancyByRequestData` middleware with custom `$onFail` handling
- **Data isolation** — multi-database (per-tenant databases) and single-database (`BelongsToTenant`, `BelongsToPrimaryModel`, `HasScopedValidationRules`, unique index scoping, `withoutTenancy()`)
- **Bootstrappers** — database, cache, filesystem, queue, Redis bootstrappers + patterns for custom bootstrappers
- **Features** — `TenantConfig` (per-tenant Laravel config), `UserImpersonation`, `TelescopeTags`, `UniversalRoutes`
- **Event system** — full lifecycle events with `JobPipeline` for sequential job execution
- **Console commands** — `tenants:migrate`, `tenants:seed`, `tenants:rollback`, `tenants:list`, `tenants:run` with `--tenants=<id>` filtering
- **Production patterns** — queue isolation strategies (tenant-specific queues, priority queues, dedicated workers), idempotent provisioning, deployment-scale migrations, Horizon job tagging, Scout Meilisearch index scoping, Spatie package integration, Livewire tenant routing
- **Testing** — fast transaction-based testing (25x speed improvement), `Event::fake()` caveats, event faking for isolation
- **Critical gotchas** — queued events + `SerializesModels` trap (never pass tenant-scoped models), `DatabaseBatchRepository` stale connection fix, bootstrapper prefix accumulation in long-running processes

## Common patterns

```php
// Tenant model with domains and databases
class Tenant extends BaseTenant implements TenantWithDatabase
{
    use HasDatabase, HasDomains;

    public function getCustomColumns(): array
    {
        return ['id', 'name', 'plan_id', 'status'];
    }
}

// Event-driven tenant lifecycle
Event::listen(TenantCreated::class, JobPipeline::make([
    CreateDatabase::class,
    MigrateDatabase::class,
    SeedDatabase::class,
])->send(fn ($event) => $event->tenant)->toListener());

// Manual tenancy control
$tenant->run(fn () => User::create([...]));
tenancy()->initialize($tenant);
tenancy()->end();

// Custom bootstrapper
class ScoutTenancyBootstrapper implements TenancyBootstrapper
{
    public function bootstrap(Tenant $tenant): void { /* scope Meilisearch */ }
    public function revert(): void { /* restore central config */ }
}

// Single-database scoping
class Post extends Model { use BelongsToTenant; }
class Comment extends Model { use BelongsToPrimaryModel; }
```

## Critical Gotchas

**Queued events + SerializesModels:** Never pass tenant-scoped models in queued payloads. `BelongsToTenant`'s global scope fires before `QueueTenancyBootstrapper` restores context. Pass scalars (`tenantId`, `modelId`) and call `tenancy()->initialize()` in `handle()`.

**DatabaseBatchRepository:** `DB::purge('tenant')` between jobs nulls the PDO. Use `houlokmah/tenancy-batch-fix` for batched jobs across tenants.

**Prefix accumulation:** Cache/Redis/filesystem bootstrappers can accumulate prefixes across tenant switches in long-running processes (Horizon, Octane). Always test after multiple cycles.

For full patterns including queue isolation strategies, transaction-based testing (25x speed), and provisioning safety, see `references/production-patterns.md` in the skill source.

## Installation

### OpenClaw

```bash
clawhub install tenancy-development
```

### Direct repo/manual install

```bash
git clone https://github.com/Xyntax01/tenancy-development.git
cp -R tenancy-development ~/.claude/skills/tenancy-development
```

### Optional Third-Party Installer

```bash
npm exec --package=skills@1.5.7 -- skills add agentskillexchange/skills --skill tenancy-development -a claude-code
```

## Documentation Links

- Official docs: https://tenancyforlaravel.com/docs/v3/
- Upstream repo: https://github.com/stancl/tenancy
- Skill source: https://github.com/Xyntax01/tenancy-development
