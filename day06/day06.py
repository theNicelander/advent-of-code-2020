def read_file(path):
    with open(path) as f:
        return f.read().split("\n\n")


def sum_unique_answers(data: list) -> int:
    data = [g.replace("\n", "") for g in data]
    unique_answers = [len(set(group)) for group in data]
    return sum(unique_answers)


def sum_duplicate_answers(data):
    number_of_intersections = [len(find_intersections(group)) for group in data]
    return sum(number_of_intersections)


def find_intersections(group):
    for index, subgroup in enumerate(group.split("\n")):
        if index == 0:
            intersection = set(subgroup)
        else:
            intersection = intersection.intersection(set(subgroup))
    return intersection


def test_part_2():
    data = read_file("test_part_2.txt")
    assert sum_duplicate_answers(data) == 6
    print("TEST PASSED")


if __name__ == "__main__":
    data = read_file("input.txt")
    test_part_2()

    print("Part 1", sum_unique_answers(data))
    print("Part 2", sum_duplicate_answers(data))
