def read_data_into_list(path: str) -> list:
    with open(path) as f:
        return f.read().splitlines()
