import datetime as dt
import textwrap

import polars as pl
import streamlit as st
import yaml
from streamlit.navigation.page import StreamlitPage

from libs.cms import back_nav_link
from libs.cms.data.layouts import cards_layout
from libs.cms.documents import load_highlighted_documents
from libs.cms.documents.layouts import cards_and_dialogs_layout, tabs_layout
from libs.cms.documents.layouts.tabs import RenderingHooks
from src.skills import SkillLevelEnum, get_skill_info, load_skills_data

SKILLS_FILEPATH = "content/skills.csv"
CATEGORIES_FILEPATH = "content/skill_categories.yaml"


@st.cache_data
def load_skill_categories() -> dict[str, dict[str, str]]:
    """Load skill categories configuration from YAML file."""
    with open(CATEGORIES_FILEPATH, "r") as f:
        config = yaml.safe_load(f)
    return config.get("categories", {})


@st.fragment
def overview() -> None:
    # Banner section with headline and value proposition
    if st.session_state.first_time:
        st.title("👋 Welcome!")
        st.session_state.first_time = False
    else:
        st.title("☕️ Thomas Marquis")

    # Professional headline and value proposition
    st.markdown("### MLOps Engineer | Scaling AI from Research to Production")
    st.markdown("**8+ years bridging software engineering and MLOps**")

    # Quick action buttons for recruiters
    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        st.page_link(
            _get_page("experiences", "View Experience →"),
            use_container_width=True,
            query_params={"from_page": "overview"},
        )
    with col2:
        st.page_link(
            _get_page("skills", "Browse Skills →"), use_container_width=True, query_params={"from_page": "overview"}
        )

    st.divider()

    # Core competencies section - optimized for quick scanning by recruiters
    st.markdown("#### :hammer_and_wrench: Core Competencies")

    # Display top expert-level skills with badges
    skills_data = load_skills_data(SKILLS_FILEPATH)
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

    # Recent experience highlight section
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
                        _get_page("experiences", "Read full details →"), query_params={"from_page": "overview"}
                    )

    st.divider()

    # Technical depth section - for technical managers, organized by categories
    st.markdown("#### :rocket: Technical Highlights")

    # Load skills data and categories configuration
    skills_data = load_skills_data(SKILLS_FILEPATH)
    category_config = load_skill_categories()

    # Get top skills per category (level >= 4 and used in production)
    top_skills_by_category = (
        skills_data.filter((pl.col("level") >= 4) & (pl.col("last_used_year") >= dt.date.today().year - 4))
        .sort(["category", "level"], descending=[False, True])
        .group_by("category")
        .agg(pl.col("name").head(10))  # Top 10 skills per category
    )

    # Create two columns for layout
    tech_col1, tech_col2 = st.columns(2)

    # Distribute categories across two columns (in the order defined in YAML)
    categories_list = [cat for cat in category_config.keys() if cat in top_skills_by_category["category"].to_list()]

    for idx, category in enumerate(categories_list):
        # Alternate between columns
        with tech_col1 if idx % 2 == 0 else tech_col2:
            skills_in_category = (
                top_skills_by_category.filter(pl.col("category") == category).select("name").to_series().to_list()
            )

            if skills_in_category and len(skills_in_category[0]) > 0:
                icon = category_config[category].get("icon", "📌")
                with st.expander(f"**{icon} {category}**", expanded=False):
                    skills_list = skills_in_category[0]
                    # Display as bullet list
                    for skill in skills_list:
                        st.markdown(f"- {skill}")

                    # Link to filtered skills page
                    st.page_link(
                        _get_page("skills", f"View all {category} skills →"),
                        query_params={"category": category, "from_page": "overview"},
                    )
    st.divider()

    # Publications and contributions section
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

    st.page_link(_get_page("publications", "View all publications →"))

    st.divider()

    # Call to action section
    st.markdown("#### :mailbox: Let's Connect")

    cta_col1, cta_col2, cta_col3 = st.columns(3)

    with cta_col1:
        st.page_link(
            _get_page("experiences", ":briefcase: Full Experience"),
            use_container_width=True,
            query_params={"from_page": "overview"},
        )

    with cta_col2:
        st.page_link(
            _get_page("projects", ":rocket: Side Projects"),
            use_container_width=True,
            query_params={"from_page": "overview"},
        )

    with cta_col3:
        st.page_link(
            _get_page("contact", ":email: Contact Me"), use_container_width=True, query_params={"from_page": "overview"}
        )


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
                "category": skill.category,
                "from_page": "experiences",
            },
        )


@st.fragment
def cv_skills() -> None:
    back_nav_link(_get_page)

    st.title(":hammer_and_wrench: Skills")

    data = (
        load_skills_data(SKILLS_FILEPATH).select(pl.exclude("highlighted")).with_columns(pl.col("link").fill_null(""))
    )

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
        full_data = load_skills_data(SKILLS_FILEPATH)

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


@st.fragment
def cv_education() -> None:
    back_nav_link(_get_page)

    cards_and_dialogs_layout(":man_student: Education", "content/education")

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


def _get_page(name: str, label: str | None = None) -> StreamlitPage:
    label = label or name.title()

    match name:
        case "overview":
            return st.Page(overview, title=label)
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
