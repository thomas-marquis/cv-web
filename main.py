from __future__ import annotations

from pathlib import Path

import streamlit as st

CONTENT_DIR = Path("content")
PROJECTS_DIR = CONTENT_DIR / "projects"
ARTICLES_DIR = CONTENT_DIR / "articles"

PAGES = ["Home", "Projects", "Writing"]

LINKS = [
    {"label": "LinkedIn", "url": "https://www.linkedin.com/in/your-handle"},
    {"label": "GitHub", "url": "https://github.com/your-handle"},
    {"label": "Email", "url": "mailto:you@example.com"},
]

PROJECTS = [
    {
        "slug": "project-alpha",
        "title": "Project Alpha",
        "summary": "Short pitch about the impact, stack, and what recruiters should notice.",
        "image": "content/images/project-alpha.png",
        "md_path": PROJECTS_DIR / "project-alpha.md",
    },
    {
        "slug": "project-beta",
        "title": "Project Beta",
        "summary": "Another project highlight with a crisp, recruiter-friendly outcome.",
        "image": "content/images/project-beta.png",
        "md_path": PROJECTS_DIR / "project-beta.md",
    },
]

ARTICLES = [
    {
        "slug": "article-1",
        "title": "Production Article",
        "summary": "A quick teaser about the core idea and takeaway.",
        "md_path": ARTICLES_DIR / "article-1.md",
    }
]


def render_markdown(path: Path) -> None:
    if path.exists():
        st.markdown(path.read_text(encoding="utf-8"))
    else:
        st.info(f"Add content at `{path}` to replace this placeholder.")


def render_link_list() -> None:
    st.subheader("Links")
    cols = st.columns(len(LINKS))
    for col, link in zip(cols, LINKS):
        with col:
            st.link_button(link["label"], link["url"])


def render_image(image_path: str) -> None:
    if Path(image_path).exists():
        st.image(image_path, use_column_width=True)
    else:
        st.caption(f"Add image at `{image_path}`.")


def get_query_param(name: str, fallback: str | None = None) -> str | None:
    value = st.query_params.get(name)
    if value is None:
        return fallback
    if isinstance(value, list):
        return value[0] if value else fallback
    return value


def set_page_params(page: str, *, project: str | None = None, article: str | None = None) -> None:
    st.query_params.clear()
    st.query_params["page"] = page
    if project:
        st.query_params["project"] = project
    if article:
        st.query_params["article"] = article


def render_home() -> None:
    st.title("Your Name")
    render_markdown(CONTENT_DIR / "intro.md")
    render_link_list()

    tabs = st.tabs(["Experiences", "Education", "Skills"])
    with tabs[0]:
        render_markdown(CONTENT_DIR / "experiences.md")
    with tabs[1]:
        render_markdown(CONTENT_DIR / "education.md")
    with tabs[2]:
        render_markdown(CONTENT_DIR / "skills.md")


def render_project_cards() -> None:
    for project in PROJECTS:
        with st.container(border=True):
            cols = st.columns([1, 3])
            with cols[0]:
                render_image(project["image"])
            with cols[1]:
                st.subheader(project["title"])
                st.write(project["summary"])
                st.markdown(f"[Read more](?page=Projects&project={project['slug']})")


def render_project_detail(project_slug: str) -> None:
    project = next((item for item in PROJECTS if item["slug"] == project_slug), None)
    if not project:
        st.warning("Project not found.")
        st.markdown("[Back to projects](?page=Projects)")
        return
    st.title(project["title"])
    render_markdown(project["md_path"])
    st.markdown("[Back to projects](?page=Projects)")


def render_projects() -> None:
    st.header("Projects")
    project_slug = get_query_param("project")
    if project_slug:
        render_project_detail(project_slug)
        return
    render_project_cards()


def render_article_cards() -> None:
    for article in ARTICLES:
        with st.container(border=True):
            st.subheader(article["title"])
            st.write(article["summary"])
            st.markdown(f"[Read more](?page=Writing&article={article['slug']})")


def render_article_detail(article_slug: str) -> None:
    article = next((item for item in ARTICLES if item["slug"] == article_slug), None)
    if not article:
        st.warning("Article not found.")
        st.markdown("[Back to writing](?page=Writing)")
        return
    st.title(article["title"])
    render_markdown(article["md_path"])
    st.markdown("[Back to writing](?page=Writing)")


def render_writing() -> None:
    st.header("Writing")
    article_slug = get_query_param("article")
    if article_slug:
        render_article_detail(article_slug)
        return
    render_article_cards()


def main() -> None:
    st.set_page_config(page_title="CV Portfolio", page_icon=":briefcase:", layout="wide")

    current_page = get_query_param("page", "Home")
    if current_page not in PAGES:
        current_page = "Home"

    st.sidebar.title("Navigate")
    selected_page = st.sidebar.radio("Pages", PAGES, index=PAGES.index(current_page))
    if selected_page != current_page:
        set_page_params(selected_page)

    if current_page == "Home":
        render_home()
    elif current_page == "Projects":
        render_projects()
    elif current_page == "Writing":
        render_writing()


if __name__ == "__main__":
    main()
