# Production Patterns for Multi-Tenant Applications

## Queue Isolation Strategies

### Tenant-Specific Queues

Dispatch each tenant's jobs to dedicated queues for fair scheduling:

```php
class TenantAwareJob implements ShouldQueue
{
    public function __construct(
        public string $tenantId,
    ) {
        $this->onQueue("tenant_{$tenantId}_default");
    }
}
```

Workers process queues round-robin, preventing one busy tenant from starving others.

### Priority Queues

Route critical jobs to high-priority queues:

```php
$this->onQueue('tenant_high');   // payments, auth
$this->onQueue('tenant_default'); // standard operations
$this->onQueue('tenant_low');    // bulk processing, analytics
```

### Dedicated Worker Servers

For high-volume tenants, provision dedicated Horizon supervisors per tenant:

```php
'supervisor-tenant-acme' => [
    'connection' => 'redis',
    'queue' => ['tenant_acme_default'],
    'balance' => 'auto',
    'processes' => 3,
],
```

### Deployment-Scale Migrations

For hundreds of tenants, run migrations asynchronously rather than blocking deployments:

```php
// Instead of: php artisan tenants:migrate
// Dispatch background jobs:
Tenant::chunk(50, fn ($tenants) => $tenants->runForEach(function () {
    Artisan::call('migrate', ['--force' => true]);
}));
```

## Provisioning Safety

Design provisioning jobs to be retry-safe (idempotent) — check if resources already exist before creating:

```php
class CreateDatabase
{
    public function handle(TenantCreated $event): void
    {
        $database = $event->tenant->database()->getName();
        DB::statement("CREATE DATABASE IF NOT EXISTS `{$database}`");
    }
}
```

Key principles:
- "create if not exists" checks for databases
- "seed if missing key records" for seeders
- State transitions guarded by expected current state
- Independent migration commands per tenant for safer rollout
