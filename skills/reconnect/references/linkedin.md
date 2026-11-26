# Authorised LinkedIn work

Before browser use, read the available browser-control skill for the selected
harness and use its supported tools. Do not use undocumented LinkedIn APIs,
credential extraction, stealth automation, or challenges bypasses.

## Execute a concrete request

1. Load the saved batch and current source tracker. Resolve which recipients the
   user's instruction covers. Record the instruction's reference on the batch with
   `authorize`; this records existing approval and never manufactures it. If the
   user has already approved this exact action, proceed without a second prompt.
2. Open each target in one authenticated tab. Check name, professional/course
   continuity, eligibility, and the profile-specific relationship control. An
   ambiguous namesake is skipped with a reason. Scores and names alone do not settle
   identity. A prior Connect state is not proof that it is still connectable.
3. If already connected or Pending, record the observed state and do not resend.
   Before a permitted send, record relationship `uncertain` with evidence that an
   authorised attempt is starting, so a crash leaves a resumable reservation.
   Use the target's own Connect control or More menu, and send according
   to the approved note preference. Do not substitute another recipient merely to
   reach a number. Keep within current tool and platform constraints.
4. Read back the target-specific Pending state before recording an invitation as
   requested. Store the profile URL, observation timestamp, and concise evidence.
   For group invitations, verify both connection/eligibility and the group action's
   own confirmation; record membership separately from connection state.
5. Stop on restrictions, warnings, CAPTCHA, invitation limits, account uncertainty,
   or an email-verification challenge. Preserve remaining reservations. Report the
   actual obstacle; never promise that a delay or smaller batch bypasses it.

## Interruptions

After a timeout or uncertain submission, record `uncertain` and keep the destination
reserved. Reopen the profile and inspect its current state before any further send.
Pending/connected resolves the attempt. A Connect control can justify a retry only
after checking identity, continued approval, and absence of a platform stop condition.
Do not release a reservation with an unresolved attempt.

## Completion

Report counts of newly sent, already Pending, already connected, skipped, unresolved,
and remaining. State what was live-verified. Update the canonical project tracker
across all source identities mapped to the destination, preserving append-only
receipts. Reconcile group state independently. If canonical writeback fails, retain
the local receipt and report that reconciliation remains unfinished.
