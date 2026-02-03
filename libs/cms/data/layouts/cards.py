import datetime as dt
from pathlib import Path

import streamlit as st

from ..datasource import Item, YamlDocumentLoader


@st.cache_data
def load_items(path: Path | str) -> list[Item]:
    return YamlDocumentLoader(path).load()


def _render_card(item: Item) -> None:
    with st.container(border=True):
        st.subheader(item.title)

        cap = ""

        if item.category:
            cap += item.category

        if item.date:
            if cap:
                cap += " - "
            cap += item.date.strftime("%b %Y")

        if cap:
            st.caption(cap)

        if item.description:
            st.write(item.description)

        with st.container(horizontal_alignment="right"):
            st.link_button("View :material/open_in_new:", item.link, type="primary")


def cards_layout(title: str, path: Path | str) -> None:
    st.title(title)

    items = load_items(path)

    if len(items) == 0:
        st.write("Nothing to show here... yet...")
        return

    for item in sorted(items, key=lambda item: item.date or dt.datetime.min, reverse=True):
        _render_card(item)
