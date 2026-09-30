# Design

Reproduce and minimise UI transition failures with explicit browser contracts.

Chromium starts with its sandbox enabled. The selected `localhost` origin tries the pinned loopback addresses 127.0.0.1 and ::1. An unavailable initial page is a setup error (exit 2); a failed DOM contract is a finding (exit 1).

Assertion selectors must be standard CSS in the main document. All predicates are evaluated together in one JavaScript turn and retried every 25 ms until the largest assertion `timeout_ms` expires (default 1000 ms). Count checks all matching nodes; the other predicates require one node, except that hidden also accepts no match. Text comparison collapses whitespace. Shadow-root and Playwright-specific assertion selectors are outside this version. Trigger selectors retain Playwright syntax.

## Scope

A failure must reproduce twice before minimisation. Each deletion candidate must preserve the same assertion signature twice. The reducer finds a deletion-minimal sequence for the supplied timings, not a globally smallest browser program. Reports distinguish non-repeatable failures from confirmed ones. `repro` objects can be saved directly as scenario JSON and rerun.

The checks cover declared DOM states. Visual differences, screenshots, video, accessibility audits, navigation interruptions and arbitrary JavaScript actions are outside this version. Reports contain selectors and the reproduction scenario, which can themselves be confidential. Review them before sharing.

Only a loopback origin is allowed by default. `--allow-remote` permits the selected public origin. A per-run local proxy pins its resolved address and refuses other origins. WebSockets are closed, service workers blocked, downloads disabled. This intentionally blocks external fonts, analytics and CDNs. The proxy is an application-level control, not an OS sandbox. Run controlled test applications. Browser contexts contain no saved login state.
