import os
import xml.etree.ElementTree as ET
from typing import Any

import requests


def arxiv_search_tool(query: str, max_results: int = 5) -> list[dict[str, Any]]:
    """Search arXiv and return compact paper records."""
    response = requests.get(
        "https://export.arxiv.org/api/query",
        params={"search_query": f"all:{query}", "start": 0, "max_results": max_results},
        timeout=30,
    )
    response.raise_for_status()

    namespace = {"atom": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(response.text)
    papers = []
    for entry in root.findall("atom:entry", namespace):
        links = entry.findall("atom:link", namespace)
        pdf_link = next(
            (link.attrib.get("href") for link in links if link.attrib.get("title") == "pdf"),
            None,
        )
        papers.append(
            {
                "title": (entry.findtext("atom:title", default="", namespaces=namespace) or "").strip(),
                "authors": [
                    (author.findtext("atom:name", default="", namespaces=namespace) or "").strip()
                    for author in entry.findall("atom:author", namespace)
                ],
                "published": (entry.findtext("atom:published", default="", namespaces=namespace) or "")[:10],
                "summary": (entry.findtext("atom:summary", default="", namespaces=namespace) or "").strip(),
                "url": (entry.findtext("atom:id", default="", namespaces=namespace) or "").strip(),
                "link_pdf": pdf_link,
            }
        )
    return papers


def tavily_search_tool(
    query: str,
    max_results: int = 5,
    include_images: bool = False,
) -> list[dict[str, Any]]:
    """Search the web with Tavily and return source records."""
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        raise ValueError("TAVILY_API_KEY is missing from .env.")

    response = requests.post(
        "https://api.tavily.com/search",
        json={
            "api_key": api_key,
            "query": query,
            "max_results": max_results,
            "include_images": include_images,
        },
        timeout=30,
    )
    response.raise_for_status()
    payload = response.json()
    return [
        {
            "title": item.get("title", ""),
            "content": item.get("content", ""),
            "url": item.get("url", ""),
            "images": item.get("images", []) if include_images else [],
        }
        for item in payload.get("results", [])
    ]


arxiv_tool_def = {
    "type": "function",
    "function": {
        "name": "arxiv_search_tool",
        "description": "Search arXiv for academic papers and return titles, authors, abstracts, and links.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Academic search query."},
                "max_results": {"type": "integer", "description": "Number of papers to return.", "default": 5},
            },
            "required": ["query"],
            "additionalProperties": False,
        },
    },
}

tavily_tool_def = {
    "type": "function",
    "function": {
        "name": "tavily_search_tool",
        "description": "Search the web for current, reliable sources and return URLs with summaries.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Web search query."},
                "max_results": {"type": "integer", "description": "Number of results to return.", "default": 5},
                "include_images": {"type": "boolean", "description": "Whether to include image URLs.", "default": False},
            },
            "required": ["query"],
            "additionalProperties": False,
        },
    },
}
