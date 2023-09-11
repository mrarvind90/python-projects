from __future__ import annotations
from math import sqrt, pow


class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width: int) -> None:
        self.width = width

    def set_height(self, height: int) -> None:
        self.height = height

    def get_area(self) -> int:
        return self.width * self.height

    def get_perimeter(self) -> int:
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self) -> float:
        return sqrt(pow(self.width, 2) + pow(self.height, 2))

    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        return '\n'.join([f"{'*' * self.width}" for _ in range(self.height)]) + '\n'

    def get_amount_inside(self, shape: Rectangle | Square) -> int:
        rect_area = self.get_area()
        shape_area = shape.get_area()

        return rect_area // shape_area


class Square(Rectangle):
    def __init__(self, side: int):
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side: int) -> None:
        self.width = side
        self.height = side

    def set_width(self, side: int) -> None:
        self.width = side
        self.height = side

    def set_height(self, side: int) -> None:
        self.width = side
        self.height = side
