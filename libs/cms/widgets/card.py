from typing import Protocol

import streamlit as st


class RunnablePage(Protocol):
    def run(self) -> None: ...


def card(
    title: str,
    subtitle: str,
    image: str | None = None,
    link: str | None = None,
    nav_page: str | RunnablePage | None = None,
    nav_label: str | None = None,
) -> None:
    """
    Render a simple card-like block using only Streamlit widgets.

    Args:
        title: Card heading text.
        subtitle: Supporting text shown under the title.
        image: Optional image URL or path.
        link: Optional URL to show as an external action button.
        nav_page: Optional Streamlit page identifier (string) or page object.
        nav_label: Optional label for the navigation button (defaults to "Open page").
    """
    with st.container(border=True):
        if image:
            st.image(image, use_container_width=True)

        text_col, action_col = st.columns([4, 1])

        with text_col:
            st.subheader(title)
            st.write(subtitle)

        with action_col:
            if link:
                st.link_button("Open", link, type="secondary", use_container_width=True)
            if nav_page and st.button(
                nav_label or "Open page", use_container_width=True, type="primary"
            ):
                _switch_page(nav_page)


def _switch_page(nav_page: str | RunnablePage) -> None:
    """Handle navigation whether a string or page object is provided."""
    if isinstance(nav_page, str):
        st.switch_page(nav_page)
        return

    run_callable = getattr(nav_page, "run", None)
    if callable(run_callable):
        run_callable()
        return

    # Fallback: attempt to switch using the object as-is (Streamlit may handle it)
    st.switch_page(nav_page)


def cared(
    title: str,
    subtitle: str,
    image: str | None = None,
    link: str | None = None,
    nav_page: str | RunnablePage | None = None,
    nav_label: str | None = None,
) -> None:
    """Backward-compatible alias for the previous typo."""
    card(
        title=title,
        subtitle=subtitle,
        image=image,
        link=link,
        nav_page=nav_page,
        nav_label=nav_label,
    )
