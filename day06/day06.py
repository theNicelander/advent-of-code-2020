def read_file(path):
    with open(path) as f:
        return f.read().split("\n\n")


def sum_unique_answers(data: list) -> int:
    data = [g.replace("\n", "") for g in data]
    unique_answers = [len(set(group)) for group in data]
    return sum(unique_answers)


def sum_duplicate_answers(data):
    number_of_intersections = [find_intersection_length(group) for group in data]
    return sum(number_of_intersections)


def find_intersection_length(group) -> int:
    intersect = "START"
    for subgroup in group.split("\n"):
        if intersect == "START":
            intersect = set(subgroup)
        intersect = intersect.intersection(set(subgroup))
    return len(intersect)


def test_part_2():
    data = read_file("test_part_2.txt")
    assert sum_duplicate_answers(data) == 6
    print("TEST PASSED")


if __name__ == "__main__":
    data = read_file("input.txt")
    test_part_2()

    print("Part 1", sum_unique_answers(data))
    print("Part 2", sum_duplicate_answers(data))
