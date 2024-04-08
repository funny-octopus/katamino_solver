from typing import List
from .point import Point
from abc import ABC
import copy


class Figure(ABC):

    code_name: str
    color: int
    rotate_number: int = 3
    is_mirror: bool = True
    position: int = 1
    mirrored: bool = False
    default_points: List[Point]
    points: List[Point]

    def __init__(self):
        self.to_default()

    def to_default(self):
        self.points = copy.deepcopy(self.default_points)
        self.position = 1
        self.mirrored = False

    def to_begin(self):
        min_y = min([point.y for point in self.points])
        min_x = min([point.x for point in self.points])
        self.move(x=min_x*(-1)+1, y=min_y*(-1)+1)

    def move(self, x: int = 0, y: int = 0):
        for point in self.points:
            point.x += x
            point.y += y
        return self

    def rotate_forward_clock(self):
        max_y = max([point.y for point in self.points])
        for point in self.points:
            point.x, point.y = abs(point.y - max_y - 1), point.x
        self.position = 1 if ((self.position + 1) == 5) else self.position + 1
        return self

    def rotate_reverse_clock(self):
        for _ in range(3):
            self.rotate_forward_clock()
        return self

    def mirror_x(self):
        max_x = max([point.x for point in self.points])
        for point in self.points:
            point.x = point.x - (point.x * 2) + max_x + 1
        self.mirrored = not self.mirrored
        return self

    def __repr__(self):
        return f"<Figure {self.code_name}, p={self.position}, m={self.mirrored}>"

    def __str__(self):
        return f"<Figure {self.code_name}, p={self.position}, m={self.mirrored}>"
