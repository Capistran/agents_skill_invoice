"""Collect official source snapshots and produce a traceable change report."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


USER_AGENT = "agentes-fiscales/0.1 (+official-source-monitoring)"


@dataclass(frozen=True)
class FetchResult:
    status: str
    content_hash: str | None
    http_status: int | None = None
    error: str | None = None


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def content_hash(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def load_catalog(path: Path) -> dict[str, Any]:
    catalog = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(catalog.get("sources"), list):
        raise ValueError("El catálogo debe contener una lista 'sources'.")
    return catalog


def fetch_source(url: str, timeout: int = 30) -> tuple[bytes, int]:
    request = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(request, timeout=timeout) as response:
        return response.read(), response.status


def compare_source(source: dict[str, Any], state_dir: Path, content_dir: Path | None) -> FetchResult:
    source_id = source["id"]
    try:
        state_dir.mkdir(parents=True, exist_ok=True)
        if content_dir is None:
            content, http_status = fetch_source(source["url"])
        else:
            fixture = content_dir / f"{source_id}.html"
            content = fixture.read_bytes()
            http_status = 200
        current_hash = content_hash(content)
        state_path = state_dir / f"{source_id}.json"
        previous = json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() else None
        status = "new" if previous is None else (
            "unchanged" if previous.get("content_hash") == current_hash else "changed"
        )
        state_path.write_text(
            json.dumps(
                {
                    "source_id": source_id,
                    "url": source["url"],
                    "content_hash": current_hash,
                    "http_status": http_status,
                    "consulted_at": utc_now(),
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        return FetchResult(status, current_hash, http_status)
    except (HTTPError, URLError, OSError, ValueError) as error:
        return FetchResult("error", None, error=str(error))


def build_report(catalog: dict[str, Any], results: dict[str, FetchResult]) -> dict[str, Any]:
    changes = []
    for source in catalog["sources"]:
        result = results[source["id"]]
        changes.append(
            {
                "source_id": source["id"],
                "title": source["title"],
                "authority": source["authority"],
                "url": source["url"],
                "status": result.status,
                "http_status": result.http_status,
                "content_hash": result.content_hash,
                "error": result.error,
            }
        )
    return {
        "jurisdiction": catalog["jurisdiction"],
        "generated_at": utc_now(),
        "changes": changes,
        "review_required": any(item["status"] in {"new", "changed", "error"} for item in changes),
    }


def collect(args: argparse.Namespace) -> int:
    catalog = load_catalog(args.catalog)
    enabled_sources = [source for source in catalog["sources"] if source.get("enabled", True)]
    args.state.mkdir(parents=True, exist_ok=True)
    results = {
        source["id"]: compare_source(source, args.state, args.content_dir)
        for source in enabled_sources
    }
    report = build_report({**catalog, "sources": enabled_sources}, results)
    args.output.mkdir(parents=True, exist_ok=True)
    report_path = args.output / f"{catalog['jurisdiction'].lower()}-latest.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(report_path)
    return 1 if any(result.status == "error" for result in results.values()) else 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    collect_parser = subparsers.add_parser("collect", help="Consulta y compara las fuentes del catálogo.")
    collect_parser.add_argument("--catalog", type=Path, required=True)
    collect_parser.add_argument("--state", type=Path, default=Path("data/state"))
    collect_parser.add_argument("--output", type=Path, default=Path("reports"))
    collect_parser.add_argument(
        "--content-dir",
        type=Path,
        help="Directorio de fixtures .html para pruebas locales, sin acceder a la red.",
    )
    collect_parser.set_defaults(handler=collect)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return args.handler(args)


if __name__ == "__main__":
    sys.exit(main())