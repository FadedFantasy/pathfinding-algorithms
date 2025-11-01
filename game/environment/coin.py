# game/environment/coin.py
import pygame
import random
from game.data.tile_data import TileData
from game.data.grid_data import GridData
from game.environment.level import Level
from game.environment.player import Player


class Coin:
    def __init__(self):
        self.grid_row = 0
        self.grid_col = 0
        self.color = (255, 215, 0)  # Gold color

    def spawn(self, level: Level, player: Player):
        """Spawn coin at random empty location"""
        while True:
            self.grid_row = random.randint(0, GridData.rows - 1)
            self.grid_col = random.randint(0, GridData.cols - 1)

            # Check if location is walkable (not a wall) AND not on player
            if (level.is_walkable(self.grid_row, self.grid_col) and
                    not (self.grid_row == player.grid_row and self.grid_col == player.grid_col)):
                break

    def get_pixel_pos(self):
        """Convert grid position to pixel position (center of tile)"""
        pixel_x = self.grid_col * TileData.size + TileData.size // 2
        pixel_y = self.grid_row * TileData.size + TileData.size // 2
        return pixel_x, pixel_y

    def draw(self, surface):
        pixel_x, pixel_y = self.get_pixel_pos()
        # Draw coin as a circle
        pygame.draw.circle(surface, self.color, (pixel_x, pixel_y), TileData.size // 3)
        # Draw border
        pygame.draw.circle(surface, (218, 165, 32), (pixel_x, pixel_y), TileData.size // 3, 2)