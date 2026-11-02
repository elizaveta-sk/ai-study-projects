import os
import xml.etree.ElementTree as ET
from typing import Any
from urllib.parse import quote

import requests


def arxiv_search_tool(query: str, max_results: int = 5) -> list[dict[str, Any]]:
    """Search arXiv for academic papers."""
    response = requests.get(
        "https://export.arxiv.org/api/query",
        params={"search_query": f"all:{query}", "start": 0, "max_results": max_results},
        timeout=30,
    )
    response.raise_for_status()
    namespace = {"atom": "http://www.w3.org/2005/Atom"}
    papers = []
    for entry in ET.fromstring(response.text).findall("atom:entry", namespace):
        papers.append({
            "title": (entry.findtext("atom:title", default="", namespaces=namespace) or "").strip(),
            "authors": [(author.findtext("atom:name", default="", namespaces=namespace) or "").strip() for author in entry.findall("atom:author", namespace)],
            "published": (entry.findtext("atom:published", default="", namespaces=namespace) or "")[:10],
            "summary": (entry.findtext("atom:summary", default="", namespaces=namespace) or "").strip(),
            "url": (entry.findtext("atom:id", default="", namespaces=namespace) or "").strip(),
        })
    return papers


def tavily_search_tool(query: str, max_results: int = 5) -> list[dict[str, str]]:
    """Search the web with Tavily."""
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        raise ValueError("TAVILY_API_KEY is missing from .env.")
    response = requests.post("https://api.tavily.com/search", json={"api_key": api_key, "query": query, "max_results": max_results}, timeout=30)
    response.raise_for_status()
    return [{"title": item.get("title", ""), "content": item.get("content", ""), "url": item.get("url", "")} for item in response.json().get("results", [])]


def wikipedia_search_tool(query: str) -> dict[str, str]:
    """Return an encyclopedic summary from Wikipedia."""
    response = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{quote(query)}", headers={"User-Agent": "planning-workflows-lab/1.0"}, timeout=30)
    response.raise_for_status()
    payload = response.json()
    return {"title": payload.get("title", ""), "summary": payload.get("extract", ""), "url": payload.get("content_urls", {}).get("desktop", {}).get("page", "")}
