def read_data_into_list(path: str) -> list:
    with open(path) as f:
        return f.read().splitlines()


def read_groups_into_list(path: str) -> list:
    """
    Reads multiple lines of strings, separated by newline into a single string.
    Treat the as groups if separated by empty new lines

    Args:
        path: path to file

    Returns:
        list of concatenated strings, grouped together by an empty new line

    Example input:
        abc
        def

        g
    Example output:
        ["abcdef", "g"]
    """
    with open(path) as f:
        raw_groups = f.read().split("\n\n")
    return [g.replace("\n", "") for g in raw_groups]
