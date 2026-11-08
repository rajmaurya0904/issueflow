"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import issueflow


def test_version_is_set() -> None:
    assert issueflow.__version__
