from pathlib import Path

import streamlit as st

from ..datasource import MarkdownDocument, MarkdownLoader


@st.cache_data
def _load_docs(folder_path: Path | str) -> list[MarkdownDocument]:
    loader = MarkdownLoader(folder_path)
    return loader.load_all()
