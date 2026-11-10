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

IssueFlow only works with public GitHub repositories and requires a personal access token with `repo` scope set in the `GITHUB_TOKEN` environment variable. It is designed for Python projects that use `pytest` as the test runner; other languages or test frameworks are not supported. The tool does not handle private repositories, complex CI pipelines, or issues without stack traces.

## Development

```bash
pip install -e ".[dev]"
pytest -q
ruff check .
```

## License

MIT -- see [LICENSE](LICENSE).
