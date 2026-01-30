from streamlit.navigation.page import StreamlitPage

from libs.cms.md import MarkdownDoc


def page_from_doc(md_doc: MarkdownDoc, backlink: str | None = None) -> StreamlitPage:
    import streamlit as st

    def _render() -> None:
        if backlink:
            if hasattr(st, "page_link"):
                st.page_link(backlink, label="Back", icon=":material/arrow_back:")
            else:
                if st.button("Back"):
                    st.switch_page(backlink)
            st.divider()

        st.title(md_doc.title)
        content = md_doc.content or "*No content provided.*"
        st.markdown(content, unsafe_allow_html=True)

    page_kwargs = {"title": md_doc.title}
    if md_doc.icon:
        page_kwargs["icon"] = md_doc.icon

    url_path = md_doc.metadata.get("url_path") if md_doc.metadata else None
    if url_path:
        page_kwargs["url_path"] = url_path

    return st.Page(_render, **page_kwargs)
