# One-time Workload Identity Federation bootstrap

This bootstrap requires an authenticated Google Cloud administrator and a GitHub repository administrator. It is the only step that may rely on interactive human credentials.

1. Record the immutable GitHub numeric repository and owner IDs.
2. Create a dedicated workload identity pool and GitHub OIDC provider.
3. Restrict the provider with an attribute condition matching both numeric IDs. Do not authorize by mutable repository name alone.
4. Create separate least-privilege service accounts for observation and mutation.
5. Grant `roles/iam.workloadIdentityUser` only to the matching repository principal set.
6. Put the provider resource name, service-account email, project ID, and default region in protected GitHub environment variables.
7. Require environment approval for mutating workflows.
8. Copy and validate the supplied observer workflow.
9. Dispatch a read-only operation and verify both the GitHub run identity and the Google Cloud audit-log principal.
10. Remove any temporary broad role used during bootstrap.

Identifiers such as project IDs and service-account emails are not private keys, but they still reveal infrastructure. Keep repository variables private unless disclosure is intentional.

Never create a service-account JSON key as a fallback. If federation fails, diagnose claims, attribute mappings, conditions, IAM bindings, and environment protection.
