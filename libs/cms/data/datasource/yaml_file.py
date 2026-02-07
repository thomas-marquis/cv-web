import datetime as dt
from dataclasses import dataclass
from pathlib import Path

import yaml

_DEFAULT_DATE_FMT = "%Y-%m"


@dataclass
class Item:
    title: str
    link: str
    description: str | None = None
    category: str | None = None
    date: dt.datetime | None = None


class YamlDocumentLoader:
    def __init__(self, path: Path | str) -> None:
        self._path = Path(path)

        if not self._path.exists():
            raise ValueError(f"File not found: {self._path}")

    def load(self) -> list[Item]:
        content: dict = yaml.safe_load(self._path.read_text())
        raw_items = []
        if isinstance(content, list):
            raw_items = content
        elif isinstance(content, dict):
            raw_items = content.get("items", [])

        items = []
        for ri in raw_items:
            date = None
            if raw_date := ri.get("date"):
                date = dt.datetime.strptime(raw_date, ri.get("date_format", _DEFAULT_DATE_FMT))
            items.append(
                Item(
                    title=ri["title"],
                    link=ri["link"],
                    description=ri.get("description", ""),
                    category=ri.get("category", ""),
                    date=date,
                )
            )

        return items
