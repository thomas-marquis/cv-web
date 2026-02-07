import datetime as dt
import textwrap
from pathlib import Path

import polars as pl
import streamlit as st

from libs.cms import DEFAULT_SECTION, Router, SectionName, get_file_data
from libs.cms.data.layouts import cards_layout
from libs.cms.documents import load_highlighted_documents
from libs.cms.documents.layouts import cards_and_dialogs_layout, tabs_layout
from libs.cms.documents.layouts.tabs import RenderingHooks
from src.skills import SkillLevelEnum, load_skill_categories, load_skills_data, render_skill_popover

_SECTION_CV: SectionName = "CV"
_SECTION_CONTRIBUTIONS: SectionName = "Contributions"
_SECTION_INFO: SectionName = "Information"

ORDERED_SECTIONS = [_SECTION_CV, _SECTION_CONTRIBUTIONS, _SECTION_INFO]

router = Router()


@router.page(DEFAULT_SECTION, title="Thomas Marquis", icon=":material/home:")
@st.fragment
def overview() -> None:
    if st.session_state.first_time:
        st.title("👋 Welcome!")
        st.session_state.first_time = False
    else:
        st.title("☕️ Thomas Marquis")

    st.subheader("MLOps Engineer | Scaling AI from Research to Production")

    cols = st.columns(2)
    with cols[0]:
        st.write(":material/check: 8 years of experience")
    with cols[1]:
        st.write(":material/check: Software engineering")
        st.write(":material/check: MLOps")
    st.space("small")

    # Quick action buttons for recruiters
    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        st.page_link(
            router.get_page("experiences", "View Experience →"),
            use_container_width=True,
            query_params={"from_page": "overview"},
        )
    with col2:
        st.page_link(
            router.get_page("skills", "Browse Skills →"),
            use_container_width=True,
            query_params={"from_page": "overview"},
        )

    with col3:
        with st.container(horizontal_alignment="right", vertical_alignment="top"):
            st.download_button(
                "Download my CV",
                data=get_file_data("content/documents/resume.pdf"),
                file_name="thomas_marquis_resume.pdf",
                type="tertiary",
                icon=":material/download:",
            )

    st.divider()

    st.markdown("#### :hammer_and_wrench: Core Competencies")

    skills_data = load_skills_data()
    top_skills = skills_data.filter(pl.col("highlighted")).sort("level", descending=True)

    if len(top_skills) > 0:
        cols = st.columns(4)
        for idx, skill in enumerate(top_skills.iter_rows(named=True)):
            with cols[idx % 4]:
                with st.container(border=True):
                    st.markdown(f"**{skill['name']}**")
                    st.caption(
                        f"⭐ {SkillLevelEnum.get_by_level(skill['level']).label} | Last: {skill['last_used_year']}"
                    )

    st.divider()

    st.markdown("#### :briefcase: Recent Experience Highlights")

    highlighted_experiences = load_highlighted_documents("content/experiences")

    if (nb := len(highlighted_experiences)) > 0:
        cols = st.columns(nb)
        for i, hexpe in enumerate(highlighted_experiences):
            with cols[i]:
                with st.container(border=True):
                    st.markdown(f"**🚀 {hexpe.title}**")
                    if p := hexpe.period:
                        per_label = f"📅 From {p.start.strftime('%b %Y')}"
                        if p.end:
                            per_label += f" to {p.end.strftime('%b %Y')}"
                        st.caption(per_label)
                    st.markdown(hexpe.description)
                    st.page_link(
                        router.get_page("experiences", "Read full details →"),
                        query_params={"from_page": "overview", "open_experience": hexpe.title},
                    )
    st.page_link(
        router.get_page("experiences", "View all experiences →"),
        query_params={"from_page": "overview"},
    )
    st.divider()

    st.markdown("#### :rocket: Technical Highlights")

    skills_data = load_skills_data()
    category_config = load_skill_categories()

    top_skills_by_category = (
        skills_data.filter((pl.col("level") >= 4) & (pl.col("last_used_year") >= dt.date.today().year - 4))
        .sort(["category", "level"], descending=[False, True])
        .group_by("category")
        .agg(pl.col("name").head(10))  # Top 10 skills per category
    )

    tech_col1, tech_col2 = st.columns(2)
    categories_list = [cat for cat in category_config.keys() if cat in top_skills_by_category["category"].to_list()]

    for idx, category in enumerate(categories_list):
        with tech_col1 if idx % 2 == 0 else tech_col2:
            skills_in_category = (
                top_skills_by_category.filter(pl.col("category") == category).select("name").to_series().to_list()
            )

            if skills_in_category and len(skills_in_category[0]) > 0:
                icon = category_config[category].get("icon", "📌")
                with st.expander(f"**{icon} {category}**", expanded=False):
                    skills_list = skills_in_category[0]
                    for skill in skills_list:
                        st.markdown(f"- {skill}")

                    st.page_link(
                        router.get_page("skills", f"View all {category} skills →"),
                        query_params={"category": category, "from_page": "overview"},
                    )
    st.divider()

    st.markdown("#### :loudspeaker: Recent Publications & Talks")

    pub_col1, pub_col2 = st.columns(2)

    with pub_col1:
        with st.container(border=True):
            st.markdown("**When Go Meets AI: Building a RAG Application with Genkit**")
            st.caption("Medium Article | September 2025")
            st.markdown(
                "Tutorial introducing Genkit fundamentals with practical examples for building RAG applications."
            )
            st.link_button(
                "Read article →",
                "https://medium.com/@thomas.marquis314/when-go-meets-ai-building-a-rag-application-with-genkit-3f0a2734eca7",
                use_container_width=True,
            )

    with pub_col2:
        with st.container(border=True):
            st.markdown("**Mini-Conf MLOps Paris**")
            st.caption("Conference Talk | December 2024")
            st.markdown("Presented on MLOps implementation strategies in complex enterprise environments.")
            st.link_button(
                "View details →",
                "https://www.linkedin.com/posts/florentpietot_premi%C3%A8re-%C3%A9dition-des-mini-conf-mlops-le-activity-7270806733076189184-ZA65/?originalSubdomain=fr",
                use_container_width=True,
            )

    st.page_link(router.get_page("publications", "View all publications →"))

    st.divider()

    st.markdown("#### :mailbox: Let's Connect")

    cta_col1, cta_col2, cta_col3 = st.columns(3)

    with cta_col1:
        st.page_link(
            router.get_page("experiences", ":briefcase: Full Experience"),
            use_container_width=True,
            query_params={"from_page": "overview"},
        )

    with cta_col2:
        st.page_link(
            router.get_page("side_projects", ":rocket: Side Projects"),
            use_container_width=True,
            query_params={"from_page": "overview"},
        )

    with cta_col3:
        st.page_link(
            router.get_page("contact", ":email: Contact Me"),
            use_container_width=True,
            query_params={"from_page": "overview"},
        )


