from game.data.levels_data import Level1Data, Level2Data
from game.game import Game
from game.pathfinding.controller import PathfindingController
from game.pathfinding.manual import ManualController


def main():
    level_data = Level2Data()
    controller = ManualController()
    #controller = PathfindingController()
    game = Game(controller=controller, level_data=level_data)
    game.start_game()


if __name__ == "__main__":
    main()