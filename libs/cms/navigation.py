from collections import defaultdict
from collections.abc import Callable
from typing import Sequence, TypedDict

import streamlit as st
from streamlit.navigation.page import StreamlitPage

type SectionName = str


DEFAULT_SECTION: SectionName = ""


class _PageConfig(TypedDict):
    key: str
    renderer: Callable[[], None]
    original_page: StreamlitPage
    show_in_nav: bool


class Router:
    def __init__(self) -> None:
        self._pages: dict[SectionName, list[_PageConfig]] = defaultdict(list)

    def render(self, sections_order: Sequence[SectionName] | None = None) -> None:
        pg = st.navigation(
            {sec: [p["original_page"] for p in pages] for sec, pages in self._pages.items()}, position="hidden"
        )
        pg.run()

        if sections_order:
            if DEFAULT_SECTION not in sections_order:
                sections_order = [DEFAULT_SECTION] + list(sections_order)
        else:
            sections_order = self._pages.keys()

        with st.sidebar:
            for i, section in enumerate(sections_order):
                st.subheader(section)
                for p in self._pages[section]:
                    if p["show_in_nav"]:
                        st.page_link(p["original_page"])

                if i < len(sections_order) - 1:
                    st.divider()

    def get_page(self, key: str, display_label: str | None = None) -> StreamlitPage:
        for sec, pages in self._pages.items():
            for p in pages:
                if p["key"] == key:
                    if not display_label:
                        return p["original_page"]
                    return st.Page(p["renderer"], title=display_label)

        raise RuntimeError(f"Page not found: {key}")

    def page(
        self,
        section: SectionName,
        key: str | None = None,
        title: str | None = None,
        show_in_nav: bool = True,
        icon: str | None = None,
        default: bool = False,
    ):
        def decorator(func: Callable):
            nonlocal key
            key = key or func.__name__
            page = st.Page(func, title=title or key.title(), icon=icon, default=default)
            self._pages[section] += [{"key": key, "original_page": page, "show_in_nav": show_in_nav, "renderer": func}]

            return func

        return decorator

    def back_nav_link(self) -> None:
        if "from_page" in st.query_params:
            page_name = st.query_params.from_page
            st.page_link(self.get_page(page_name, f"<- Back to {page_name.title()}"))
