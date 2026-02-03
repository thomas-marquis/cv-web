import textwrap

import polars as pl
import streamlit as st
from streamlit.navigation.page import StreamlitPage

from libs.cms.documents.layouts import cards_and_dialogs_layout
from libs.cms.documents.layouts.tabs import tabs_layout
from libs.cms.md import MarkdownLoader

SKILLS_FILEPATH = "content/skills.csv"

xp_loader = MarkdownLoader("content/experiences")


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
    if "from_page" in st.query_params:
        page_name = st.query_params.from_page
        st.page_link(_get_page(page_name, f"<- Back to {page_name.title()}"))

    cards_and_dialogs_layout(":briefcase: Professional Experiences", "content/experiences", _get_page)

    st.divider()
    with st.container(horizontal_alignment="right"):
        st.page_link(
            _get_page("education", "See education ->"),
            query_params={"from_page": "experiences"},
        )


@st.cache_data()
def _load_data(path: str) -> pl.DataFrame:
    return pl.read_csv(path, has_header=True).cast(
        {
            "level": pl.Int64,
            "last_used_year": pl.Int64,
            "in_industrial_context": pl.Boolean,
        }
    )


@st.fragment
def cv_skills() -> None:
    st.title(":hammer_and_wrench: Skills")

    data = _load_data(SKILLS_FILEPATH)

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
            skill_name = st.text_input("Filter by skill name", key="skill_name")
            if skill_name:
                filters.append({"type": "is_match_str", "column": "name", "value": skill_name})

    if "skill_name" in st.query_params:
        filters.append({"type": "is_equal", "column": "name", "value": st.query_params.skill_name})

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
            case _:
                raise ValueError(f"Unknown filter type: {f['type']}")

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


@st.fragment
def cv_education() -> None:
    if "from_page" in st.query_params:
        page_name = st.query_params.from_page
        st.page_link(_get_page(page_name, f"<- Back to {page_name.title()}"))

    cards_and_dialogs_layout(":man_student: Education", "content/education", _get_page)

    st.divider()
    with st.container(horizontal_alignment="right"):
        st.page_link(
            _get_page("experiences", "See experiences ->"),
            query_params={"from_page": "education"},
        )


@st.fragment
def other_side_projects() -> None:
    tabs_layout(
        ":rocket: Side projects",
        "content/side-projects",
        _get_page,
        rendering_hooks={
            "overview_before": lambda: st.write(
                textwrap.dedent("""
            Alongside my professional activity, I like to develop and experiment my own ideas.\n
            Some of them are pure private project, but sooner, I've started to open-source some of them.\n
            This list is going to grow over time:
            """)
            ),
        },
    )


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
