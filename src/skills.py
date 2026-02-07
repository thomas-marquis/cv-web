from collections import namedtuple
from dataclasses import dataclass
from enum import Enum

import polars as pl
import streamlit as st
import yaml

from libs.cms import Router

SKILLS_FILEPATH = "content/skills.csv"
CATEGORIES_FILEPATH = "content/skill_categories.yaml"

SkillLevel = namedtuple("SkillLevel", ["level", "label", "description", "examples"])


class SkillLevelEnum(Enum):
    BEGINNER = SkillLevel(
        level=1,
        label="Beginner",
        description="Basic theoretical understanding. Can perform simple tasks under supervision.",
        examples=[
            "Following step-by-step tutorials to set up a Kubernetes environment",
            "Writing basic Python scripts without advanced error handling",
            "Using basic Docker commands (e.g., docker run)",
            "Understanding pgvector concepts without production experience",
        ],
    )

    BASIC_INTERMEDIATE = SkillLevel(
        level=2,
        label="Basic Intermediate",
        description="Able to apply the skill in familiar contexts with occasional help.",
        examples=[
            "Configuring a basic CI/CD pipeline in AzureDevOps (YAML)",
            "Using MLflow for experiment tracking without optimization",
            "Writing simple SQL queries for PostgreSQL",
        ],
    )

    INTERMEDIATE = SkillLevel(
        level=3,
        label="Intermediate",
        description="Autonomous for standard tasks. Can adapt existing solutions to similar needs.",
        examples=[
            "Developing a Golang application with GORM and PostgreSQL",
            "Creating Helm Charts to deploy applications on Kubernetes",
            "Using Langchain to create a basic chatbot with embeddings",
        ],
    )

    ADVANCED = SkillLevel(
        level=4,
        label="Advanced",
        description="Masters the skill and can innovate or optimize solutions. Handles complex cases.",
        examples=[
            "Developing a Python library for data science workflows",
            "Creating complex AzureDevOps pipelines with YAML templates",
            "Implementing a RAG system with Golang and pgvector",
            "Deploying Transformers models in production with GPU optimization",
        ],
    )

    EXPERT = SkillLevel(
        level=5,
        label="Expert",
        description="Authority on the subject. Can teach, architect complex solutions, or innovate.",
        examples=[
            "Making strategic technical decisions (e.g., choosing between on-premise vs cloud LLM stacks)",
            "Training teams on scalable architectures and clean code",
        ],
    )

    def __str__(self):
        return f"{self.name}: {self.value.label} (Level {self.value.level})"

    @property
    def examples_formatted(self):
        """Returns formatted examples for better readability."""
        return "\n- ".join([""] + self.value.examples)

    @classmethod
    def get_by_level(cls, level: int) -> SkillLevel:
        """Get skill level enum by level number."""
        res = [s.value for s in cls if s.value.level == level]
        if len(res) == 0:
            raise RuntimeError(f"No skill level found for level {level}")
        return res[0]


@dataclass
class SkillInfo:
    name: str
    level: SkillLevel
    category: str
    last_used_year: int | None = None
    in_industrial_context: bool = False
    link: str | None = None


@st.cache_data
def load_skill_categories() -> dict[str, dict[str, str]]:
    with open(CATEGORIES_FILEPATH, "r") as f:
        config = yaml.safe_load(f)
    return config.get("categories", {})


@st.cache_data()
def load_skills_data() -> pl.DataFrame:
    return (
        pl.read_csv(SKILLS_FILEPATH, has_header=True)
        .cast(
            {
                "level": pl.Int64,
                "last_used_year": pl.Int64,
                "in_industrial_context": pl.Boolean,
                "highlighted": pl.Boolean,
            }
        )
        .sort("level", descending=True)
    )


@st.cache_data()
def get_skill_info(skill_name: str) -> SkillInfo | None:
    all_skills = load_skills_data()
    skill_row = all_skills.filter(pl.col("name").str.to_lowercase() == skill_name.lower())
    if len(skill_row) == 0:
        return None
    if len(skill_row) > 1:
        skill_row = skill_row.head(1)

    level = (
        tmp[0] if (tmp := [it.value for it in SkillLevelEnum if it.value.level == skill_row["level"].item()]) else None
    )

    return SkillInfo(
        name=skill_row["name"].item(),
        last_used_year=skill_row["last_used_year"].item(),
        level=level,
        in_industrial_context=skill_row["in_industrial_context"].item(),
        link=skill_row["link"].item(),
        category=skill_row["category"].item(),
    )


def render_skill_popover(skill_name: str, router: Router) -> None:
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
            router.get_page("skills", "View all related skills ->"),
            query_params={
                "category": skill.category,
                "from_page": "experiences",
            },
        )
