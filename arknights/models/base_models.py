from typing import Literal
from pydantic import BaseModel, Field, field_validator
from .enums import Branch, Class

__all__ = [
    "Candidate",
    "Talent",
    "SPData",
    "SkillLevel",
    "Skill",
    "Operator",
]


class Candidate(BaseModel):
    name: str
    description: str
    potential: int = Field(alias="requiredPotentialRank")
    unlock_condition: dict = Field(alias="unlockCondition")


class Talent(BaseModel):
    candidates: list[Candidate]


class SPData(BaseModel):
    sp_type: Literal[
        "INCREASE_WITH_TIME", "INCREASE_WHEN_ATTACK", "INCREASE_WHEN_TAKEN_DAMAGE"
    ] = Field(alias="spType")
    sp_cost: int = Field(alias="spCost")
    initial_sp: int = Field(alias="initSp")


class SkillLevel(BaseModel):
    name: str
    description: str
    skill_type: str = Field(alias="skillType")
    duration_type: str
    sp_data: SPData = Field(alias="spData")
    duration: int
    blackboard: list[dict]


class Skill(BaseModel):
    skill_id: str = Field(alias="skillId")
    levels: list[SkillLevel]


class Operator(BaseModel):
    """Represents an operator

    Attributes:
        id (str): The operator's ID.
        name (str): The operator's name.
        trait (str): The operator's trait
        description (str): The operator's description
        position (Literal["RANGED", "MELEE"]): The operator's position
        tag_list (list[str]): The operator's tags
        rarity [Literal["TIER_6", "TIER_5", "TIER_4", "TIER_3", "TIER_2", "TIER_1"]]: The operator's rarity
        class_ (Class): The operator's class.
        branch (Branch): The operator's branch.
        talents (list[Talent]): The operator's talents.
        skills (list[Skill]): The operator's skills.
    """

    id: str = Field(alias="potentialItemId")
    name: str
    trait: str = Field(alias="description")
    description: str = Field(alias="itemUsage")
    position: Literal["RANGED", "MELEE"]
    tag_list: list[str] = Field(alias="tagList")
    rarity: Literal["TIER_6", "TIER_5", "TIER_4", "TIER_3", "TIER_2", "TIER_1"]
    class_: str = Field(alias="profession")
    branch: str = Field(alias="subProfessionId")
    talents: list[Talent]
    skills: list[Skill]

    @field_validator("id", mode="before")
    def strip_id(cls, v):
        return v.replace("p_", "")

    @field_validator("branch", mode="before")
    def validate_branch(cls, v):
        if v in Branch.__members__:
            return Branch[v]
        return v.title()

    @field_validator("class_", mode="before")
    def validate_class(cls, v):
        return Class[v]
