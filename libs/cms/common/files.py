from pathlib import Path

import streamlit as st


@st.cache_resource(show_spinner=True)
def get_file_data(path: str | Path) -> bytes:
    with open(path, "rb") as f:
        return f.read()
