"""Synthetic public GitHub bug-bounty code-search fixture."""

SEARCH_MARKER = "GHAW_INDEX_PUBLIC_4d26a1c78e3b905f"


def describe_fixture() -> dict[str, str]:
    """Return inert, public-only fixture metadata."""
    return {
        "purpose": "authorized GitHub Agentic Workflows code-search control",
        "visibility": "public",
        "marker": SEARCH_MARKER,
        "data_class": "synthetic",
    }

