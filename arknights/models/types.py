from typing import TypedDict

__all__ = ["Blackboard", "UnlockCondition"]


class Blackboard(TypedDict):
    key: str
    value: float


class UnlockCondition(TypedDict):
    phase: str
    level: int
