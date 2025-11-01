from dataclasses import dataclass


@dataclass
class WindowData:
    fps: int = 10
    title: str = "Pathfinding Algorithms"