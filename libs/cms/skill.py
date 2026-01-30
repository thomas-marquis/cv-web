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
            "Developing a simple REST API with Spring Boot or Golang (GORM)",
            "Configuring a basic CI/CD pipeline in AzureDevOps (YAML)",
            "Using MLflow for experiment tracking without optimization",
            "Writing simple SQL queries for PostgreSQL",
            "Deploying a pre-trained PyTorch model without customization"
        ]
    )

    INTERMEDIATE = SkillLevel(
        level=3,
        label="Intermediate",
        description="Autonomous for standard tasks. Can adapt existing solutions to similar needs.",
        examples=[
            "Developing a Golang application with GORM and PostgreSQL (memory #7)",
            "Creating Helm Charts to deploy applications on Kubernetes",
            "Industrializing a Jupyter notebook into an Argo workflow (memory #3)",
            "Setting up an MLflow model registry (memory #6)",
            "Implementing unit tests with TDD (Python/Go)",
            "Using Langchain to create a basic chatbot with embeddings"
        ]
    )

    ADVANCED = SkillLevel(
        level=4,
        label="Advanced",
        description="Masters the skill and can innovate or optimize solutions. Handles complex cases.",
        examples=[
            "Architecting a complete MLOps solution with MLflow + Kubernetes (memory #6)",
            "Optimizing vector queries with pgvector (memory #7)",
            "Developing a Python library for data science workflows (memory #3)",
            "Creating complex AzureDevOps pipelines with YAML templates (memory #5)",
            "Mentoring teams on MLOps best practices",
            "Implementing a RAG system with Golang and pgvector (memory #7)",
            "Configuring a Kubernetes cluster with monitoring (Prometheus/Grafana)",
            "Deploying Transformers models in production with GPU optimization"
        ]
    )

    EXPERT = SkillLevel(
        level=5,
        label="Expert",
        description="Authority on the subject. Can teach, architect complex solutions, or innovate.",
        examples=[
            "Designing a self-hosted MLOps platform (MLflow + Helm + AzureDevOps) (memory #6)",
            "Developing an OpenID Connect library in Python (memory #3)",
            "Creating reusable frameworks for AI workflows (Langgraph/Genkit)",
            "Making strategic technical decisions (e.g., choosing between on-premise vs cloud LLM stacks)",
            "Training teams on scalable architectures and clean code",
            "Writing reference technical articles about Golang/AI (memory #7)",
            "Optimizing embeddings for specific use cases with pgvector",
            "Architecting multi-cloud solutions (Azure + on-premise)"
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