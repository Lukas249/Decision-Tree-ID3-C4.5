from typing import List

from calculate_entropy import calculate_entropy
from calculate_gain_info import calculate_gain_info
from calculate_info import calculate_info
from get_all_occurrences_by_column import get_all_occurrences_by_column


def find_best_column_to_divide(table: List[List[str]], info: float, y_column_idx: int) -> int:
    best_column_idx = -1
    best_column_gain_ratio = -1

    if info == 0:
        return best_column_idx

    for column_idx in range(len(table[0]) - 1):
        column_info = calculate_info(table, column_idx, y_column_idx)

        info_gain = calculate_gain_info(info, column_info)

        occurrences = get_all_occurrences_by_column(table, column_idx)
        split_info = calculate_entropy(occurrences)

        if split_info == 0:
            continue


        gain_ratio = info_gain / split_info

        if gain_ratio > best_column_gain_ratio:
            best_column_gain_ratio = gain_ratio
            best_column_idx = column_idx

    return best_column_idx