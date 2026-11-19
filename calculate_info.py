from typing import List

from calculate_entropy import calculate_entropy
from get_all_occurrences_by_column import get_all_occurrences_by_column


def calculate_info(table: List[List[str]], column_idx: int, y_column_idx: int) -> float:
    occurrences = get_all_occurrences_by_column(table, column_idx)

    divide_info = 0

    y_occurrences = {}

    for i in range(len(table)):
        col_val = table[i][column_idx]
        y_val = table[i][y_column_idx]

        if col_val not in y_occurrences:
            y_occurrences[col_val] = {}

        if y_val not in y_occurrences[col_val]:
            y_occurrences[col_val][y_val] = 0

        y_occurrences[col_val][y_val] += 1


    for value in occurrences.keys():
        p = occurrences[value] / len(table)
        divide_info += p * calculate_entropy(y_occurrences[value])

    return divide_info