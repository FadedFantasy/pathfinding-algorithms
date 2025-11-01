import pygame

from game.data.tile_data import TileData


class Wall:
    def __init__(self, grid_row: int, grid_col: int):
        self.grid_row = grid_row
        self.grid_col = grid_col
        self.color = (50, 50, 50)

    def get_pixel_pos(self):
        """Convert grid position to pixel position (top-left corner)"""
        pixel_x = self.grid_col * TileData.size
        pixel_y = self.grid_row * TileData.size
        return pixel_x, pixel_y

    def draw(self, surface):
        pixel_x, pixel_y = self.get_pixel_pos()
        # Draw filled rectangle
        pygame.draw.rect(surface, self.color,
                         (pixel_x, pixel_y, TileData.size, TileData.size))
        # Draw border
        pygame.draw.rect(surface, (30, 30, 30),
                         (pixel_x, pixel_y, TileData.size, TileData.size), 2)
