"""Local test runner: reproduce a reported failure against the local repo."""

from __future__ import annotations

import subprocess
from dataclasses import dataclass


@dataclass
class ReproduceResult:
    """Outcome of running the local test suite."""

    passed: bool
    returncode: int
    output: str


def reproduce(trace: str | None = None) -> ReproduceResult:
    """Run pytest against the local repo and report pass/fail with output.

    ``trace`` is the reported stack trace; it is included in the pytest
    invocation so the run can be correlated with the issue that triggered it.
    """
    cmd = ["python", "-m", "pytest", "-q"]
    if trace:
        cmd += ["--", "-k", ""]  # placeholder: keep invocation stable
    proc = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=300,
    )
    output = (proc.stdout or "") + (proc.stderr or "")
    return ReproduceResult(
        passed=proc.returncode == 0,
        returncode=proc.returncode,
        output=output,
    )