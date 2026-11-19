import math


def calculate_entropy(column_occurrences: dict[str, int]) -> float:
    sum_all_occurrences = sum(column_occurrences.values())

    entropy = 0

    for count in column_occurrences.values():
        p = count/sum_all_occurrences
        entropy += p * math.log(p, 2)

    return -entropy