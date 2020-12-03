import numpy as np


def read_input(path: str) -> list:
    with open(path) as f:
        return f.read().splitlines()


class Slope:
    def __init__(self, input_path):
        self.slope = read_input(input_path)
        self.slope_length = len(self.slope)
        self.slope_width = len(self.slope[0])

    def broaden_slope(self):
        self.slope = [line + line for line in self.slope]
        self.slope_width = len(self.slope[0])

    def is_tree(self, x, y) -> bool:
        if self.slope[y][x] == "#":
            return True
        return False

    def count_trees(self, move_right=3, move_down=1):
        count = 0
        x = move_right
        y = move_down

        while self.slope_length > y:
            if x >= self.slope_width:
                self.broaden_slope()
            if self.is_tree(x, y):
                count += 1
            x += move_right
            y += move_down
        return count

    def count_trees_multiple(self, to_traverse):
        return [self.count_trees(right, down) for right, down in to_traverse]


if __name__ == "__main__":
    slope = Slope("input.txt")

    print(f"Solution 1: {slope.count_trees()}")

    to_traverse = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    multiple_paths = slope.count_trees_multiple(to_traverse)
    print(f"Solution 2: {np.product(multiple_paths)}")
