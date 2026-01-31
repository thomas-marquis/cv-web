from operator import attrgetter

import streamlit as st
import polars

from libs.cms.md import MarkdownLoader, MarkdownDoc
from libs.cms.skill import SkillLevelEnum

SKILLS_FILEPATH = "content/skills.csv"

xp_loader = MarkdownLoader("content/experiences")


def overview() -> None:
    st.title(":man_technologist: Overview")


    st.subheader("Last experience")



@st.dialog("About this experience", width="medium")
def _open_experience(doc: MarkdownDoc) -> None:
    st.markdown(doc.content, unsafe_allow_html=True)

    if not doc.skills:
        return
    st.divider()
    st.subheader("Skills used during this experience:")
    for skill in doc.skills:
        label = f"{skill.name}"
        if skill.details:
            label += " :material/info:"
        with st.expander(label, expanded=False):
            if skill.details:
                st.write(skill.details)


def cv_experiences() -> None:
    st.title(":briefcase: Professional Experiences")

    docs = xp_loader.load_all()

    for i, xp_doc in enumerate(sorted(docs, key=attrgetter("weight"), reverse=True)):
        if xp_doc.period and (start := xp_doc.period.start):
            end = xp_doc.period.end
            label = start.strftime("%B %Y - ")
            if end:
                label += end.strftime("%B %Y")
            else:
                label += "Present"
            st.subheader(f"-> {label}")

        with st.container(border=True):
            st.subheader(xp_doc.title)

            if d := xp_doc.description:
                st.write(d)

            if skills := xp_doc.skills:
                skills_list = ", ".join(skill.name for skill in skills)
                st.caption(f"Skills used: {skills_list}")

            if st.button("Read the full story ->", key=f"details_open_btn_{xp_doc.title}"):
                _open_experience(xp_doc)

        if i < len(docs) - 1:
            st.space("small")





st.cache_data()
def _get_skills() -> polars.DataFrame:
    return (
        polars.read_csv(SKILLS_FILEPATH, has_header=True)
        .sort("last_used_year", descending=True)
        .rename({
            "name": "Skill",
            "level": "Level (see above)",
            "last_used_year": "Last used",
            "in_industrial_context": "Used in production?",
        })
    )



def cv_skills() -> None:
    st.title(":hammer_and_wrench: Skills")

    skills_df = _get_skills()

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

    st.dataframe(skills_df, height=600)



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