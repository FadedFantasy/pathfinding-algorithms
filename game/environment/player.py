import pygame
from game.data.tile_data import TileData
from game.data.grid_data import GridData


class Player:
    def __init__(self, grid_row: int, grid_col: int):
        self.grid_row = grid_row
        self.grid_col = grid_col

    def move_up(self, level):
        self._move(-1, 0, level)

    def move_down(self, level):
        self._move(1, 0, level)

    def move_left(self, level):
        self._move(0, -1, level)

    def move_right(self, level):
        self._move(0, 1, level)

    def _move(self, d_row: int, d_col: int, level):
        """Internal move with collision checking"""
        new_row = self.grid_row + d_row
        new_col = self.grid_col + d_col

        # Check bounds and walls
        if (0 <= new_row < GridData.rows and
                0 <= new_col < GridData.cols and
                level.is_walkable(new_row, new_col)):
            self.grid_row = new_row
            self.grid_col = new_col
            return True
        return False

    def get_pixel_pos(self):
        """Convert grid position to pixel position (center of tile)"""
        pixel_x = self.grid_col * TileData.size + TileData.size // 2
        pixel_y = self.grid_row * TileData.size + TileData.size // 2
        return pixel_x, pixel_y

    def draw(self, surface):
        pixel_x, pixel_y = self.get_pixel_pos()
        pygame.draw.circle(surface, (255, 0, 0), (pixel_x, pixel_y), TileData.size // 2)