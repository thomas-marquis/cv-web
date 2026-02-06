import streamlit as st

from src import pages


def main() -> None:
    st.set_page_config(page_title="CV Portfolio", page_icon="☕️")

    st.session_state.setdefault("first_time", True)

    pages_map = {
        "": [
            st.Page(pages.overview, title="Thomas Marquis", icon=":material/home:"),
        ],
        "CV": [
            st.Page(pages.cv_experiences, title="Experiences", icon=":material/business_center:"),
            st.Page(pages.cv_skills, title="Skills", icon=":material/handyman:"),
            st.Page(pages.cv_education, title="Education", icon=":material/school:"),
        ],
        "Other": [
            st.Page(pages.other_side_projects, title="Side Projects", icon=":material/code:"),
            st.Page(pages.other_publications, title="Publications", icon=":material/book:"),
            # TODO: Repos
        ],
        "Information": [
            # TODO: Download
            st.Page(pages.info_contact, title="Contact", icon=":material/email:"),
        ],
    }

    pg = st.navigation(pages_map, position="hidden", expanded=True)
    pg.run()

    with st.sidebar:
        st.page_link(st.Page(pages.overview, title="Thomas Marquis", icon=":material/home:"))

        with st.container(vertical_alignment="distribute", height="stretch"):
            st.subheader("CV")
            st.page_link(st.Page(pages.cv_experiences, title="Experiences", icon=":material/business_center:"))
            st.page_link(st.Page(pages.cv_skills, title="Skills", icon=":material/handyman:"))
            st.page_link(st.Page(pages.cv_education, title="Education", icon=":material/school:"))
            st.divider()

            st.subheader("Other")
            st.page_link(st.Page(pages.other_side_projects, title="Side Projects", icon=":material/code:"))
            st.page_link(st.Page(pages.other_publications, title="Publications", icon=":material/book:"))
            st.divider()

            st.subheader("Information")
            st.page_link(st.Page(pages.info_contact, title="Contact", icon=":material/email:"))


if __name__ == "__main__":
    main()
