def read_data_into_list(path: str) -> list:
    with open(path) as f:
        return f.read().splitlines()


def read_groups_into_list(path: str) -> list:
    with open(path) as f:
        raw_groups = f.read().split("\n\n")
    return [g.replace("\n", "") for g in raw_groups]