@router.page(_SECTION_CV, title="Experiences", icon=":material/business_center:")
@st.fragment
def experiences() -> None:
    router.back_nav_link()

    cards_and_dialogs_layout(
        router,
        ":briefcase: Professional Experiences",
        "content/experiences",
        {"on_skill_popover": render_skill_popover},
        opened_doc_title=st.query_params.get("open_experience"),
    )

    st.divider()
    with st.container(horizontal_alignment="right"):
        st.page_link(
            router.get_page("education", "See education ->"),
            query_params={"from_page": "experiences"},
        )


@router.page(_SECTION_CV, title="Skills", icon=":material/handyman:")
@st.fragment
def skills() -> None:
    router.back_nav_link()

    st.title(":hammer_and_wrench: Skills")

    data = load_skills_data().select(pl.exclude("highlighted")).with_columns(pl.col("link").fill_null(""))

    filters = []

    with st.expander("Filters...", expanded=False):
        cols = st.columns(3)
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
            # Category filter
            categories = sorted(data["category"].unique().to_list())
            selected_category = st.selectbox(
                "Filter by category",
                options=["All"] + categories,
                key="category_filter",
            )
            if selected_category != "All":
                filters.append({"type": "is_equal", "column": "category", "value": selected_category})

        with cols[2]:
            max_age = st.slider("Show skills used after...", 2017, dt.date.today().year, 2017, step=1, key="max_age")
            filters.append({"type": "is_greater_or_equal", "column": "last_used_year", "value": max_age})

        skill_name = st.text_input("Filter by skill name", key="skill_name")
        if skill_name:
            filters.append({"type": "is_match_str", "column": "name", "value": skill_name})

    # Handle query parameters
    if "skill_name" in st.query_params:
        filters.append({"type": "is_match_str", "column": "name", "value": st.query_params.skill_name})
        st.query_params.pop("skill_name", None)

    if "category" in st.query_params:
        filters.append({"type": "is_equal", "column": "category", "value": st.query_params.category})
        st.query_params.pop("category", None)

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
        column_order=["name", "level", "last_used_year", "in_industrial_context", "category", "link"],
        column_config={
            "name": st.column_config.TextColumn(
                "Skill",
                pinned=True,
                width=180,
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
            "category": st.column_config.TextColumn(
                "Category",
                help="Skill category for classification",
            ),
            "link": st.column_config.LinkColumn(
                "More info...",
                help="Link to the skill documentation",
                default="",
                display_text=r"https?://(.*?)\/.*",
            ),
        },
    )

    # Bar chart of skills per category
    with st.expander("📊 Skills Distribution by Category", expanded=False):
        # Reload full dataset for the chart (ignoring filters)
        full_data = load_skills_data()

        # Count skills per category
        category_counts = full_data.group_by("category").agg(pl.len().alias("count")).sort("count", descending=True)

        st.bar_chart(
            category_counts,
            x="category",
            y="count",
            x_label="Category",
            y_label="Number of Skills",
            horizontal=False,
        )

        st.caption(f"Total: {len(full_data)} skills across {len(category_counts)} categories")

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


