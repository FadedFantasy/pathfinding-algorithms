from dataclasses import dataclass


@dataclass
class WindowData:
    fps: int = 1
    title: str = "Pathfinding Algorithms"