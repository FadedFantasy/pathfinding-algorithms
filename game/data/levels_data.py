from dataclasses import dataclass, field

from game.data.grid_data import GridData
from game.environment.wall import Wall


@dataclass
class Level1Data:
    grid: GridData = GridData
    walls: list[Wall] | None = None

@dataclass
class Level2Data:
    grid: GridData = GridData
    walls: list[Wall] = field(default_factory=lambda: [
        Wall(15, 15),
        Wall(15, 16),
        Wall(15, 17),
        Wall(15, 18),
        Wall(15, 19),
        Wall(15, 20),
        Wall(15, 21),
    ])

