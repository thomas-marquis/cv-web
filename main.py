import streamlit as st

from src.pages import router


def main() -> None:
    st.set_page_config(page_title="CV Portfolio", page_icon="☕️")

    st.session_state.setdefault("first_time", True)

    router.render(sections_order=["CV", "Contributions", "Information"])


if __name__ == "__main__":
    main()
