import datetime as dt
import textwrap

import polars as pl
import streamlit as st
from streamlit.navigation.page import StreamlitPage

from libs.cms import back_nav_link
from libs.cms.data.layouts import cards_layout
from libs.cms.documents.layouts import cards_and_dialogs_layout, tabs_layout
from libs.cms.documents.layouts.tabs import RenderingHooks
from src.skills import SkillLevelEnum, get_skill_info, load_skills_data

SKILLS_FILEPATH = "content/skills.csv"


@st.fragment
def overview() -> None:
    if st.session_state.first_time:
        st.title("👋 Welcome to my CV!")
        st.session_state.first_time = False
    else:
        st.title("☕️ About me")

    st.subheader("Last experience")


@st.fragment
def cv_experiences() -> None:
    back_nav_link(_get_page)

    cards_and_dialogs_layout(
        ":briefcase: Professional Experiences", "content/experiences", {"on_skill_popover": _render_skill_popover}
    )

    st.divider()
    with st.container(horizontal_alignment="right"):
        st.page_link(
            _get_page("education", "See education ->"),
            query_params={"from_page": "experiences"},
        )


def _render_skill_popover(skill_name: str) -> None:
    skill = get_skill_info(skill_name)
    if skill is None:
        return

    nb_cols = 0
    if skill.level:
        nb_cols += 1
    if skill.link:
        nb_cols += 1

    cols = st.columns(nb_cols)

    if skill.level:
        with cols[0]:
            st.metric(
                "Level", skill.level.level, None, help=f"{skill.level.label}: {skill.level.description}", format="%d/5"
            )

    if skill.link:
        with cols[1]:
            st.link_button("About :material/open_in_new:", skill.link, type="secondary")

    if skill.last_used_year:
        msg = f"Used for the last time in {skill.last_used_year}"
        if skill.in_industrial_context is not None and not skill.in_industrial_context:
            msg += " (never in production)"
        st.caption(msg)

    with st.container(horizontal_alignment="right"):
        st.page_link(
            _get_page("skills", "View all related skills ->"),
            query_params={
                "skill_name": skill.name,
                "from_page": "experiences",
            },
        )


@st.fragment
def cv_skills() -> None:
    back_nav_link(_get_page)

    st.title(":hammer_and_wrench: Skills")

    data = load_skills_data(SKILLS_FILEPATH)

    filters = []

    with st.expander("Filters...", expanded=False):
        cols = st.columns(2)
        with cols[0]:
            prod_only = st.radio(
                "Show only skills used in production?",
                (None, True, False),
                format_func=lambda x: {True: "Yes", False: "No", None: "View All"}[x],
                key="prod_filter",
            )
            if prod_only is not None:
                filters.append({"type": "is_equal", "column": "in_industrial_context", "value": prod_only})
        with cols[1]:
            max_age = st.slider("Show skills used after...", 2017, dt.date.today().year, 2017, step=1, key="max_age")
            filters.append({"type": "is_greater_or_equal", "column": "last_used_year", "value": max_age})

            skill_name = st.text_input("Filter by skill name", key="skill_name")
            if skill_name:
                filters.append({"type": "is_match_str", "column": "name", "value": skill_name})

    if "skill_name" in st.query_params:
        filters.append({"type": "is_match_str", "column": "name", "value": st.query_params.skill_name})
        st.query_params.pop("skill_name", None)

    if st.button("Reset filters", key="reset_filters"):
        filters = []

    for f in filters:
        if "type" not in f:
            raise RuntimeError("Filter must have a type")

        match f["type"]:
            case "is_equal":
                data = data.filter(pl.col(f["column"]) == f["value"])
            case "is_match_str":
                data = data.filter(pl.col(f["column"]).str.contains_any([f["value"]], ascii_case_insensitive=True))
            case "is_greater_or_equal":
                data = data.filter(pl.col(f["column"]) >= f["value"])
            case _:
                raise RuntimeError(f"Unknown filter type: {f['type']}")

    st.dataframe(
        data,
        height="content",
        column_config={
            "name": st.column_config.TextColumn(
                "Skill",
                pinned=True,
            ),
            "level": st.column_config.ProgressColumn(
                "Level",
                help="Self-evaluated level for the skill. "
                "It correspond to the level reached the last time I used the skill. "
                'So, you need to consider this value regarding to the value of the column "Last used". '
                "See bellow for details about skill levels",
                min_value=0,
                max_value=5,
                format="%d/5",
            ),
            "last_used_year": st.column_config.NumberColumn(
                "Last used",
                help="Year when I last used this skill",
            ),
            "in_industrial_context": st.column_config.CheckboxColumn(
                "Used in production?",
                help="Whether I used this skill in real production context or not",
            ),
            "link": st.column_config.LinkColumn(
                "More info...",
                help="Link to the skill documentation",
                default="-",
                display_text=r"https?://(.*?)\/.*",
            ),
        },
    )

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


@st.fragment
def cv_education() -> None:
    back_nav_link(_get_page)

    cards_and_dialogs_layout(":man_student: Education", "content/education", _get_page)

    st.divider()
    with st.container(horizontal_alignment="right"):
        st.page_link(
            _get_page("experiences", "See experiences ->"),
            query_params={"from_page": "education"},
        )


@st.fragment
def other_side_projects() -> None:
    back_nav_link(_get_page)

    hooks: RenderingHooks = {
        "overview_before": lambda: st.write(
            textwrap.dedent("""
            Alongside my professional work, I enjoy developing and experimenting with my own ideas.\n
            Some of these are purely personal projects, but over time, I’ve begun open-sourcing several of them.\n
            This list will continue to grow as I work on new projects.
            """)
        ),
    }

    tabs_layout(
        ":rocket: Side projects",
        "content/side-projects",
        _get_page,
        rendering_hooks=hooks,
    )


@st.fragment
def other_publications() -> None:
    back_nav_link(_get_page)
    cards_layout(":loudspeaker: Articles and Talks", "content/publications.yaml")


@st.fragment
def info_contact() -> None:
    back_nav_link(_get_page)
    st.title(":mailbox: Contact")
    st.write("TODO: contact info and form")


def _get_page(name: str, label: str | None = None) -> StreamlitPage:
    label = label or name.title()

    match name:
        case "experiences":
            return st.Page(cv_experiences, title=label)
        case "skills":
            return st.Page(cv_skills, title=label)
        case "education":
            return st.Page(cv_education, title=label)
        case "projects":
            return st.Page(other_side_projects, title=label)
        case "publications":
            return st.Page(other_publications, title=label)
        case "contact":
            return st.Page(info_contact, title=label)
        case _:
            raise ValueError(f"Unknown page name: {name}")
