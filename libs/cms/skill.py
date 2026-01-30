from collections import namedtuple
from enum import Enum
from dataclasses import dataclass

SkillLevel = namedtuple("SkillLevel", ["level", "label",  "description", "examples"])


class SkillLevelEnum(Enum):
    """
    Enumeration of technical competence levels, adapted to Thomas Marquis' profile.
    Inspired by memories #3, #6, #7, #9 (Python, MLOps, Golang, AI).
    """
    BEGINNER = SkillLevel(
        level=1,
        label="Beginner",
        description="Basic theoretical understanding. Can perform simple tasks under supervision.",
        examples=[
            "Following step-by-step tutorials to set up a Kubernetes environment",
            "Writing basic Python scripts without advanced error handling",
            "Using basic Docker commands (e.g., docker run)",
            "Understanding pgvector concepts without production experience"
        ]
    )

    BASIC_INTERMEDIATE = SkillLevel(
        level=2,
        label="Basic Intermediate",
        description="Able to apply the skill in familiar contexts with occasional help.",
        examples=[
            "Configuring a basic CI/CD pipeline in AzureDevOps (YAML)",
            "Using MLflow for experiment tracking without optimization",
            "Writing simple SQL queries for PostgreSQL",
        ]
    )

    INTERMEDIATE = SkillLevel(
        level=3,
        label="Intermediate",
        description="Autonomous for standard tasks. Can adapt existing solutions to similar needs.",
        examples=[
            "Developing a Golang application with GORM and PostgreSQL",
            "Creating Helm Charts to deploy applications on Kubernetes",
            "Using Langchain to create a basic chatbot with embeddings"
        ]
    )

    ADVANCED = SkillLevel(
        level=4,
        label="Advanced",
        description="Masters the skill and can innovate or optimize solutions. Handles complex cases.",
        examples=[
            "Developing a Python library for data science workflows",
            "Creating complex AzureDevOps pipelines with YAML templates",
            "Implementing a RAG system with Golang and pgvector",
            "Deploying Transformers models in production with GPU optimization"
        ]
    )

    EXPERT = SkillLevel(
        level=5,
        label="Expert",
        description="Authority on the subject. Can teach, architect complex solutions, or innovate.",
        examples=[
            "Making strategic technical decisions (e.g., choosing between on-premise vs cloud LLM stacks)",
            "Training teams on scalable architectures and clean code",
        ]
    )

    def __str__(self):
        return f"{self.name}: {self.value.label} (Level {self.value.level})"

    @property
    def examples_formatted(self):
        """Returns formatted examples for better readability."""
        return "\n- ".join([""] + self.value.examples)


@dataclass
class UsedSkill:
    name: str
    """skill's name acts as a unique identifier"""

    details: str | None = None
    """details about how the skill was used in which context"""