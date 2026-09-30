# Data handling

MotionBreak has no telemetry, update checks, cloud account or model API integration. Reports are written only to the chosen local output directory. HTML uses no remote scripts, fonts or images.

A failure must reproduce twice before minimisation. Each deletion candidate must preserve the same assertion signature twice. The reducer finds a deletion-minimal sequence for the supplied timings, not a globally smallest browser program. Reports distinguish non-repeatable failures from confirmed ones. `repro` objects can be saved directly as scenario JSON and rerun.

The checks cover declared DOM states. Visual differences, screenshots, video, accessibility audits, navigation interruptions and arbitrary JavaScript actions are outside this version. Reports contain selectors and the reproduction scenario, which can themselves be confidential. Review them before sharing.

Only a loopback origin is allowed by default. `--allow-remote` permits the selected public origin. A per-run local proxy pins its resolved address and refuses other origins. WebSockets are closed, service workers blocked, downloads disabled. This intentionally blocks external fonts, analytics and CDNs. The proxy is an application-level control, not an OS sandbox. Run controlled test applications. Browser contexts contain no saved login state.

Dependencies are installed separately from package providers. GitHub Actions checks out the source and runs the test suite on GitHub-hosted runners. Workflows receive read-only repository permissions and publish no artifacts. Review inputs and reports before sharing them. Keep synthetic examples in this repository; do not commit real credentials, exports or receipts.

If you find a security issue, report it privately to the repository owner without including live credentials or personal data.
