from enum import StrEnum

__all__ = ["SubProfession"]


class SubProfession(StrEnum):
    bearer = "Flagbearer"
    artsfghter = "Arts Fighter"
    sword = "Swordmaster"
    musha = "Soloblade"
    fearless = "Dreadnought"
    librator = "Liberator"
    unyield = "Juggernaut"
    artsprotector = "Arts Protector"
    fastshot = "Marksman"
    closerange = "Heavyshooter"
    aoesniper = "Artilleryman"
    longrange = "Deadeye"
    reaperrange = "Spreadshooter"
    siegesniper = "Besieger"
    bombarder = "Flinger"
    corecaster = "Core Caster"
    splashcaster = "Splash Caster"
    funnel = "Mech-accord Caster"
    phalanx = "Phalanx Caster"
    mystic = "Mystic Caster"
    chain = "Chain Caster"
    blastcaster = "Blast Caster"
    physician = "Medic"
    ringhealer = "Multitarget Medic"
    healer = "Therapist"
    wandermedic = "Wandering Medic"
    slower = "Decel Binder"
    craftsman = "Artificer"
    blessing = "Abjurer"
    underminer = "Hexer"
    pusher = "Push Stroker"
    stalker = "Ambusher"
    traper = "Trapmaster"
    incantationmedic = "Incantation Medic"
    shotprotector = "Sentinel Iron Guard"
    chainhealer = "Chain Healer"
    primcaster = "Primal Caster"


class SPType(StrEnum):
    INCREASE_WITH_TIME: str
    INCREASE_WHEN_ATTACK: str
    INCREASE_WHEN_TAKEN_DAMAGE: str


class SkillType(StrEnum):
    MANUAL: str
    AUTO: str
    PASSIVE: str
