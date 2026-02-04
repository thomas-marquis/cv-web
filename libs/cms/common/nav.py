import streamlit as st

from .page import Pager


def back_nav_link(pager: Pager) -> None:
    if "from_page" in st.query_params:
        page_name = st.query_params.from_page
        st.page_link(pager(page_name, f"<- Back to {page_name.title()}"))
