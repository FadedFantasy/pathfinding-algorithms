import random

from game.environment.coin import Coin
from game.environment.level import Level
from game.environment.player import Player


class PathfindingController:
    @staticmethod
    def execute_action(player: Player, level: Level, coins: list[Coin], grid_rows: int, grid_cols: int):
        """
        Execute one action based on game state.

        Available information:
        - player.grid_row, player.grid_col: Current player position
        - coins: List of coins, each with .grid_row and .grid_col
        - level.is_walkable(row, col): Check if position is walkable
        - grid_rows, grid_cols: Grid dimensions

        Available actions:
        - player.move_up(level)
        - player.move_down(level)
        - player.move_left(level)
        - player.move_right(level)
        """
        # Students implement their algorithm here
        # Example: Random movement
        action = random.choice([
            player.move_up,
            player.move_down,
            player.move_left,
            player.move_right
        ])
        action(level)