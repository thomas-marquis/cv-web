import streamlit as st

from src import pages


def main() -> None:
    st.set_page_config(page_title="CV Portfolio", page_icon="☕️")

    st.session_state.setdefault("first_time", True)

    pg = {
        "": [
            st.Page(pages.overview, title="Thomas Marquis", icon=":material/home:"),
        ],
        "CV": [
            st.Page(pages.cv_experiences, title="Experiences", icon=":material/business_center:"),
            st.Page(pages.cv_skills, title="Skills", icon=":material/handyman:"),
            st.Page(pages.cv_education, title="Education", icon=":material/school:")
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



    pg = st.navigation(pg, position="sidebar", expanded=True)

    pg.run()



if __name__ == "__main__":
    main()
