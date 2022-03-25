from enum import Enum, unique

@unique
class StatusEnum(Enum):
     ACTIF = "ACTIF"
     PASSIF = "PASSIF"
     SUSPENDU = "SUSPENDU"