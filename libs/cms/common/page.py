from typing import Protocol

from streamlit.navigation.page import StreamlitPage


class Pager(Protocol):
    def __call__(self, page_name: str, display_label: str) -> StreamlitPage: ...