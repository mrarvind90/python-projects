from __future__ import annotations

import copy
import random


class Hat:
    random.seed(95)

    def __init__(self, **kwargs):
        self.contents = [key for key, value in kwargs.items() for _ in range(value)]

    def __repr__(self):
        return f"Hat(contents={self.contents})"

    def draw(self, num_to_draw: int) -> list[str]:
        if num_to_draw > len(self.contents):
            copied_list = self.contents.copy()
            self.contents.clear()

            return copied_list

        return [self.contents.pop(random.randrange(0, len(self.contents))) for _ in range(num_to_draw)]


def experiment(hat: Hat, expected_balls: dict[str, int], num_balls_drawn: int, num_experiments: int) -> float:
    expected_num_of_balls: list[int] = [num for color, num in expected_balls.items()]
    count_of_matches: int = 0

    for i in range(num_experiments):
        copied_hat: Hat = copy.deepcopy(hat)
        drawn_balls: list[str] = copied_hat.draw(num_balls_drawn)
        num_of_balls: list[int] = [drawn_balls.count(color) for color in expected_balls]
        count_of_matches += 1 if num_of_balls >= expected_num_of_balls else 0

    return count_of_matches / num_experiments
