from operator import attrgetter
from unittest import case

import streamlit as st
import polars
from streamlit.navigation.page import StreamlitPage

from libs.cms.md import MarkdownLoader, MarkdownDoc
from libs.cms.skill import SkillLevelEnum
from src.experience import experience_card

SKILLS_FILEPATH = "content/skills.csv"

xp_loader = MarkdownLoader("content/experiences")

@st.fragment
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
            st.page_link(_get_page("skills", "Skills overview"),
                         query_params={"skill_name": skill.name, "from_page": "experiences"})


@st.fragment
def cv_experiences() -> None:
    st.title(":briefcase: Professional Experiences")

    docs = xp_loader.load_all()

    for i, xp_doc in enumerate(sorted(docs, key=attrgetter("weight"), reverse=True)):
        experience_card(xp_doc, _open_experience)
        # if xp_doc.period and (start := xp_doc.period.start):
        #     end = xp_doc.period.end
        #     label = start.strftime("%B %Y - ")
        #     if end:
        #         label += end.strftime("%B %Y")
        #     else:
        #         label += "Present"
        #     st.subheader(f"-> {label}")
        #
        # with st.container(border=True):
        #     st.subheader(xp_doc.title)
        #
        #     if d := xp_doc.description:
        #         st.write(d)
        #
        #     if skills := xp_doc.skills:
        #         skills_list = ", ".join(skill.name for skill in skills)
        #         st.caption(f"Skills used: {skills_list}")
        #
        #     btn_key = f"details_open_btn_{xp_doc.title}"
        #     if st.button("Read the full story ->", key=btn_key, type="primary"):
        #         _open_experience(xp_doc)

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


@st.fragment
def cv_skills() -> None:
    st.title(":hammer_and_wrench: Skills")

    if "from_page" in st.query_params:
        match st.query_params.from_page:
            case "experiences":
                st.page_link(_get_page("experiences", "<- Back to experiences"))

    skills_df = _get_skills()

    if "skill_name" in st.query_params:
        skill_name: str = st.query_params.skill_name
        skills_df = skills_df.filter(skills_df["Skill"] == skill_name)

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


@st.fragment
def cv_education() -> None:
    st.title(":man_student: Education")
    st.write("TODO: education career")

@st.fragment
def other_side_projects() -> None:
    st.title(":rocket: Side projects")

    loader = MarkdownLoader("content/projects")
    docs = loader.load_by_section("personal")


    nb = len(docs)
    tabs = st.tabs([f"Side projects ({nb})"] + [d.title for d in docs])
    with tabs[0]:
        st.write("TODO: side projects")

        for doc in docs:
            st.write(f"- {doc.title}")


    for i in range(1, nb+1):
        with tabs[i]:
            st.markdown(docs[i-1].content, unsafe_allow_html=True)


@st.fragment
def other_publications() -> None:
    st.title(":loudspeaker: Articles and Talks")
    st.write("TODO: articles and talks")

@st.fragment
def info_contact() -> None:
    st.title(":mailbox: Contact")
    st.write("TODO: contact info and form")



def _get_page(name: str, label: str | None = None) -> StreamlitPage:
    label = label or name.title()

    match name:
        case "experiences": return st.Page(cv_experiences, title=label)
        case "skills": return st.Page(cv_skills, title=label)
        case "education": return st.Page(cv_education, title=label)
        case "projects": return st.Page(other_side_projects, title=label)
        case "publications": return st.Page(other_publications, title=label)
        case "contact": return st.Page(info_contact, title=label)
        case _: raise ValueError(f"Unknown page name: {name}")