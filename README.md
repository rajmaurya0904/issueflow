# IssueFlow

**An automated GitHub issue triage agent that reads incoming bug reports, reproduces stack traces against local tests, and labels regressions.**

The current manual triage of GitHub issues is time‑consuming and error‑prone.
Developers must read each bug report, reproduce failures locally, and decide which labels apply, often missing regressions.
IssueFlow automates this workflow, instantly matching stack traces to failing tests and applying appropriate labels.

## Example

<!-- A real command and its REAL pasted output. Run it first. -->

## Install

```bash
pip install -e ".[dev]"
```

## Usage

<!-- The 2-4 commands people actually need, one line each. -->

## How it works

<!-- 3-6 bullets: what it checks, computes or produces. -->

## Limitations

<!-- Honest and short: what it does NOT do, known gaps. -->

## Development

```bash
pip install -e ".[dev]"
pytest -q
ruff check .
```

## License

MIT -- see [LICENSE](LICENSE).
