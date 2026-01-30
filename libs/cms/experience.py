from dataclasses import dataclass


@dataclass
class Experience:
    title: str
    company: str
    description: str
    detailed_page_filename: str | None = None
    image: str | None = None