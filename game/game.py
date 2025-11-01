import pygame

from game.data.grid_data import GridData
from game.data.tile_data import TileData
from game.data.window_data import WindowData
from game.environment.coin import Coin
from game.environment.level import Level
from game.environment.player import Player


class Game:
    def __init__(self, controller, level_data):
        pygame.init()

        screen_width = GridData.cols * TileData.size
        screen_height = GridData.rows * TileData.size

        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption(WindowData.title)
        self.font_style = pygame.font.SysFont(None, 50)
        self.clock = pygame.time.Clock()
        self.fps = WindowData.fps
        self.running = False
        self.score = 0

        self.level = Level(level_data.grid, level_data.walls)
        self.player = Player(5, 5)
        self.controller = controller

        self.coin = Coin()
        self.coin.spawn(self.level, self.player)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self):
        """Execute action"""
        self.controller.execute_action(self.player, self.level)

    def draw_score(self):
        """Draw score on screen"""
        score_text = self.font_style.render(f"Score: {self.score}", True, (0, 0, 0))
        self.screen.blit(score_text, (10, 10))

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
        self.coin.draw(self.screen)
        self.draw_score()
        pygame.display.flip()

    def start_game(self):
        self.running = True
        while self.running:
            self.clock.tick(self.fps)
            self.handle_events()
            self.update()
            self.render()

        pygame.quit()