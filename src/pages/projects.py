from pathlib import Path

import streamlit as st

from src.business.md import MarkdownLoader

PROJECT_DIR = Path("content/projects")


def render():
    md_loader = MarkdownLoader(PROJECT_DIR)
    st.header("Projects")

    docs = md_loader.load_all()
    if not docs:
        st.write("No project found.")
        return

    tabs = st.tabs([doc.tab_label for doc in docs])
    for doc, tab in zip(docs, tabs):
        content = doc.body or "*No content provided.*"
        tab.markdown(content, unsafe_allow_html=True)


if __name__ == "__main__":
    render()
