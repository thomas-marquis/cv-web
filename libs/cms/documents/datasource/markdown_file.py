from __future__ import annotations

import base64
import datetime as dt
import mimetypes
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import streamlit as st
import yaml

from ...common import Skill, TimePeriod


@dataclass
class MarkdownDocument:
    path: Path
    title: str
    icon: str | None = None
    description: str | None = None
    metadata: dict[str, str] = field(default_factory=dict)
    section: str | None = None
    skills: list[Skill] = field(default_factory=list)
    weight: int = 0
    period: TimePeriod | None = None
    image_path: Path | None = None
    highlighted: bool = False

    _content: str | None = None

    @classmethod
    def from_metadata(cls, path: Path, doc_metadata: dict[str, str]) -> MarkdownDocument:
        skills: list[dict[str, str]] = doc_metadata.get("skills", [])

        tp = None
        if period := doc_metadata.get("period", {}):
            fmt = period.get("format", "%Y-%m-%d")
            tp = TimePeriod(
                start=dt.datetime.strptime(s, fmt) if (s := period.get("from")) else None,
                end=dt.datetime.strptime(e, fmt) if (e := period.get("to")) else None,
            )

        image_path = Path(p) if (p := doc_metadata.get("image")) else None

        doc = cls(
            path=path,
            title=doc_metadata.get("title", path.stem.replace("-", " ").title()),
            metadata=doc_metadata.get("metadata", {}),
            section=doc_metadata.get("section"),
            icon=doc_metadata.get("icon"),
            description=doc_metadata.get("description"),
            skills=[Skill(name=s["name"], details=s.get("details")) for s in skills],
            weight=int(doc_metadata.get("weight", 0)),
            period=tp,
            image_path=image_path,
            highlighted=doc_metadata.get("highlighted", False),
        )

        return doc

    @property
    def content(self) -> str:
        if self._content is not None:
            return self._content

        content = self.path.read_text(encoding="utf-8")
        if not content.startswith("---"):
            self._content = content
            return content

        lines = content.splitlines()[1:]

        body_start_idx = next((i for i, line in enumerate(lines) if line.strip() == "---"), None)

        if body_start_idx is None:
            content = "\n".join(lines).lstrip()
            return content

        content = "\n".join(lines[body_start_idx + 1 :]).lstrip()
        content = self._embed_local_images(content) if content else ""

        self._content = content

        return content

    def _embed_local_images(self, md: str) -> str:
        """Inline local image references as data URIs so Streamlit can render them."""

        doc_dir = self.path.parent

        def to_data_uri(url: str) -> str | None:
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", url) or url.startswith("data:"):
                return None

            img_path = (doc_dir / url).resolve()
            if not img_path.exists() or not img_path.is_file():
                return None

            mime, _ = mimetypes.guess_type(img_path.name)
            mime = mime or "image/png"
            encoded = base64.b64encode(img_path.read_bytes()).decode("ascii")
            return f"data:{mime};base64,{encoded}"

        def markdown_repl(match: re.Match[str]) -> str:
            alt_text, url = match.group(1), match.group(2).strip()
            data_uri = to_data_uri(url)
            if not data_uri:
                return match.group(0)
            return f"![{alt_text}]({data_uri})"

        def html_repl(match: re.Match[str]) -> str:
            before, url, after = match.group(1), match.group(2).strip(), match.group(3)
            data_uri = to_data_uri(url)
            if not data_uri:
                return match.group(0)
            return f'<img{before} src="{data_uri}"{after}>'

        image_pattern = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
        html_image_pattern = re.compile(r"<img\b([^>]*?)\bsrc=[\"']([^\"']+)[\"']([^>]*?)>", re.IGNORECASE)

        md = image_pattern.sub(markdown_repl, md)
        return html_image_pattern.sub(html_repl, md)


class MarkdownLoader:
    def __init__(self, dir_path: Path | str) -> None:
        if isinstance(dir_path, str):
            dir_path = Path(dir_path)
        if not dir_path.is_dir():
            raise ValueError(f"Directory not found: {dir_path}")

        self._dir_path = dir_path

    def load_all(self) -> list[MarkdownDocument]:
        return self.load_by_section("")

    def load_by_section(self, section: str) -> list[MarkdownDocument]:
        docs: list[MarkdownDocument] = []
        for path in sorted(self._dir_path.glob("*.md")):
            metadata = self._parse_front_matter(path.read_text(encoding="utf-8"))
            if not section or metadata.get("section") == section:
                md = MarkdownDocument.from_metadata(path, metadata)
                docs.append(md)
        return docs

    def load_by_filename(self, filename: str) -> MarkdownDocument | None:
        path = self._dir_path / filename
        if not path.is_file():
            return None
        return MarkdownDocument.from_metadata(path, self._parse_front_matter(path.read_text(encoding="utf-8")))

    @staticmethod
    def _parse_front_matter(text: str) -> dict[str, str]:
        """Extract YAML-like front matter and return metadata."""

        if not text.startswith("---"):
            return {}

        lines = text.splitlines()
        end_index = None
        for idx in range(1, len(lines)):
            if lines[idx].strip() == "---":
                end_index = idx
                break

        if end_index is None:
            return {}

        front_lines = lines[1:end_index]

        yaml_content = "\n".join(front_lines)
        metadata: dict[str, Any] = yaml.safe_load(yaml_content) or {}

        return metadata


@st.cache_data
def load_documents(dir_path: Path | str) -> list[MarkdownDocument]:
    return MarkdownLoader(dir_path).load_all()


@st.cache_data
def load_highlighted_documents(dir_path: Path | str) -> list[MarkdownDocument]:
    docs = load_documents(dir_path)
    return [doc for doc in docs if doc.highlighted]
