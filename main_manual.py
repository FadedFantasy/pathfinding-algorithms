from game.data.levels_data import Level2Data
from game.game import Game
from game.pathfinding.manual import ManualController


def main():
    level_data = Level2Data()
    controller = ManualController()
    game = Game(controller=controller, level_data=level_data, seed=42)
    game.start_game()


if __name__ == "__main__":
    main()