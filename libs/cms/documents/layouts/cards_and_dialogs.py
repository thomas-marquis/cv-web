from operator import attrgetter
from pathlib import Path
from typing import Callable

import streamlit as st

from ...common import Pager
from ..datasource import MarkdownDocument, MarkdownLoader
from ._load import _load_docs


@st.dialog("About this experience", width="medium")
def _open_experience(doc: MarkdownDocument, pager: Pager) -> None:
    st.markdown(doc.content, unsafe_allow_html=True)

    if not doc.skills:
        return
    st.divider()
    st.subheader("Skills used:")
    for skill in doc.skills:
        label = f"{skill.name}"
        if skill.details:
            label += " :material/info:"
        with st.expander(label, expanded=False):
            if skill.details:
                st.write(skill.details)
            with st.popover("About this skill", type="tertiary"):
                st.write(skill.details)
                with st.container(horizontal_alignment="right"):
                    st.page_link(
                        pager("skills", "View all related skills ->"),
                        query_params={
                            "skill_name": skill.name,
                            "from_page": "experiences",
                        },
                    )


@st.fragment
def card(
    doc: MarkdownDocument,
    pager: Pager,
    on_click: Callable[[MarkdownDocument, Pager], None],
) -> None:
    if doc.period and (start := doc.period.start):
        end = doc.period.end
        label = start.strftime("%B %Y - ")
        if end:
            label += end.strftime("%B %Y")
        else:
            label += "Present"
        st.subheader(f":material/line_start_circle: {label} :material/line_end_circle:")

    with st.container(border=True):
        st.subheader(doc.title)

        if doc.image_path:
            with st.container(horizontal_alignment="center"):
                st.image(doc.image_path, width=250)

        if d := doc.description:
            st.write(d)

        if skills := doc.skills:
            skills_list = ", ".join(skill.name for skill in skills)
            st.caption(f"Main skills: {skills_list}")

        with st.container(horizontal_alignment="right"):
            btn_key = f"details_open_btn_{doc.title}"
            if st.button("Read the full story ->", key=btn_key, type="primary"):
                on_click(doc, pager)


@st.fragment
def cards_and_dialogs_layout(title: str, folder_path: Path | str, pager: Pager) -> None:
    st.title(title)

    docs = _load_docs(folder_path)

    if len(docs) == 0:
        st.write("Nothing to show here... yet...")
        return

    for i, xp_doc in enumerate(sorted(docs, key=attrgetter("weight"), reverse=True)):
        card(xp_doc, pager, _open_experience)

        if i < len(docs) - 1:
            st.space("small")
