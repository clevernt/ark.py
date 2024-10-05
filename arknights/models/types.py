from typing import TypedDict


class Blackboard(TypedDict):
    key: str
    value: float


class UnlockCondition(TypedDict):
    phase: str
    level: int
