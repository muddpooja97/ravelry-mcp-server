import os
from typing import Any

import requests
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

mcp = FastMCP("ravelry")

RAVELRY_USERNAME = os.getenv("RAVELRY_USERNAME")
RAVELRY_PASSWORD = os.getenv("RAVELRY_PASSWORD")
RAVELRY_BASE_URL = "https://api.ravelry.com"


def ravelry_get(path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
    if not RAVELRY_USERNAME or not RAVELRY_PASSWORD:
        raise RuntimeError("RAVELRY_USERNAME and RAVELRY_PASSWORD must be set")

    response = requests.get(
        f"{RAVELRY_BASE_URL}{path}",
        params=params or {},
        auth=(RAVELRY_USERNAME, RAVELRY_PASSWORD),
        timeout=30,
    )
    response.raise_for_status()
    return response.json()


@mcp.tool()
def current_user() -> dict[str, Any]:
    """
    Return information about the authenticated Ravelry user.
    """
    payload = ravelry_get("/current_user.json")
    return payload


@mcp.tool()
def search_patterns(query: str, page: int = 1) -> dict[str, Any]:
    """
    Search Ravelry patterns by a text query.
    """
    payload = ravelry_get(
        "/patterns/search.json",
        params={"query": query, "page": page},
    )
    return payload


@mcp.tool()
def get_pattern(pattern_id: int) -> dict[str, Any]:
    """
    Fetch a specific Ravelry pattern by ID.
    """
    payload = ravelry_get(f"/patterns/{pattern_id}.json")
    return payload


@mcp.tool()
def get_yarn(yarn_id: int) -> dict[str, Any]:
    """
    Fetch a specific yarn by ID.
    """
    payload = ravelry_get(f"/yarns/{yarn_id}.json")
    return payload


if __name__ == "__main__":
    mcp.run()
