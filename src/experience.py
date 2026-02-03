from typing import Callable

import streamlit as st

from libs.cms.md import MarkdownDoc


@st.fragment
def card(xp_doc: MarkdownDoc, on_click: Callable[[MarkdownDoc], None]) -> None:
    if xp_doc.period and (start := xp_doc.period.start):
        end = xp_doc.period.end
        label = start.strftime("%B %Y - ")
        if end:
            label += end.strftime("%B %Y")
        else:
            label += "Present"
        st.subheader(f":material/line_start_circle: {label} :material/line_end_circle:")

    with st.container(border=True):
        st.subheader(xp_doc.title)

        if xp_doc.image_path:
            with st.container(horizontal_alignment="center"):
                st.image(xp_doc.image_path, width=250)

        if d := xp_doc.description:
            st.write(d)

        if skills := xp_doc.skills:
            skills_list = ", ".join(skill.name for skill in skills)
            st.caption(f"Skills used: {skills_list}")

        with st.container(horizontal_alignment="right"):
            btn_key = f"details_open_btn_{xp_doc.title}"
            if st.button("Read the full story ->", key=btn_key, type="primary"):
                on_click(xp_doc)