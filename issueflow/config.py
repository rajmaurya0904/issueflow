"""Configuration for IssueFlow triage runs."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TriageConfig:
    """Settings controlling how IssueFlow triages issues.

    Attributes:
        repo: GitHub repository in ``owner/name`` form to triage.
        labels: Labels applied to issues that reproduce locally.
        test_command: Command used to reproduce a reported failure.
        dry_run: When true, report actions without mutating the repo.
    """

    repo: str = "owner/repo"
    labels: list[str] = field(default_factory=lambda: ["bug", "reproduced"])
    test_command: str = "pytest -q"
    dry_run: bool = True