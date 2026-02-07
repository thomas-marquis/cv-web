from collections import namedtuple
from enum import Enum
from dataclasses import dataclass

SkillLevel = namedtuple("SkillLevel", ["level", "label",  "description", "examples"])


@dataclass
class Skill:
    name: str
    """skill's name acts as a unique identifier"""

    details: str | None = None
    """details about how the skill was used in which context"""