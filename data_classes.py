from dataclasses import dataclass

@dataclass
class PlayerData:
    url: str
    name: str
    year_min: int
    year_max: int
    pos: str
    height: int
    weight: int



