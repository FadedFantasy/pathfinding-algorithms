import random

import pygame

from game.data.grid_data import GridData
from game.data.tile_data import TileData


class Coin:
    def __init__(self):
        self.grid_row = 0
        self.grid_col = 0
        self.color = (255, 215, 0)

    def spawn(self, level, player, existing_coins=None):
        """Spawn coin at random empty location (avoid walls, player, and other coins)"""
        if existing_coins is None:
            existing_coins = []

        while True:
            self.grid_row = random.randint(0, GridData.rows - 1)
            self.grid_col = random.randint(0, GridData.cols - 1)

            # Check if location is valid
            if not level.is_walkable(self.grid_row, self.grid_col):
                continue
            # Check if not on player
            if self.grid_row == player.grid_row and self.grid_col == player.grid_col:
                continue
            # Check if not on another coin
            if any(coin.grid_row == self.grid_row and coin.grid_col == self.grid_col
                   for coin in existing_coins):
                continue
            break  # Found valid position

    def get_pixel_pos(self):
        """Convert grid position to pixel position (center of tile)"""
        pixel_x = self.grid_col * TileData.size + TileData.size // 2
        pixel_y = self.grid_row * TileData.size + TileData.size // 2
        return pixel_x, pixel_y

    def draw(self, surface):
        pixel_x, pixel_y = self.get_pixel_pos()
        pygame.draw.circle(surface, self.color, (pixel_x, pixel_y), TileData.size // 3)
        pygame.draw.circle(surface, (218, 165, 32), (pixel_x, pixel_y), TileData.size // 3, 2)