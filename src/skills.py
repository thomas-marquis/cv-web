from collections import namedtuple
from dataclasses import dataclass
from enum import Enum
from unicodedata import category

import polars as pl
import streamlit as st

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


@st.cache_data()
def load_skills_data(path: str) -> pl.DataFrame:
    return pl.read_csv(path, has_header=True).cast(
        {
            "level": pl.Int64,
            "last_used_year": pl.Int64,
            "in_industrial_context": pl.Boolean,
            "highlighted": pl.Boolean,
        }
    )


@st.cache_data()
def get_skill_info(skill_name: str) -> SkillInfo | None:
    all_skills = load_skills_data("content/skills.csv")
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
