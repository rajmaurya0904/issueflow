"""Fetch GitHub issues for triage."""

from __future__ import annotations

import json
import urllib.error
import urllib.request

API_URL = "https://api.github.com/repos/{repo}/issues"


class IssueFlowError(Exception):
    """Raised when the GitHub API cannot be reached or returns an error."""


def fetch_open_issues(repo: str) -> list[dict]:
    """Fetch open issues for ``repo`` (``owner/name``).

    Returns:
        A list of dicts, each with ``number``, ``title`` and ``body``.

    Raises:
        IssueFlowError: If the API request fails or returns an error.
    """
    url = API_URL.format(repo=repo)
    request = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    try:
        with urllib.request.urlopen(request) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, urllib.error.HTTPError, ValueError) as exc:
        raise IssueFlowError(f"Failed to fetch issues for {repo}: {exc}") from exc
    if not isinstance(payload, list):
        raise IssueFlowError(f"Unexpected response from GitHub API for {repo}")
    issues = []
    for item in payload:
        if not isinstance(item, dict) or "pull_request" in item:
            continue
        issues.append(
            {
                "number": item.get("number"),
                "title": item.get("title"),
                "body": item.get("body"),
            }
        )
    return issues