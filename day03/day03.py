def read_input(path: str) -> list:
    with open(path) as f:
        return f.read().splitlines()


def is_tree(input: list, y: int, x: int) -> bool:
    if input[y][x] == "#":
        return True
    return False


def broaden_slope(slope: list) -> list:
    return [line + line for line in slope]


def count_trees(slope: list):
    count = 0
    current_y = 0
    current_x = 0
    slope_length = len(slope)
    slope_width = len(slope[0])

    while slope_length > current_y:
        if current_x > slope_width:
            slope = broaden_slope(slope)
            slope_width = len(slope[0])

        if is_tree(slope, current_y, current_x):
            count += 1
        current_y += 1
        current_x += 3

    return count


if __name__ == "__main__":
    slope = read_input("input.txt")

    number_of_trees = count_trees(slope)

    print(number_of_trees)
