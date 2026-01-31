from typing import Callable

from streamlit.navigation.page import StreamlitPage


type PageSelector = Callable[[str], StreamlitPage]