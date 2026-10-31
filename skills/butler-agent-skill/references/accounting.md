# Accounting contract

Read-only previews: `gpu-gate --project SLUG --request GPU_HOURS --gpus COUNT --hours WALL_HOURS`. Preview does not hold capacity. It can be stale immediately; only reserve performs the admission-and-append under one POSIX file lock. The lock file itself may be created by ledger operations.

Atomic reservation: `gpu-reserve --project SLUG --job JOB --reservation-id STABLE_ID --gpus COUNT --hours WALL_HOURS --estimated-cost AMOUNT --currency CODE --disk-gb SIZE`. Reuse the same identifier only for the same logical reservation. A gate/reservation does not launch or authorize a provider job. Persist the reservation identifier with provider job provenance.

Reconciliation: `gpu-reconcile --project SLUG --reservation-id STABLE_ID --actual-gpu-hours MEASURED --actual-cost MEASURED --outcome completed`. Supported terminal outcomes also include failed, failed_infrastructure, killed, cancelled, launch_failed. Outcome does not erase consumed resources. Retained disk remains a commitment when specified. Only record disk release after independent provider/path evidence; the command does not delete storage.

Defaults are not authorizations: absent GPU limits are unbounded. Inspect private project JSON and `gpu-policy --help` before work. GPU-hour windows, concurrent GPU count, grant limits, cash limits and disk limits are independent. Shared scopes live in private config's `gpu_scopes`; they aggregate explicitly declared project members. An unlimited policy is a deliberate destructive budget-policy change requiring attributed authority.

Usage import requires a stable usage ID, timestamp, outcome and evidence. Exact replay does not double count; conflicts fail. Ledger corruption fails closed for admission, including invalid numerical fields and duplicated reservation IDs. A torn final append is treated differently from malformed committed interior rows.

Limitations: no exchange-rate conversion, cloud billing reconciliation, remote enforcement or actual Codex quota integration. Optional Claude provider-cache reports retain fetched timestamps and may be stale. Missing actual monetary cost is recorded as zero by the legacy API; this is not evidence of free usage. Supply measured costs whenever cash accounting matters. Ordinary config/policy edits are not serialized across every CLI entrypoint; do not edit policy while another process is admitting work.
