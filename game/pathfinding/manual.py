import pygame

from game.environment.level import Level
from game.environment.player import Player


class ManualController:
    @staticmethod
    def execute_action(player: Player, level: Level):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.move_up(level)
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.move_down(level)
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.move_left(level)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.move_right(level)