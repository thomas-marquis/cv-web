import streamlit as st

from libs.cms.md import MarkdownLoader, MarkdownDoc
from libs.cms.widgets.card import card
from src.skills import SkillLevelEnum


def overview() -> None:
    st.title(":man_technologist: Overview")
    st.write("TODO: quick profile overview")




@st.dialog("Coucou", width="large")
def dialog_coucou(doc: MarkdownDoc) -> None:
    st.markdown(doc.content, unsafe_allow_html=True)
    if st.button("Even more"):
        dialog_coucou(doc)


def cv_experiences() -> None:
    st.title(":briefcase: Professional Experiences")

    card(title="Platform Tech lead for the AI team at Peaksys",
         subtitle="July 2022 - December 2025")

    loader = MarkdownLoader("content/projects")
    docs = loader.load_by_section("personal")

    if st.button("Show more"):
        dialog_coucou(docs[0])





def cv_skills() -> None:
    st.title(":hammer_and_wrench: Skills")

    with st.expander("About skill levels...", expanded=False):
        for level in SkillLevelEnum:
            label_col, desc_col, ex_col = st.columns(3)
            with label_col:
                st.write(f"**{level.value.level}-{level.value.label}**")
            with desc_col:
                st.write(f"{level.value.description}")
            with ex_col:
                with st.expander("Examples...", expanded=False):
                    st.write(level.examples_formatted)



def cv_education() -> None:
    st.title(":man_student: Education")
    st.write("TODO: education career")


def other_side_projects() -> None:
    st.title(":rocket: Side projects")

    loader = MarkdownLoader("content/projects")
    docs = loader.load_by_section("personal")


    nb = len(docs)
    tabs = st.tabs([f"Side projects ({nb})"] + [d.title for d in docs])
    with tabs[0]:
        st.write("TODO: side projects")

        for doc in docs:
            # with st.container(border=True):
            st.write(f"- {doc.title}")


    for i in range(1, nb+1):
        with tabs[i]:
            st.markdown(docs[i-1].content, unsafe_allow_html=True)



def other_publications() -> None:
    st.title(":loudspeaker: Articles and Talks")
    st.write("TODO: articles and talks")


def info_contact() -> None:
    st.title(":mailbox: Contact")
    st.write("TODO: contact info and form")