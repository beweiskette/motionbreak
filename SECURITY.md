# Data handling

motionbreak writes reports to the selected local directory. It has no telemetry or model API integration. HTML reports contain no remote assets.

A failure must reproduce twice before minimisation. Each deletion candidate must preserve the same assertion signature twice. The reducer finds a deletion-minimal sequence for the supplied timings, not a globally smallest browser program. Reports distinguish non-repeatable failures from confirmed ones. `repro` objects can be saved directly as scenario JSON and rerun.

The checks cover declared DOM states. Visual differences, screenshots, video, accessibility audits, navigation interruptions and arbitrary JavaScript actions are outside this version. Reports contain selectors and the reproduction scenario, which can themselves be confidential. Review them before sharing.

Only a loopback origin is allowed by default. `--allow-remote` permits the selected public origin. A per-run local proxy pins its resolved address and refuses other origins. WebSockets are closed, service workers blocked, downloads disabled. This intentionally blocks external fonts, analytics and CDNs. The proxy is an application-level control, not an OS sandbox. Run controlled test applications. Browser contexts contain no saved login state.

Chromium uses its sandbox. Error summaries may contain the selected URL or selector; review reports before sharing.

GitHub Actions uses read-only repository permissions and publishes no artifacts. Dependency installation contacts package providers. Report security issues privately to the repository owner without live credentials.
