from operator import attrgetter
from pathlib import Path
from typing import Callable, TypedDict

import streamlit as st

from ...common import Pager
from ..datasource import load_documents


class RenderingHooks(TypedDict, total=False):
    overview_before: Callable[[], None]
    overview_after: Callable[[], None]


def tabs_layout(
    title: str, folder_path: Path | str, pager: Pager, rendering_hooks: RenderingHooks | None = None
) -> None:
    st.title(title)

    docs = load_documents(folder_path)
    if len(docs) == 0:
        st.write("Nothing to show here... yet...")
        return

    docs = sorted(docs, key=attrgetter("weight"), reverse=True)

    nb = len(docs)
    tabs = st.tabs([f"Overview ({nb})"] + [d.title for d in docs])
    with tabs[0]:
        if rendering_hooks and rendering_hooks.get("overview_before"):
            rendering_hooks["overview_before"]()
        for doc in docs:
            st.write(f"- **{doc.title}**")
            if doc.description:
                st.write(doc.description)
        if rendering_hooks and rendering_hooks.get("overview_after"):
            rendering_hooks["overview_after"]()

    for i in range(1, nb + 1):
        with tabs[i]:
            st.markdown(docs[i - 1].content, unsafe_allow_html=True)
