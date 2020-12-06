def read_file(path):
    with open(path) as f:
        return f.read().split("\n\n")


def sum_unique_answers(groups_with_newlines: list) -> int:
    groups_without_newlines = [g.replace("\n", "") for g in groups_with_newlines]
    unique_answers_in_groups = [len(set(g)) for g in groups_without_newlines]
    return sum(unique_answers_in_groups)


def sum_duplicate_answers(data):
    return sum([intersection_length(group) for group in data])


def intersection_length(group: str) -> int:
    """Splits string by newline, then finds length of intersection
    Example:
        input: "abc\nbc"
        {b,c} is the intersection
        output: 2
    """
    subgroup_sets = map(set, group.split("\n"))
    intersections = set.intersection(*subgroup_sets)
    return len(intersections)


def test_part_2():
    data = read_file("test_part_2.txt")
    assert sum_duplicate_answers(data) == 6
    print("TEST PASSED")


if __name__ == "__main__":
    test_part_2()

    data = read_file("input.txt")
    print("Part 1", sum_unique_answers(data))
    print("Part 2", sum_duplicate_answers(data))
