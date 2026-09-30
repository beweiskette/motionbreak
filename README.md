# MotionBreak

Interrupt a UI transition at several timings, check the declared final state, then reduce repeatable failures to a smaller interruption sequence.

Version 0.1.0. [Deutsch](README.de.md). Python 3.11 or newer. MIT licence.

## Install

From a clone of this repository:

```sh
python -m venv .venv
# Linux/macOS:
. .venv/bin/activate
# Windows PowerShell instead:
# .\.venv\Scripts\Activate.ps1
python -m pip install -e ".[test]"
```

## Run

```sh
motionbreak run examples/scenario.json --out outputs/check
```

In a separate terminal, run `python -m http.server 8765 --bind 127.0.0.1 --directory examples`. The scenario starts with `fixed.html`. Change its URL to `broken.html` to reproduce an overlay that reappears after Escape.

Install Chromium with `python -m playwright install chromium`, or pass `--browser /absolute/path/to/chrome`. Every attempt gets a fresh browser context. The JSON scenario contains `url`, `trigger`, `delays_ms`, `interruptions`, `settle_ms`, and `assertions`. Supported interruptions are `escape`, `retrigger` and `resize` (with `width` and `height`). They run in order after each initial delay. An empty interruption list checks the baseline.

Assertions use `kind` and `selector`. Kinds are `visible`, `hidden`, `focused`, `count` and `text`; the last two also require `value`. Optional `timeout_ms` is limited to 5000. See the example for a complete contract.

Reports are local JSON and self-contained HTML. Exit status is 0 for a pass, 1 for findings, and 2 for an input or runtime setup error. Commands do not publish reports or contact a model API.

## Boundaries

A failure must reproduce twice before minimisation. Each deletion candidate must preserve the same assertion signature twice. The reducer finds a deletion-minimal sequence for the supplied timings, not a globally smallest browser program. Reports distinguish non-repeatable failures from confirmed ones. `repro` objects can be saved directly as scenario JSON and rerun.

The checks cover declared DOM states. Visual differences, screenshots, video, accessibility audits, navigation interruptions and arbitrary JavaScript actions are outside this version. Reports contain selectors and the reproduction scenario, which can themselves be confidential. Review them before sharing.

Only a loopback origin is allowed by default. `--allow-remote` permits the selected public origin. A per-run local proxy pins its resolved address and refuses other origins. WebSockets are closed, service workers blocked, downloads disabled. This intentionally blocks external fonts, analytics and CDNs. The proxy is an application-level control, not an OS sandbox. Run controlled test applications. Browser contexts contain no saved login state.

## Verify

```sh
python -m pytest -q
```

Set `BROWSER_TEST=1` after installing Playwright Chromium, or set `TEST_BROWSER` to an existing Chromium executable. The integration test runs both the fixed and intentionally broken fixture and checks the reduced reproduction.

GitHub Actions runs tests on Windows and Linux. Integration jobs use synthetic local fixtures. No deployment or package publication workflow is configured. Dependency installation and browser/image downloads are explicit setup steps that contact their respective package providers.

See [DESIGN.md](DESIGN.md) for the scope decisions and [SECURITY.md](SECURITY.md) for data handling.
