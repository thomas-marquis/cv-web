from pathlib import Path
import sys

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from src.business.md import MarkdownDoc, MarkdownLoader


class TestMarkdownDoc:
    @pytest.fixture
    def make_doc(self, tmp_path):
        def _make_doc(content: str, filename: str = "doc.md") -> MarkdownDoc:
            path = tmp_path / filename
            path.write_text(content, encoding="utf-8")
            return MarkdownDoc(path=path, title="Sample")

        return _make_doc

    class TestFromMetadata:
        def test_uses_defaults_when_metadata_missing(self, tmp_path):
            path = tmp_path / "hello-world.md"
            path.write_text("Body", encoding="utf-8")

            doc = MarkdownDoc.from_metadata(path, {})

            assert doc.title == "Hello World"
            assert doc.metadata == {}
            assert doc.section is None
            assert doc.icon is None
            assert doc.path == path

        def test_prefers_values_from_metadata(self, tmp_path):
            path = tmp_path / "note.md"
            path.write_text("Body", encoding="utf-8")
            metadata = {
                "title": "Custom Title",
                "metadata": {"key": "value"},
                "section": "intro",
                "icon": "star",
            }

            doc = MarkdownDoc.from_metadata(path, metadata)

            assert doc.title == "Custom Title"
            assert doc.metadata == {"key": "value"}
            assert doc.section == "intro"
            assert doc.icon == "star"
            assert doc.path == path

    class TestContent:
        def test_returns_plain_text_when_no_front_matter(self, make_doc):
            doc = make_doc("Plain content")

            assert doc.content == "Plain content"

        def test_caches_content_after_first_read(self, make_doc):
            doc = make_doc("Original content")
            first_read = doc.content
            doc.path.write_text("Updated content", encoding="utf-8")

            assert doc.content == first_read

        def test_strips_front_matter_and_trims_body(self, make_doc):
            doc = make_doc("---\ntitle: Demo\n---\n\nBody text")

            assert doc.content == "Body text"

        def test_missing_closing_marker_is_not_cached(self, make_doc):
            doc = make_doc("---\ntitle: Draft\nBody without closing marker")
            first_read = doc.content
            doc.path.write_text("---\nnew content\nstill open", encoding="utf-8")

            assert first_read == "title: Draft\nBody without closing marker"
            assert doc.content == "new content\nstill open"

        def test_keeps_remote_images_unchanged(self, make_doc):
            doc = make_doc("---\ntitle: Demo\n---\n![Alt](https://example.com/image.png)")

            assert doc.content == "![Alt](https://example.com/image.png)"

        def test_returns_empty_string_when_body_missing(self, make_doc):
            doc = make_doc("---\ntitle: Empty\n---\n")

            assert doc.content == ""

        def test_embeds_local_images_with_data_uri(self, make_doc, tmp_path):
            image_path = tmp_path / "image.png"
            image_path.write_bytes(b"\x89PNG\r\n\x1a\ncontent")
            doc = make_doc(f"---\ntitle: Demo\n---\n![Alt]({image_path.name})")

            content = doc.content

            assert "![Alt](data:image/png;base64," in content
            assert image_path.name not in content


class TestMarkdownLoader:
    class TestInit:
        def test_raises_for_missing_directory(self, tmp_path):
            missing_dir = tmp_path / "missing"

            with pytest.raises(ValueError, match="Directory not found"):
                MarkdownLoader(missing_dir)

    @pytest.fixture
    def markdown_dir(self, tmp_path):
        dir_path = tmp_path / "markdown"
        dir_path.mkdir()
        (dir_path / "about.md").write_text(
            "---\n"
            "title: About\n"
            "section: about\n"
            "metadata:\n"
            "  tag: intro\n"
            "---\n"
            "About body",
            encoding="utf-8",
        )
        (dir_path / "work.md").write_text(
            "---\n"
            "title: Work\n"
            "section: work\n"
            "icon: briefcase\n"
            "---\n"
            "Work body",
            encoding="utf-8",
        )
        (dir_path / "draft.md").write_text(
            "---\n"
            "title: Draft\n"
            "Body without closing marker",
            encoding="utf-8",
        )
        (dir_path / "plain-text.md").write_text("Plain body", encoding="utf-8")
        return dir_path

    @pytest.fixture
    def loader(self, markdown_dir):
        return MarkdownLoader(markdown_dir)

    class TestLoadAll:
        def test_loads_every_markdown_file(self, loader):
            docs_by_title = {doc.title: doc for doc in loader.load_all()}

            assert set(docs_by_title) == {"About", "Work", "Draft", "Plain Text"}
            assert docs_by_title["About"].metadata == {"tag": "intro"}
            assert docs_by_title["Work"].section == "work"
            assert docs_by_title["Plain Text"].metadata == {}

        def test_preserves_paths_for_loaded_docs(self, loader, markdown_dir):
            docs = loader.load_all()
            loaded_paths = {doc.path for doc in docs}
            expected_paths = set(markdown_dir.glob("*.md"))

            assert loaded_paths == expected_paths

    class TestLoadBySection:
        def test_filters_docs_by_section(self, loader):
            docs = loader.load_by_section("about")

            assert [doc.title for doc in docs] == ["About"]

        def test_returns_empty_list_for_unknown_section(self, loader):
            assert loader.load_by_section("unknown") == []