@router.page(_SECTION_CV, title="Education", icon=":material/school:")
@st.fragment
def education() -> None:
    router.back_nav_link()

    cards_and_dialogs_layout(router, ":man_student: Education", "content/education")

    st.divider()
    with st.container(horizontal_alignment="right"):
        st.page_link(
            router.get_page("experiences", "See experiences ->"),
            query_params={"from_page": "education"},
        )


@router.page(_SECTION_CONTRIBUTIONS, title="Side Projects", icon=":material/code:")
@st.fragment
def side_projects() -> None:
    router.back_nav_link()

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
        rendering_hooks=hooks,
    )


@router.page(_SECTION_CONTRIBUTIONS, title="Publications", icon=":material/book:")
@st.fragment
def publications() -> None:
    router.back_nav_link()
    cards_layout(":loudspeaker: Articles and Talks", "content/publications.yaml")


@router.page(_SECTION_INFO, title="Contact", icon=":material/email:")
@st.fragment
def contact() -> None:
    router.back_nav_link()
    st.title(":mailbox: Contact")

    st.space("medium")

    with st.container(horizontal_alignment="center"):
        st.subheader("Find me on...")
        cols = st.columns(3)
        with cols[0]:
            with st.container(horizontal=False, horizontal_alignment="center"):
                st.image("content/assets/images/linkedin-logo.png", caption="", width=50)
                st.link_button(
                    "LinkedIn",
                    "https://www.linkedin.com/in/thomas-marquis-contact/?locale=en",
                    type="tertiary",
                    icon=":material/open_in_new:",
                )
        with cols[1]:
            with st.container(horizontal=False, horizontal_alignment="center"):
                st.image("content/assets/images/github-logo.png", caption="", width=50)
                st.link_button(
                    "GitHub", "https://github.com/thomas-marquis", type="tertiary", icon=":material/open_in_new:"
                )
        with cols[2]:
            with st.container(horizontal=False, horizontal_alignment="center"):
                st.image("content/assets/images/medium-logo.png", caption="", width=50)
                st.link_button(
                    "Medium", "https://medium.com/@thomas.marquis314", type="tertiary", icon=":material/open_in_new:"
                )

        st.space("medium")
        st.success(
            "Feel free to reach out to me for any questions or collaboration opportunities, preferably via **LinkedIn**."
        )

        st.space("medium")

        st.info("References available on request")
