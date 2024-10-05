from typing import List, Literal, Union
from pydantic import BaseModel, Field, field_validator
from .enums import SubProfession
from .types import Blackboard, UnlockCondition


class Candidate(BaseModel):
    name: str
    description: str
    # blackboard: List[Blackboard]
    potential: int = Field(alias="requiredPotentialRank")
    unlock_condition: UnlockCondition = Field(alias="unlockCondition")


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
    skill_type: Literal["MANUAL", "AUTO", "PASSIVE"] = Field(alias="skillType")
    durationType: str
    sp_data: SPData = Field(alias="spData")
    duration: int
    blackboard: Union[Blackboard, List[Blackboard]]


class Skill(BaseModel):
    skill_id: str = Field(alias="skillId")


class SkillDetails(BaseModel):
    skill_id: str = Field(alias="skillId")
    levels: List[SkillLevel]


class OperatorDetail(BaseModel):
    id: str = Field(alias="potentialItemId")
    trait: str = Field(alias="description")
    description: str = Field(alias="itemUsage")
    position: str
    tag_list: List[str] = Field(alias="tagList")
    rarity: str
    profession: str
    sub_profession: str = Field(alias="subProfessionId")
    talents: List[Talent]
    skills: List[SkillDetails]

    @field_validator("id")
    def strip_id(cls, v):
        return v.replace("p_", "")

    @field_validator("sub_profession")
    def validate_sub_profession(cls, v):
        if v in SubProfession.__members__:
            return SubProfession[v]
        return v.title()
