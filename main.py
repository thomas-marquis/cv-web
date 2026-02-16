import streamlit as st

from src.pages import ORDERED_SECTIONS, router


def main() -> None:
    with open("content/assets/images/site-logo-tr.png", "rb") as f:
        logo_image = f.read()
    st.set_page_config(page_title="Thomas Marquis | MLOps & AI Engineer", page_icon=logo_image)
    st.logo(logo_image, size="large")

    st.session_state.setdefault("first_time", True)

    router.render(sections_order=ORDERED_SECTIONS)


if __name__ == "__main__":
    main()
