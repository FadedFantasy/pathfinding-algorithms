from game.data.grid_data import GridData
from game.environment.wall import Wall


class Level:
    def __init__(self, grid: GridData, walls: list[Wall] | None):
        self.grid = grid
        self.walls = walls

    def is_walkable(self, row: int, col: int) -> bool:
        """Check if a grid position is walkable (not a wall)"""
        if not self.walls:
            return True
        for wall in self.walls:
            if wall.grid_row == row and wall.grid_col == col:
                return False
        return True

    def draw(self, surface):
        """Draw all walls"""
        if not self.walls:
            return
        for wall in self.walls:
            wall.draw(surface)




