import random

from game.environment.level import Level
from game.environment.player import Player


class PathfindingController:
    @staticmethod
    def execute_action(player: Player, level: Level):
        """Directly call player movement methods"""
        action = random.choice([
            player.move_up,
            player.move_down,
            player.move_left,
            player.move_right
        ])
        action(level)