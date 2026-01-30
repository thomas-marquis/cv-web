from pathlib import Path

import streamlit as st

from libs.cms.md import MarkdownLoader

PROJECT_DIR = Path("content/projects")


def projects_page():
    md_loader = MarkdownLoader(PROJECT_DIR)
    st.header("Projects")

    docs = md_loader.load_by_section("personal")
    if not docs:
        st.write("No project found.")
        return

    tabs = st.tabs([doc.title for doc in docs])
    for doc, tab in zip(docs, tabs):
        content = doc.content or "*No content provided.*"
        tab.markdown(content, unsafe_allow_html=True)
