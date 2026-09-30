# Version 0.1 design

Interrupt a UI transition at several timings, check the declared final state, then reduce repeatable failures to a smaller interruption sequence.

The design was reviewed once through a read-only Claude adapter before implementation. That consultation received feature proposals and synthetic examples, not repository contents or credentials. Implementation and local verification were performed separately; the consultation was a design review, not a code audit.

The selected scope favours explicit user contracts and local evidence. Automatic uploads, model-generated pass criteria, background monitoring and publishing are excluded. This version makes no claim that the idea is unique or that it will attract a particular number of GitHub stars.

## Acceptance evidence

Set `BROWSER_TEST=1` after installing Playwright Chromium, or set `TEST_BROWSER` to an existing Chromium executable. The integration test runs both the fixed and intentionally broken fixture and checks the reduced reproduction.

## Deliberate limits

A failure must reproduce twice before minimisation. Each deletion candidate must preserve the same assertion signature twice. The reducer finds a deletion-minimal sequence for the supplied timings, not a globally smallest browser program. Reports distinguish non-repeatable failures from confirmed ones. `repro` objects can be saved directly as scenario JSON and rerun.

The checks cover declared DOM states. Visual differences, screenshots, video, accessibility audits, navigation interruptions and arbitrary JavaScript actions are outside this version. Reports contain selectors and the reproduction scenario, which can themselves be confidential. Review them before sharing.

Only a loopback origin is allowed by default. `--allow-remote` permits the selected public origin. A per-run local proxy pins its resolved address and refuses other origins. WebSockets are closed, service workers blocked, downloads disabled. This intentionally blocks external fonts, analytics and CDNs. The proxy is an application-level control, not an OS sandbox. Run controlled test applications. Browser contexts contain no saved login state.
