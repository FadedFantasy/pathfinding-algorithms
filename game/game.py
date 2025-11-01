import random

import pygame

from game.data.grid_data import GridData
from game.data.tile_data import TileData
from game.data.window_data import WindowData
from game.environment.coin import Coin
from game.environment.level import Level
from game.environment.player import Player


class Game:
    def __init__(self, controller, level_data, seed: int):
        random.seed(seed)
        pygame.init()

        screen_width = GridData.cols * TileData.size
        screen_height = GridData.rows * TileData.size

        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption(WindowData.title)
        self.font_style = pygame.font.SysFont(None, 50)
        self.clock = pygame.time.Clock()
        self.fps = WindowData.fps
        self.running = False
        self.frame_count = 0
        self.coins = []

        self.level = Level(level_data.grid, level_data.walls)
        self.player = Player(5, 5)
        self.controller = controller

        self._setup_coins(num_coins=5)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def _setup_coins(self, num_coins: int):
        """Spawn initial coins"""
        for _ in range(num_coins):
            coin = Coin()
            coin.spawn(self.level, self.player, self.coins)
            self.coins.append(coin)

    def check_coin_collection(self):
        """Check if player collected any coin"""
        for coin in self.coins[:]:  # Use slice to iterate over copy
            if self.player.grid_row == coin.grid_row and self.player.grid_col == coin.grid_col:
                self.coins.remove(coin)
                break

    def update(self):
        """Execute action"""
        self.controller.execute_action(
            self.player,
            self.level,
            self.coins,
            GridData.rows,
            GridData.cols
        )
        self.check_coin_collection()
        self.check_coin_collection()

        # Only count frames if coins remain
        if self.coins:
            self.frame_count += 1

    def draw_frame_count(self):
        """Draw frame count on screen"""
        frame_text = self.font_style.render(f"Frames: {self.frame_count}", True, (0, 0, 0))
        self.screen.blit(frame_text, (10, 10))

        # Show completion message
        if len(self.coins) == 0:
            complete_text = self.font_style.render("Complete!", True, (0, 255, 0))
            self.screen.blit(complete_text, (10, 60))

    def draw_grid(self):
        """Draw grid lines"""
        # Horizontal lines
        for row in range(GridData.rows + 1):
            y = row * TileData.size
            pygame.draw.line(self.screen, (150, 150, 150),
                             (0, y), (GridData.cols * TileData.size, y), 1)

        # Vertical lines
        for col in range(GridData.cols + 1):
            x = col * TileData.size
            pygame.draw.line(self.screen, (150, 150, 150),
                             (x, 0), (x, GridData.rows * TileData.size), 1)

    def render(self):
        self.screen.fill(pygame.Color("gray"))
        self.draw_grid()
        self.level.draw(self.screen)
        self.player.draw(self.screen)
        for coin in self.coins:
            coin.draw(self.screen)
        self.draw_frame_count()
        pygame.display.flip()

    def start_game(self):
        self.running = True
        while self.running:
            self.clock.tick(self.fps)
            self.handle_events()
            self.update()
            self.render()

        pygame.quit()
