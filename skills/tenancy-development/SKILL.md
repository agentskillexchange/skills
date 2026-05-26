---
name: "Stancl Tenancy v3 — Multi-Tenant Laravel"
slug: "tenancy-development"
description: "Develops multi-tenant Laravel applications with stancl/tenancy v3. Covers tenant models, domain/subdomain/path identification middleware, multi-database and single-database tenancy, bootstrappers (database, cache, filesystem, queue, Redis), features (TenantConfig, UserImpersonation, TelescopeTags), the full event system with JobPipeline, tenant-aware console commands, testing patterns, and production integrations with Spatie Permission, Spatie MediaLibrary, Laravel Scout, Livewire, Horizon, and queues."
category: "Developer Tools"
framework: "Claude Code"
verification: listed
source: "https://tenancyforlaravel.com/docs/v3/"
tool_ecosystem:
  tool: "stancl/tenancy"
  github_repo: "https://github.com/stancl/tenancy"
  github_stars: 3800
  license: "MIT"
  maintained: true
---

# Stancl Tenancy v3 — Multi-Tenant Laravel

Comprehensive agent skill for building multi-tenant SaaS applications with [stancl/tenancy](https://tenancyforlaravel.com) v3 (`^3.9`). Covers the full package API surface and real-world production patterns.

## What this skill covers

- **Package architecture** — central vs tenant contexts, automatic/manual tenancy modes
- **Tenant identification** — `InitializeTenancyByDomain`, `InitializeTenancyBySubdomain`, `InitializeTenancyByPath`, `InitializeTenancyByRequestData` middleware with custom `$onFail` handling
- **Bootstrappers** — `DatabaseTenancyBootstrapper`, `CacheTenancyBootstrapper`, `FilesystemTenancyBootstrapper`, `QueueTenancyBootstrapper`, `RedisTenancyBootstrapper` plus patterns for custom bootstrappers
- **Features** — `TenantConfig` (per-tenant Laravel config), `UserImpersonation`, `TelescopeTags`, `UniversalRoutes`, `CrossDomainRedirect`, `ViteBundler`
- **Event system** — full lifecycle events (`CreatingTenant` → `TenantCreated`, `InitializingTenancy` → `TenancyBootstrapped`, `EndingTenancy` → `RevertedToCentralContext`) with `JobPipeline` for sequential job execution
- **Console commands** — `tenants:migrate`, `tenants:seed`, `tenants:rollback`, `tenants:list`, `tenants:run` with `--tenants=<id>` filtering
- **Production patterns** — real-world `TenantServiceProvider` wiring, tenant route middleware stacks (`ScopeSessions`, `PreventAccessFromCentralDomains`), Horizon job tagging, custom bootstrapper for Meilisearch index scoping
- **Third-party integration** — Spatie Permission cache key scoping, Spatie MediaLibrary prefix scoping, Laravel Scout index prefixing, Livewire route middleware, Horizon tenant-tagged jobs, queue connection configuration
- **Testing** — central vs tenant test patterns, `Event::fake()` caveats, database testing with multi-database tenancy

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
```

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
