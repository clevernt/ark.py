from pydantic import BaseModel, Field, field_validator
from .enums import SPType, SkillType, SubProfession

__all__ = [
    "Candidate",
    "Talent",
    "SPData",
    "SkillLevel",
    "Skill",
    "SkillDetails",
    "OperatorDetail",
]


class Candidate(BaseModel):
    name: str
    description: str
    potential: int = Field(alias="requiredPotentialRank")
    unlock_condition: dict[str, float] = Field(alias="unlockCondition")


class Talent(BaseModel):
    candidates: list[Candidate]


class SPData(BaseModel):
    sp_type: SPType = Field(alias="spType")
    sp_cost: int = Field(alias="spCost")
    initial_sp: int = Field(alias="initSp")


class SkillLevel(BaseModel):
    name: str
    description: str
    skill_type: SkillType = Field(alias="skillType")
    durationType: str
    sp_data: SPData = Field(alias="spData")
    duration: int
    blackboard: dict[str, float] | list[dict[str, float]]


class Skill(BaseModel):
    skill_id: str = Field(alias="skillId")


class SkillDetails(BaseModel):
    skill_id: str = Field(alias="skillId")
    levels: list[SkillLevel]


class OperatorDetail(BaseModel):
    id: str = Field(alias="potentialItemId")
    name: str
    trait: str = Field(alias="description")
    description: str = Field(alias="itemUsage")
    position: str
    tag_list: list[str] = Field(alias="tagList")
    rarity: str
    profession: str
    sub_profession: str = Field(alias="subProfessionId")
    talents: list[Talent]
    skills: list[SkillDetails]

    @field_validator("id")
    def strip_id(cls, v):
        return v.replace("p_", "")

    @field_validator("sub_profession")
    def validate_sub_profession(cls, v):
        if v in SubProfession.__members__:
            return SubProfession[v]
        return v.title()
