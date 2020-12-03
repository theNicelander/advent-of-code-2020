import numpy as np


def read_input(path: str) -> list:
    with open(path) as f:
        return f.read().splitlines()


def is_tree(slope, x, y) -> bool:
    if slope[y][x] == "#":
        return True
    return False


def broaden_slope(slope: list) -> list:
    return [line + line for line in slope]


def count_trees(slope: list, move_right=3, move_down=1):
    count = 0
    current_x = move_right
    current_y = move_down
    slope_length = len(slope)
    slope_width = len(slope[0])

    while slope_length > current_y:
        if current_x >= slope_width:
            slope = broaden_slope(slope)
            slope_width = len(slope[0])

        if is_tree(slope, current_x, current_y):
            count += 1
        current_x += move_right
        current_y += move_down

    return count


def traverse_multiple_slopes(slope) -> list:
    to_traverse = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

    tree_list = []
    for right, down in to_traverse:
        number_of_trees = count_trees(slope, right, down)
        tree_list.append(number_of_trees)
    return tree_list


if __name__ == "__main__":
    slope = read_input("input.txt")
    print(f"Trees solution 1: {count_trees(slope)}")

    multiple_trees = traverse_multiple_slopes(slope)
    print(f"Trees solution 2: {np.prod(multiple_trees)}")
