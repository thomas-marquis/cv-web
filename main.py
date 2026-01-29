import streamlit as st



def main() -> None:
    st.set_page_config(page_title="CV Portfolio", page_icon=":briefcase:")
    st.title("Thomas Marquis")

    home_page = st.Page("src/pages/home.py", title="Home")
    projects_page = st.Page("src/pages/projects.py", title="Projects")
    pg = st.navigation([home_page, projects_page], position="sidebar")

    pg.run()



if __name__ == "__main__":
    main()
