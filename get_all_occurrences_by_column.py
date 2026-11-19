from typing import List


def get_all_occurrences_by_column(table: List[List[str]], column: int) -> dict[str, int]:
    m = len(table)

    occurrences = {}

    for i in range(m):
        occurrences[table[i][column]] = occurrences.get(table[i][column], 0) + 1

    return occurrences