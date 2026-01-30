from typing import Callable

import streamlit as st

from libs.cms.md import MarkdownLoader, MarkdownDoc


def make_page(md_loader: MarkdownLoader, section: str = "") -> Callable[[], None]:
    def page() -> None:
        st.header("Experiences")

        sub_pages = md_loader.load_by_section(section)

        tabs = st.tabs([
            e.title for e in sub_pages
        ])

        for tab, sp in zip(tabs, sub_pages):
            with tab:
                content = sp.content or "*No content provided.*"
                st.markdown(content, unsafe_allow_html=True)
    return page


def make_single_page(md_doc: MarkdownDoc) -> Callable[[], None]:
    def page() -> None:
        content = md_doc.content or "*No content provided.*"
        st.markdown(content, unsafe_allow_html=True)

    return page